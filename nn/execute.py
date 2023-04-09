import pygame
import sys
from game import game


pygame.init()

current_game = Game()
current_game.play()
pygame.quit()
sys.exit()