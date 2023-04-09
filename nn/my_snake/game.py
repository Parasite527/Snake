import pygame

class Snake:
    def __init__(self, x, y, skin):
        self.head = [x, y]
        self.body = ()
        self.speed = 5
        self.vector = [0, 1]
        self.effects = []
        self.skin = ()
        self.dead = False

    def eat(self):
        if 

    def move(self):
        self.head[0] += speed * self.vector[0]
        self.head[1] += speed * self.vector[1]

    def display(self):
        ..


class Effects:
    def __init__(self):
        self.time = () #todo
        # /*
        # here shoul be boosted characteristics
        # background, speed+-, snake-skin, catcher snake, new level, dead
        # */

class Food:
    def __init__(self, image, x, y):
        self.image = ()
        self.size = ()
        self.center = ()

    def display(self):
        ..

    def erasing(self):
        ..

    #todo mb 
    def is_eaten(self):
        ..

class Super_Food(Food):
    # includes extra effect
    bhfds

class Background:
    def __init__(self, image, window_size):
        background = pygame.image.load(image)
        self.image = background

    def display(self, window):    
        window.blit(self._image, (0, 0))

class Game:
    ....

class Displayer:
    ...

class Builder:
    ...

class Saver:
    ...