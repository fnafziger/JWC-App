import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.stock import Stock
from backend.market import MarketSimulation
from fastapi import FastAPI # install with "pip install fastapi uvicorn" run with "uvicorn main:app --reload"
from fastapi.middleware.cors import CORSMiddleware
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

async def continuouslyUpdateStocks():
    while True:
        for stock in market.stocks:
            stock.updateValue()
        await asyncio.sleep(2)

@app.on_event("startup")
async def start_price_updater():
    asyncio.create_task(continuouslyUpdateStocks())

@app.get("/")
def read_root():
    return {"msg": "API is running."}

@app.get("/{ticker}")
def getPrice(ticker):
    target = stock_dict.get(ticker)
    if target: return {"symbol": ticker, "price": target.value}
    else: return {"error": "Stock not found."}

class Trade(BaseModel):
    ticker: str
    quantity: int
    action: str  # buy or sell

@app.post("/trade")
async def make_trade(trade: Trade):
    print(f"Received: {trade.action.upper()} {trade.quantity} shares of {trade.ticker}")
    return {
        "message": f"{trade.action.upper()} {trade.quantity} shares of {trade.ticker.upper()}",
        "status": "success"
    }