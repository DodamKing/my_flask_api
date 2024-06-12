import FinanceDataReader as fdr
import pprint
import yfinance as yf
import pandas as pd

def search_stock(query: str):
    stocks = pd.read_csv('stocks.csv')
    stocks = stocks[stocks['Name'].str.contains(query, case=False, na=False)]
    print(stocks)
    print(stocks.to_json(orient='records', force_ascii=False))


    # nasdaq = fdr.StockListing('NASDAQ')
    # nasdaq = nasdaq[nasdaq['Name'].str.contains(query, case=False, na=False)]
    # nasdaq = nasdaq[['Symbol', 'Name']]

    # sp500 = fdr.StockListing('S&P500')
    # sp500 = sp500[sp500['Name'].str.contains(query, case=False, na=False)]
    # sp500 = sp500[['Symbol', 'Name']]

    # usetf = fdr.StockListing('ETF/US')
    # usetf = usetf[usetf['Name'].str.contains(query, case=False, na=False)]
    # usetf = usetf[['Symbol', 'Name']]

    # krx = fdr.StockListing('KRX')
    # krx = krx[krx['Name'].str.contains(query, case=False, na=False)]
    # krx = krx[['Code', 'Name']].rename(columns={'Code': 'Symbol'})

    # kretf = fdr.StockListing('ETF/KR')
    # kretf = kretf[kretf['Name'].str.contains(query, case=False, na=False)]
    # kretf = kretf[['Symbol', 'Name']]

    # stocks = pd.concat([nasdaq, sp500, usetf, krx, kretf])
    # pprint.pprint(stocks)
    # stocks.to_csv('stocks.csv')


    # exchange = 'S&P500'
    # stocks = fdr.StockListing(exchange)
    # result = stocks[stocks['Name'].str.contains(query, case=False, na=False)]
    # print(result)

    # return result.to_json(orient='records', force_ascii=False)

search_stock('삼성')

def current_price(symbol):
    ticker = yf.Ticker(symbol)
    current_price1 = ticker.history(period="1d")['Close'].iloc[-1]
    print('1: ', current_price1)

    df = fdr.DataReader(symbol)
    current_price2 = df['Close'].iloc[-1]
    print('2: ', current_price2)
    # return {current_price1, current_price2}

# current_price('qqq')