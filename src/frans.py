import matplotlib.pyplot as plt
import time

x = []
ansX = []
y = []
ansY = []
iteration = -1

def drawLines(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], marker="o", markersize=3, markeredgecolor="red", markerfacecolor="red")

def findMidPoint(x1, y1, x2, y2):
    ansX = (x1+x2)/2
    ansY = (y1+y2)/2
    drawLines(x1, y1, x2, y2)
    return ansX, ansY

def dncBezier(oldX, oldY, curIteration, leftX, leftY, rightX, rightY):
    if(curIteration < iteration):
        # banyak titik saat ini
        n = len(oldX)
        if(n == 1):
            ansX.append(oldX[0])
            ansY.append(oldY[0])
            return
        else:
            # titik baru hasil midpoint beberapa titik
            newX = []
            newY = []

            # menghitung midpoint beberapa titik
            for i in range(n - 1):
                newAnsX, newAnsY = findMidPoint(oldX[i], oldY[i], oldX[i+1], oldY[i+1])
                newX.append(newAnsX)
                newY.append(newAnsY)

            leftX.append(newX[0])
            leftY.append(newY[0])

            dncBezier(newX, newY, curIteration, leftX, leftY, rightX, rightY)

            dncBezier(leftX, leftY, curIteration + 1, [], [], [], [])

            # print("new x2 : ")
            # print(newX)
            rightX.append(newX[n-2])
            rightY.append(newY[n-2])

            # print("right x : ")
            # print(rightX)

            dncBezier(rightX, rightY, curIteration + 1, [], [], [], [])

tempX = int(input("Titik awal x : "))
tempY = int(input("Titik awal y : "))
x.append(tempX)
y.append(tempY)
ansX.append(tempX)
ansY.append(tempY)
nTikon = int(input("Masukkan jumlah titik kontrol : "))
for i in range(nTikon):
    tempX = int(input(f"Titik kontrol x ke-{i+1} : "))
    tempY = int(input(f"Titik kontrol y ke-{i+1} : "))
    x.append(tempX)
    y.append(tempY)
tempX = int(input("Titik akhir x :"))
tempY = int(input("Titik akhir y :"))
x.append(tempX)
y.append(tempY)
iteration = int(input("Masukkan jumlah iterasi yang diinginkan : "))

# process
dncBezier(x, y, 0, [x[0]], [y[0]], [], [])

ansX.append(tempX)
ansY.append(tempY)

# print(ansX)
# print(ansY)

# display
plt.plot(ansX, ansY)
plt.show()