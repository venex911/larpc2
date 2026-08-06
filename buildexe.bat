@echo off

title LARP Builder
color 4

echo Building LARP.exe...
pyinstaller --onefile --name=LARP.exe --icon=meow.ico larp.py
echo LARP.exe has been built successfully in the 'dist' folder.
oause >nul