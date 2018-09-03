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
		self.stack.append(cell)
		return self.output()

	def output(self):
		c = self.stack.pop()
		print(c)
		c.velocity = self.velocity_map[self.direction]
		cx, cy = c.position
		dx, dy = c.velocity
		c.position = (cx + dx, cy + dy)
		print(c.velocity)
		return c

class Data(Cell):
	def __init__(self, value, pos=(0, 0), vel=(1, 0)):
		super().__init__(pos, vel)
		self.stack.append(value)

class Emitter(Rotator):
	def __init__(self, pos=(0, 0), vel=(0, 0), direction=Direction.NORTH):
		super().__init__(pos, vel, direction)

	def output(self):
		c = self.stack.pop()
		new_c = copy(c)
		new_c.velocity = self.velocity_map[self.direction]
		c.step()
		new_c.step()
		return [c, new_c]

class Filter(Cell):
	def __init__(self, pos=(0, 0), vel=(0, 0)):
		super().__init__(pos, vel)

