class Cell:
	def __init__(self, pos=(0, 0), vel=(1, 0)):
		self.position = pos
		self.velocity = vel
		self.stack = []

	def step(self, cell=None):
		pass

	def interact(self, cell):
		pass

	def operate(self):
		pass

	def output(self):
		pass