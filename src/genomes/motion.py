from .base import Cell
from enum import Enum

Direction = Enum('Direction', ['NORTH', 'EAST', 'SOUTH', 'WEST'])
velocities = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def clockwise_velocity(v):
    dx, dy = v
    dx += 1
    dy -= 1

    return (dx, dy)


def counterclockwise_velocity(v):
    dx, dy = v
    dx -= 1
    dy += 1

    return (dx, dy)


class Rotator(Cell):
    def __init__(self, pos, vel, direction=Direction.NORTH):
        self.direction = direction
        self.velocity_map = {
            Direction.NORTH: (-1, 0),
            Direction.SOUTH: (1, 0),
            Direction.EAST: (0, 1),
            Direction.WEST: (0, -1),
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
