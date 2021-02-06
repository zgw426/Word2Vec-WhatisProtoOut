## Word2Vec-WhatisProtoOut

スクリプトの実行コマンド(Python3 スクリプトです)

```
$ python whatisprotoout.py
```

■ 学習データの格納

以下のように作成した学習データをdataディレクトリ配下に格納します。

```console
│  whatisprotoout.py
└─data
        01.txt
        02.txt
          :
```

■ 学習データをdataディレクトリ配下に格納します。lfilesに学習データのファイル名を設定します。

```
path = "./data/"
lfiles = [
    "01.txt","02.txt","03.txt","04.txt","05.txt","06.txt","07.txt","08.txt","09.txt","10.txt",
    "11.txt","12.txt","13.txt","14.txt","15.txt","16.txt","17.txt","18.txt","19.txt","20.txt",
    "21.txt","22.txt","23.txt","24.txt","25.txt","26.txt","27.txt","28.txt","29.txt","30.txt",
    "41.txt","42.txt","43.txt","44.txt","45.txt","46.txt","47.txt","48.txt","49.txt","40.txt",
    "51.txt","52.txt","53.txt","54.txt","55.txt"
]
```

■ 学習データ内の文字列を調整したい単語を`dlist`に設定します。単語`protoout`を`プロトアウト`に変換する場合は、`"protoout":"プロトアウト"`と設定します。

```
dlist = {
    "protoout":"プロトアウト",
    "studio":"スタジオ",
    "protoout studio":"プロトアウトスタジオ",
    "protoout.studio":"プロトアウトスタジオ",
    "プロトアウト スタジオ":"プロトアウトスタジオ",
    "\"":"",
    "/":"",
}
```

■ target_word_listに登録した単語について以下を実行します。
・類似単語を表示
・グラフでその単語を中心に円を描画

```
target_word_list = [
    "プロトアウトスタジオ",
    "プロダクト",
    "アウトプット",
    "クラウドファンディング",
    "qiita"
]
```

※以下のメッセージが出力されますが一応動きます。（このメッセージが出ない対処方法あるらしい、いつかなおすかも）

```
whatisprotoout.py:129: DeprecationWarning: Call to deprecated `__getitem__` (Method will be removed in 4.0.0, use self.wv.__getitem__() instead).
```
