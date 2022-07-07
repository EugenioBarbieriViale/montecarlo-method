import random
import numpy as np
import matplotlib.pyplot as plt

r = 1000
pi = 0
ar = []
count = 0

for i in range(r**2):
    x = random.randint(0,r)
    y = random.randint(0,r)
    if (x**2+y**2<=r**2):
        count+=1
        pi = count*4/r**2
        ar.append(pi)

x = np.linspace(0,r**2,count)
y = ar

plt.axhline(np.pi,0,r**2)
plt.plot(x,y)
plt.show()
