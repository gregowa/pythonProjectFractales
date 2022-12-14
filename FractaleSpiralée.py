import numpy as np
import matplotlib.pyplot as plt
from random import *

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

po = [[0], [2]]

def h1(x, y):
    return [x / 3 + 2, y / 3]


def h2(x, y):
    return [(x * np.cos(phi) - y * np.sin(phi)) * (b ** -phi),
            (x * np.sin(phi) + y * np.cos(phi)) * (b ** -phi)]

def HQ3(pts) :
    resX = []
    resY = []
    for p in range(0, len(pts[0])):
        resh1 = h1(pts[0][p], pts[1][p])
        resX.append(resh1[0])
        resY.append(resh1[1])
    for p in range(0, len(pts[0])):
        resh2 = h2(pts[0][p], pts[1][p])
        resX.append(resh2[0])
        resY.append(resh2[1])
    plt.show()
    return [resX, resY]


def H(pts) :
    resX = []
    resY = []
    if random() < 0.5:
        for p in range(0, len(pts[0])):
            resh1 = h1(pts[0][p], pts[1][p])
            resX.append(resh1[0])
            resY.append(resh1[1])
    else:
        for p in range(0, len(pts[0])):
            resh2 = h2(pts[0][p], pts[1][p])
            resX.append(resh2[0])
            resY.append(resh2[1])
    return [resX, resY]


def H4bis(pts) :
    resX = []
    resY = []
    if random() < 0.5:
        for p in range(0, len(pts[0])):
            resh1 = h1(p)
            resX.append(resh1[0])
            resY.append(resh1[1])
    else:
        for p in range(0, len(pts[0])):
            resh2 = h2(pts[0][p], pts[1][p])
            resX.append(resh2[0])
            resY.append(resh2[1])
    return [resX, resY]

def spiralesQ3(pts, n):
    spirale_finale = pts
    for i in range(0, n):
        spirales_temp = []
        for s in spirale_finale:
            spirales_temp.append(H(s))
        spirale_finale.clear()
        spirale_finale = spirales_temp
    for s in spirale_finale:
        plt.plot(s[0], s[1])
    plt.show()


def spiralesQ4(pts, n):
    spirale_finale = [pts]
    for i in range(0, n):
        spirales_temp = []
        for s in spirale_finale:
            spirales_temp.append(H(s))
        for s in spirales_temp:
            spirale_finale.append(s)
    for s in spirale_finale:
        plt.plot(s[0], s[1])
    plt.show()

def spiralesQ4bis(pts, n):
    spirale_finale = pts
    print(spirale_finale)
    for i in range(0, n):
        spirales_tempX = []
        spirales_tempY = []
        for s in spirale_finale:
            spirales_tempX.append(H4bis(s)[0])
            spirales_tempY.append(H4bis(s)[1])
        for x in spirales_tempX :
            spirale_finale[0].append(x)
        for y in spirales_tempX :
            spirale_finale[0].append(y)
        print(spirale_finale)
    for s in spirale_finale:
        plt.plot(s[0], s[1])
    plt.show()

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


spiralesQ4bis(po, 2)
