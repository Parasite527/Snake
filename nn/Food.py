import pygame

class Simple_Food(pygame.sprite.Sprite):
    def __init__(self, pos, skin, screen):
        super(Simple_Food, self).__init__()
        self.skin = skin
        self.pos = pos
        self.screen = screen
        self.is_eaten = False
        self.rect = self.skin.get_rect(center=pos)

    def eaten(self):
        self.is_eaten = True

    def draw(self):
        self.screen.blit(self.skin, self.pos)

class Boost:
    def __init__(self, speed = 0, time = 0, new_level = False, is_deadly = False, event = None, grow = 1):
        self.speed = speed
        self.time = time
        self.new_level = new_level
        self.is_deadly = is_deadly
        self.event = event
        self.grow = grow
        # /*
        # here shoul be boosted characteristics
        # background, speed+-, snake-skin, catcher snake, new level, dead
        # */

class Super_Food(Simple_Food):
    def __init__(self, pos, skin, boost, screen):
        super().__init__(pos, skin, screen)
        self.boost = boost
        