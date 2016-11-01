# Robert White
# ILLC @ UvA
# ai.robert.wangshuai@gmail.com

import random
from strategy import *


class Agent: # the default one is a Naive agent playing simple a strategy
	name = 'example'
	pureStrategies = []
	N = []
	M = []
	piN = 0
	def __init__ (self, name, pureStrategies):
		self.name = name
		self.pureStrategies = pureStrategies
		# at the beginning N is inialised as an arbitrary pure strategy
		self.piN = random.choice(self.pureStrategies).convertToMixed()
		self.N = [self.piN.support()] 
		# M is initialised as empty list
		self.__M = []

	def play(self):
		return self.piN

	def printInfo(self):
		print 'This agent is called: ', self.name
		print 'There are the following strategies:'
		for p in self.pureStrategies:
			print '\t', p

	def iteration (self, numIter):#
		for i in range(numIter):
			# start this iteration with discovering new strategies by the heuristic
			T = self.searchWithHeuristic(3)
			# test against piN and obtain the winners
			W = 

	def searchWithHeuristic(self, num):
		for n in range(num):
			# obtain a mixed strategy of random size
			size = randrange(1, len(self.pureStrategies)+1)# any number between 1 and len(self.pureStragegies)
			st = [] # the 
			pc = [] # the percentage
			for m in range(size):
				s.append(random.choice(self.pureStrategies))