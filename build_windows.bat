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

python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo  [ERROR] Python 3 not found.
    echo  Download: https://www.python.org/downloads/
    echo  Tick "Add Python to PATH" during install.
    pause & exit /b 1
)

echo  [1/3] Installing packages...
pip install pyinstaller selenium --quiet
IF ERRORLEVEL 1 ( echo  [ERROR] pip install failed. & pause & exit /b 1 )

echo  [2/3] Building EXE...
pyinstaller ^
    --onefile --console ^
    --name "QEC-AutoFiller-Windows" ^
    --collect-all selenium ^
    --hidden-import selenium.webdriver.chrome.webdriver ^
    --hidden-import selenium.webdriver.chromium.webdriver ^
    --hidden-import selenium.webdriver.remote.webdriver ^
    --hidden-import selenium.webdriver.remote.remote_connection ^
    --hidden-import selenium.webdriver.remote.errorhandler ^
    --hidden-import selenium.webdriver.remote.command ^
    --hidden-import selenium.webdriver.remote.switch_to ^
    --hidden-import selenium.webdriver.remote.mobile ^
    --hidden-import selenium.webdriver.remote.webelement ^
    --hidden-import selenium.webdriver.common.driver_finder ^
    --hidden-import selenium.webdriver.common.selenium_manager ^
    --hidden-import selenium.webdriver.common.service ^
    --hidden-import selenium.webdriver.common.utils ^
    --hidden-import selenium.webdriver.common.by ^
    --hidden-import selenium.webdriver.common.keys ^
    --hidden-import selenium.webdriver.common.options ^
    --hidden-import selenium.webdriver.common.alert ^
    --hidden-import selenium.webdriver.support.ui ^
    --hidden-import selenium.webdriver.support.wait ^
    --hidden-import selenium.webdriver.support.expected_conditions ^
    --hidden-import selenium.webdriver.support.select ^
    --hidden-import selenium.common.exceptions ^
    QEC-FORM.py

IF ERRORLEVEL 1 ( echo  [ERROR] Build failed. & pause & exit /b 1 )

echo  [3/3] Done!
echo.
echo  =====================================================
echo   EXE ready: dist\QEC-AutoFiller-Windows.exe
echo  =====================================================
echo.
echo  Share only that .exe — users just need Chrome installed.
echo.
pause
