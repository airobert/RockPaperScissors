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
	# payoff  function
	def __init__ (self, name, pureStrategies):
		self.name = name
		self.pureStrategies = pureStrategies
		# at the beginning N is inialised as an arbitrary pure strategy
		self.piN = random.choice(self.pureStrategies).convertToMixed()
		self.N = self.piN.support() 
		# M is initialised as empty list
		self.M = []


	def printInfo(self):
		print ('This agent is called: ', self.name)
		print ('There are the following strategies:')
		for p in self.pureStrategies:
			print ('\t', p)

	# def iteration (self, numIter):#
	# 	for i in range(numIter):
	# 		# start this iteration with discovering new strategies by the heuristic

	def iteration (self, num):
		print ('-----------------the current strategy is', self.piN)
		T = self.searchWithHeuristic(num)
		# test against piN and obtain the winners
		W = []
		print ('----------------discover strategies (T)------------------------')
		for t in T:
			print (t)
		print ('-----------------find winning strategies (W)--------------------')
		for t in T:
			if self.payoff (t, self.piN) > 0:
				W.append(t)
				print ('one of the winning strategies is: ', t)

		print('------------------find N+M+W ------------------------------')
		# solve and find the piN'
		# set union N, M, W
		for n in self.N:
			print ('N', n)
		for m in self.M:
			print ('M', m)
		l = []
		for w in W:
			l += w.support()

		WNM = l + self.N + self.M
		# remove duplicates
		WNM2 = []
		for i in range(len(WNM)):
			flag = False
			for w in WNM2:
				if WNM[i].value == w.value:
					flag = True
			if flag == False:
				WNM2.append(WNM[i])
		for a in WNM2:
			print ('W+N+M: ', a)
		WNM = WNM2

		print ('---------------- use linear programming and solve --------')
		self.piN = self.solve(WNM2)
		print ('----------------the updated piN is ------------------')

	def solve(self, WNM):
		pass
	# TODO : Robert

	def searchWithHeuristic(self, num):
		# TODO: Yang, so far it is just a random choice and return a mixed strategy
		strategies = []
		for n in range(num):
			# obtain a mixed strategy of random size
			size = random.randrange(1, len(self.pureStrategies)+1) # any number between 1 and len(self.pureStragegies)
			# print('size',size)
			st = [] # the pure strategy 
			pc = [] # the percentage

			total = 0
			for i in range(size):
				st.append(random.choice(self.pureStrategies).value)
				pc.append(random.randint(0, 5))
				total += pc[i]
				# print ('total',total)

			if total == 0:
				# this mixed strategy is of size one
				strategies.append(random.choice(self.pureStrategies).convertToMixed())
			else:
				for i in range(size):
					pc[i] = pc[i]/total
				strategies.append(MixedStrategy(st, pc))

		return strategies




	def play(self):
		return self.piN