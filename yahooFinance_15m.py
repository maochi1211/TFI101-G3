import yfinance as yf
import yahoo_fin.stock_info as si

path = "C:\\Users\\TibeMe_user\\Desktop\\Project\\nasdaq\\"

tickers1 = si.tickers_sp500(True)['Symbol']
tickers2 = si.tickers_nasdaq(True)['Symbol']
# tickers = list(set(tickers2)-set(tickers1))

# 語法是 yf.download(
#    股票代號,
#    period=日期範圍 (1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max)
#    interval=頻率 (1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo)
#    )
c = 1
for symbol in tickers1:
    print(c)
    try:
        quote = si.get_quote_table(symbol)

        if quote["Avg. Volume"] > 5000000:
            print(symbol)
            yahoo = yf.download(symbol, period='1y', interval='1d')
            print(quote["Avg. Volume"])

            yahoo.to_csv(path + '{}.csv'.format(symbol))

    except:
        pass
    c+=1
