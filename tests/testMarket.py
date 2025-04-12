import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.market import MarketSimulation
from backend.stock import Stock
import unittest
from datetime import datetime, timezone, timedelta

class TestMarket(unittest.TestCase):
    def setUp(self):
        self.market = MarketSimulation( # open
            idCode="ABCD",
            timeOpenUTC=datetime.now(timezone.utc).time(),
            timeCloseUTC=(datetime.now(timezone.utc) + timedelta(hours=1)).time()
        )
        self.market_closed = MarketSimulation(
            idCode="ABCD",
            timeOpenUTC=(datetime.now(timezone.utc) + timedelta(hours=1)).time(),
            timeCloseUTC=(datetime.now(timezone.utc) + timedelta(hours=2)).time()
        )
    
    def test_isOpen_open(self):
        self.assertTrue(self.market.isOpen())
    
    def test_isOpen_closed(self):
        self.assertFalse(self.market_closed.isOpen())
    
    def test_addStock_single(self):
        stock = Stock("AAPL", "Apple", 10.0, 1000)
        self.market.addStock(stock)
        self.assertEqual(len(self.market.stocks), 1)
        self.assertIs(self.market.stocks[0], stock)
    
    def test_addStock_multiple(self):
        stocks = [Stock("AAPL", "Apple", 10.0, 1000),
                  Stock("TSLA", "Tesla", 10.0, 1000)]
        self.market.addStock(stocks)
        self.assertEqual(len(self.market.stocks), 2)
        self.assertIs(self.market.stocks[0], stocks[0])
        self.assertIs(self.market.stocks[1], stocks[1])
        