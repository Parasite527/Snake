import pygame
from Snake import  Skin
from Food_Generator import Food_Generator
from Food import Boost
from config import screen


snake_skin = Skin(pygame.image.load('heads/head1/head1_d.png'),
                  pygame.image.load('heads/head1/head1_u.png'),
                  pygame.image.load('heads/head1/head1_l.png'),
                  pygame.image.load('heads/head1/head1_r.png'),
                  
                  pygame.image.load('straits/strait_v.png'),
                  pygame.image.load('straits/strait_v.png'),
                  pygame.image.load('straits/strait_h.png'),
                  pygame.image.load('straits/strait_h.png'),
                  
                  pygame.image.load('tails/tail.png'),
                  pygame.image.load('tails/tail.png'),
                  pygame.image.load('tails/tail.png'),
                  pygame.image.load('tails/tail.png')
                  )

egg_pic = pygame.image.load('Food/SimpleFood/egg.png')
wall_pic = pygame.image.load('walls/wall3.png')
rabbit_pic = pygame.image.load('Food/SuperFood/rabbit1.png')

egg_boost = Boost(0, 0, False, False, 1)
wall_boost = Boost(0, 0, False, True, 0) 
rabbit_boost = Boost(speed=0.05, score=10)

obstacle_generator = Food_Generator()



