from board import Board
from genome import *
from parser import Parser
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Domain:
	def __init__(self):
		self.species = []
		self.mapping = {}
		self.cell_to_token = {}
		self.i = 0

	def add_species(self, cell):
		self.species.append(cell)
		cell.token = i
		self.mapping[self.i] = cell
		self.cell_to_token[cell] = self.i
		self.i += 1

def run(filename, n_generations=15, dpi=100, interval=20, save=False):
	p = Parser(filename)
	board = p.create_board()
	fig = plt.figure(dpi=dpi)
	plt.axis("off")
	ims = []
	for i in range(n_generations):
		universe = board.get_state()
		ims.append((plt.imshow(universe, cmap=plt.cm.BuPu_r),))
		board.update()
	im_ani = animation.ArtistAnimation(
		fig, ims, interval=interval, repeat_delay=3000, blit=True
	)
	if save:
		im_ani.save(("./neuron.gif"), writer="imagemagick")
	plt.show()

run('../boards/neuron.mc', save=False)