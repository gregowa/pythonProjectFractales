#classe définissant un objet de type segment à partir des coordonnées de ces deux extrémités
from math import sqrt
import numpy as np

class Segment:
    x1=0
    y1=0
    x2=0
    y2=0
    seg = [np.linspace(x1, x2), np.linspace(y1, y2)]
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.seg=[np.linspace(x1, x2), np.linspace(y1, y2)]

    def getX1(self):
        return self.x1

    def getX2(self):
        return self.x2

    def getY1(self):
        return self.y1

    def getY2(self):
        return self.y2

    def getX1(self):
        return self.x1

    def getSeg(self):
        return self.seg

    def longueur(self):
        return sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)

segment = Segment(0,0,2,0)
print(segment.longueur())
