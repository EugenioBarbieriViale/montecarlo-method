import random
import numpy as np
import matplotlib.pyplot as plt

n_simulation = 1000
n_flips = 1000
av_vals = []

for i in range(n_simulation):
    val = 0
    values = []

    for j in range(n_flips):
        coin = random.randint(0,1)

        val += coin
        prob = val/(j+1)

        values.append(prob)

    x = np.linspace(0,n_flips,n_flips)
    plt.plot(x,values)
    av_vals.append(sum(values)/len(values))

print("Probability of getting head: {}%".format(sum(av_vals)/len(av_vals)))
plt.title("Flipping a coint - Montecarlo simulation")
plt.xlabel("Flips number")
plt.ylabel("Probabilty")
plt.axhline(0.5,0,n_flips,color="red")
plt.show()
