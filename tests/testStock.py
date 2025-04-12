import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.market import MarketSimulation
from backend.stock import Stock
import unittest
from datetime import time, datetime, timezone, timedelta

class TestStock(unittest.TestCase):
    def setUp(self):
        self.stock = Stock(
            
        )