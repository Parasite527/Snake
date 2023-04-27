import pygame
from source.Menu import Menu


pygame.init()

menu = Menu()
while True:
    menu.draw()
    pygame.display.update()
    for event in pygame.event.get():
        menu.get_event(event)






# <a href="https://www.flaticon.com/ru/free-icons/-" title="- иконки">- иконки от Freepik - Flaticon</a>
# <a href="https://www.flaticon.com/ru/free-icons/" title="кролик иконки">Кролик иконки от Icongeek26 - Flaticon</a>
# <a href="https://www.flaticon.com/ru/free-icons/" title="кирпич иконки">Кирпич иконки от Freepik - Flaticon</a>
# <a href="https://www.flaticon.com/ru/free-icons/-" title="строительство и инструменты иконки">Строительство и инструменты иконки от ADMS ICons - Flaticon</a>