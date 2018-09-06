from .genome import Cell

stack = []

class Sponge(Cell):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		super().__init__(pos, vel)

	def interact(self, cell):
		return None

class Swap(Cell):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		self.storage = None
		super().__init__(pos, vel)

	def interact(self, cell):
		to_return = self.storage
		self.storage = cell
		return to_return

class Push(Cell):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		super().__init__(pos, vel)

	def interact(self, cell):
		stack.push(cell)

class Append(Cell):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		super().__init__(pos, vel)

	def interact(self, cell):
		stack.append(cell)

class Pop(Cell):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		super().__init__(pos, vel)

	def interact(self, cell):
		try:
			return stack.pop()
		except:
			return None

class Index(Cell):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		super().__init__(pos, vel)

	def interact(self, cell):
		if type(cell) != Data:
			return None
		
		try:
			return stack.index(cell.value)
		except:
			return cell

class GetHead(Cell):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		super().__init__(pos, vel)

	def interact(self, cell):
		try:
			return stack[0]
		except:
			return None

class GetTail(Cell):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		super().__init__(pos, vel)

	def interact(self, cell):
		try:
			return stack[-1]
		except:
			return None