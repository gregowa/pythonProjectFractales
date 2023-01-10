from math import sqrt
import numpy as np
import matplotlib.pyplot as plt


def g1(x):
    return [x[0] / 2, x[1] / 2]


def g2(x):
    return [1 / 2 + x[0] / 2, x[1] / 2]


def g3(x):
    return [x[0] / 2, 1 / 2 + x[1] / 2]


def G_polygone(pts):
    res = []
    for p in pts:
        temp = list(zip(p[0], p[1]))
        for g in [g1, g2, g3]:
            abs, ord = [], []
            for i in range(len(temp)):
                image = g(temp[i])
                abs.append(image[0])
                ord.append(image[1])
            res.append([abs, ord])
    return res


def sierpinski(pts, n):
    pts_finaux = pts
    for i in range(n):
        pts_finaux = G_polygone(pts_finaux)
    for p in pts_finaux:
        plt.fill(p[0], p[1])
    plt.show()

triangle = [[[0, 1, 0], [0, 0, 1]]]
sierpinski(triangle, 3)

carre = [[[0, 1, 1, 0], [0, 0, 1, 1]]]
sierpinski(carre, 5)

hexagone = [[[0.5, 1, 1, 0.5, 0, 0], [0, 0.2, 0.8, 1, 0.8, 0.2]]]
sierpinski(hexagone, 5)


