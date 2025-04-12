import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime, timezone, timedelta
from backend.market import MarketSimulation
from backend.stock import Stock



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

# Initialize the plot
plt.ion()  # Turn on interactive mode
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
ax.set_ylim(0, 50)  # Starting from 0–50, will rescale later
ax.set_xlabel("Time (frames)")
ax.set_ylabel("Stock Value ($)")
ax.set_title("Stock Value Simulation")
ax.legend()

# Animation update function
def update(frame):
    x_data.append(frame)
    for stock in market.stocks:
        stock.updateValue()
        y_data[stock.symbol].append(stock.value)
        lines[stock.symbol].set_data(x_data, y_data[stock.symbol])
    
    # Auto-rescale the y-axis after each update
    ax.relim()
    ax.autoscale_view()
    
    # Draw the updated plot
    plt.draw()
    return list(lines.values())  # Return updated lines

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=NUM_FRAMES, blit=False, interval=10, repeat=False  # interval set to 50 ms for faster speed
)

# Save the animation as a GIF while displaying it
ani.save("stock_simulation.gif", writer='pillow', fps=6)  # fps set to 30 for faster GIF
print("✅ Saved as stock_simulation.gif")

# Keep the plot open for a bit after saving
plt.pause(2)
plt.ioff()  # Turn off interactive mode
plt.show()
