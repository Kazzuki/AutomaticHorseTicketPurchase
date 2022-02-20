## 開発ステップ
#### STEP 1
- 東京競馬場のみ
- スクレイピングした情報を元に、各レースに¥100をかけていく
- レース結果を、各レース終了後、集計しJSONで出力

#### STEP N
- 東京、阪神、小倉で購入する
- 独自のアルゴリズム(後述)を元に、各レースにかける
- レース結果を、各レース終了後、集計し出力する
- トータルの集計結果をリッチなUIで提供

## アルゴリズム
![アルゴリズム](/doc/algorism.png) 

## ヒアリングする事
- 最大の掛け金(最大連続レース数)はいくらに設定するか？
- 使用するブラウザは、GoogleChromeでいいか？
    - GoogleChromeのバージョンとPCのOSにあった、Chromedriverのinstall必要
- 購入するタイミングと、レースが終わってからの次の購入フローに移るまでの作業内容