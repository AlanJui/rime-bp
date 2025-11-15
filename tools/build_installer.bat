@echo off
chcp 65001 >nul
echo ==========================================
echo 🚀 RIME 閩拚輸入法安裝程式打包工具
echo ==========================================
echo.

cd /d "%~dp0"

echo 📍 當前目錄: %CD%
echo.

echo 🔄 檢查 Python 環境...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 找不到 Python，請先安裝 Python 3.6+ 版本
    echo    下載網址: https://www.python.org/downloads/
    pause
    exit /b 1
)

python --version
echo ✅ Python 環境正常
echo.

echo 🔄 開始打包...
python build_installer.py

echo.
echo 📦 打包完成，請檢查 ../release/installer_package/ 目錄
echo.

pause