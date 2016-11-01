# Robert White
# ILLC @ UvA
# ai.robert.wangshuai@gmail.com

import random

from strategy import *
import sys



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

	def printInfo(self):
		print ('This agent is called: ', self.name)
		print ('There are the following strategies:')
		for p in self.pureStrategies:
			print ('\t', p)

	def play(self):
		return self.piN