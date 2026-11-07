#!/usr/bin/env python3
"""Update Noark 5 source checksums in an existing local repository.

Standard library only. Run from the repository root or via the BAT file.
No files in the Noark source collection are modified except the two indexes.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NOARK = REPO / "docs" / "kilder" / "noark"
NOARK5 = NOARK / "noark5"
MANIFEST = NOARK / "SOURCE-MANIFEST.json"
SUMS = NOARK / "SHA256SUMS.txt"
SOURCE_DIR_NAMES = {"schemas", "spesifikasjoner"}
CHECKSUM_LINE = re.compile(r"^([0-9a-fA-F]{64})  (.+)$")


def digest(path: Path) -> str:
    checksum = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            checksum.update(chunk)
    return checksum.hexdigest()


def relpath(path: Path) -> str:
    return path.relative_to(NOARK).as_posix()


def source_files() -> list[Path]:
    """Only index actual original files under versioned source directories."""
    found = []
    for path in NOARK5.iterdir():
        if not path.is_dir() or not path.name.startswith("v"):
            continue
        for folder in SOURCE_DIR_NAMES:
            source_dir = path / folder
            if source_dir.is_dir():
                found.extend(p for p in source_dir.rglob("*") if p.is_file())
    return sorted(found, key=lambda p: relpath(p).casefold())


def atomic_text_write(path: Path, content: str) -> bool:
    """Write only if changed. Replace files atomically on the same volume."""
    old = path.read_text(encoding="utf-8-sig") if path.exists() else None
    if old == content:
        return False
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", newline="\n", dir=path.parent,
        prefix=f".{path.name}.", suffix=".tmp", delete=False,
    ) as temp:
        temp_path = Path(temp.name)
        temp.write(content)
    try:
        os.replace(temp_path, path)
    finally:
        if temp_path.exists():
            temp_path.unlink()
    return True


def main() -> int:
    if not MANIFEST.is_file() or not SUMS.is_file() or not NOARK5.is_dir():
        print("ERROR: Expected docs/kilder/noark files not found.", file=sys.stderr)
        print(f"Expected repository root: {REPO}", file=sys.stderr)
        return 1

    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8-sig"))
        entries = data["files"]
        if not isinstance(entries, list) or any(not isinstance(x, dict) for x in entries):
            raise ValueError("SOURCE-MANIFEST.json: 'files' must be a list of objects")
        original_by_path = {}
        for entry in entries:
            path = entry.get("path")
            if not isinstance(path, str) or path in original_by_path:
                raise ValueError(f"Duplicate or invalid path: {path!r}")
            original_by_path[path] = entry

        source_list = source_files()
        if not source_list:
            raise ValueError("No Noark 5 source files found in schemas/ or spesifikasjoner/")
        actual = {relpath(path): path for path in source_list}

        tracked_noark5 = {p for p in original_by_path if p.startswith("noark5/")}
        missing = sorted(tracked_noark5 - set(actual))
        if missing:
            raise ValueError("Previously indexed Noark 5 files are missing:\n  " + "\n  ".join(missing))

        # Existing Noark 3 and 4 records are preserved, and their hashes are
        # checked against local copies when the original files are present.
        for name, entry in original_by_path.items():
            if name.startswith("noark5/") or "sha256" not in entry:
                continue
            file_path = NOARK / Path(name)
            if file_path.is_file():
                checksum = digest(file_path)
                if checksum.lower() != str(entry["sha256"]).lower():
                    raise ValueError(f"Existing checksum mismatch: {name}")

        updated = [entry for name, entry in original_by_path.items() if not name.startswith("noark5/")]
        new_checksums = {}
        for name, path in actual.items():
            new_entry = dict(original_by_path.get(name, {}))
            new_entry["path"] = name
            new_entry["size_bytes"] = path.stat().st_size
            new_entry["sha256"] = digest(path)
            # Do not guess the original download URL, source archive or date.
            if not any(k in new_entry for k in ("source_archive", "source_url", "source_path_in_original_zip")):
                new_entry.setdefault("source_status", "not_documented")
            updated.append(new_entry)
            new_checksums[name] = new_entry["sha256"]

        data["files"] = sorted(updated, key=lambda d: d["path"].casefold())
        data["collection"] = "Noark 3, Noark 4 and Noark 5 standard sources"
        # Existing top-level source_archive is legacy metadata for Noark 3/4,
        # NOT evidence of provenance for newly indexed Noark 5 files.
        if "source_archive" in data:
            data["source_archive_scope"] = "Legacy Noark 3 and 4 files only"
        manifest_text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"

        # Preserve old checksum lines; replace only Noark 5 lines.
        original_lines = SUMS.read_text(encoding="utf-8-sig").splitlines()
        preserved = []
        for line in original_lines:
            parsed = CHECKSUM_LINE.match(line)
            if parsed and parsed.group(2).replace("\\", "/").startswith("noark5/"):
                continue
            if line.strip():
                preserved.append(line.rstrip())
        sums_text = "\n".join(preserved + [
            f"{new_checksums[name]}  {name}" for name in sorted(new_checksums, key=str.casefold)
        ]) + "\n"

        changed_manifest = atomic_text_write(MANIFEST, manifest_text)
        changed_sums = atomic_text_write(SUMS, sums_text)
        print(f"Noark 5 source files indexed: {len(actual)}")
        print(f"SOURCE-MANIFEST.json: {'updated' if changed_manifest else 'unchanged'}")
        print(f"SHA256SUMS.txt: {'updated' if changed_sums else 'unchanged'}")
        print("Noark 3/4 entries were preserved and available original checksums verified.")
        print("Noark 5 source origins are marked not_documented where not supplied.")
        print("Review changes before git commit. No Git commands were run.")
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        print("No source files were modified. Check input and try again.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
