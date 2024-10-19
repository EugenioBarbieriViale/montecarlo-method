import numpy as np
import matplotlib.pyplot as plt

R = 2
r = 1

N = 1000

angles = np.linspace(-np.pi/2, np.pi/2, 100)
circle_x = R * np.cos(angles)
circle_y = R * np.sin(angles)

circle1_x = r * np.cos(angles)
circle1_y = r * np.sin(angles)

x = np.random.rand(N) * r
y = np.random.rand(N) * np.sqrt(r**2 - x**2)

X = np.random.rand(N) * R
Y = np.random.rand(N) * np.sqrt(R**2 - X**2) + np.sqrt((R+r)**2 - x**2)

plt.scatter(x, y)
plt.scatter(X, Y)

plt.xlim((0,R*2))
plt.ylim((-R,3*R))

plt.hlines(0, 0, R)

plt.plot(circle_x, circle_y)
plt.plot(circle1_x, circle1_y)
plt.show()
