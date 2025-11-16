# GitHub Actions Workflow 更新摘要

## 修改日期

2025-11-16

## 修改目的

簡化 GitHub Actions workflow，專注於閩拚輸入法（BP）方案的發行作業。

## 主要變更

### 1. Workflow 名稱

- **舊名稱**: "Build & Release YAML bundles (ALL / TLPA / ZU2 / BP)"
- **新名稱**: "Build & Release 閩拚輸入法 (BP)"

### 2. build-bundles Job 簡化

#### 變更前：

- 產生 4 個方案包：
  - `rime-tlpa-all-{TAG}.zip` (完整版)
  - `rime-tlpa-tlpa-{TAG}.zip` (TLPA 方案)
  - `rime-tlpa-zu2-{TAG}.zip` (注音二式)
  - `rime-tlpa-bp-{TAG}.zip` (閩拼方案)

#### 變更後：

- 只產生 1 個方案包：
  - `rime-bp-{TAG}.zip` (閩拼方案)

#### 技術細節：

- 直接從 `release-include.txt` 讀取檔案清單
- 移除不必要的 COMMON/TLPA/ZU2/KB 分類邏輯
- 簡化打包流程
- 保留完整的錯誤處理和除錯訊息

### 3. Release Notes 更新

#### 變更前：

- 列出所有 4 個方案的下載說明
- 通用的安裝指引

#### 變更後：

- 聚焦於閩拚輸入法
- 明確的兩種安裝方式：
  1. Windows 安裝程式（推薦）
  2. 手動安裝 YAML 配置
- 增加系統需求說明
- 增加檔案驗證說明

### 4. 支援的標籤格式

保持不變，仍支援：

- `v*` - 通用版本
- `bp-*` - 閩拼專用版本
- `kb-*` - 鍵盤練習工具版本
- `zu-*` - 注音二式版本（保留以供未來可能使用）

## 發行內容

每次 Release 現在會包含：

### 檔案清單

1. `rime-bp-installer-{TAG}.zip` - Windows 安裝程式
2. `rime-bp-installer-{TAG}.zip.sha256` - 安裝程式校驗碼
3. `rime-bp-{TAG}.zip` - YAML 配置包
4. `rime-bp-{TAG}.zip.sha256` - 配置包校驗碼

### 檔案用途

- **安裝程式**: 適合一般使用者，一鍵安裝
- **配置包**: 適合進階使用者手動安裝

## 使用方式

### 發行新版本

```bash
# 建立版本標籤
git tag v1.0.0

# 推送到 GitHub
git push origin v1.0.0
```

### 自動執行流程

1. ✅ GitHub Actions 自動觸發
2. ✅ 建置 Windows 安裝程式
3. ✅ 打包 YAML 配置
4. ✅ 建立 GitHub Release
5. ✅ 上傳所有檔案

## 效益

### 簡化維護

- ✅ 減少打包時間（從 4 個包減少到 1 個）
- ✅ 降低 workflow 複雜度
- ✅ 更清晰的專案定位

### 提升使用者體驗

- ✅ 明確的下載選項
- ✅ 清楚的安裝指引
- ✅ 專注於單一方案，避免混淆

### 資源效率

- ✅ 減少 GitHub Actions 執行時間
- ✅ 減少儲存空間使用
- ✅ 更快的下載速度

## 相關檔案

- `.github/workflows/release-yamls.yml` - Workflow 定義
- `tools/_203_GitHub_Actions_自動發行作業程序.md` - 詳細說明文檔
- `release-include.txt` - 要打包的檔案清單

## 測試建議

在正式發行前，建議：

1. 使用手動觸發測試 workflow
2. 標記為 pre-release
3. 驗證所有檔案都正確生成
4. 測試下載和安裝流程

```bash
# 建立測試標籤
git tag v0.9.0-test
git push origin v0.9.0-test
```

## 向後相容性

- ✅ 現有的觸發機制保持不變
- ✅ 手動觸發介面保持不變
- ✅ Artifact 傳遞機制保持不變

---

更新者：GitHub Copilot
