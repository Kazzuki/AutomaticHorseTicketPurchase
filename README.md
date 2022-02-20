# 馬券自動購入システム要件・開発ログ

### 【要件整理】

■購入サイト

[JRAネット投票](https://www.ipat.jra.go.jp/sp/)

■レース結果サイト

[パラメータエラー](https://www.jra.go.jp/JRADB/accessS.html)

![スクリーンショット 2022-02-19 1.06.30.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7f122367-cf60-459a-9205-60ff7e192e55/スクリーンショット_2022-02-19_1.06.30.png)

■As is

- ３画面に各Webページを表示しながら手動で馬券を購入している

■ToBe

- 馬券をある理論を元に自動購入するシステムを構築する

### 【ヒアリング】確認する事

- 最大の掛け金(最大連続レース数)はいくらに設定するか？
- 使用するブラウザは、GoogleChromeでいいか？
    - GoogleChromeのバージョンとPCのOSにあった、Chromedriverのinstall必要
- 

### 【技術選定】言語と主要ライブラリ

- Python
    - Selenium(Webブラウザの操作を自動化するフレームワーク)
    - time(サーバへのリクエスト間隔を調整するライブラリ)
- 選定理由
    - Web操作自動化・スクレイピングなどのライブラリが充実してる
    - UIを作り込む際のライブラリも使用可能ものがある

[開発ログ](https://www.notion.so/73f4f1928981411a8525c91913f9c0dc)

■フロー

- スクレイピング
- 購入
- 結果集計