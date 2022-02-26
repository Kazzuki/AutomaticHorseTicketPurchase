# 馬券自動購入システム要件・開発ログ

## 【要件整理】
#### AsIsとToBe
- AsIs
    - ３画面に対象Webページを表示しながら手動で馬券を購入している
    - 定形化できる作業であるが、システム化されていないので時間をかけ実行している
- ToBe
    - 馬券を独自のアルゴリズムにのっとり、自動購入できる
    
#### 対象Webページ
- [netkeiba(オッズの確認)](https://race.netkeiba.com/top/)
- [JRA(ホームページ)](https://jra.jp/)
- [JRA(ネット投票)](https://www.ipat.jra.go.jp/sp/)

## 【アーキテクチャ】
![全体像](/doc/architecture.png) 
■スクレイピング先ページ
- [オッズ](https://race.netkeiba.com/odds/index.html?race_id=202206020109)

## 【技術選定】言語・ライブラリ・その他
#### 言語・ライブラリ
- Python
    - Selenium(Webブラウザの操作を自動化するフレームワーク)
    - time(サーバへのリクエスト間隔を調整するライブラリ)
- 選定理由
    - Web操作自動化・スクレイピングなどのライブラリが充実してる
    - UIを作り込む際のライブラリも使用可能ものがある

#### その他
- Notion
    - ドキュメント整理
- diagrams.net(旧：draw.io)
    - アーキテクチャ図作成
- Zoom
    - 開発MTG実施


[開発ログ(非公開)](https://www.notion.so/73f4f1928981411a8525c91913f9c0dc)
