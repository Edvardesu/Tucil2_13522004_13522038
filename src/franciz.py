import matplotlib.pyplot as plt
import numpy as np

def berzierCurve(control_points, iteration):
    # Plot the original control points
    x, y = zip(*control_points)
    plt.plot(x, y, 'ro--', linewidth=0.5, markersize=3, label='Kontrolle bolo')
    
    for i in range(iteration + 1):
        drawLines(control_points, i / iteration)

    # Plotting the curve
    bezier_points = [titikBerthier(control_points, t) for t in np.linspace(0, 1, 100)]
    bx, by = zip(*bezier_points)
    plt.plot(bx, by, 'b-', label='Sakmenee bolo')

def drawLines(points, t, color='red'):
    while len(points) > 1:
        new_points = []
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            mid_point = (x1 + (x2 - x1) * t, y1 + (y2 - y1) * t)
            new_points.append(mid_point)
        plt.plot(*zip(*new_points), marker='o', markersize=2, linestyle='-', color=color, linewidth=0.5)
        points = new_points

def titikBerthier(points, t):
    while len(points) > 1:
        points = [(p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t) for p1, p2 in zip(points[:-1], points[1:])]
    return points[0]

# Input
control_points = []
control_points.append((int(input("Titik awal x : ")), int(input("Titik awal y : "))))
nTikon = int(input("Masukkan jumlah titik kontrol : "))
for i in range(nTikon):
    control_points.append((int(input(f"Titik kontrol x ke-{i+1} : ")), int(input(f"Titik kontrol y ke-{i+1} : "))))
control_points.append((int(input("Titik akhir x :")), int(input("Titik akhir y :"))))
iteration = int(input("Masukkan jumlah iterasi yang diinginkan : "))

berzierCurve(control_points, iteration)
plt.legend()
plt.show()
