#This is an app to record and display data surrounding a fair coin toss.
import random
import numpy
import matplotlib.pyplot as plt


def flip_coin(n):
	coin_outcomes = [0,1]
	record_outcome = []
	for i in range(n):
		record_outcome.append(random.choice(coin_outcomes))		
	return record_outcome


def flip_distribution(x, n, flip_coin):
        results = []
        for i in range(x):
                avg = (sum(flip_coin(n))/ float(n))
                results.append(avg)
        return results

def x_axis(x):
        x_values = []
        for i in range(x):
                x_values.append(1+i)
                
        return x_values

plt.axis([0, 500, 0, 1])
plt.plot(x_axis(500), flip_distribution(500, 10000, flip_coin))
plt.show()

plt.hist(flip_distribution(500, 10000, flip_coin), bins=3)
plt.show()