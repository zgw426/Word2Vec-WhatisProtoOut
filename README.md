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


■ おまけ

Windows環境で`scikit-learn`がインストールできないときはこのサイトが役に立つかも
https://scikit-learn.org/stable/install.html#error-caused-by-file-path-length-limit-on-windows


```
PS C:\> pip install scikit-learn
Collecting scikit-learn
  Using cached scikit_learn-0.24.0-cp38-cp38-win_amd64.whl (6.9 MB)
Requirement already satisfied: joblib>=0.11 in c:\users\user01\appdata\local\packages\pythonsoftwarefoundation.python.3.8_qbz5n2kfra8p0\localcache\local-packages\python38\site-packages (from scikit-learn) (1.0.0)
Requirement already satisfied: numpy>=1.13.3 in c:\users\user01\appdata\local\packages\pythonsoftwarefoundation.python.3.8_qbz5n2kfra8p0\localcache\local-packages\python38\site-packages (from scikit-learn) (1.19.4)
Requirement already satisfied: threadpoolctl>=2.0.0 in c:\users\user01\appdata\local\packages\pythonsoftwarefoundation.python.3.8_qbz5n2kfra8p0\localcache\local-packages\python38\site-packages (from scikit-learn) (2.1.0)
Requirement already satisfied: scipy>=0.19.1 in c:\users\user01\appdata\local\packages\pythonsoftwarefoundation.python.3.8_qbz5n2kfra8p0\localcache\local-packages\python38\site-packages (from scikit-learn) (1.6.0)
Installing collected packages: scikit-learn
ERROR: Could not install packages due to an EnvironmentError: [Errno 2] No such file or directory: 'C:\\Users\\user01\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python38\\site-packages\\sklearn\\datasets\\tests\\data\\openml\\292\\api-v1-json-data-list-data_name-australian-limit-2-data_version-1-status-deactivated.json.gz'
```

```
>>> import matplotlib as mpl
>>> mpl.matplotlib_fname()
'C:\\Users\\user01\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python38\\site-packages\\matplotlib\\mpl-data\\matplotlibrc'
```
