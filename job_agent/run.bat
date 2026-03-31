@echo off
echo ==========================================
echo Job Agent - Starting Application
echo ==========================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Virtual environment not found!
    echo Please run setup.bat first.
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate

REM Start the application
echo Starting Job Agent...
echo.
echo Open your browser and navigate to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server.
echo.

python run.py

pause