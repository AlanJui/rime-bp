#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RIME 安裝程式測試工具
用於測試打包後的執行檔是否正常運作
"""

import subprocess
import sys
import time
from pathlib import Path


def test_exe_exists():
    """測試執行檔是否存在"""
    # 智能檢測執行檔位置
    current_dir = Path.cwd()

    # 可能的執行檔位置
    possible_paths = [
        current_dir / "release" / "installer_package" / "rime_installer.exe",  # 從根目錄執行
        current_dir.parent / "release" / "installer_package" / "rime_installer.exe"  # 從 tools 目錄執行
    ]

    exe_path = None
    for path in possible_paths:
        if path.exists():
            exe_path = path
            break

    if not exe_path:
        print("❌ 找不到執行檔")
        for i, path in enumerate(possible_paths):
            print(f"   檢查位置 {i+1}: {path}")
        return None
    if exe_path.exists():
        file_size = exe_path.stat().st_size / (1024 * 1024)
        print(f"✅ 找到執行檔: {exe_path}")
        print(f"📊 檔案大小: {file_size:.1f} MB")
        return exe_path
    else:
        print(f"❌ 找不到執行檔: {exe_path}")
        return None

def test_exe_launch():
    """測試執行檔啟動"""
    exe_path = test_exe_exists()
    if not exe_path:
        return False

    print("🔄 測試執行檔啟動...")
    try:
        # 啟動程式但立即終止（避免實際安裝）
        process = subprocess.Popen(
            [str(exe_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=exe_path.parent
        )

        # 等待一秒讓程式初始化
        time.sleep(1)

        # 終止程式
        process.terminate()

        try:
            stdout, stderr = process.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            stdout, stderr = process.communicate()

        print("✅ 執行檔可以正常啟動")
        if stdout:
            print("📝 標準輸出預覽:")
            print(stdout[:200] + "..." if len(stdout) > 200 else stdout)

        return True

    except Exception as e:
        print(f"❌ 執行檔啟動失敗: {e}")
        return False

def test_dependencies():
    """測試相依檔案"""
    # 智能檢測安裝包目錄
    current_dir = Path.cwd()

    possible_dirs = [
        current_dir / "release" / "installer_package",  # 從根目錄執行
        current_dir.parent / "release" / "installer_package"  # 從 tools 目錄執行
    ]

    package_dir = None
    for dir_path in possible_dirs:
        if dir_path.exists():
            package_dir = dir_path
            break

    if not package_dir:
        print("❌ 找不到安裝包目錄")
        return False

    required_files = [
        "rime_installer.exe",
        "安裝說明.txt",
        "README.md"
    ]

    required_dirs = [
        "rime_files",
        "config"
    ]

    optional_files = [
        "release-include.txt"
    ]

    print("📋 檢查必要檔案...")
    all_good = True

    for file_name in required_files:
        file_path = package_dir / file_name
        if file_path.exists():
            print(f"✅ {file_name}")
        else:
            print(f"❌ 缺少: {file_name}")
            all_good = False

    print("\n📁 檢查必要目錄...")
    for dir_name in required_dirs:
        dir_path = package_dir / dir_name
        if dir_path.exists() and dir_path.is_dir():
            file_count = len(list(dir_path.iterdir()))
            print(f"✅ {dir_name}/ ({file_count} 個檔案)")
        else:
            print(f"❌ 缺少目錄: {dir_name}/")
            all_good = False

    print("\n📄 檢查選用檔案...")
    for file_name in optional_files:
        file_path = package_dir / file_name
        if file_path.exists():
            print(f"✅ {file_name}")
        else:
            print(f"⚠️ 選用檔案未找到: {file_name}")

    return all_good

def test_rime_directory():
    """檢查 RIME 目錄（不執行實際安裝）"""
    rime_dir = Path.home() / "AppData" / "Roaming" / "Rime"

    print("📍 檢查 RIME 安裝狀態...")
    if rime_dir.exists():
        print(f"✅ 找到 RIME 目錄: {rime_dir}")

        # 檢查重要檔案
        important_files = ["default.yaml", "weasel.yaml"]
        for file_name in important_files:
            file_path = rime_dir / file_name
            if file_path.exists():
                print(f"  ✅ {file_name}")
            else:
                print(f"  ⚠️ 未找到: {file_name}")

        return True
    else:
        print(f"⚠️ 未找到 RIME 目錄: {rime_dir}")
        print("   請先安裝 RIME 小狼毫輸入法")
        return False

def generate_test_report():
    """生成測試報告"""
    print("\n" + "=" * 60)
    print("📊 生成測試報告...")

    results = {
        "執行檔存在": test_exe_exists() is not None,
        "相依檔案完整": test_dependencies(),
        "RIME 環境": test_rime_directory(),
        "執行檔啟動": False  # 將在後面測試
    }

    # 測試執行檔啟動（放在最後，因為可能需要用戶交互）
    if results["執行檔存在"]:
        print("\n🚀 測試執行檔啟動...")
        results["執行檔啟動"] = test_exe_launch()

    print("\n" + "=" * 60)
    print("📋 測試結果總結")
    print("=" * 60)

    for test_name, result in results.items():
        status = "✅ 通過" if result else "❌ 失敗"
        print(f"{test_name:15} : {status}")

    passed = sum(results.values())
    total = len(results)
    success_rate = (passed / total) * 100

    print(f"\n📊 總體結果: {passed}/{total} ({success_rate:.0f}%)")

    if success_rate >= 75:
        print("🎉 測試結果良好，可以進行分發!")
    elif success_rate >= 50:
        print("⚠️ 測試結果一般，建議檢查失敗項目")
    else:
        print("❌ 測試結果不佳，請檢查並修正問題")

    return results

def main():
    """主函式"""
    print("=" * 60)
    print("🧪 RIME 閩拚輸入法安裝程式測試工具")
    print("=" * 60)

    # 檢查測試環境
    print("📍 檢查測試環境...")
    print(f"Python 版本: {sys.version}")
    print(f"當前目錄: {Path.cwd()}")

    # 執行測試
    results = generate_test_report()

    print("\n📝 建議事項:")
    if not results["執行檔存在"]:
        print("- 請先執行 build_installer.py 進行打包")

    if not results["相依檔案完整"]:
        print("- 檢查打包過程是否包含所有必要檔案")

    if not results["RIME 環境"]:
        print("- 測試環境需要安裝 RIME 小狼毫輸入法")

    if not results["執行檔啟動"]:
        print("- 檢查執行檔是否有相依性問題")
        print("- 在乾淨的 Windows 環境測試")

    input("\n按 Enter 鍵結束...")
    return all(results.values())

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)