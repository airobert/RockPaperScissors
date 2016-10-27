# Robert White
# ILLC @ UvA
# ai.robert.wangshuai@gmail.com

import random
from strategy import *


class Agent: # the default one is a Naive agent playing simple a strategy

	def __init__(self, name):
		self.name = name

	def printInfo(self):
		print 'this is agent', self.name , 'playing'


class PureStrategyAgent(Agent):
		
	def __init__ (self, name, pureStrategies):
		self.name == name
		self.strategy = pureStrategies
		Agent.__init__(self, name)

	def play(self):
		return PureStrategy(random.choice(self.pureStrategies))

	

class MixedStrategyAgent(Agent):
		
	def __init__ (self, name, pureStrategies):
		self.name == name
		self.strategy = pureStrategies
		Agent.__init__(self, name)

	def playPure(self):
		return PureStrategy(random.choice(self.pureStrategies)




