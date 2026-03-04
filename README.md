# ClawRouter Docs

這個 repo 是 ClawRouter 文件站，使用 Docsify 呈現，內容來源為 NewAPI 遷移後的 Markdown。

## 給同事的入口
- Repo：[clawrouter-docs](https://github.com/kristine-build/clawrouter-docs)
- 文件首頁：[docs/_index.md](docs/_index.md)
- 側欄定義結果：[docs/_sidebar.md](docs/_sidebar.md)

## 目錄約定
- 根目錄入口：`index.html`
- 部署設定：`vercel.json`
- 側欄來源：`sidebar_source.txt`
- 文件內容：`docs/`
- 自動化腳本：`scripts/`

## 更新 sidebar 與重建文件
1. 編輯 `sidebar_source.txt`（2 個空白縮排一層）。
2. 在 repo 根目錄執行：

```bash
python3 scripts/build_docs.py
```

此命令會自動：
- 修正誤提交的 `*.html.txt / *.md.txt / *.json.txt`
- 清理 `docs/*.md`（保留 code fence 內容）
- 生成 `docs/_sidebar.md`
- 生成 `docs/_missing.txt`（未成功映射節點）
- 生成 `docs/_mapping.json`（映射信心與原因）

## 備註
- 若有檔名衝突，會保留 `.txt` 原檔並輸出 `docs/_rename_collisions.txt`。
