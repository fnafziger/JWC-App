import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.market import MarketSimulation
from backend.stock import Stock
import matplotlib.pyplot as plt
import numpy as np
from datetime import time

for t in range(5):

    market = MarketSimulation('XABC', time(0, 0, 0), time(1, 1, 1), 0.0)
    market2 = MarketSimulation('XABD', time(0, 0, 0), time(1, 1, 1), 0.0)
    market3 = MarketSimulation('XABD', time(0, 0, 0), time(1, 1, 1), 0.0)
    market4 = MarketSimulation('XABD', time(0, 0, 0), time(1, 1, 1), 0.0)
    market5 = MarketSimulation('XABD', time(0, 0, 0), time(1, 1, 1), 0.0)


    stocks = [
        Stock('MON', 'Money Ulimited', 10.0, 1000, 0.0),
        Stock('STO', 'STONG', 10.0, 1000, 0.0),
        Stock('LOO', 'Loomy', 10.0, 1000, 0.0),
        Stock('POM', 'Poom', 10.0, 1000, 0.0),
        Stock('BON', 'Bongo', 10.0, 1000, 0.0),
    ]

    stocks2 = [
        Stock('MON', 'Money Ulimited', 10.0, 1000, 0.0),
        Stock('STO', 'STONG', 10.0, 1000, 0.0),
        Stock('LOO', 'Loomy', 10.0, 1000, 0.0),
        Stock('POM', 'Poom', 10.0, 1000, 0.0),
        Stock('BON', 'Bongo', 10.0, 1000, 0.0),
    ]
    stocks3 = [
        Stock('MON', 'Money Ulimited', 10.0, 1000, 0.0),
        Stock('STO', 'STONG', 10.0, 1000, 0.0),
        Stock('LOO', 'Loomy', 10.0, 1000, 0.0),
        Stock('POM', 'Poom', 10.0, 1000, 0.0),
        Stock('BON', 'Bongo', 10.0, 1000, 0.0),
    ]
    stocks4 = [
        Stock('MON', 'Money Ulimited', 10.0, 1000, 0.0),
        Stock('STO', 'STONG', 10.0, 1000, 0.0),
        Stock('LOO', 'Loomy', 10.0, 1000, 0.0),
        Stock('POM', 'Poom', 10.0, 1000, 0.0),
        Stock('BON', 'Bongo', 10.0, 1000, 0.0),
    ]
    stocks5 = [
        Stock('MON', 'Money Ulimited', 10.0, 1000, 0.0),
        Stock('STO', 'STONG', 10.0, 1000, 0.0),
        Stock('LOO', 'Loomy', 10.0, 1000, 0.0),
        Stock('POM', 'Poom', 10.0, 1000, 0.0),
        Stock('BON', 'Bongo', 10.0, 1000, 0.0),
    ]
    # stocks = Stock('BON', 'Bongo', 100.0, 1000, 0.0)


    market.addStock(stocks)
    market2.addStock(stocks2)
    market3.addStock(stocks3)
    market4.addStock(stocks4)
    market5.addStock(stocks5)
    x = []
    y = []
    z = []
    w = []
    v = []
    u = []

    for i in range(518400 * 5):
        x.append(i / 1440)
        bb = market.updateAllStocks()
        cc = market2.updateAllStocks()
        dd = market3.updateAllStocks()
        ee = market4.updateAllStocks()
        ff = market5.updateAllStocks()
        y.append(bb)
        z.append(cc)
        w.append(dd)
        v.append(ee)
        u.append(ff)
        
    xpoints = np.array(x)
    ypoints = np.array(y)
    zpoints = np.array(z)
    wpoints = np.array(w)
    vpoints = np.array(v)
    upoints = np.array(u)

    # plt.plot(xpoints, zpoints)
    # plt.show()

    plt.plot(xpoints, ypoints)
    plt.plot(xpoints, zpoints)
    plt.plot(xpoints, wpoints)
    plt.plot(xpoints, vpoints)
    plt.plot(xpoints, upoints)

    print(str(t + 1) + "/5")

plt.show()