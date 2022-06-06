import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 30
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
GEMS = 20
ROCKS = 10

def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y - FONT_SIZE)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the gems

    for _ in range(GEMS):

        g_text = "*"
        g_x = random.randint(1, COLS - 1)
        g_y = random.randint(1, ROWS - 1)
        
        g_position = Point(g_x, g_y)
        g_position = g_position.scale(CELL_SIZE)

        g_r = 0
        g_g = 0
        g_b = 255
        g_color = Color(g_r, g_g, g_b)
        
        # creates the gem object
        gems_art = Artifact()

        # set gem to *
        gems_art.set_text(g_text)
        
        # gem size
        gems_art.set_font_size(FONT_SIZE)
        # gem color
        gems_art.set_color(g_color)
        # gem position
        gems_art.set_position(g_position)
        # add gems to game space
        cast.add_actor("gems", gems_art)
    
    # create the rocks
    for _ in range(ROCKS):

        r_text = "O"
        r_x = random.randint(1, COLS - 1)
        r_y = MAX_Y
        
        r_position = Point(r_x, r_y)
        r_position = r_position.scale(CELL_SIZE)

        r_r = 255
        r_g = 0
        r_b = 0
        r_color = Color(r_r, r_g, r_b)
        
        # crea el objeto gemas
        rocks_art = Artifact()

        # fijar el texto de las gemas
        rocks_art.set_text(r_text)
        
        # tamaño de la letra en las gemas
        rocks_art.set_font_size(FONT_SIZE)
        # les da color a las gemas
        rocks_art.set_color(r_color)
        # fija la posicion de las gemas
        rocks_art.set_position(r_position)

        rocks_art.move_next(MAX_X,MAX_Y)
        rocks_art.set_velocity(50)
        # agrega las gemas al espacio
        cast.add_actor("rocks", rocks_art)


    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()