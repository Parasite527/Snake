import pygame
from source.config import screen

class Boost:
    def __init__(self, speed = 0, timer = None, new_level = False, is_deadly = False, score = 0):
        self.speed = speed
        self.timer = timer
        self.new_level = new_level
        self.is_deadly = is_deadly
        self.score = score
        # /*
        # here shoul be boosted characteristics
        # background, speed+-, catcher snake, new level, dead
        # */
    def apply(self, snake):
        snake.speed = self.speed
        snake.is_dead = self.is_deadly
    
    def get_score(self):
        return self.score
        

class SimpleFood(pygame.sprite.Sprite):
    def __init__(self, center, skin, boost=None):
        super(SimpleFood, self).__init__()
        self.image = skin
        self.center = center
        self.is_eaten = False

        self.rect = self.image.get_rect(center=center) # topleft
        self.boost = boost

    def eaten(self):
        self.is_eaten = True

    def get_boost(self):
        return self.boost
    
    def get_image(self):
        return self.image

    def draw(self):
        screen.blit(self.image, self.rect)

        