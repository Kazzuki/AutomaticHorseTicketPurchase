# 馬券自動購入システム要件・開発ログ

### 【要件整理】

■対象サイト
- [オッズ確認サイト](https://race.netkeiba.com/top/)
- [JRAネット投票](https://www.ipat.jra.go.jp/sp/)

■AsIsとToBe
- AsIs
    - ３画面に各Webページを表示しながら手動で馬券を購入している
- ToBe
    - 馬券をある理論を元に自動購入するシステムを構築する

### アーキテクチャ
![全体像](/doc/architecture.png) 

### 【ヒアリング】確認する事

- 最大の掛け金(最大連続レース数)はいくらに設定するか？
- 使用するブラウザは、GoogleChromeでいいか？
    - GoogleChromeのバージョンとPCのOSにあった、Chromedriverのinstall必要

### 【技術選定】言語・ライブラリ・その他
■言語・ライブラリ
- Python
    - Selenium(Webブラウザの操作を自動化するフレームワーク)
    - time(サーバへのリクエスト間隔を調整するライブラリ)
- 選定理由
    - Web操作自動化・スクレイピングなどのライブラリが充実してる
    - UIを作り込む際のライブラリも使用可能ものがある

■その他
- Notion
    - ドキュメント整理
- diagrams.net(旧：draw.io)
    - アーキテクチャ図作成
- Zoom
    - 開発MTG実施


[開発ログ(非公開)](https://www.notion.so/73f4f1928981411a8525c91913f9c0dc)
