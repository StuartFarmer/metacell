from genome import Cell
import math

class InlineFunction(Cell):
	def __init__(self, pos, vel):
		super().__init__(pos, vel)

	def interact(self, cell):
		if type(cell) != Data:
			return None

class TwoArgumentFunction(Cell):
	def __init__(self, pos, vel):
		self.storage = None
		super().__init__(pos, vel)

	def interact(self, cell):
		if type(cell) != Data:
			return None

		if self.storage is None:
			self.storage = cell
			return None

		else:
			v1 = cell.value
			v2 = self.storage.value
			self.storage = None
			return v1, v2

class Adder(TwoArgumentFunction):
	def __init__(self, pos, vel):
		super().__init__(pos, vel)

	def interact(self, cell):
		data = super().interact(cell)
		if data is not None:
			v1, v2 = data
			return Data(v1+v2, pos=self.position, vel=cell.velocity)

class Multiplier(TwoArgumentFunction):
	def __init__(self, pos, vel):
		super().__init__(pos, vel)

	def interact(self, cell):
		data = super().interact(cell)
		if data is not None:
			v1, v2 = data
			return Data(v1*v2, pos=self.position, vel=cell.velocity)

class Sigmoid(InlineFunction):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		super().__init__(pos, vel)

	def interact(self, cell):
		super.interact(cell)
		cell.value = 1 / (1 + math.exp(-cell.value))
		return cell

class Tanh(InlineFunction):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		super().__init__(pos, vel)

	def interact(self, cell):
		super.interact(cell)
		cell.value = math.tanh(cell.value)
		return cell

class SquareRoot(InlineFunction):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		super().__init__(pos, vel)

	def interact(self, cell):
		super.interact(cell)
		cell.value = math.sqrt(cell.value)
		return cell

class CubeRoot(InlineFunction):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		super().__init__(pos, vel)

	def interact(self, cell):
		super.interact(cell)
		cell.value = math.pow(cell.value, -3)
		return cell

class nRoot(TwoArgumentFunction):
	pass

class Square(InlineFunction):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		super().__init__(pos, vel)

	def interact(self, cell):
		super.interact(cell)
		cell.value = math.exp(cell.value)
		return cell

class Cube(InlineFunction):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		super().__init__(pos, vel)

	def interact(self, cell):
		super.interact(cell)
		cell.value = math.pow(cell.value, 3)
		return cell

class Power(TwoArgumentFunction):
	pass