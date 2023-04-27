import pygame
from source.Food import SimpleFood
import random
from source.config import screen


class FoodGenerator:
    def __init__(self):
        pass

    def get_possible_place(self, snake, all_food, skin, boost):
        full_snake = pygame.sprite.Group()
        full_snake = snake.collidable_body.copy()
        full_snake.add(snake)
        while True:
                pic_width = skin.get_rect().width
                pic_height = skin.get_rect().height
                self.pos = (random.randint(0 + pic_width // 2, screen.get_width() - pic_width // 2), 
                            random.randint(0 + pic_height // 2, screen.get_height() - pic_height // 2))
                checker = SimpleFood(self.pos, skin, boost)
                # print(self.pos)
                collided_with_snake = pygame.sprite.spritecollideany(checker, full_snake)
                collided_with_obstacles = pygame.sprite.spritecollideany(checker, all_food)

                if not (collided_with_snake or collided_with_obstacles):
                    break

                del checker

        del full_snake


    def generate(self, skin, boost = None, pos=None, snake=None, all_food=None):
        # todo not to spawn in snake
        self.pos = pos
        if pos == None:
            self.get_possible_place(snake, all_food, skin, boost)

        # print(self.pos)
        return SimpleFood(self.pos, skin, boost)

  