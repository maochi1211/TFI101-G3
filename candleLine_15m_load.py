import mplfinance as mpf
import yahoo_fin.stock_info as si
import pandas as pd
import matplotlib

matplotlib.use("Agg")

path = 'C:\\Users\\TibeMe_user\\Desktop\\Project\\nasdaq\\'

#-------------------------------------------
# 存放csv的檔案夾
import os
tickers = os.listdir(path)
tickers.sort(key=str.lower)
#-------------------------------------------

def k_candle_15m_chart(symbol):
    try:
        df = pd.read_csv(path + '{}.csv'.format(symbol), index_col=0, parse_dates=True)
        df.index.name = 'Date'

        df = df.drop(columns='Close')
        df = df.drop(columns='Volume')  # Volume is zero anyway for this intraday data set
        df.rename(columns={'Adj Close': 'Close'}, inplace=True)

        df = df.reindex(columns=['Open', 'Close', 'High', 'Low'])

        saveImgPath = 'C:/Users/TibeMe_user/Desktop/Project/nasdaq_k/'

        mc = mpf.make_marketcolors(up='r', down='g',
                                   edge='inherit',
                                   wick='black')
        s = mpf.make_mpf_style(marketcolors=mc)

        df_img = mpf.plot(df, type='candle', style=s, title=symbol, savefig=saveImgPath + '{}_1d.jpg'.format(symbol), figsize=(9.6, 5.4))
        return df_img
    except:
        pass

for symbol in tickers:
    str2 = "."
    ticker = symbol[:symbol.index(str2)]
    k_candle_15m_chart(ticker)
    print(ticker)


