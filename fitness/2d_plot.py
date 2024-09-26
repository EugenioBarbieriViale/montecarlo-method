import matplotlib.pyplot as plt
import numpy as np

N = 80000
radius = 1

angles = np.linspace(0, np.pi/2, 100)
circle_x = radius * np.cos(angles)
circle_y = radius * np.sin(angles)

x = np.random.rand(N) * radius
y = np.random.rand(N) * np.sqrt(radius**2 - x**2)

def goodness(x, y):
    a = y
    b = x
    c = radius - np.sqrt(x**2 + y**2)
    return min(a,b,c)

goodnesses = [goodness(x[i], y[i]) for i in range(N)]
max_good = np.max(goodnesses)

index = goodnesses.index(max_good)
max_coords = (round(x[index], 4), round(y[index], 4))

color = [1 - g for g in goodnesses]

plt.xlim((0, radius))
plt.ylim((0, radius))

string_title = f"Best point: {max_coords[0]}, {max_coords[1]} with goodness {round(max_good,4)}"
plt.title(string_title)

plt.plot(circle_x, circle_y)

plt.scatter(x, y, c=color)
plt.scatter(max_coords[0], max_coords[1], color="red")

plt.show()
