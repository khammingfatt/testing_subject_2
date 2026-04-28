@echo off
title HDB Resale Price Predictor - Setup ^& Run
echo ===================================================
echo   HDB Resale Price Predictor - Environment Setup
echo ===================================================

:: Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not added to your PATH.
    echo Please install Python and try again.
    pause
    exit /b
)

:: Check for Virtual Environment
if not exist "venv\Scripts\activate.bat" (
    echo [INFO] Creating a new virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to create virtual environment.
        pause
        exit /b
    )
    echo [SUCCESS] Virtual environment created.
)

:: Activate the environment
echo [INFO] Activating the virtual environment...
call venv\Scripts\activate.bat

:: Install Requirements
echo [INFO] Installing required packages from requirements.txt...
pip install -r requirements.txt

:: Start Streamlit
echo [INFO] Starting the Streamlit application...
echo.
streamlit run src/app.py

pause
