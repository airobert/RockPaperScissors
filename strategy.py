# Robert White
# ILLC @ UvA
# ai.robert.wangshuai@gmail.com

ROCK = 0
PAPER = 1
SCISSORS = 2


class PureStrategy(object):
	def __init__(self, value):
		self.value = value

	def convertToMixed(self):
		return MixedStrategy([self.value], [1.0])

	def __str__(self):
		if self.value == ROCK:
			return 'ROCK'
		if self.value == PAPER:
			return 'PAPER'
		if self.value == SCISSORS:
			return 'SCISSORS'
	def __eq__(self, other): 
		return (self.value)

class MixedStrategy(object):
	def __init__(self, values, probabilities): # values is basically pure strategies (of probability 1)
		if len(values) == len(probabilities) and 1 - sum(probabilities) < 0.0001 :
			self.values = values
			self.probabilities = probabilities
		else:
			print ('error', values, probabilities, sum(probabilities)) # TODO: make this an exception
		
	def convertToPure(self):
		for i in range(len(self.probabilities)):
			if self.probabilities[i] == 1:
				return PureStrategy(self.values[i])
	def support (self):
		l = []
		for i in range(len(self.probabilities)):
			if self.probabilities[i] != 0:
				l.append(PureStrategy(self.values[i]))
		return l

	def __str__(self):
		s = ''
		for i in range (len(self.values)):

			if self.values[i] == ROCK:
				s += 'ROCK'
			if self.values[i] == PAPER:
				s += 'PAPER'
			if self.values[i] == SCISSORS:
				s += 'SCISSORS'#
			s += ' '+ str(self.probabilities[i])[:5]
			if i != len(self.values) - 1:
				s += '\t'
		return s


	