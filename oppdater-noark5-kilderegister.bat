@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
    py -3 "tools\oppdater_noark5_kilderegister.py"
) else (
    python "tools\oppdater_noark5_kilderegister.py"
)
if errorlevel 1 (
    echo.
    echo ERROR: Source inventory was not updated. See message above.
    pause
    exit /b 1
)
echo.
echo Review docs\kilder\noark\SOURCE-MANIFEST.json and SHA256SUMS.txt
pause
endlocal
