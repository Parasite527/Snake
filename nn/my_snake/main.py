import pygame
import os
import sys

from Snake import Snake
from Food_Generator import Food_Generator
import Food


pygame.init()

screen = pygame.display.set_mode((1400, 800)) 

egg_pic = pygame.image.load('project/my_snake/Food/SimpleFood/egg.png')


sn_x = 300
sn_y = 300


snake = Snake([400, 400], 1, screen)

egg_gen = Food_Generator(egg_pic, 1, screen)
egg = egg_gen.generate()

all_food = pygame.sprite.Group()
all_food.add(egg)


all_food.remove

screen.blit(egg_pic,(sn_x, sn_y))

print(screen)

pygame.display.update()
running = True
angle = 0
pos = (sn_x, sn_y)
while snake.dead == False:
    screen.fill((0, 0, 0))
    egg.draw()

    snake.draw()
    pygame.display.update()
    

    res = pygame.sprite.spritecollideany(snake, all_food)
    if res:
        snake.grow()
        screen.fill((0, 0, 0))
        snake.draw()
        all_food.remove(res)
        egg = egg_gen.generate()
        all_food.add(egg)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            snake.change_vector(event.key)

    snake.move()





# <a href="https://www.flaticon.com/ru/free-icons/-" title="- иконки">- иконки от Freepik - Flaticon</a>
# <a href="https://www.flaticon.com/ru/free-icons/" title="кролик иконки">Кролик иконки от Icongeek26 - Flaticon</a>
# <a href="https://www.flaticon.com/ru/free-icons/" title="кирпич иконки">Кирпич иконки от Freepik - Flaticon</a>
# <a href="https://www.flaticon.com/ru/free-icons/-" title="строительство и инструменты иконки">Строительство и инструменты иконки от ADMS ICons - Flaticon</a>