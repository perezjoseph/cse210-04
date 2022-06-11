import random
from game.shared.point import Point 
from game.directing.director import Director
# "This class will move the gems and rocks down works with the class timer"
class flyingObject(Director):
    
    def __init__(self, keyboard_service, video_service):
        super().__init__(keyboard_service, video_service)
    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        gems = cast.get_actors("gems")
        rocks = cast.get_actors("rocks")
        velocityGem = self._keyboard_service.move()
        for gem in gems:
            gem.set_velocity(velocityGem)
        for rock in rocks:
            rock.set_velocity(velocityGem)

        velocity = self._keyboard_service.get_direction()      
        robot.set_velocity(velocity)