import pygame
from Creating import wall_boost, obstacle_generator
from config import screen, creator_basic_img_name

class Level: #todo fill spites of walls into game.all_food
    def __init__(self, file_name, wall_img=creator_basic_img_name, background=None):
        self.file_name = file_name
        self.wall_img = pygame.image.load(creator_basic_img_name)
        self.walls = []
        self.background = background
        positions = []
        coords = []
        with open(file_name, 'r') as f:
            positions = f.read().split('|')

        # print(positions)
        
        if positions == ['']:
            return
        
        
        try:
            positions.remove('\n')
        except:
            pass

        try:
            positions.remove('')
        except:
            pass


        for i in positions:
            coords.append(i.split())

        for pos in coords:
            self.walls.append(obstacle_generator.generate(self.wall_img, wall_boost, (int(pos[0]), int(pos[1]))))


    def create(self):
        return self.walls
    
    def draw(self):
        for wall in self.walls:
            wall.draw()
