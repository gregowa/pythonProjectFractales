from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from segment import Segment


def f1(x):
    return [x[0] / 3, x[1] / 3]

def f2(x):
    return [1 / 3 + x[0] / 6 - sqrt(3) * x[1] / 6, sqrt(3) * x[0] / 6 + x[1] / 6]


def f3(x):
    return [2 / 3 + (x[0] - 1) / 6 + sqrt(3) * x[1] / 6, - sqrt(3) * (x[0] - 1) / 6 + x[1] / 6]


def f4(x):
    return [2 / 3 + x[0] / 3, x[1] / 3]


def longueur(a, c, b, d) :
    return sqrt((b - a)**2 + (c - d)**2)


def f_gene(x, a, c, b, d):
    l = longueur(a, c, b, d)
    f1 = [x[0] / 3, x[1] / 3]
    f2 = [l*(1 / 3) + x[0] / 6 - sqrt(3) * x[1] / 6, sqrt(3) * x[0] / 6 + x[1] / 6]
    f3 = [l*(2 / 3) + (x[0] - l*1) / 6 + sqrt(3) * x[1] / 6, - sqrt(3) * (x[0] - l*1) / 6 + x[1] / 6]
    f4 = [l*(2 / 3) + x[0] / 3, x[1] / 3]


def graph_fi(a, c, b, d):
    # plt.plot([a,b],[c,d])
    x = [np.linspace(a, b), np.linspace(c, d)]
    plt.plot(f1(x)[0], f1(x)[1])
    plt.plot(f2(x)[0], f2(x)[1])
    plt.plot(f3(x)[0], f3(x)[1])
    plt.plot(f4(x)[0], f4(x)[1])
    plt.show()


def segment(a, c, b, d):
    # segment entre les points (a,c) et (b,d)
    return [np.linspace(a, b), np.linspace(c, d)]


def segment1(a, b):
    x = np.linspace(a, b)
    return [x, 1 - x]


def F_ligne_brisee(L):
    res = [None] * len(L)
    for i in range(0, len(L)):
        # L[i] : i-ème segment de la ligne brisée
        # res[i] : liste des images du i-ème segment par les 4 applications
        # res : liste de liste d'images de chaque segment
        res[i] = [f1(L[i]), f2(L[i]), f3(L[i]), f4(L[i])]
    return res


def vonkoch(L0, n):
    for k in range(0, n):
        res = F_ligne_brisee(L0)
        # pour chaque segment de la ligne brisée
        size = len(L0)
        L0.clear()
        for i in range(0, size):
            # ajoute les nouveaux segments crées à la ligne brisée
            L0.append(res[i][0])
            L0.append(res[i][1])
            L0.append(res[i][2])
            L0.append(res[i][3])
        # affichage
        if k == n - 1:
            for i in range(0, len(res)):
                # pour les 4 transformations
                for j in range(0, 4):
                    # affiche leur image
                    plt.plot(res[i][j][0], res[i][j][1])
    plt.show()


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


# graph_fi(0, 0, 1, 0)
# plt.plot(seg1[0],seg1[1])

seg1 = segment(0, 0, 1, 0)
seg2 = segment(0, 0, 0, 1)
seg3 = segment1(0, 1)
seg4 = segment(1, 1, 1, 0)
seg5 = segment(0, 1, 1, 1)

L0 = [seg1]
L1 = [seg2]
L2 = [seg4]
L3 = [seg5]

#cotesPolygones = [L0,L1,L2,L3]
#sierpinski(cotesPolygones, 1)
#vonkoch([seg1],1)

a = 1
b = 2
c = 3
d = 4

dir = (d-c)/(b-a)

l = longueur(a, c, b, d)

def f1_gene(x):
    return [(2*a + x[0]) / 3, (2*c + x[1]) / 3]


def f2_gene(x):
    return [(b-a) / 3 + (a + x[0]) / 6 - sqrt(3) * (a + x[1]) / 6, sqrt(3) * (c + x[0]) / 6 + (c + x[1]) / 6]


def f3_gene(x):
    return [2*(b-a) / 3 + ( a + (x[0] - 1)) / 6 + sqrt(3) * (a + x[1] )/ 6, - sqrt(3) * (c + x[0] - 1) / 6 + ( c +x[1]) / 6]


def f4_gene(x):
    return [2*(b-a) / 3 + (2*a + x[0]) / 3, (2*c + x[1] + 2*(d-c)) / 3 ]

x = [np.linspace(0, 1), np.linspace(0, 0)]
y = [np.linspace(a, b), np.linspace(c, d)]
plt.plot(x[0], x[1])
plt.plot(y[0], y[1])
plt.plot(f1_gene(y)[0], f1_gene(y)[1])
plt.plot(f2_gene(y)[0], f2_gene(y)[1])
#plt.plot(f3_gene(y)[0], f3_gene(y)[1])
plt.plot(f4_gene(y)[0], f4_gene(y)[1])

plt.show()

# res = F_ligne_brisee(L)
# pour tous les segments
# for i in range(0,len(res)):
# pour les 4 transformations
#   for j in range(0,4):
# affiche leur image
#      plt.plot(res[i][j][0],res[i][j][1])
# plt.show()

