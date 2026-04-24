@echo off
setlocal EnableDelayedExpansion

@REM Activate virtual environment and run the app.
if not exist ".venv\Scripts\activate.bat" (
    echo ERROR: .venv not found. Create it first with: python -m venv .venv
    exit /b 1
)

call ".venv\Scripts\activate.bat"

set "COMMANDS_FILE=%~1"
if not "%COMMANDS_FILE%"=="" (
    if not exist "%COMMANDS_FILE%" (
        echo ERROR: Commands file not found: %COMMANDS_FILE%
        exit /b 1
    )

    echo Running with %COMMANDS_FILE%
    python main.py "%COMMANDS_FILE%"
    exit /b %errorlevel%
)

set "FOUND=0"
set "FAILED=0"

for %%F in (commands_*.txt command_*.txt) do (
    if exist "%%~F" (
        set "FOUND=1"
        echo Running with %%~F
        python main.py "%%~F"
        echo ----------------------------------------------------------------
        if errorlevel 1 set "FAILED=1"
    )
)

if "!FOUND!"=="0" (
    echo ERROR: No command files found matching commands_*.txt or command_*.txt
    exit /b 1
)

if "!FAILED!"=="1" exit /b 1
exit /b 0
