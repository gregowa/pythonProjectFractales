import numpy as np
import matplotlib.pyplot as plt
from random import *

#paramètres de la spirale
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

#point de départ
p0 = [0, 2]

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
    if random() < 0.2:
        for p in range(0, len(pts[0])):
            resh1= h1(pts[0][p], pts[1][p])
            resX.append(resh1[0])
            resY.append(resh1[1])
    else:
        for p in range(0, len(pts[0])):
            resh2 = h2(pts[0][p], pts[1][p])
            resX.append(resh2[0])
            resY.append(resh2[1])
    return [resX, resY]

#fonction spirales qui renvoie la liste de points crées à chaque itération (soit 2 spirales reliées)
def spiralesQ3(pts, n):
    spirale_finale = [pts]
    for i in range(0, n):
        spirales_temp = []
        for s in spirale_finale:
            spirales_temp.append(HQ3(s))
        spirale_finale.clear()
        spirale_finale = spirales_temp
    for s in spirale_finale:
        plt.scatter(s[0], s[1], s=0.1)
    plt.show()

#fonction spirales qui renvoie la liste de points crées à chaque itération (soit l'image par h1 soit l'image par h2)
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
    spirale_finale = p0
    print(spirale_finale)
    for i in range(0, n):
        print(i)
        spirales_tempX = []  #liste des abscisses
        spirales_tempY = []
        newP = H4bis(spirale_finale)
        spirales_tempX.append(newP[0])
        spirales_tempY.append(newP[1])
        print('spirale_tempX')
        print(spirales_tempX)
        print('spirale_tempY')
        print(spirales_tempY)
        for x in spirales_tempX :
            spirale_finale[0].append(x)
        for y in spirales_tempX :
            spirale_finale[0].append(y)
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

#première idée : utilisation de plot
#fonction spirales qui effectue n fois h1 et m fois h2
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



#Q5
def spiralesPoints(P0, n):
    ptsToShow = [[],[]]
    newPts = [[], []]
    newPts[0].append(P0[0])
    newPts[1].append(P0[1])
    for i in range(0,n):
        res = H4bis(newPts)
        #efface de la liste des nouveaux points
        #les points dont on a déjà calculé l'image
        newPts[0].clear()
        newPts[1].clear()
        for p in range (0,len(res[0])):
            newPts[0].append(res[0][p])
            newPts[1].append(res[1][p])
            ptsToShow[0].append(res[0][p])
            ptsToShow[1].append(res[1][p])
    plt.scatter(ptsToShow[0],ptsToShow[1],s=0.1)
    plt.show()

spiralesQ3(pts,10)
#spiralesPoints(p0, 100000)

