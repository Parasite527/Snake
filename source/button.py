import pygame, time
from source.config import screen, creator_basic_img_name, wall_button_pos

class Wall:
	def __init__(self, img, rect):
		self.img = img
		self.rect = rect

	def draw(self):
		screen.blit(self.img, self.rect)


class Button:
	def __init__(self, pos, img=None):
		#Core attributes 
		self.pos = pos
		self.pressed = False
		self.img = img
		self.top_rect = self.img.get_rect(center = pos)	

		

	def draw(self):
		screen.blit(self.img, self.top_rect)


	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		
		if self.top_rect.collidepoint(mouse_pos):
			if pygame.mouse.get_pressed()[0]:
				self.pressed = True
				time.sleep(0.2)
				# self.pressed = False

	def is_pressed(self):
		self.check_click()
		return self.pressed

	def create_wall(self):
		rect = self.img.get_rect(center=self.pos)
		self.pressed = False
		return Wall(self.img, rect)
		

		
class Creator:
	def __init__(self, file_name):
		img = pygame.image.load(creator_basic_img_name)
		self.buttons = [Button(wall_button_pos, img=img)]
		self.walls = []
		self.file_name = file_name

	def start(self):
		class Saved(Exception): pass
		try:
			while True:
				self.draw()

				pygame.display.update()
				
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						quit()
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_s:
							self.quit()
							raise Saved
							
				for button in self.buttons:
					if button.is_pressed():
						
						wall = button.create_wall()
						self.moving_wall(wall)
						# wall.move()
						self.walls.append(wall)
		except Saved:
			pass

	def draw(self):
		screen.fill('black')		
		for button in self.buttons:
			button.draw()

		for wall in self.walls:
			wall.draw()



	def moving_wall(self, wall):
		class Moved(Exception): pass
		try:
			while True:
				self.draw()
				wall.draw()
				pygame.display.update()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						quit()
					elif event.type == pygame.MOUSEBUTTONDOWN:
						raise Moved
					elif event.type == pygame.MOUSEMOTION:
						wall.rect.move_ip(event.rel)
		except Moved:
			pass

	def quit(self):
		# todo user inits filename
		with open(self.file_name, 'w') as f:
			for wall in self.walls:
				f.write(str(wall.rect.center[0]) + ' ' + str(wall.rect.center[1]) + '|')
				

pygame.init()	