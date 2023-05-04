import pygame
from source.config import screen_width, screen_height, screen


class Background:
    def __init__(self, color=None, back_pic=None):
        try:
            self.image = pygame.transform.scale(back_pic, (screen_width, screen_height))
        except:
            self.image = None
        
        self.color = color

    def set_color(self, color):
        self.color = color
        self.image = None

    def set_image(self, back_pic):
        self.color = None
        self.image = pygame.transform.scale(back_pic, (screen_width, screen_height))
        
    def draw(self):
        if self.image != None:
            screen.blit(self.image, (0, 0))
        else:
            screen.fill(pygame.Color(self.color))