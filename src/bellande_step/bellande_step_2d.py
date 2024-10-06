# Copyright (C) 2024 Bellande Robotics Sensors Research Innovation Center, Ronaldson Bellande

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

#!/usr/bin/env python3

from header_imports import *

class Node2D:
    def __init__(self, x, y, parent=None):
        self.coord = (x, y)
        self.parent = parent

    @property
    def x(self):
        return self.coord[0]

    @property
    def y(self):
        return self.coord[1]


def bellande_step_2d(node0, node1, limit=75):
    delta_x = node1.x - node0.x
    delta_y = node1.y - node0.y
    dist = np.sqrt(delta_x ** 2 + delta_y ** 2)

    if dist < limit:
        return node1

    ratio = limit / dist
    step_x = node0.x + delta_x * ratio
    step_y = node0.y + delta_y * ratio

    return Node2D(step_x, step_y)
