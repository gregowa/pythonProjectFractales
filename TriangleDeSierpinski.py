from math import sqrt
import numpy as np
import matplotlib.pyplot as plt


def segment(a, c, b, d):
    # segment entre les points (a,c) et (b,d)
    return [np.linspace(a, b), np.linspace(c, d)]


def segment1(a, b):
    x = np.linspace(a, b)
    return [x, 1 - x]


def g1(x):
    return [x[0] / 2, x[1] / 2]


def g2(x):
    return [1 / 2 + x[0] / 2, x[1] / 2]


def g3(x):
    return [x[0] / 2, 1 / 2 + x[1] / 2]


def G_polygone(L):
    res = [None] * len(L)
    for i in range(0, len(L)):
        # L[i] : i-ème segment de la ligne brisée
        # res[i] : liste des images du i-ème segment par les 4 applications
        # res : liste de liste d'images de chaque segment
        res[i] = [g1(L[i]), g2(L[i]), g3(L[i])]
    return res


def sierpinski(cotesPolygone, n):
    for c in cotesPolygone:
        for k in range(0, n):
            res = G_polygone(c)
            # pour chaque segment de la ligne brisée
            size = len(c)
            for i in range(0, size):
                # ajoute les nouveaux segments crées à la ligne brisée
                L0.append(res[i][0])
                L0.append(res[i][1])
                L0.append(res[i][2])
            # affichage
            if k == n - 1:
                for i in range(0, len(res)):
                    # pour les 4 transformations
                    for j in range(0, 3):
                        # affiche leur image
                        plt.plot(res[i][j][0], res[i][j][1])

        plt.show()


seg1 = segment(0, 0, 1, 0)
seg2 = segment(0, 0, 0, 1)
seg3 = segment1(0, 1)
seg4 = segment(1, 1, 1, 0)
seg5 = segment(0, 1, 1, 1)

L0 = [seg1]
L1 = [seg2]
L2 = [seg4]
L3 = [seg5]

cotesPolygones = [L0,L1,L2,L3]
sierpinski(cotesPolygones, 1)


