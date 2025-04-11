import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.stock import Stock
from backend.market import MarketSimulation
import matplotlib.pyplot as plt
import numpy as np
from datetime import time

market = MarketSimulation('XABC', time(0, 0, 0), time(1, 1, 1), 0.0)

stocks = [
    Stock('MON', 'Money Ulimited', 10.0, 1000, 0.0),
    Stock('STO', 'STONG', 10.0, 1000, 0.0),
    Stock('LOO', 'Loomy', 10.0, 1000, 0.0),
    Stock('POM', 'Poom', 10.0, 1000, 0.0),
    Stock('BON', 'Bongo', 10.0, 1000, 0.0),
]

market.addStock(stocks)
print(market.marketValue)
x = []
y = []

for i in range(100):
    x.append(i)
    bb = market.updateAllStocks()
    y.append(market.updateAllStocks())
    print(bb)
xpoints = np.array(x)
ypoints = np.array(y)

plt.plot(xpoints, ypoints)
plt.show()