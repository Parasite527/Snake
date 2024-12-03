import pygame
from enum import Enum
from source.config import *



class Skin:
    def __init__(self, head_down_pic, head_up_pic, head_left_pic, head_right_pic,
                 body_down_pic, body_up_pic, body_left_pic, body_right_pic,
                 tail_down_pic, tail_up_pic, tail_left_pic, tail_right_pic):
        
        self.head_down_pic = head_down_pic
        self.head_right_pic = head_right_pic
        self.head_left_pic = head_left_pic
        self.head_up_pic = head_up_pic

        self.tail_down_pic = tail_down_pic
        self.tail_right_pic = tail_right_pic
        self.tail_left_pic = tail_left_pic
        self.tail_up_pic = tail_up_pic

        self.body_down_pic = body_down_pic
        self.body_right_pic = body_right_pic
        self.body_left_pic = body_left_pic
        self.body_up_pic = body_up_pic


class Tile_type(Enum):
        head = 1
        body = 2
        tail = 3

class Tile(pygame.sprite.Sprite):
    def get_current_img(self, direction):
        if direction == [0, 1]:
            return self.down_pic
        elif direction == [0, -1]:
            return self.up_pic
        elif direction == [-1, 0]:
            return self.left_pic
        else:
            return self.right_pic
        
    def __init__(self, vector, center, 
                 skin, tyle_tipe, parent=None):
        super(Tile, self).__init__()
        self.tile_tipe = tyle_tipe
        self.parent = parent

        if self.tile_tipe == Tile_type.body:
            self.down_pic = skin.body_down_pic
            self.right_pic = skin.body_right_pic
            self.left_pic = skin.body_left_pic
            self.up_pic = skin.body_up_pic
        elif self.tile_tipe == Tile_type.head:
            self.down_pic = skin.head_down_pic
            self.right_pic = skin.head_right_pic
            self.left_pic = skin.head_left_pic
            self.up_pic = skin.head_up_pic
        else:
            self.down_pic = skin.tail_down_pic
            self.right_pic = skin.tail_right_pic
            self.left_pic = skin.tail_left_pic
            self.up_pic = skin.tail_up_pic



        self.rect = self.get_current_img(vector).get_rect(center=center)
        self.center = center
        self.vector = vector
        self.tyle_type = tyle_tipe 

    def get_rect(self):
        self.rect = self.get_current_img(self.vector).get_rect(center=self.center)
        return self.rect

    def change_vector(self, key):
        if key == pygame.K_LEFT:
            self.vector = [-1,0]
            self.current_pic = self.left_pic
        elif key == pygame.K_RIGHT:
            self.vector = [1,0]
            self.current_pic = self.right_pic
        elif key == pygame.K_UP:
            self.vector = [0,-1]
            self.current_pic = self.up_pic
        elif key == pygame.K_DOWN:
            self.vector = [0,1]
            self.current_pic = self.down_pic

    def move(self):
        self.center = [(self.center[0] + basic_speed * self.vector[0]) % screen.get_width(),
                       (self.center[1] + basic_speed * self.vector[1]) % screen.get_height()]
        # print(self.vector, '----', self.center)
    
    def draw(self):
        #print(self.center)
        screen.blit(self.get_current_img(self.vector), 
                         self.get_current_img(self.vector).get_rect(center=self.center))


class Snake(pygame.sprite.Sprite):
    def __init__(self, center, skin: Skin):
        super(Snake, self).__init__()

        head = Tile(basic_vector, basic_center, skin, Tile_type.head)
        self.body = [head]
        self.effects = []
        self.skin = skin
        self.is_dead = False
        self.speed = basic_speed
        self.relocation = 0
        self.rect = self.body[0].rect

        self.prev_rotates = []

        self.boosts = []

        self.collidable_body = pygame.sprite.Group()

        self.grow()
        self.grow()
        

    def change_vector(self, key):
        prev_vec = [*self.body[0].vector]
        self.body[0].change_vector(key)
        if prev_vec != self.body[0].vector:
          if(len(self.body) > 1):
                self.prev_rotates.append([[*self.body[0].vector], [*self.body[0].center]])

        

    def move(self, boosts):
        self.rect = self.body[0].rect
        additional_speed = 0
        for i in boosts:
            additional_speed += i.speed

        self.relocation += additional_speed + self.speed

        while self.relocation >= 1:
            for i in self.body:
                i.move()
                i.get_rect()

                for j in self.prev_rotates:
                    # if (0 < (i.center[0] + i.vector[0] * (self.speed + additional_speed) - j[1][0]) * i.vector[0] <= (self.speed + additional_speed) and \
                    #     abs(i.center[1] - j[1][1]) < min(self.body[1].rect.height, self.body[0].rect.width) or \
                    #     0 < (i.center[1] + i.vector[1] * (self.speed + additional_speed) - j[1][1]) * i.vector[1] <= (self.speed + additional_speed) and \
                    #     abs(i.center[0] - j[1][0]) < min(self.body[1].rect.height, self.body[0].rect.width)) and i.vector != j[0]:
                    if i.center[1] == j[1][1] and i.center[0] == j[1][0]:

                        block_len = max(self.rect.height, self.rect.width)
                        # i.center = [i.parent.center[0] - block_len * j[0][0],
                        #         i.parent.center[1] - block_len * j[0][1]]

                        i .center = [*j[1]]

                        i.vector = [*j[0]]
                        
                        if i == self.body[-1]:
                            self.prev_rotates.pop(0)
                        continue

            self.relocation -= 1


    def get_boost(self, boost):
        self.is_dead = boost.is_deadly
        self.boosts.append(boost)
        self.grow()

    def grow(self):
        block_len = max(self.rect.height, self.rect.width)

        body_tile = Tile(vector=self.body[-1].vector, 
                    center=[self.body[-1].center[0] - block_len * self.body[-1].vector[0],
                            self.body[-1].center[1] - block_len * self.body[-1].vector[1]], 
                            skin=self.skin, tyle_tipe=Tile_type.body, parent=self.body[-1])
        
        self.body.append(body_tile)
        
        if len(self.body) > 2:
            self.collidable_body.add(self.body[-1]) # todo
        # print(self.body)

    def draw(self):
        for i in self.body:
            i.draw()
