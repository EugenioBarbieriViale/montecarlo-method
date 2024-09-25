import matplotlib.pyplot as plt
import numpy as np
import random

N = 80000
radius = 1

# Create circle
angles = np.linspace(0, np.pi/2, 100)
circle_x = radius * np.cos(angles)
circle_y = radius * np.sin(angles)

# Draw points
x = np.random.rand(1, N) * radius
y = [random.random() * np.sqrt(radius**2 - x[0][i]**2) for i in range(N)]

def goodness(x, y):
    a = y
    b = x
    c = radius - np.sqrt(x**2 + y**2)
    return min(a,b,c)

goodnesses = [round(goodness(x[0][i], y[i]) / radius, 4) for i in range(N)]
max_good = np.max(goodnesses)

index = goodnesses.index(max_good)
max_coords = (round(x[0][index],4), round(y[index],4))

angles1 = np.linspace(0, np.pi*2, 100)
mean = ((max_coords[0] + max_coords[1])/2)
circle_x1 = mean * np.cos(angles1) + mean
circle_y1 = mean * np.sin(angles1) + mean

color = [1 - g for g in goodnesses]

plt.xlim((0, radius))
plt.ylim((0, radius))

string_title = f"Best point: {max_coords[0]}, {max_coords[1]} with goodness {max_good}"
plt.title(string_title)

plt.plot(circle_x, circle_y)
plt.plot(circle_x1, circle_y1, linewidth=3)

plt.scatter(x, y, c=color)
plt.scatter(max_coords[0], max_coords[1], color="red")

plt.show()
