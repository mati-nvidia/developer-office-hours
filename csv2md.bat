@echo off

call "%~dp0tools\packman\python.bat" %~dp0tools\scripts\csv2md.py %*
if %errorlevel% neq 0 ( goto Error )

:Success
exit /b 0

:Error
exit /b %errorlevel%
