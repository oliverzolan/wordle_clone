@echo off
echo 🚀 Starting Wordle Clone deployment process...

echo Running tests...
coverage run -m unittest discover tests
if %ERRORLEVEL% NEQ 0 (
    echo Tests failed! Aborting deployment.
    exit /b 1
)

echo Generating coverage report...
coverage report -m

echo Building executable...
pyinstaller --onefile run_game.py --name wordle

echo ✅ Deployment completed successfully!
echo Executable is available at: .\dist\wordle.exe

set /p RUN_GAME=Do you want to run the game now? (y/n) 
if /i "%RUN_GAME%"=="y" (
    .\dist\wordle.exe
) 