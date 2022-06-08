import random
from game.shared.point import Point 
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()      
        robot.set_velocity(velocity) 
    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        gems = cast.get_actors("gems")
        rocks = cast.get_actors("rocks")
        
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.wrap(max_x, max_y)
        
        for gem in gems:
            gem.move_next(max_x, max_y)
            if robot.get_position().equals(gem.get_position()):
                g_x = random.randint(1, 599)
                g_y = random.randint(1, 1)
                robot.sumScore()
                gem.set_position(Point(g_x, g_y))
                banner.set_text(f'Score: {robot.points}')
                #Increase score
        for rock in rocks:
            rock.move_next(max_x, max_y)
            if robot.get_position().equals(rock.get_position()):
                robot.sub()
                r_x = random.randint(1, 599)
                r_y = random.randint(1, 1)
                banner.set_text(f'Score: {robot.points}')
                rock.set_position(Point(r_x, r_y))
                # Decrease score
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

# "This class will move the gems and rocks down"
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
    

         
        