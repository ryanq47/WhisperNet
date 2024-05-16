@echo off

REM Check if 'venv' virtual environment folder exists
REM IF NOT EXIST "venv" (
REM     python -m venv venv
REM     echo Virtual environment created.
REM )

REM Activate virtual environment
REM CALL venv\Scripts\activate

REM Install dependencies
REM pip install flask markdown

REM Start the server
python main.py

REM Deactivate the virtual environment
REM CALL venv\Scripts\deactivate
