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
    df = fdr.DataReader(symbol)  # 종목의 데이터 가져오기
    if not df.empty:
        price = df['Close'].iloc[-1]  # 가장 최근 종가 가져오기
        return {"symbol": symbol, "price": float(price)}
    return {"error": "Symbol not found"}