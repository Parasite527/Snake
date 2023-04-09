import pygame
import Snake
from Food import Simple_Food, Super_Food
import random
# from Creating.py import screen # todo

#todo screensize is needed
screensize = (1400, 800)


class Food_Generator:
    def __init__(self, skin, event, screen, boost = None):
        self.food_skin = skin
        self.event = event
        self.food_boost = boost
        self.screen = screen
        
    def generate(self):
        # todo not to spawn in snake
        pos = (random.randint(0, screensize[0]), random.randint(0, screensize[1]))
        if self.food_boost == None:
            return Simple_Food(pos, self.food_skin, self.screen)
        else:
            return Super_Food(pos, self.food_skin, self.food_boost, self.screen)
  