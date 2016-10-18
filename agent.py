# Rober White
# ILLC @ UvA
# ai.robert.wangshuai@gmail.com

import random

class Agent: # the default one is a Naive agent playing simple a strategy

	def __init__(self, name, domain):
		self.name = name
		self.domain = domain
		self.N = [] # in corresponding to the nash memory
		self.M = [] # in corresponding to the nash memory
	
	def play(self):
		return self.domain[0]

	def react(self, observe):
		return self.domain[0] # the default agent returns plays only the first one in the domain

	def print_info(self):
		print 'this is agent', self.name , 'playing'
		print 'it is playing within the domain of ', self.domain
		print 'the current nash memory is as follows:'
		print 'N = ', self.N
		print 'M = ', self.M

class RandomAgent (Agent):

	def __init__ (self, name, domain):
		Agent.__init__(self, name, domain)

	def react(self, observe):
		return random.choice(self.domain) # return a random value in the domain
	
	def play(self):
		return random.choice(self.domain) # return a random value in the domain
	
