import pygame
from heads import *


class Snake(pygame.sprite.Sprite):
    def __init__(self, pos, skin, screen):
        super(Snake, self).__init__()
        # self.head = pos
        self.body = [[[0, 1], pos]]
        self.speed = 0.5
        # self.vector = [0, 1]
        self.effects = []
        self.skin = ()
        self.dead = False
        self.screen = screen # todo
        
        self.head_down_pic = pygame.image.load('heads/head1/head1_d.png')
        self.head_up_pic = pygame.image.load('heads/head1/head1_u.png')
        self.head_right_pic = pygame.image.load('heads/head1/head1_r.png')
        self.head_left_pic = pygame.image.load('heads/head1/head1_l.png')

        self.up = pygame.image.load('straits/strait_v.png')
        self.down = pygame.image.load('straits/strait_v.png')
        self.left = pygame.image.load('straits/strait_h.png')
        self.right = pygame.image.load('straits/strait_h.png')

        self.tail_down_pic = pygame.image.load('heads/head1/head1_d.png')
        self.tail_up_pic = pygame.image.load('heads/head1/head1_u.png')
        self.tail_right_pic = pygame.image.load('heads/head1/head1_r.png')
        self.tail_left_pic = pygame.image.load('heads/head1/head1_l.png')

        self.current_head_pic = self.head_down_pic
        self.current_tail_pic = None
        self.rect = self.current_head_pic.get_rect(center=self.body[0][1])

        self.rotates = []
        
        # self.strait_pic = pygame.image.load('strait.png')
        # self.lu_corner = pygame.image.load('lu_corner.png')

    def change_vector(self, key):
        print(self.rotates)
        if key == pygame.K_LEFT:
            self.body[0][0] = [-1,0]
            self.current_head_pic = self.head_left_pic
            if(len(self.body) > 1):
                self.rotates.append([[self.body[0][0][0], self.body[0][0][1]], [self.body[0][1][0], self.body[0][1][1]]])
        elif key == pygame.K_RIGHT:
            self.body[0][0] = [1,0]
            self.current_head_pic = self.head_right_pic
            if(len(self.body) > 1):
                self.rotates.append([[self.body[0][0][0], self.body[0][0][1]], [self.body[0][1][0], self.body[0][1][1]]])
        elif key == pygame.K_UP:
            self.body[0][0] = [0,-1]
            self.current_head_pic = self.head_up_pic
            if(len(self.body) > 1):
                self.rotates.append([[self.body[0][0][0], self.body[0][0][1]], [self.body[0][1][0], self.body[0][1][1]]])
        elif key == pygame.K_DOWN:
            self.body[0][0] = [0,1]
            self.current_head_pic = self.head_down_pic
            if(len(self.body) > 1):
                self.rotates.append([[self.body[0][0][0], self.body[0][0][1]], [self.body[0][1][0], self.body[0][1][1]]])
        
        


    # def set_tail(self):
    #     if self.body[-2][0] == 'up':
    #         self.current_tail_pic = self.tail_up_pic
    #     elif self.body[-2][0] == 'down':
    #         self.current_tail_pic = self.tail_down_pic
    #     elif self.body[-2][0] == 'left':
    #         self.current_tail_pic = self.tail_left_pic
    #     else:
    #         self.current_tail_pic = self.tail_right_pic

    def move(self):
        # self.head[0] += self.speed * self.vector[0]
        # self.head[1] += self.speed * self.vector[1]
        self.rect = self.current_head_pic.get_rect(center=self.body[0][1])
        for i in self.body:
            i[1][0] += self.speed * i[0][0]
            i[1][1] += self.speed * i[0][1]
            # try:
            #     print(abs(i[0][0]) == 1, abs(i[1][1] == self.rotates[0][1][1] < 30), abs(i[1][0] - self.rotates[0][1][0] < 40))
            # except:
            #     pass
            if self.body[0][1][0] < 0 or self.body[0][1][0] > self.screen.get_width() or self.body[0][1][1] < 0 or self.body[0][1][1] > self.screen.get_height():
                self.dead = True

            for j in self.rotates:
                if i[0][0] == 0 and abs(i[1][0] - j[1][0] == 0) and abs(i[1][1] - j[1][1] == 0):
                    i[0] = [*j[0]]
                    if i == self.body[-1]:
                        self.rotates.pop(0)
                elif abs(i[0][0]) == 1 and abs(i[1][1] - j[1][1] == 0) and abs(i[1][0] - j[1][0] == 0):
                    i[0] = [*j[0]]
                    if i == self.body[-1]:
                        self.rotates.pop(0)
                    
        # if len(self.rotates) > 0:
            # print(self.rotates)
            # print(self.body)

    def tile_current_img(self, direction):
        if direction == [0, 1]:
            return self.up
        elif direction == [0, -1]:
            return self.down
        elif direction == [-1, 0]:
            return self.left
        else:
            return self.right

    def grow(self):
        if(len(self.body) > 1):
            self.body.append([self.body[-1][0], [self.body[-1][1][0] - 40 * self.body[-1][0][0],
                                              self.body[-1][1][1] - 40 * self.body[-1][0][1]]])
        else:
            self.body.append([self.body[-1][0], [self.body[-1][1][0] - 40 * self.body[-1][0][0],
                                              self.body[-1][1][1] - 40 * self.body[-1][0][1]]])
        
        # print(self.body)

    def draw(self):
        self.screen.blit(self.current_head_pic, self.body[0][1])
        if len(self.body) == 1:
            return
        
        for i in range(1, len(self.body), 1):
            self.screen.blit(self.tile_current_img(self.body[i][0]), self.body[i][1])
        # self.screen.blit(self.current_tail_pic, self.head)