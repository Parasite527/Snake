import pygame
from Game import Game, Level
from config import screen, font_size
from button import Creator
import random


class Menu:
    def __init__(self):
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.font = pygame.font.Font(None, font_size)

        self.active_index = 0
        self.options = ["Start Game", "Create New Level", "Highest Scores", "Quit Game"]

    def handle_action(self):
        if self.active_index == 0:
            self.start_game()
        elif self.active_index == 1:
            self.goto_creator_mod()
        elif self.active_index == 2:
            self.output_scores()
        elif self.active_index == 3:
            self.quit()
        
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.active_index = (self.active_index - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.active_index = (self.active_index + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                self.handle_action()


    def render_text(self, index):
        color = pygame.Color("red") if index == self.active_index else pygame.Color("white")
        return self.font.render(self.options[index], True, color)

    def get_text_position(self, text, index, x_offset=0, y_offset=0):
        center = (self.screen_rect.center[0] + x_offset,
                  self.screen_rect.center[1] + y_offset)
        return text.get_rect(center=center)

    def draw(self):
        screen.fill(pygame.Color("black"))
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            screen.blit(text_render, self.get_text_position(text_render, index, y_offset=(index * 2 * font_size)))


    def choose_level(self):
        n = self.get_levels_num()
        return 'Levels/level' + str(random.randint(0, n-1))



    def start_game(self):
        game = Game()
        game.start(self.choose_level())
        del(game)
        self.ending_func()

    def ending_func(self):
        screen.fill(pygame.Color("black"))
        color = pygame.Color("red") 

        text_render = pygame.font.Font(None, font_size).render('Return back to Menu(Enter)', True, color)
        screen.blit(text_render, (self.screen_rect.center[0], self.screen_rect.center[1]))

        pygame.display.update()

        while True:
            b = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        b = True
                        break
            if b:
                break       
        
        self.draw()

    def output_scores(self):
        screen.fill(pygame.Color("black"))
        color = pygame.Color("red") 
        
        with open("scores.txt", 'r') as f:
            scores = f.read()

        j = 0

        for i in scores.split():
            text_render = pygame.font.Font(None, font_size).render(i, True, color)
            screen.blit(text_render, (0, 0 + j * font_size))
            j += 1

        text_render = pygame.font.Font(None, font_size).render('Return back to Menu(Enter)', True, color)
        screen.blit(text_render, (self.screen_rect.center[0], self.screen_rect.center[1]))

        pygame.display.update()

        while True:
            b = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        b = True
                        break
            if b:
                break       
        
        self.draw()


    def get_levels_num(self):
        with open('num_of_levels', 'r') as f:
            return int(f.read())

    def goto_creator_mod(self):
        n = self.get_levels_num()
        file_name = 'Levels/level' + str(n)
        creator = Creator(file_name=file_name)
        
        creator.start()

        n += 1

        with open('num_of_levels', 'w') as f:
            f.write(str(n))

        self.ending_func()
        pass

    def quit(self):
        pygame.quit()
        quit()