from backend.stock import Stock
from backend.market import MarketSimulation
from fastapi import FastAPI, HTTPException # install with "pip install fastapi uvicorn" run with "uvicorn main:app --reload"
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from graphGenerators.stocksGraphGenerator import stocksGraphGenerator
from graphGenerators.stockGraphGenerator import stockGraphGenerator
from pydantic import BaseModel
from datetime import datetime, timezone, timedelta
import asyncio

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Market
market = MarketSimulation(
    idCode="ABCD",
    timeOpenUTC=datetime.now(timezone.utc).time(),
    timeCloseUTC=(datetime.now(timezone.utc) + timedelta(hours=1)).time()
)
stocks = [
        Stock('MON', 'Money Ulimited', 10.0, 1000, 0.0),
        Stock('STO', 'STONG', 10.0, 1000, 0.0),
        Stock('LOO', 'Loomy', 10.0, 1000, 0.0),
        Stock('POM', 'Poom', 10.0, 1000, 0.0),
        Stock('BON', 'Bongo', 10.0, 1000, 0.0),
    ]
stock_dict = {stock.symbol: stock for stock in stocks}
market.addStock(stocks)

# Stocks and Updating
async def continuouslyUpdateStocks():
    while True:
        for stock in market.stocks:
            stock.updateValue()
        await asyncio.sleep(0.5)

@app.on_event("startup")
async def start_price_updater():
    asyncio.create_task(continuouslyUpdateStocks())

# Graphs
@app.get("/stock-graph")
def getStocksGraph():
    if not market.stocks:
        raise HTTPException(status_code=404, detail="No stocks in market")
    img_buf = stocksGraphGenerator(market, num_frames=100)
    return StreamingResponse(img_buf, media_type="image/png")

@app.get("/{ticker}-stock-graph")
def getStockGraph(ticker):
    img_buf = stockGraphGenerator(stock_dict[ticker], num_frames=100)
    return StreamingResponse(img_buf, media_type="image/png")

# Ticker Input and Price
@app.get("/tickers")
def getTickers():
    tickerAndNameList = []
    for ticker in sorted(stock_dict):
        target = stock_dict.get(ticker) # not the best name for this var but idk what else to name it
        tickerAndNameString = ticker + ": " + target.name
        tickerAndNameList.append(tickerAndNameString)
    return tickerAndNameList

@app.get("/{ticker}")
def getPrice(ticker):
    target = stock_dict.get(ticker)
    if target: return {"symbol": ticker, "price": target.value}
    else: return {"error": "Stock not found."}

# Trading 
class Trade(BaseModel):
    ticker: str
    name: str
    quantity: int
    action: str  # buy or sell

@app.post("/trade")
async def make_trade(trade: Trade):
    print(f"{trade.action.capitalize()} order for {trade.quantity} shares of {trade.name} ({trade.ticker.upper()}) received.")
    return {
        "message": f"{trade.action.capitalize()} order for {trade.quantity} shares of {trade.name} ({trade.ticker.upper()}) received.",
        "status": "success"
    }
