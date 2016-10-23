# Rober White, Yang Xu
# ILLC @ UvA
# ai.robert.wangshuai@gmail.com, danliangchen@gmail.com

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
		print ('this is agent', self.name , 'playing')
		print ('it is playing within the domain of ', self.domain)
		print ('the current nash memory is as follows:')
		print ('N = ', self.N)
		print ('M = ', self.M)

class RandomAgent (Agent):

	def __init__ (self, name, domain):
		Agent.__init__(self, name, domain)

	def react(self, observe):
		return random.choice(self.domain) # return a random value in the domain
	
	def play(self):
		return random.choice(self.domain) # return a random value in the domain

class PerfectAgent (Agent):

	def __init__ (self, name, domain):
		Agent.__init__(self, name, domain)

	def react(self, observe):
		# rock = 0, paper = 1, scissors = 2
		# +-------------------------------------------+
		# |           | rock 0 | paper 1 | scissors 2 |  
		# | rock 0    |      0 |      -1 |          1 |
		# | paper 1   |      1 |       0 |         -1 |
		# | scissors 2|     -1 |       1 |          0 |
		# +-------------------------------------------+  

		matrix = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
		perfectReaction = self.domain[0] # initialize perfect reaction as the first one in the domain

		for i in range(len(self.domain)):
			if matrix[i][observe] > 0:
				perfectReaction = i

		return self.domain[perfectReaction] # return a perfect reaction in the domain	

		
	
	def play(self):
		return random.choice(self.domain) # return a random value in the domain
	
