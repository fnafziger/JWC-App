import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
from datetime import datetime, timezone, timedelta
from backend.market import MarketSimulation
from backend.stock import Stock
import numpy as np

# Add backend to path


# Simulation settings
NUM_FRAMES = 500

# Create a market that is currently open
market = MarketSimulation(
    idCode="ABCD",
    timeOpenUTC=datetime.now(timezone.utc).time(),
    timeCloseUTC=(datetime.now(timezone.utc) + timedelta(hours=1)).time()
)

# Create some stocks
stocks = [
    Stock('MON', 'Money Ulimited', 10.0, 1000, 0.0),
    Stock('STO', 'STONG', 10.0, 1000, 0.0),
    Stock('LOO', 'Loomy', 10.0, 1000, 0.0),
    Stock('POM', 'Poom', 10.0, 1000, 0.0),
    Stock('BON', 'Bongo', 10.0, 1000, 0.0)
]
market.addStock(stocks)

# Init plot
plt.ion()
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['blue', 'green', 'red', 'orange', 'purple']
lines = {}
x_data = []
y_data = {stock.symbol: [] for stock in market.stocks}

# Create line objects for each stock
for i, stock in enumerate(market.stocks):
    line, = ax.plot([], [], label=stock.symbol, color=colors[i])
    lines[stock.symbol] = line

# Plot setup
ax.set_xlim(0, NUM_FRAMES)
ax.set_ylim(8, 12)  # Starting from 0–50, will rescale later
ax.set_xlabel("Time (frames)")
ax.set_ylabel("Stock Value ($)")
ax.legend()
ax.set_title("Live Stock Value Simulation")

# Run simulation
for t in range(NUM_FRAMES):
    x_data.append(t)
    for stock in market.stocks:
        stock.updateValue()
        y_data[stock.symbol].append(stock.value)
        lines[stock.symbol].set_data(x_data, y_data[stock.symbol])

    # Dynamically update limits based on visible data
    ax.relim()
    ax.autoscale_view()
    plt.draw()
    plt.pause(0.1)

plt.ioff()
plt.pause(2)  # Keep window open for a moment
plt.show()
