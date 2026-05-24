@echo off
:: ============================================================
:: build_windows.bat — Build QEC-AutoFiller-Windows.exe
:: Just double-click this on any Windows PC with Python 3
:: ============================================================

echo.
echo  =====================================================
echo   QEC Auto-Filler  ^|  Windows EXE Builder
echo  =====================================================
echo.

:: Check Python
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo  [ERROR] Python 3 not found.
    echo  Download from: https://www.python.org/downloads/
    echo  Make sure to tick "Add Python to PATH" during install.
    pause
    exit /b 1
)

echo  [1/3] Installing required packages...
pip install pyinstaller selenium --quiet
IF ERRORLEVEL 1 (
    echo  [ERROR] pip install failed. Check your internet connection.
    pause
    exit /b 1
)

echo  [2/3] Building EXE with PyInstaller...
pyinstaller ^
    --onefile ^
    --console ^
    --name "QEC-AutoFiller-Windows" ^
    --hidden-import selenium ^
    --hidden-import selenium.webdriver ^
    --hidden-import selenium.webdriver.chrome ^
    --hidden-import selenium.webdriver.chrome.service ^
    --hidden-import selenium.webdriver.support.ui ^
    --hidden-import selenium.webdriver.support.expected_conditions ^
    --hidden-import selenium.webdriver.common.by ^
    --hidden-import selenium.webdriver.common.keys ^
    --hidden-import selenium.common.exceptions ^
    QEC-FORM.py

IF ERRORLEVEL 1 (
    echo.
    echo  [ERROR] Build failed. See output above for details.
    pause
    exit /b 1
)

echo  [3/3] Done!
echo.
echo  =====================================================
echo   Your EXE is ready at:
echo   dist\QEC-AutoFiller-Windows.exe
echo  =====================================================
echo.
echo  Share ONLY that .exe file.
echo  Users only need Chrome installed — nothing else.
echo.
pause
