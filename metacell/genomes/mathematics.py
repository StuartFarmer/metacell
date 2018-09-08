from .base import Cell
from .input_output import Data
import math
from functools import partial


class InlineFunction(Cell):
    def __init__(self, pos, vel, modifer):
        super().__init__(pos, vel)
        self.modifer = modifer

    def interact(self, cell):
        if type(cell) != Data:
            return None

        cell.value = self.modifer(cell.value)
        return cell


class TwoArgumentFunction(Cell):
    def __init__(self, pos=(0, 0), vel=(0, 0), modifer=None):
        self.storage = None
        self.modifer = modifer
        super().__init__(pos, vel)

    def interact(self, cell):
        if cell.__class__ != Data:
            return None

        if self.storage is None:
            self.storage = cell
            return cell

        else:
            v1 = cell.value
            v2 = self.storage.value
            self.storage = None
            cell.value = self.modifer(v1, v2)
        return cell


# Activation functions
Swish = partial(InlineFunction, modifer=lambda x: x * (1 / (1 + math.exp(-x))))
Relu = partial(InlineFunction, modifer=lambda x: max(0, x))
Sigmoid = partial(InlineFunction, modifer=lambda x: 1 / (1 + math.exp(-x)))
Tanh = partial(InlineFunction, modifer=lambda x: math.tanh(x))

# Exponentials
SquareRoot = partial(InlineFunction, modifer=lambda x: math.sqrt(x))
CubeRoot = partial(InlineFunction, modifer=lambda x: math.pow(x, -3))
Square = partial(InlineFunction, modifer=lambda x: math.exp(x))
Cube = partial(InlineFunction, modifer=lambda x: math.pow(x))

Adder = partial(TwoArgumentFunction, modifer=lambda x, y: x + y)
Multiplier = partial(TwoArgumentFunction, modifer=lambda x, y: x * y)
