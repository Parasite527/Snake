import pygame
from config import screen,  scores_num
from Snake import Snake
from Creating import obstacle_generator, egg_pic, egg_boost, \
rabbit_boost, rabbit_pic, wall_pic, snake_skin
from Level import Level

    
class Game:
    def __init__(self):
        self.score = 0

    def render_text(self, index):
        color = pygame.Color("red") 
        return pygame.font.Font(None, 32).render(str(self.score), True, color)

    def print_score(self):
        # for index, option in enumerate(self.options):
        text_render = self.render_text(self.score)
        screen.blit(text_render, (0, 0))

    def start(self, level=None):
        if level != None:
            self.level = Level(level, wall_pic, None)
            print(level)
            # self.background = self.level.background
        else:
            pass # todo
        
        snake = Snake([0, 0], snake_skin)

        all_food = pygame.sprite.Group()
        egg = obstacle_generator.generate(egg_pic, egg_boost, snake=snake, all_food=all_food)

        rabbit = obstacle_generator.generate(rabbit_pic, rabbit_boost, snake=snake, all_food=all_food)



        all_food.add(egg)
        all_food.add(rabbit)
        all_food.add(self.level.create())
        del level

        self.boosts = []
    
    
        while snake.is_dead == False:
            
            screen.fill((0, 0, 0))
            all_food.draw(screen)
            snake.draw()
            self.print_score()

            pygame.display.update()
            

            if pygame.sprite.spritecollideany(snake, snake.collidable_body):
                break


            res = pygame.sprite.spritecollideany(snake, all_food)
            if res:
                snake.get_boost(res.get_boost())
                self.score += res.get_boost().get_score()
                self.boosts.append(res.get_boost())

                if res.get_boost().new_level:
                    print('todo!!!!!')
                    pygame.quit()
                    quit()


                
                screen.fill((0, 0, 0))
                
                snake.draw()
                all_food.remove(res)
                obstacle = obstacle_generator.generate(res.get_image(), res.get_boost(), snake=snake, all_food=all_food)

                all_food.add(obstacle)
                # all_food.add(wall)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if event.type == pygame.QUIT:
                        self.quit()
                if event.type == pygame.KEYDOWN:
                    snake.change_vector(event.key)
                    
            snake.move(self.boosts)
            
        # print(len(snake.body))
        self.quit()
            
    def quit(self):
        # save score
        with open('scores.txt', 'r') as f:
            scores = f.read().split()

        for i in scores:
            i = int(i)

        scores.sort(reverse=True)

        if len(scores) < scores_num:
            scores.append(str(self.score) + '\n')

        else:
            for h_score in scores:
                if self.score > int(h_score):
                    scores[scores.index(h_score)] = self.score
                    break
        
        with open('scores.txt', 'w') as f:
            for i in scores:
                f.write(str(i) + '\n')
    # def body(self):
