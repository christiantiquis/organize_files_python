@echo off
setlocal

rem Get the directory of the batch file
set "SCRIPT_DIR=%~dp0"

rem Check if a directory argument was provided
if "%~1"=="" (
    echo Please provide the directory path as an argument.
    echo Usage: run_organize_files.bat "C:\path\to\target\directory"
    pause
    exit /b
)

rem Run the Python script with the provided directory path
python "%SCRIPT_DIR%organize_files_bypath.py" "%~1"
pause
