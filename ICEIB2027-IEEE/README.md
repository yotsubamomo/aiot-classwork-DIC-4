# ICEIB2027-IEEE：Moto Touring Copilot 會議論文（Overleaf 用）

IEEEtran `[conference]` 格式的英文稿，**用 pdfLaTeX 編譯**（Overleaf 預設）。中文版的課程 Proposal 仍在 `moto-touring-copilot/docs/proposal/`。

## 上傳到 Overleaf

1. 把這個資料夾的檔案打包成 zip，`main.tex` 要在 zip 的最上層。
2. Overleaf → New Project → Upload Project → 選這個 zip。
3. 如果是沿用之前的專案，記得把 Compiler 從 XeLaTeX 改回 **pdfLaTeX**（左下角齒輪 → Compiler）。用 XeLaTeX 也能編譯，但字型會跟 IEEE 範本不同。

## 檔案

| 檔案 | 內容 | 狀態 |
| --- | --- | --- |
| `main.tex` | 文件類別、套件、標題、作者 | 作者欄位待填 |
| `sections/00_abstract.tex` | 英文摘要與 Index Terms | 完成（約 300 字，需確認 ICEIB 的字數上限） |
| `sections/01_introduction.tex` | 緒論（A–F 架構，英文） | 完成，由中文 `01-introduction.md` 翻譯 |
| `sections/02_related_work.tex` | 相關研究 | 骨架，已接上比較表 |
| `sections/03_proposed_scheme.tex` | ①–⑧ 架構、Agent、配速模型、演算法 | 模組說明完成，其餘為骨架 |
| `sections/04_experiments.tex` | 實驗設計 E1–E4 | 實驗表格完成，預期成果待補 |
| `sections/05_conclusion.tex` | 結論 | 骨架 |
| `tables/comparison.tex` | 既有方法與本系統的比較 | 只用緒論已查證的內容填寫 |
| `references.bib` | 參考文獻 [I1]–[I21] | Related Work 的 [1]–[19] 尚未加入 |
| `figures/architecture.pdf` | 英文架構圖 | **待補**；檔案放進來之前，PDF 上會顯示外框佔位 |

還沒完成的地方都用 `\todo{}` 標示，PDF 上會顯示粗體的 **[TODO: …]**。投稿前在 Overleaf 搜尋 `TODO`，確認全部清掉。

## 注意事項

- 中文 Proposal 裡的架構圖和流程圖標籤是中文，不能直接放進英文論文，需要重畫成英文版。
- 中文來源的英文標題是我們自己翻譯的，`references.bib` 裡都標了 `(in Chinese)`。[I20] 作者姓名的拼音也是我們拼的，有官方英文署名的話以署名為準。
- 還沒做實驗前，`04_experiments.tex` 只寫實驗設計和預期成果，不放結果。
- `.tex` 檔裡不能出現中文字，pdfLaTeX 會報錯。

## 原始資料

從 `aiot-classwork-DIC-3` 複製到這個 repo 的 `dic3-參考資料/`：

| 檔案 | 用途 |
| --- | --- |
| `dic3-參考資料/_AIoT_-DA_L16_打造_AGENT_(目標系統架構PDAC)OVERLEAF.pdf` | L16 講義：ICEIB 2027 要求（英文、4–8 頁、2027-03-01 交摘要）與本專案結構 |
| `dic3-參考資料/期末專題提案作業規範.pdf` | 課程作業規範（A–F、Related Work 表格、①–⑧ 架構、不得捏造結果） |
| `dic3-參考資料/delivery/03-ieee-abstract-en.md` | `00_abstract.tex` 的來源 |
| `dic3-參考資料/delivery/01-a-to-f-revision.md` | A–F 修正稿，文末列出查證後不採用的說法 |
| `dic3-參考資料/delivery/02-summary-300.md` | 300 字中文摘要 |

其餘章節的中文原稿（Introduction、Related Work、Proposed Scheme 與評估計畫）在 `moto-touring-copilot/docs/proposal/source/`，各 `.tex` 檔開頭的註解有寫對應的檔案。
