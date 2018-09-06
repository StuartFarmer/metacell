from enum import Enum
from copy import copy
import math

Direction = Enum('Direction', ['NORTH', 'EAST', 'SOUTH', 'WEST'])

class Cell:
	def __init__(self, pos=(0, 0), vel=(1, 0)):
		self.position = pos
		self.velocity = vel

	def step(self, cell=None):
		x, y = self.position
		dx, dy = self.velocity
		self.position = (x + dx, y + dy)

	def interact(self, cell):
		raise NotImplementedError

class Rotator(Cell):
	def __init__(self, pos, vel, direction=Direction.NORTH):
		self.direction = direction
		self.velocity_map = {
			Direction.NORTH : (-1, 0),
			Direction.SOUTH : (1, 0),
			Direction.EAST : (0, 1),
			Direction.WEST : (0, -1),
		}
		super().__init__(pos, vel)

	def interact(self, cell):
		cell.velocity = self.velocity_map[self.direction]
		return cell

class ClockwiseRotator(Cell):
	def __init__(self, pos, vel):
		self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
		super().__init__(pos, vel)

	def interact(self, cell):
		dx, dy = cell.velocity
		dx += 1
		dy -= 1
		cell.velocity = (dx, dy)
		return cell

class CounterClockwiseRotator(Cell):
	def __init__(self, pos, vel):
		super().__init__(pos, vel)

	def interact(self, cell):
		dx, dy = cell.velocity
		dx -= 1
		dy += 1
		cell.velocity = (dx, dy)
		return cell

class HorizonalMirror(Cell):
	def __init__(self, pos, vel):
		super().__init__(pos, vel)

	def interact(self, cell):
		dx, dy = cell.velocity
		dy *= -1
		cell.velocity = (dx, dy)
		return cell

class VerticalMirror(Cell):
	def __init__(self, pos, vel):
		super().__init__(pos, vel)

	def interact(self, cell):
		dx, dy = cell.velocity
		dx *= -1
		cell.velocity = (dx, dy)
		return cell

class Adder(Cell):
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

			return Data(v1+v2, pos=self.position, vel=cell.velocity)

class Multiplier(Cell):
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

			return Data(v1*v2, pos=self.position, vel=cell.velocity)

class Data(Cell):
	def __init__(self, value, pos=(0, 0), vel=(1, 0)):
		super().__init__(pos, vel)
		self.value = value

class Emitter(Rotator):
	def __init__(self, pos=(0, 0), vel=(0, 0), direction=Direction.NORTH):
		super().__init__(pos, vel, direction)

	def interact(self, cell):
		new_c = copy(cell)
		new_c.velocity = self.velocity_map[self.direction]
		return [cell, new_c]

class Filter(Cell):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		super().__init__(pos, vel)
		self.state = True

	def interact(self, cell):
		if self.state:
			cell.velocity = (-1, 0)
			self.state = False
		elif not self.state:
			cell.velocity = (1, 0)
			self.state = True
		return cell

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

class Sigmoid(Cell):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		self.storage = None
		super().__init__(pos, vel)

	def interact(self, cell):
		to_return = self.storage
		self.storage = cell
		return to_return