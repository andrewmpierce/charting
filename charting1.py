#This is an app to record and display data surrounding a fair coin toss
import random
#import matplotlib.pyplot as plt


def flip_coin(n):
	coin_outcomes = [0,1]
	record_outcome = []
	
	for i in range(n):
		record_outcome.append(random.choice(coin_outcomes))
		
	return record_outcome

coin_results500 = float(sum(flip_coin(500))/500

print "Hello"
#print:(coin_results500)
