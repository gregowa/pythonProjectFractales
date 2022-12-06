import numpy as np
import matplotlib.pyplot as plt

a = 2
b = 1.19

phi = np.pi / 6

rads = list(reversed(np.arange(0, (8 * np.pi), 0.01)))

pts = []

x = []
y = []

for rad in rads:
    x.append(a * b ** -rad * np.cos(rad))
    y.append(a * b ** -rad * np.sin(rad))

pts.append(x)
pts.append(y)


def h1(x, y):
    return [x / 3 + 2, y / 3]


def h2(x, y):
    return [(x * np.cos(phi) - y * np.sin(phi)) * (b ** -phi),
            (x * np.sin(phi) + y * np.cos(phi)) * (b ** -phi)]


def H1(pts) :
    resX = []
    resY = []
    for p in range(0, len(pts[0])):
        res = h1(pts[0][p], pts[1][p])
        resX.append(res[0])
        resY.append(res[1])
    return [resX, resY]


def H2(pts):
    resX = []
    resY = []
    for p in range(0, len(pts[0])):
        res = h2(pts[0][p], pts[1][p])
        resX.append(res[0])
        resY.append(res[1])
    return [resX, resY]


def spirales(pts, n, m):
    spirale_finale = [pts]
    for i in range(0, n):
        spirales_m = []
        for s in spirale_finale:
            res1 = H1(s)
            temp = res1
            spirales_m.append(temp)
            for k in range(0, m):
                res2 = H2(temp)
                spirales_m.append(res2)
                temp = res2
        spirale_finale.clear()
        spirale_finale = spirales_m
    for s in spirale_finale:
        plt.plot(s[0], s[1])
    plt.show()


spirales(pts, 3, 30)
