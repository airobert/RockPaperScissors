# Robert White
# ILLC @ UvA
# ai.robert.wangshuai@gmail.com

from agent import *
import random
import sys
from strategy import *


rounds = 5 # how many rounds of games do we iterate
# repeat = 10 # repeat ten times for each round and calculate the average payoff

ROCK = 0
PAPER = 1
SCISSORS = 2

class  Platform(object):
	
	def __init__(self, agents, domain):
		self.agents = agents
		self.domain = domain # for now, this is always 3, so hardcoded
		for a in agents:
			a.payoff = self.expectedPayoff

	# the expected payoff for (pure strategy c1 against c2)
	def payoff (self, c1, c2): # zero sum game
		# rock = 0, paper = 1, scissors = 2
		# +-------------------------------------------+
		# |           | rock 0 | paper 1 | scissors 2 |  
		# | rock 0    |      0 |      -1 |          1 |
		# | paper 1   |      1 |       0 |         -1 |
		# | scissors 2|     -1 |       1 |          0 |
		# +-------------------------------------------+  

		matrix = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]

		return matrix[c1][c2]


	def expectedPayoff (self, m ,n):
		# m and n can be pure or mixed strategies but here we use a uniform implementation
		# if m or n is pure strategy, then convert it to a mixed strategy and evaluate

		if 'PureStrategy' in str(type(m)):
			m = m.convertToMixed()

		if 'PureStrategy' in  str(type(n)):
			n = n.convertToMixed()

		em = 0 # expected payoff for m
		for i in range(len(m.values)):
			e = 0
			for j in range(len(n.values)):
				e += self.payoff(m.values[i], n.values[j])* n.probabilities[j]
			em += e * m.probabilities[i]
		return em


		
def main():

	# since this game is symmetric, we consider only one agent
	r = PureStrategy(ROCK)
	p = PureStrategy(PAPER)
	s = PureStrategy(SCISSORS)
	a = Agent('bob', [r, p, s])
	pl = Platform ([a], [r, p, s]) # initialise the domain#

	a.printInfo()
	a.iteration(3, 5) # discover to the most 3 stategies and terminate if no winning
	# strategy discovered in 5 rounds of searching
	
	
if __name__ == "__main__":
	main()