# 【閩拚輸入法】專案摘要

根據【閩拼方案】，發展【羅馬字母拼音輸入法】及【注音輸入法】。

## 專案目標

本專案試行之輸入法，需滿足以下需求規格：

- 【拼音系統】：閩拼方案（簡稱：閩拼/BP）
- 【字典編碼】：漢字讀音編碼採【閩拼方案】
- 【輸入類型】：拼音輸入法、注音輸入法
- 【注音符號】：閩拼本為基於【羅馬字母】制定之拼音方案；而此專案使用之【注音符號】，乃【方音符號】
  使用之極簡化方音符號。
- 【特性簡介】：
  1. 羅馬拼音字母，鼻化韻母採「前綴識別標示法」，如下行所示；
  2. 【侯選清單】：採兩欄標示〔sⁿia5〕 【ㄒㄥㄧㄚˇ】；
  3. 【聲調標示】：
     - 採【台羅八聲調】；
     - 【拼音輸入法】：使用數值標示聲調，以利閱讀。
     - 【注音輸入法】：使用【閩拼】聲調符號，代替【方音符號】標示聲調。

![2025-11-16_20-05-45](https://github.com/user-attachments/assets/39b91a19-4652-43bc-af81-291a4ccd8cc7)

## 安裝流程

以下說明為下載及安裝作業之摘要參考。

1. **下載及安裝 [RIME 中州韻輸入法引擎](http://rime.im)**；

   不同作業系統的 RIME 名稱：
   - macOS: 鼠鬚管
   - Windows: 小狼毫
   - Linux: 中州韻 (ibus-rime, fcitx-rime, fcitx5-rime)

   【註】： 由於 Linux 作業系統發布版眾多（如：Ubuntu, LinuxMint, ArchLinux）...，
   且 Linux 的各個發布版又有不同的【輸入法框架】，如：iBus, Fcitx 和 Gcin...。
   目前 RIME 在 Linux 作業系統可運作的輸入法框架，有：ibus-rime, fcitx-rime
   及 fcit5-rime 共三種。所以，在安裝 RIME 之前，得先確認 Linux 作業
   系統安裝的【輸入法框架】為何者。

2. **下載及安裝【閩拚輸入法】**。

請參考 [使用安裝程式安裝作業]([https://github.com/AlanJui/rime-bp/wiki](https://github.com/AlanJui/rime-bp/wiki/%E4%BD%BF%E7%94%A8%E5%AE%89%E8%A3%9D%E7%A8%8B%E5%BC%8F%E5%AE%89%E8%A3%9D%E4%BD%9C%E6%A5%AD)) 之操作指引，完成【閩拚輸入方案】之下載及安裝。

### 四聲八調之調名、調號與五度標記調值

<img align="top" width="400" height="" alt="image" src="https://github.com/user-attachments/assets/ceeb0903-ab26-40f4-a5b0-41953c5e82d0" />

<br/><br/>

<img align="top" width="400" height="" alt="image" src="https://github.com/user-attachments/assets/2a9bb132-a38b-4bf5-b289-d72c1ca5b6d7" />

### W聲調圖

<img alt="image" src="https://github.com/user-attachments/assets/dc785e8f-01f0-4d00-be7d-dc64275cc170" />

### 聲調與按鍵對映

<img alt="image" src="https://github.com/user-attachments/assets/996c8da9-add8-4340-92bc-3273879f171d" />

## 注音輸入法

### 方音符號

<img alt="image" src="https://github.com/AlanJui/rime-tlpa/raw/main/docs/static/img/zu_im_hong_im.png" />

### 方音符號按鍵

<img alt="image" src="https://github.com/user-attachments/assets/737558c8-e04d-458a-b3a7-2f5b601595f9" />

### 聲調按鍵

| 調號 | 四聲八調   | 聲調按鍵 | 漢字 | 台語音標 | 按鍵輸入  |
| :--: | :--------- | :------: | :--: | :------- | :-------- |
|  1   | 陰平 (ㄚ)  |  \<SP\>  |  東  | tong1    | ㄊㆲ      |
|  2   | 陰上 (ㄚˋ) |    4     |  黨  | tong2    | ㄊㆲˋ     |
|  3   | 陰去 (ㄚ˪) |    3     |  棟  | tong3    | ㄊㆲ˪     |
|  4   | 陰入 (ㄚ˙) |    7     |  督  | tok4     | ㄊㆦㄎ    |
|  5   | 陽平 (ㄚˊ) |    6     |  同  | tong5    | ㄊㆲˊ     |
|  6   | 陽上 (ㄚˋ) |    4     |  動  | tong6    | ㄊㆲˋ     |
|  7   | 陽去 (ㄚ˫) |    5     |  洞  | tong7    | ㄊㆲ˫     |
|  8   | 陽入 (ㄚ˙) |    7     |  毒  | tok8     | ㄊㆦㄎ˙   |
|  0   | 輕聲 (ㄚ˙) |    7     |  㧒  | hiat0    | ㄏㄧㄚㄊ˙ |

## 拼音輸入法

### 鍵盤按鍵

<img alt="image" src="https://github.com/AlanJui/rime-tlpa/raw/main/docs/static/img/ping_im_gian_buann.png" />

## 聲調按鍵

| 調號 | 四聲八調  | W聲調圖 | 聲調按鍵 | 漢字 | 台語音標 | 按鍵輸入 |
| :--: | :-------- | :------ | :------: | :--: | :------- | :------- |
|  1   | 陰平 (a)  | 高音調  |    ;     |  東  | tong1    | tong;    |
|  7   | 陽去 (ā)  | 中音調  |    -     |  洞  | tong7    | tong-    |
|  3   | 陰去 (à)  | 低音調  |    \_    |  棟  | tong3    | tong\_   |
|  2   | 陰上 (á)  | 高降調  |    \     |  黨  | tong2    | tong\\   |
|  5   | 陽平 (â)  | 低升調  |    /     |  同  | tong5    | tong/    |
|  4   | 陰入 (ah) | 低促調  |    [     |  督  | tok4     | tok[     |
|  8   | 陽入 (a̍h) | 高促調  |    ]     |  毒  | tok8     | tok]     |
|  0   | 輕聲 (a̍h) | 輕聲調  |    .     |  㧒  | hiat0    | tok.     |

## 方音符號與 Unidoce 編碼

### Unicode 編碼區段

「方音符號」有專屬的 Unicode 區段：

方音符號：U+31A0 ～ U+31BF

注音符號：U+3100 ～ U+312F

注音符號擴充：U+31A0 ～ U+31BF

台灣方音符號補充（部分符號會在 Unicode Extensions 或 CJK 擴充區裡）

### 瀏覽字型對方音符號的支援

某些字型不支援【方音符號】；或是會發顯示錯誤之問題。

- 無法顯示【台語注音調號】
  - 陰去調：˪ U+02EA MODIFIER LETTER YIN DEPARTING TONE MARK
  - 陽去調：˫ U+02EB MODIFIER LETTER YANG DEPARTING TONE MARK

- 無法顯示入聲韻尾符號/或是將 ㆻ 顯示成 ㆶ
  - ㆴ U+31B4 BOPOMOFO FINAL LETTER P
  - ㆵ U+31B5 BOPOMOFO FINAL LETTER T
  - ㆶ U+31B6 BOPOMOFO FINAL LETTER K
  - ㆷ U+31B7 BOPOMOFO FINAL LETTER H
  - ㆻ U+31BB BOPOMOFO FINAL LETTER G（收錄於2020年Unicode v.13，當下多數作業系統內建字體都尚未添加此字）

### 查檢工具

想確認某字型是否支援【方音符號】，可借助 Windows 11 內附之軟體工具：[字元對應表](https://support.microsoft.com/zh-tw/office/%E6%8F%92%E5%85%A5-ascii-%E6%88%96-unicode-%E6%8B%89%E4%B8%81%E6%96%87%E5%9E%8B%E7%9A%84%E7%AC%A6%E8%99%9F%E5%92%8C%E5%AD%97%E5%85%83-%E6%A9%9F%E5%99%A8%E7%BF%BB%E8%AD%AF-d13f58d3-7bcb-44a7-a4d5-972ee12e50e0)。

<img width="484" height="578" alt="image" src="https://github.com/user-attachments/assets/78096200-45b0-4c90-a615-2503cef13717" />

**【操作方法】**：

勾選「進階檢視」，告知【字元對應表】軟體，您需使用此方面之功能。然後，在【到 Unicode】欄位，輸入【方音符號】區塊的【起始編碼】：【31A0】，即可定位到 Unicode 字元所對應到的字形樣式。最後，按下【選取】指令按鈕，便能以較舒適的方式檢視及確認。

- U+3100 → 注音符號區塊開始

- U+31A0 → 方音符號區塊開始

**【參考文章】**：

- [用Ruby，寫台語](https://bobtung.medium.com/%E7%94%A8ruby-%E5%AF%AB%E5%8F%B0%E8%AA%9E-3a1e3ed9bf3c)

## 字形

以下建議使用之字形，均為開源、免費字形：

- [吳守禮台語注音字型](https://xiaoxue.iis.sinica.edu.tw/download/wsl_tps_font.htm)

- [思源宋體字（Noto Serif Traditional Chinese](https://fonts.google.com/noto/specimen/Noto+Serif+TC)

- [思源黑體字（Noto Sans Traditional Chinese）](https://fonts.google.com/noto/specimen/Noto+Sans+TC)

- [字咍字咍台語字型](https://buttaiwan.github.io/taigivs/intro)

- [豆腐烏](https://github.com/glll4678/tshiuthau)

- [霞鶩文楷](https://github.com/lxgw/LxgwWenkaiTC)

- [Fira Sans](https://github.com/mozilla/Fira)（羅馬拼音字母美化用字型）

## 中州韻輸入方案參考範例

- [Taigi-TPS 台語方音輸入法](https://github.com/YuRen-tw/rime-taigi-tps)

- [rime-moetaigi 萌台語](https://github.com/whyjz/rime-moetaigi)

- [RIME輸入法 - 閩南語輸入方案](https://github.com/a-thok/rime-hokkien)

- [rime-hokkien-poj](https://github.com/yangwenbo99/rime-hokkien-poj)




