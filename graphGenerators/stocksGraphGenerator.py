import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'graphGenerators')))

import io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# All Stocks
def stocksGraphGenerator(market, num_frames=100):
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['blue', 'green', 'red', 'orange', 'purple']

    for i, stock in enumerate(market.stocks):
        y_data = stock.history[-num_frames:] # fill the graph out to 100 frames then starts deleting the old data (stock prices)

        x_data = list(range(len(y_data))) # [0, 1, 2, 3, ..., 99] if num_frames = 100
        ax.plot(x_data, y_data, label=stock.symbol, color=colors[i % len(colors)])

    ax.set_xlim(0, num_frames)
    ax.set_ylim(0, 20)
    ax.set_xlabel("Time (frames)")
    ax.set_ylabel("Stock Value ($)")
    ax.legend()
    ax.set_title("All Stocks")

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf



