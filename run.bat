@echo off
set FLASK_APP=app.py
set FLASK_ENV=development
set FLASK_DEBUG=1

:: Start Flask server
flask run
