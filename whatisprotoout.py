
from janome.tokenizer import Tokenizer
from gensim.models import Word2Vec
import itertools
from sklearn.decomposition import PCA
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib import rcParams
import random

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'Noto Sans CJK JP']

path = "./data/"
lfiles = [
    "01.txt","02.txt","03.txt","04.txt","05.txt","06.txt","07.txt","08.txt","09.txt","10.txt",
    "11.txt","12.txt","13.txt","14.txt","15.txt","16.txt","17.txt","18.txt","19.txt","20.txt",
    "21.txt","22.txt","23.txt","24.txt","25.txt","26.txt","27.txt","28.txt","29.txt","30.txt",
    "41.txt","42.txt","43.txt","44.txt","45.txt","46.txt","47.txt","48.txt","49.txt","40.txt",
    "51.txt","52.txt","53.txt","54.txt","55.txt"
]

t = Tokenizer() # Tokenneizerインスタンスの生成 
word_all = []   # 全ての単語をリスト形式で格納

### 関数 ###
# テキストを引数として、形態素解析の結果、名詞・動詞・形容詞の原形のみを配列で抽出する関数を定義 
def extract_words(text):
    tokens = t.tokenize(text)
    return [token.base_form for token in tokens 
        if token.part_of_speech.split(',')[0] in['名詞', '動詞','形容詞']]
# 類似単語の表示
def model_simulate( target_word ):
    try:
        print("■ {0}".format(target_word) )
        ret = model.wv.most_similar(positive=[target_word]) 
        for item in ret:
            print("\t{0} ({1})".format(item[0], item[1]) )
    except:
        print("[ERROR] {0}".format(target_word) )

def replaceStr(data):
    data = data.lower()
    # 文字列を置換する一覧 『 変換前：変換後 』
    dlist = {
        "protoout":"プロトアウト",
        "studio":"スタジオ",
        "protoout studio":"プロトアウトスタジオ",
        "protoout.studio":"プロトアウトスタジオ",
        "プロトアウト スタジオ":"プロトアウトスタジオ",
        "\"":"",
        "/":"",
        "画像":"",
        "0":"",
        "1":"",
        "2":"",
        "3":"",
        "4":"",
        "5":"",
        "6":"",
        "7":"",
        "8":"",
        "9":"",
        "月":"",
        "期生":"",
        "期":"",
        "土井":"",
        "com":"",
        ".":"",
        "-":"",
        "さん":"",
        "のびすけ":"",
        "コロナ":"",
        "(":"",
        ")":"",
        ":":"",
        "１":"",
        "飲む":"",
        "変化":"",
        "事":"",
    }

    for d in dlist:
        data = data.replace(d,dlist[d])
    return(data)

for file in lfiles:
    f = open( path + file, 'r', encoding='UTF-8')
    data = f.read()
    data = replaceStr(data)
    sentences = data.split('。')    # 全体のテキストを句点('。')で区切った配列にする。 
    word_list = [extract_words(sentence) for sentence in sentences] # それぞれの文章を単語リストに変換(処理に数分かかります)
    word_all += word_list
    f.close()

model = Word2Vec(
        word_all, 
        size=200,       # size: 圧縮次元数
        min_count=35,   # min_count: 出現頻度の低いものをカットする
        window=5,       # window: 前後の単語を拾う際の窓の広さを決める
        iter=100        # iter: 機械学習の繰り返し回数(デフォルト:5)十分学習できていないときにこの値を調整する
    )

target_word_list = [
    "プロトアウトスタジオ",
    "プロダクト",
    "アウトプット",
    "クラウドファンディング",
    "qiita",
]

for target_word in target_word_list:
    model_simulate( target_word )

########################################
# 参考：https://programming-info.dream-target.jp/python_word2vec
# プロットしたい単語を設定する
# 以下の例は、fire,earthquakeなどを設定しています。
words = []

for word in model.wv.index2word:
    words.append([word,"r"])

length = len(words)
data = []
 
j = 0
while j < length:
    data.append(model[words[j][0]])
    j += 1

#主成分分析により２次元に圧縮する
pca = PCA(n_components=2)
pca.fit(data)
data_pca= pca.transform(data)

length_data = len(data_pca)

### グラフ化 ######################

fig=plt.figure(figsize=(20,12),facecolor='w')
ax = plt.axes()

plt.rcParams["font.size"] = 10
i = 0
while i < length_data:
    plt.plot(data_pca[i][0], data_pca[i][1], ms=5.0, zorder=2, marker="x", color=words[i][1])   #点プロット
    plt.annotate(words[i][0], (data_pca[i][0], data_pca[i][1]), size=12)    #文字プロット
    for wd in target_word_list:
        if( words[i][0] == wd ):
            # 円を描く。色はランダム
            r=random.uniform(1,0)
            g=random.uniform(1,0)
            b=random.uniform(1,0)
            c = patches.Circle(xy=(data_pca[i][0], data_pca[i][1]), label=wd, radius=1.0, color=(r,g,b,0.5) )
            ax.add_patch(c)
    i += 1
ax.legend()
plt.show()
