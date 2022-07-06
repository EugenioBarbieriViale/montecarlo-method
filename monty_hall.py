import random
import numpy as np
import matplotlib.pyplot as plt

n_games = 1000
doors = [True, False, False]
keep_win = 0
switch_win = 0
keep_wins = []
switch_wins = []

for i in range(n_games):
    random.shuffle(doors)

    choose = random.randint(0,2)

    if doors[choose]:
        keep_win += 1
    else:
        switch_win += 1

    keep_wins.append(keep_win/(i+1))
    switch_wins.append(switch_win/(i+1))

plt.title("Monty hall problem -  Montecarlo simulation")

plt.xlabel("Number of games")
plt.ylabel("Probability of winning")

plt.axhline(1/3,0,n_games,color="red")
plt.axhline(2/3,0,n_games,color="green")

x = np.linspace(0,n_games,n_games)

plt.plot(x,keep_wins)
plt.plot(x,switch_wins)

print("Prob. of win if always switch: {}".format(sum(switch_wins)/len(switch_wins)))
print("Prob. of win if always keep your original choice: {}".format(sum(keep_wins)/len(keep_wins)))

plt.show()
