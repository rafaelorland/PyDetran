@echo off
cd C:\Users\rafael\PyDetran\PyDetran
call Scripts\activate.bat
cd pydetran
start /B python manage.py runserver
start chrome http://127.0.0.1:8000/
