import pygame
from source.Snake import Skin
from source.Food_Generator import FoodGenerator
from source.Food import Boost
from source.config import screen, basic_background_color
from source.Background import Background

background = Background(color=basic_background_color)

snake_skin = Skin(pygame.image.load('images/heads/head1/head1_d.png'),
                  pygame.image.load('images/heads/head1/head1_u.png'),
                  pygame.image.load('images/heads/head1/head1_l.png'),
                  pygame.image.load('images/heads/head1/head1_r.png'),
                  
                  pygame.image.load('images/straits/strait_v.png'),
                  pygame.image.load('images/straits/strait_v.png'),
                  pygame.image.load('images/straits/strait_h.png'),
                  pygame.image.load('images/straits/strait_h.png'),
                  
                  pygame.image.load('images/tails/tail.png'),
                  pygame.image.load('images/tails/tail.png'),
                  pygame.image.load('images/tails/tail.png'),
                  pygame.image.load('images/tails/tail.png')
                  )

egg_pic = pygame.image.load('images/Food/SimpleFood/egg.png')
wall_pic = pygame.image.load('images/walls/wall3.png')
rabbit_pic = pygame.image.load('images/Food/SuperFood/rabbit1.png')

egg_boost = Boost(0, 0, False, False, 1)
wall_boost = Boost(0, 0, False, True, 0) 
rabbit_boost = Boost(speed=0.05, score=10)

obstacle_generator = FoodGenerator()



