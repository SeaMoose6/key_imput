import pygame
import math
import random

#in terminal "pip install pygame"

pygame.init()

# constants
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


PI = math.pi
display_width = 1000
display_height = 750
SIZE = (display_width, display_height)
FPS = 60


# functions

class Box():
    def __init__(self, display, x, y, width, height):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 0
        self.velo = 0

    def draw_box(self):
        pygame.draw.rect(self.display, RED,
                         (self.x, self.y, self.width, self.height))

    def update(self):
        self.x += self.speed
        self.y += self.velo

        if self.x <=0:
            self.x = 0
        elif self.x + self.width >= display_width:
            self.x = display_width - self.width

        if self.y <=0:
            self.y = 0
        elif self.y + self.height >= display_height:
            self.y = display_height - self.height

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("The Beach")

clock = pygame.time.Clock()

#player
player_width = 50
x_loc = (display_width - player_width)/2
y_loc = display_height - 2*player_width
player = Box(screen, x_loc, y_loc, player_width, player_width)
#enemy
enemy_width = 50
enemy_list = []
for i in range(7):
    x_cord = i * enemy_width // 6
    random_y = random.randrange(-100, 0, 5)
    enemy_list.append(Box(screen, x_cord, random_y, enemy_width, enemy_width))
running = True

while running:

    for event in pygame.event.get():

        # check for specific user event
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.speed = 5
            if event.key == pygame.K_LEFT:
                player.speed = -5
            if event.key == pygame.K_UP:
                player.velo = -5
            if event.key == pygame.K_DOWN:
                player.velo = 5
        if event.type != pygame.KEYDOWN:
            player.speed = 0
            player.velo = 0

    screen.fill(WHITE)
    player.draw_box()
    player.update()

    for enemy in enemy_list:
        enemy.draw_box()
        enemy.drop_box()

        if enemy.y > display_height:
            enemy.y = random.randrange(-100, 0, 5)
            enemy.y_speed = random.ranint(1, 5)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()

