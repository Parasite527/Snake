import pygame

screen_width = 1400
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

basic_background_color = 'black'

# color backgrounds
background_color1 = 'black'
background_color2 = 'red'
background_color3 = 'purple'
# picture-back_grounds
sky_background1 = pygame.image.load('images/backgrounds/sky.jpeg')
galaxy_background2 = pygame.image.load('images/backgrounds/galaxy1.jpeg')



basic_speed = 1
basic_vector = [0, -1]
basic_center = (100, screen.get_height() - 100)

scores_num = 10
score_pos = (0, 0)

font_size = 32

creator_basic_img_name = 'images/walls/wall4.png'
wall_button_pos = (100, screen.get_height() - 100)
