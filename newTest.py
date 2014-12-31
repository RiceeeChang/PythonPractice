class Some:
	def __init__(self, number):
		self.number = number

	def printSome(self):
		print(self.number+5)

s = Some(10)
s.printSome()