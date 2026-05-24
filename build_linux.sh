#!/usr/bin/env bash
# ============================================================
# build_linux.sh — Build QEC-AutoFiller-Linux ELF binary
# ============================================================
set -e

echo ""
echo " ====================================================="
echo "  QEC Auto-Filler  |  Linux Binary Builder"
echo " ====================================================="
echo ""

if ! command -v python3 &>/dev/null; then
    echo " [ERROR] python3 not found."
    echo " Install: sudo apt install python3 python3-pip"
    exit 1
fi

echo " [1/3] Installing packages..."
pip3 install pyinstaller selenium --quiet

echo " [2/3] Building binary..."
pyinstaller \
    --onefile --console \
    --name "QEC-AutoFiller-Linux" \
    --collect-all selenium \
    --hidden-import selenium.webdriver.chrome.webdriver \
    --hidden-import selenium.webdriver.chromium.webdriver \
    --hidden-import selenium.webdriver.remote.webdriver \
    --hidden-import selenium.webdriver.remote.remote_connection \
    --hidden-import selenium.webdriver.remote.errorhandler \
    --hidden-import selenium.webdriver.remote.command \
    --hidden-import selenium.webdriver.remote.switch_to \
    --hidden-import selenium.webdriver.remote.mobile \
    --hidden-import selenium.webdriver.remote.webelement \
    --hidden-import selenium.webdriver.common.driver_finder \
    --hidden-import selenium.webdriver.common.selenium_manager \
    --hidden-import selenium.webdriver.common.service \
    --hidden-import selenium.webdriver.common.utils \
    --hidden-import selenium.webdriver.common.by \
    --hidden-import selenium.webdriver.common.keys \
    --hidden-import selenium.webdriver.common.options \
    --hidden-import selenium.webdriver.common.alert \
    --hidden-import selenium.webdriver.support.ui \
    --hidden-import selenium.webdriver.support.wait \
    --hidden-import selenium.webdriver.support.expected_conditions \
    --hidden-import selenium.webdriver.support.select \
    --hidden-import selenium.common.exceptions \
    QEC-FORM.py

echo " [3/3] Done!"
echo ""
echo " ====================================================="
echo "  Binary ready: dist/QEC-AutoFiller-Linux"
echo " ====================================================="
echo ""
echo " Run with:"
echo "   chmod +x dist/QEC-AutoFiller-Linux"
echo "   ./dist/QEC-AutoFiller-Linux"
echo ""
