import matplotlib.pyplot as plt
import time

# print(time.time())

x = []
y = []
iter = -1

def findMidPoint(x1, y1, x2, y2):
    ansX = (x1+x2)/2
    ansY = (y1+y2)/2
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

def b(P0, P1, P2, t):
    return (1-t)**2 * P0 + 2*(1-t)*t*P1 + t*t*P2

def bruteForce(P0X, P0Y, P1X, P1Y, P2X, P2Y, iteration):
    # t = 0
    for i in range((iteration) + 1):
        ansX = b(P0X, P1X, P2X, i/iteration)
        ansY = b(P0Y, P1Y, P2Y, i/iteration)
        xBrute.append(ansX)
        yBrute.append(ansY)

# input
tempX = int(input("Titik awal x :"))
tempY = int(input("Titik awal y :"))
x.append(tempX)
xBrute.append(tempX)
y.append(tempY)
yBrute.append(tempY)

conX = int(input("Titik kontrol x :"))
conY = int(input("Titik kontrol y :"))

tempX = int(input("Titik akhir x :"))
tempY = int(input("Titik akhir y :"))
iter = int(input("Masukkan jumlah iterasi : "))

startDNC = time.perf_counter()
bezierCurve(xBrute[0], yBrute[0], conX, conY, tempX, tempY, 0)
endDNC = time.perf_counter()

# print(startDNC)
# print(endDNC)

print("DnC: ", end = "")
print(endDNC-startDNC)

startBF = time.perf_counter()
bruteForce(x[0], y[0], conX, conY, tempX, tempY, iter*2)
endBF = time.perf_counter()

# print(startBF)
# print(endBF)

print("Brute Force: ", end = "")
print(endBF-startBF)

x.append(tempX)
xBrute.append(tempX)
y.append(tempY)
yBrute.append(tempY)

# print(x)
# print(y)
# print(xBrute)
# print(yBrute)

print(len(x))
print(len(xBrute))


# display
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.subplot(1, 2, 2)
plt.plot(xBrute, yBrute)
plt.show()