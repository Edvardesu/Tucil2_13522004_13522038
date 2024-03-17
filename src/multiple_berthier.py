import matplotlib.pyplot as plt
import time

x = []
y = []
iter = -1

def findMidPoint(x1, y1, x2, y2):
    ansX = (x1+x2)/2
    ansY = (y1+y2)/2
    # drawLines(x1, y1, x2, y2)
    return ansX, ansY

def bezierCurve(leftPointX, leftPointY, controlX, controlY, rightPointX, rightPointY, curIteration):
    if(curIteration < iter):
        midPointLeftX, midPointLeftY = findMidPoint(leftPointX, leftPointY, controlX, controlY)
        midPointRightX, midPointRightY = findMidPoint(rightPointX, rightPointY, controlX, controlY)
        midX, midY = findMidPoint(midPointLeftX, midPointLeftY, midPointRightX, midPointRightY)
        # kiri
        bezierCurve(leftPointX, leftPointY, midPointLeftX, midPointLeftY, midX, midY, curIteration+1)
        x.append(midX)
        y.append(midY)
        # kanan
        bezierCurve(midX, midY, midPointRightX,  midPointRightY, rightPointX, rightPointY, curIteration+1)

xBrute = []
yBrute = []

# function for bezier curve with multiple control
# def berzierMultipleControl(leftPointX, leftPointY, controlX, controlY, rightPointX, rightPointY, curIteration):

def drawLines(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], marker="o", markersize=3, markeredgecolor="red", markerfacecolor="red")

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

# input
tempX = int(input("Titik awal x :"))
tempY = int(input("Titik awal y :"))
x.append(tempX)
xBrute.append(tempX)
y.append(tempY)
yBrute.append(tempY)

# mainkan
pointsX = []
pointsY = []
kontrols = int(input("Kontrolem ono piro : "))
for i in range (kontrols):
    conX = int(input("Titik kontrol x :"))
    x.append(conX)
    conY = int(input("Titik kontrol y :"))
    y.append(conY)

tempX = int(input("Titik akhir x :"))
x.append(tempX)
tempY = int(input("Titik akhir y :"))
y.append(tempY)
iter = int(input("Masukkan jumlah iterasi : "))

for i in range (kontrols):
    bezierCurve(x[i], y[i], x[i+1], y[i+1], x[i+2], y[i+2], 0)



# startDNC = time.perf_counter()
# bezierCurve(xBrute[0], yBrute[0], conX, conY, tempX, tempY, 0)
# endDNC = time.perf_counter()

# print("DnC: ", end = "")
# print(endDNC-startDNC)

# bezierCurve(xBrute[0], yBrute[0], conX, conY, tempX, tempY, 0)

# startBF = time.perf_counter()
# bruteForce(x[0], y[0], conX, conY, tempX, tempY, iter)
# endBF = time.perf_counter()

# print("Brute Force: ", end = "")
# print(endBF-startBF)

# x.append(tempX)
# y.append(tempY)

print(x)
print(y)

# display
# plt.subplot(1, 2, 1)
plt.plot(x, y)
# plt.subplot(1, 2, 2)
# plt.plot(xBrute, yBrute)
plt.show()