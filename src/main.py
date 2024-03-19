import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from termcolor import colored

# Initialize lists to store the points
x = []
xBrute = []
y = []
lines = []
yBrute = []

# Function to find the midpoint and store the line endpoints
def findMidPoint(x1, y1, x2, y2, animation):
    ansX = (x1 + x2) / 2
    ansY = (y1 + y2) / 2
    if(animation == "ya"):
        lines.append(((x1, y1), (x2, y2)))
        drawLines(x1, y1, x2, y2)
    return ansX, ansY

def drawLines(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], linestyle='--', color='black', marker='o', markersize=3)

# Recursive function to generate the bezier curve points
def bezierCurve(leftPointX, leftPointY, controlX, controlY, rightPointX, rightPointY, curIteration, maxIterations, animation):
    if curIteration < maxIterations:
        midPointLeftX, midPointLeftY = findMidPoint(leftPointX, leftPointY, controlX, controlY, animation)
        midPointRightX, midPointRightY = findMidPoint(rightPointX, rightPointY, controlX, controlY, animation)
        midX, midY = findMidPoint(midPointLeftX, midPointLeftY, midPointRightX, midPointRightY, animation)
        # kiri
        bezierCurve(leftPointX, leftPointY, midPointLeftX, midPointLeftY, midX, midY, curIteration + 1, maxIterations, animation)
        x.append(midX)
        y.append(midY)
        # kanan
        bezierCurve(midX, midY, midPointRightX,  midPointRightY, rightPointX, rightPointY, curIteration + 1, maxIterations, animation)

# Brute Force Approach
def b(P0, P1, P2, t):
    return (1-t)**2 * P0 + 2*(1-t)*t*P1 + t*t*P2        

def bruteForce(P0X, P0Y, P1X, P1Y, P2X, P2Y, iteration):
    t = 1/(2**iteration)
    while t <= 1:
        ansX = b(P0X, P1X, P2X, t)
        ansY = b(P0Y, P1Y, P2Y, t)
        xBrute.append(ansX)
        yBrute.append(ansY)
        t += 1/(2**iteration)

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

# input
print("  ______           _ __   ___      ______    __                     __   ___        ______                                         ")
print(" /_  __/_  _______(_) /  |__ \    / ____/___/ /_  ______ __________/ /  ( _ )      / ____/________ _____  ________  ______________ ")
print("  / / / / / / ___/ / /   __/ /   / __/ / __  / / / / __ `/ ___/ __  /  / __ \/|   / /_  / ___/ __ `/ __ \/ ___/ _ \/ ___/ ___/ __ \\")
print(" / / / /_/ / /__/ / /   / __/   / /___/ /_/ / /_/ / /_/ / /  / /_/ /  / /_/  <   / __/ / /  / /_/ / / / / /__/  __(__  ) /__/ /_/ /")
print("/_/  \__,_/\___/_/_/   /____/  /_____/\__,_/\__,_/\__,_/_/   \__,_/   \____/\/  /_/   /_/   \__,_/_/ /_/\___/\___/____/\___/\____/ ")
                                                                                                                                   
tempX = int(input("Titik awal x : "))
tempY = int(input("Titik awal y : "))
x.append(tempX)
xBrute.append(tempX)
y.append(tempY)
yBrute.append(tempY)

conX = int(input("Titik kontrol x : "))
conY = int(input("Titik kontrol y : "))

tempX = int(input("Titik akhir x : "))
tempY = int(input("Titik akhir y : "))

iter = int(input("Masukkan jumlah iterasi : "))

print(colored("WARNING!   ", 'red'), end = "")
print("Menggunakan animasi bisa memakan waktu yang lebih lama pada Divide and Conquer!")
animation = input("Apakah ingin menggunakan animasi ? (ya/tidak) : ")
while animation != "ya" and animation != "tidak":
    animation = input("Apakah ingin menggunakan animasi ? (ya/tidak) : ")

# Generate bezier curve points

startDNC = time.perf_counter()
bezierCurve(x[0], y[0], conX, conY, tempX, tempY, 0, iter, animation)
endDNC = time.perf_counter()

print("\nWaktu eksekusi menggunakan Divide and Conquer: ", end = "")
print(f"{endDNC-startDNC} detik.")

startBF = time.perf_counter()
bruteForce(x[0], y[0], conX, conY, tempX, tempY, iter)
endBF = time.perf_counter()

print("\nWaktu eksekusi menggunakan Brute Force: ", end = "")
print(f"{endBF-startBF} detik.")

diffTime = (endBF-startBF) - (endDNC-startDNC)

if(diffTime < 0):
    print(f"\nBrute Force memiliki kecepatan eksekusi yang lebih cepat sebesar {-1 * diffTime} detik.")
else:
    print(f"\nDivide and Conquer memiliki kecepatan eksekusi yang lebih cepat sebesar {diffTime} detik.")

x.append(tempX)
y.append(tempY)

# Create animation
ani = FuncAnimation(fig, update, frames=range(len(lines)), init_func=init, blit=True, interval=500)

plt.plot(x, y)

plt.show()
