import numpy as np
import random
import matplotlib.pyplot as plt

class Montecarlo:
    def __init__(self,s,b):
        self.n_simulations = s
        self.bet = b
        self.balance = [1000]

        self.n_rolls = 1000
        self.n_win = 0

        self.prob_win = []
        self.end_balance = []

        self.dice1 = 0
        self.dice2 = 0

    def calc_balance(self):
        self.balance = [1000]
        self.n_win = 0

        for i in range(self.n_rolls-1):
            # self.dice_1 = np.random.randint(1,6)
            # self.dice_2 = np.random.randint(1,6)

            self.dice_1 = random.randint(1,6)
            self.dice_2 = random.randint(1,6)

            if self.dice_1 == self.dice_2:
                #self.balance += 4*self.bet
                self.balance.append(self.balance[-1] + 4 * self.bet)
                self.n_win += 1
            else:
                self.balance.append(self.balance[-1] - self.bet)

            #self.balances.append(self.balance)
        return self.balance

    def repeat_simulation(self):
        for i in range(self.n_simulations):
            self.x = np.linspace(0,self.n_rolls,1000)
            self.y = self.calc_balance()

            plt.plot(self.x,self.y)

            self.end_balance.append(self.y[-1])
            self.prob_win.append(self.n_win/self.n_rolls)

    def render(self):
        plt.title("Montecarlo simulation ({} times)".format(self.n_simulations))
        plt.xlabel("Number of rolls")
        plt.ylabel("Player balance")

        print("Average final balance: ${}".format(np.sum(self.end_balance)/len(self.end_balance)))
        print("Average probability to win: {}".format(np.sum(self.prob_win)/len(self.prob_win)))

        plt.show()

simulation = Montecarlo(100,1)
simulation.calc_balance()
simulation.repeat_simulation()
simulation.render()
