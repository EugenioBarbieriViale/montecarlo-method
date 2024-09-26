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
max_coords = (x[index], y[index])

plane_arr = np.linspace(0,1,100)
plane_x, plane_y = np.meshgrid(plane_arr, plane_arr)

z_good = [max_good-0.25 for i in range(100)]
plane_z, plane_z = np.meshgrid(z_good, z_good)

fig = plt.figure()
ax = plt.axes(projection="3d")

ax.plot(circle_x, circle_y, color="black")
ax.plot_surface(plane_x, plane_y, plane_z, alpha=0.4)

color = [1 - goodness(x[i], y[i]) for i in range(N)]
ax.scatter(x, y, goodnesses, c=color)

string_title = f"Best point: {round(max_coords[0],4)}, {round(max_coords[1],4)} with goodness {round(max_good,4)}"
plt.title(string_title)

ax.set_xlim((0,1))
ax.set_ylim((0,1))
ax.set_zlim((0,0.8))

plt.show()
