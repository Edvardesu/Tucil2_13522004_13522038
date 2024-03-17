import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Initialize lists to store the points
x = []
y = []
lines = []

# Function to find the midpoint and store the line endpoints
def findMidPoint(x1, y1, x2, y2):
    ansX = (x1 + x2) / 2
    ansY = (y1 + y2) / 2
    lines.append(((x1, y1), (x2, y2)))
    return ansX, ansY

# Recursive function to generate the bezier curve points
def bezierCurve(leftPointX, leftPointY, controlX, controlY, rightPointX, rightPointY, curIteration, maxIterations):
    if curIteration < maxIterations:
        midPointLeftX, midPointLeftY = findMidPoint(leftPointX, leftPointY, controlX, controlY)
        midPointRightX, midPointRightY = findMidPoint(rightPointX, rightPointY, controlX, controlY)
        midX, midY = findMidPoint(midPointLeftX, midPointLeftY, midPointRightX, midPointRightY)
        
        bezierCurve(leftPointX, leftPointY, midPointLeftX, midPointLeftY, midX, midY, curIteration + 1, maxIterations)
        x.append(midX)
        y.append(midY)
        bezierCurve(midX, midY, midPointRightX,  midPointRightY, rightPointX, rightPointY, curIteration + 1, maxIterations)

# Function to initialize the animation
def init():
    line.set_data([], [])
    return line,

# Animation update function
def update(frame):
    line.set_data([lines[frame][0][0], lines[frame][1][0]], [lines[frame][0][1], lines[frame][1][1]])
    return line,

# Setting up the figure
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
line, = ax.plot([], [], 'r', lw=2)

# Example input
x.append(1) # Start x
y.append(1) # Start y
conX = 5    # Control point x
conY = 10   # Control point y
x.append(9) # End x
y.append(1) # End y
iterations = 4 # Number of iterations

# Generate bezier curve points
bezierCurve(x[0], y[0], conX, conY, x[1], y[1], 0, iterations)

# Create animation
ani = FuncAnimation(fig, update, frames=range(len(lines)), init_func=init, blit=True, interval=500)

plt.show()
