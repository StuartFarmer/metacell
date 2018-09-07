from . import base
from functools import partial


class AbstractFilter(base.Cell):
    def __init__(self, comparator, pos=(0, 0), vel=(0, 0)):
        super().__init__(pos, vel)
        self.comparator = comparator

    def interact(self, cell):
        if self.comparator(cell):
            cell.velocity = (-1, 0)
        else:
            cell.velocity = (1, 0)
        return cell


BinaryFilter = partial(AbstractFilter, comparator=lambda x: x.value > 0)
