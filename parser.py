from board import Board
from genome import *

class Parser:
	def __init__(self, filename):
		self.data = []
		with open(filename) as f:
			for line in f:
				_line = []
				for l in line:
					if l != '\n':
						_line.append(l)
				self.data.append(_line)


	def create_board(self):
		b = Board(size=(len(self.data), len(self.data[0])))
		for i in range(len(self.data)):
			for j in range(len(self.data[0])):
				c = self.parse_token(self.data[i][j], (i, j))
				if c is not None:
					#print(i, j)
					b.add_cell(c)

		return b

	def parse_token(self, ch, coor):
		parse_map = {
			'>': Rotator(pos=coor, vel=(0, 0), direction=Direction.EAST),
			'<': Rotator(pos=coor, vel=(0, 0), direction=Direction.WEST),
			'^': Rotator(pos=coor, vel=(0, 0), direction=Direction.NORTH),
			'V': Rotator(pos=coor, vel=(0, 0), direction=Direction.SOUTH),
			'~': Emitter(pos=coor, vel=(0, 0), direction=Direction.EAST),
			'0': Data(pos=coor, vel=(-1, 0), value=0)
		}

		try:
			return parse_map[ch]
		except:
			return None