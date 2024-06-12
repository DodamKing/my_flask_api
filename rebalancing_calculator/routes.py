from flask import Blueprint, request, jsonify
import FinanceDataReader as fdr
import pandas as pd

rc = Blueprint('rebalancing-calculator', __name__)

@rc.get("/search/<query>")
def search_stock(query: str):
    try:
        stocks = pd.read_csv('stocks.csv')
        result = stocks[stocks['Name'].str.contains(query, case=False, na=False)]

        return jsonify(result.to_json(orient='records', force_ascii=False)), 200
    
    except Exception as e:
        print(f"검색 에러 남: {e}")
        return jsonify(), 500

@rc.get("/price/<symbol>")
def get_stock_price(symbol: str):
    try:
        price = None
        df = fdr.DataReader(symbol)

        if not df.empty and 'Close' in df.columns:
            price = int(df['Close'].iloc[-1])
            return jsonify({"symbol": symbol, "price": price}), 200
        
        else: return jsonify(), 400

    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")

        return jsonify({"error": f"Could not retrieve data for {symbol}"}), 500


@rc.get("/search/<by>/<query>")
def get_stocks(by, query: str):
    exchange = request.args.get('exchange', 'ETF/KR')
    stocks = fdr.StockListing(exchange)

    if by == 'name':
        result = stocks[stocks['Name'].str.contains(query, case=False, na=False)]

        return result.to_json(orient='records', force_ascii=False)

    elif by == 'symbol':
        stock = stocks[stocks['Symbol'] == query]

        if not stock.empty:
            price = int(stock['Price'].iloc[0])
            return {"symbol": query, "price": price}
        else:
            return 'no symbol'