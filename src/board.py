'''
RULES: If a cell was on a space first, it consumes the other. If a cell has a velocity of zero, if consumes the other.
'''

import numpy as np

class Domain:
	def __init__(self):
		self.mapping = {}
		self.cell_to_token = {}
		self.i = 1

	def add_species(self, cell):
		cell.token = self.i

		try:
			self.cell_to_token[cell]
		except:
			self.mapping[self.i] = cell
			self.cell_to_token[cell] = self.i
			self.i += 1

	def get_token(self, cell):
		t = self.cell_to_token[cell]
		s = max(self.mapping)
		t = t/s * -1
		return t

class Board:
	def __init__(self, size=(10, 10)):
		self.size = size
		self.cells = []
		self.domain = Domain()

	def coor_out_of_bounds(self, coor):
		x, y = coor
		sx, sy = self.size
		print(x, y)
		print(sx, sy)
		if x >= sx or y >= sy or x < 0 or y < 0:
			return True
		return False

	def update(self):
		for c in self.cells:
			c.step()
			if c.position[0] >= self.size[0] or \
			   c.position[1] >= self.size[1] or \
			   c.position[0] < 0 or \
			   c.position[1] < 0:
				self.cells.remove(c)

		already_interacted = []
		outputted_cells = []
		for i in range(len(self.cells)): # idx 1
			for j in range(len(self.cells)):
				if i != j and \
				self.cells[i].position == self.cells[j].position and \
				self.cells[i] not in already_interacted and \
				self.cells[j] not in already_interacted: # remember not to process cells that are the same! they will always intersect!
					# intersection! let's do something fun

					# Rule 1: if a cell has a velocity of 0, it consumes the other.
					potential_output = None
					if self.cells[i].velocity == (0, 0):
						potential_output = self.cells[i].interact(self.cells[j])
						already_interacted.append(self.cells[j])

					elif self.cells[j].velocity == (0, 0):
						potential_output = self.cells[i].interact(self.cells[j])
						already_interacted.append(self.cells[i])

					elif i < j:
						potential_output = self.cells[i].interact(self.cells[j])
						already_interacted.append(self.cells[j])

					elif j < i:
						potential_output = self.cells[i].interact(self.cells[j])
						already_interacted.append(self.cells[i])

					if potential_output is not None:
						if type(potential_output) == list:
							outputted_cells.extend(potential_output)
						else:
							outputted_cells.append(potential_output)

		# remove the cells they should be copied into the stack of the other cell if they are important
		[self.cells.remove(c) for c in already_interacted]
		self.add_cells(outputted_cells)
					
	def get_state(self):
		b = np.zeros(shape=self.size)
		for c in self.cells:
			x, y = c.position
			try:
				b[x][y] = self.domain.get_token(type(c))
			except:
				print('blart')
				self.cells.remove(c)
		return b

	def add_cell(self, cell):
		x, y = cell.position
		bx, by = self.size
		if x < bx and y < by:
			self.domain.add_species(type(cell))
			self.cells.append(cell)

	def add_cells(self, i):
		[self.add_cell(c) for c in i]

	def has_cell_at(self, pos):
		for c in self.cells:
			if c.position == pos:
				return c
		return False