import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'graphGenerators')))

import io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from fastapi import HTTPException

# Single Stock
def stockGraphGenerator(stock, num_frames=100):
    fig, ax = plt.subplots(figsize=(10, 6))

    y_data = stock.history[-num_frames:]
    x_data = list(range(len(y_data)))
    ax.plot(x_data, y_data, label=stock.symbol, color="red")

    ax.set_xlim(0, num_frames)
    ax.set_ylim(0, 20)
    ax.set_xlabel("Time (frames)")
    ax.set_ylabel("Stock Value ($)")
    ax.legend()
    ax.set_title(stock.name)

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()
    return buf
