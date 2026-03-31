@echo off
echo ==========================================
echo Job Agent - Setup Script
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed! Please install Python 3.8 or higher.
    exit /b 1
)

echo Python found!
python --version
echo.

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Failed to create virtual environment!
        exit /b 1
    )
    echo Virtual environment created successfully!
) else (
    echo Virtual environment already exists.
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
if errorlevel 1 (
    echo Failed to activate virtual environment!
    exit /b 1
)
echo Virtual environment activated!
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo Failed to upgrade pip!
    exit /b 1
)
echo.

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install dependencies!
    exit /b 1
)
echo Dependencies installed successfully!
echo.

REM Create database
echo Initializing database...
python -c "from app import app, db; app.app_context().push(); db.create_all(); print('Database initialized!')"
if errorlevel 1 (
    echo Failed to initialize database!
    exit /b 1
)
echo.

echo ==========================================
echo Setup completed successfully!
echo ==========================================
echo.
echo To start the application, run:
echo   run.bat
echo.
echo Or manually:
echo   venv\Scripts\activate
echo   python run.py
echo.
pause