from enum import Enum
from genome import *

State = Enum('State', ['INIT', 'ALIVE'])

class Terminator(Cell):
	def __init__(self, pos, vel):
		super().__init__(pos, vel)

class StemCell(Cell):
	def __init__(self, pos, vel):
		self.state = State.INIT
		super().__init__(pos, vel)

	def load_argument(self, cell):
		# spec = inspect.getfullargspec(cell.__init__)
		# _s = spec.args[1:]

		# arg_d = {i : cell.__dict__.get(i) for i in _s}
		# type(cell)(**cell.arg_d)

	def _interact(self, cell):
		if type(cell) == Terminator:
			self.state = State.ALIVE

		if self.state == State.INIT:
			self.load_argument(cell)

		else:
			self.interact(cell)

s = StemCell(pos=(0, 0), vel=(0, 0))
r = Rotator(pos=(0, 0), vel=(0, 0), direction=Direction.EAST)

s._interact(r)