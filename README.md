# PygEngine

PygEngine is a simple wrapper around the Pygame library for Python.  It simplifies the starting of a new project without having to worry about building another game loop to test your new idea.

To get started, you'll want to clone this repo into an Engine folder.  Use the code below as a start to get going:

````python

import pygame
from Engine.Engine import Engine  # 1


class Game: # 2
    def __init__(self): # 3
        pass
    
    def update(self, dt): # 4
        pass
       
    def draw(self, canvas): # 5
        pygame.draw.rect(canvas, (200, 0, 0), (20, 20, 20, 20))
    
    def handle_event(self, event): # 6
        pass


e = Engine(Game) #7
e.game_loop() #8
````

### Description

1.  This is our wrapper around pygame.  To use it, we need to instantiate it with a class reference.
2.  This is our Game object.  The game object requires an update, draw, and handle_event methods.  The Engine will call these when the time comes
3.  This is where the setup of the game should happen
4.  Update is called on each iteration of the game loop.  It is handed a dt, which is the amount of milliseconds since the last update as an int.  Need to double check that.
5.  The draw method is handed the canvas to draw on, and is called on each game loop.
6.  When an input event happens, the Engine calls this method with the event object as an argument.  You can also poll which keys are pressed at any point in the process by using pygame.keys.get_pressed()
7.  To start all this, we hand the Engine a reference to our Game class.  The engine itself will instantiate the class.
8.  Call the game_loop method on our engine to start the game
