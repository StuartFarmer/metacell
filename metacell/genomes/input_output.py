from . import base
from .motion import clockwise_velocity, Rotator, Direction
from copy import copy


class Data(base.Cell):
    def __init__(self, value, pos=(0, 0), vel=(1, 0)):
        super().__init__(pos, vel)
        self.value = value


class Input(base.Cell):
    def __init__(self, pos=(0, 0), vel=(0, 0), stream=None):
        self.stream = stream
        super().__init__(pos, vel)

    def interact(cell):
        try:
            data = self.stream.pop()
        except:
            return None
        return Data(data, pos=cell.position, vel=clockwise_velocity(cell.velocity))


class Output(base.Cell):
    def __init__(self, pos=(0, 0), vel=(0, 0)):
        super().__init__(pos, vel)

    def interact(self, cell):
        if type(cell) == Data:
            print(cell.value)


class Emitter(Rotator):
    def __init__(self, pos=(0, 0), vel=(0, 0), direction=Direction.NORTH):
        super().__init__(pos, vel, direction)

    def interact(self, cell):
        new_c = copy(cell)
        new_c.velocity = self.velocity_map[self.direction]
        return [cell, new_c]
