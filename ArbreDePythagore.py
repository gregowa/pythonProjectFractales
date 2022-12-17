import numpy as np
import matplotlib.pyplot as plt

def segment(a, c, b, d):
    # segment entre les points (a,c) et (b,d)
    return [np.linspace(a, b), np.linspace(c, d)]

def f1(x):
    theta = np.pi / 4
    return [(x[0]/np.sqrt(2))*np.cos(theta) - (x[1]/np.sqrt(2))*np.sin(theta) ,
            (x[0]/np.sqrt(2))*np.cos(theta) + (x[1]/np.sqrt(2))*np.sin(theta) + 1]

#pas la bonne expression de f2
def f2(x):
    theta = +3*np.pi / 4
    return [(x[0]/np.sqrt(2))*np.cos(theta) - (x[1]/np.sqrt(2))*np.sin(theta) +0.5,
            (x[0]/np.sqrt(2))*np.cos(theta) + (x[1]/np.sqrt(2))*np.sin(theta) + 1.5]


def arbreDePythagore(segs,n):
        for i in range (0,n):
            res = []
            for s in segs:
                res.append(f1(s))
                res.append(f2(s))
            #segs.clear()
            #ajoute les nouveaux segments calculés :
            for r in res:
                segs.append(r)
            if (i==n-1):
                for s in segs:
                    plt.plot(s[0],s[1])
                plt.show()


S1 = segment(0,0,1,0)
S2 = segment(0,0,0,1)
S3 = segment(1,0,1,1)
S4 = segment(0,1,1,1)
segs = [S1,S2,S3,S4]


arbreDePythagore(segs,6)
