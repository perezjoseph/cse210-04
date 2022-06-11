from game.services.keyboard_service import KeyboardService
from game.shared.point import Point
import random
"This Class controls the movement of rocks and gems"
class timer(KeyboardService):

    def __init__(self, cell_size = 1):
        super().__init__()
    def move(self):
        dx=0
        dy =0
        dy = 1
        direction = Point(dx,dy)
        direction = direction.scale(self._cell_size)
        return direction