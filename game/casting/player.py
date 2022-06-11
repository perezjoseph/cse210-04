from game.casting.actor import Actor
from game.shared.point import Point
"The responsability of this class is to control how the robot wraps, also control the area of the grid and contains the score"
class Player(Actor):
    def __init__(self):
        super().__init__()
        self.points = 0
    "Limits the movement of the robot"
    def wrap(self, max_x, max_y):
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y())
        if y > max_y - 20 :
            #y = self._position.get_y() - self._position.get_y() ##int(round(max_y /10))
            y = max_y - 20
        if y < max_y - 100:
            y = max_y - 100
        self._position = Point(x, y)
    "Add Score"
    def sumScore(self):
        self.points += 100
    "Substract Score"
    def sub(self): 
        self.points -= 100