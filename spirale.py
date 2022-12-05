import numpy as np
import matplotlib.pyplot as plt

a = 2
b = 1.19

phi = np.pi/8

rads = list(reversed(np.arange(0, (8 * np.pi), 0.01)))

x = []
x1 = []
x2 = []
x3 = []
x4 = []

y = []
y1 = []
y2 = []
y3 =[]
y4= []

for rad in rads:
    x.append((a * b ** -rad * np.cos(rad)))
    y.append((a * b ** -rad * np.sin(rad)))
    x1.append((a * b ** -rad * np.cos(rad)) / 3 + 2)
    y1.append((a * b ** -rad * np.sin(rad)) / 3)
    x2.append(((a * b ** -rad * np.cos(rad) / 3 + 2)/3 + 2))
    y2.append((a * b ** -rad * np.sin(rad) / 3/3))

for i in range(0, len(rads)):
    x3.append(x1[i] * np.cos(phi) - y1[i] * np.sin(phi))
    y3.append(x1[i] * np.sin(phi) + y1[i] * np.cos(phi))
    x4.append(x2[i] * np.cos(phi / 8) - y2[i] * np.sin(phi / 8))
    y4.append(x2[i] * np.sin(phi / 8) + y2[i] * np.cos(phi / 8))

plt.plot(x, y)
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.show()

