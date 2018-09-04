from cell import Cell
from enum import Enum
from copy import copy

Direction = Enum('Direction', ['NORTH', 'EAST', 'SOUTH', 'WEST'])

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
		

class Data(Cell):
	def __init__(self, value, pos=(0, 0), vel=(1, 0)):
		super().__init__(pos, vel)
		self.stack.append(value)

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
