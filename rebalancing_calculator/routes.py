from flask import Blueprint, request
import FinanceDataReader as fdr

rc = Blueprint('rebalancing-calculator', __name__)

@rc.get("/search/<query>")
def search_stock(query: str):
    exchange = request.args.get('exchange', 'ETF/KR')
    stocks = fdr.StockListing(exchange)
    result = stocks[stocks['Name'].str.contains(query, case=False, na=False)]

    return result.to_json(orient='records', force_ascii=False)

@rc.get("/price/<symbol>")
def get_stock_price(symbol: str):
    exchange = request.args.get('exchange', 'ETF/KR')
    stocks = fdr.StockListing(exchange)
    stock = stocks[stocks['Symbol'] == symbol]
    price = int(stock['Price'].iloc[0])

    return {"symbol": symbol, "price": price}

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