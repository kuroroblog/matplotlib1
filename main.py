import pandas as pd
import matplotlib.pyplot as plt

# テキストをまとめる。
satisfactionText = '満足度'
purchasesText = '購買回数'
subSatisfactionText = '満足度 - 満足度平均値'
subPurchasesText = '購買回数 - 購買回数平均値'

# データフレームを作成する。
df = pd.DataFrame({satisfactionText: [85, 73, 52, 88, 98, 81, 92, 87, 96, 88], purchasesText: [8, 6, 2, 2, 9, 7, 9, 8, 5, 4]},
                  index=['１人目', '２人目', '3人目', '4人目', '5人目', '6人目', '7人目', '8人目', '9人目', '10人目'])

# 満足度の平均値を算出する。
aveSatisfaction = df.mean()[satisfactionText].astype('int')
# 購買回数の平均値を算出する。
avePurchases = df.mean()[purchasesText].astype('int')

# 満足度 - 満足度の平均値 を算出する。
df[subSatisfactionText] = df[satisfactionText] - aveSatisfaction
# 購買回数 - 購買回数の平均値 を算出する。
df[subPurchasesText] = df[purchasesText] - avePurchases

# フォントの設定を行う。
plt.rcParams['font.family'] = 'Hiragino Sans'

# タイトルの入力
plt.title("タイトルを入力してください。")
# x軸のラベル入力
plt.xlabel(satisfactionText)
# y軸のラベル入力
plt.ylabel(purchasesText)
# grid(目盛)を入れるかどうか
plt.grid(True)

# https://www.delftstack.com/ja/howto/matplotlib/how-to-plot-horizontal-and-vertical-line-in-matplotlib/#axvline-%E3%81%A7%E5%9E%82%E7%9B%B4%E7%B7%9A%E3%82%92%E3%83%97%E3%83%AD%E3%83%83%E3%83%88%E3%81%99%E3%82%8B
plt.axvline(x=aveSatisfaction, ymin=0, ymax=1.0)
plt.axhline(y=avePurchases, xmin=0, xmax=1.0)

# https://pythondatascience.plavox.info/matplotlib/%E6%95%A3%E5%B8%83%E5%9B%B3
plt.scatter(df[satisfactionText], df[purchasesText], s=50,
            c="pink")

# 画像の書き出し処理を行う。
plt.savefig("./result.png")
