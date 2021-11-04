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
    def __init__(self, display, x, y, width, height, color, img):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 0
        self.velo = random.randint(3, 5)
        self.color = color
        self.img = img

    def draw_box(self):
        # pygame.draw.rect(self.display, self.color,
        #                  (self.x, self.y, self.width, self.height))
        self.display.blit(self.img, [self.x, self.y])

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

    def drop_box(self):
        if self.y > display_height:
            self.x = random.randrange(0, display_width, 5)
            self.y = random.randrange(-100, 0, 5)
            self.velo = random.randint(3, 5)

        self.y += self.velo
    def is_collided(self, other):
        counter = 0
        if (self.x <= other.x <= self.x+self.width or \
        self.x <= other.x+other.width <= self.x+self.width) and \
        (self.y <= other.y <= self.y+ self.width or \
        self.y <= other.y + other.width <= self.y + self.width):

            counter += 1
            other.color = WHITE
        if counter == 3:
            return True

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("The Beach")
background_image = pygame.image.load("space.jpg")
player_img = pygame.image.load("space_ship.png")
collide_sound = pygame.mixer.Sound("laser5.ogg")


clock = pygame.time.Clock()

#player
player_width = 50
x_loc = (display_width - player_width)/2
y_loc = display_height - 2*player_width
player = Box(screen, x_loc, y_loc, player_width, player_width, BLUE, player_img)

#enemy
enemy_width = 20
enemy_list = []
for i in range(7):
    x_cord = random.randrange(0, display_width, 5)
    random_y = random.randrange(-100, 0, 5)
    enemy_list.append(Box(screen, x_cord, random_y, enemy_width, enemy_width, RED, player_img))

pygame.mouse.set_visible(False)
running = True

while running:

    pos = pygame.mouse.get_pos()
    player.x = pos[0]-.5*player.width
    player.y = pos[1]
    for event in pygame.event.get():

        # check for specific user event
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         player.speed = 5
        #     if event.key == pygame.K_LEFT:
        #         player.speed = -5
        #     if event.key == pygame.K_UP:
        #         player.velo = -5
        #     if event.key == pygame.K_DOWN:
        #         player.velo = 5
        # if event.type != pygame.KEYDOWN:
        #     player.speed = 0
        #     player.velo = 0

    screen.blit(background_image, [0, 0])


    for enemy in enemy_list:
        enemy.draw_box()
        enemy.drop_box()
        player.is_collided(enemy)



        #if enemy.y > display_height:
         #   enemy.y = random.randrange(-100, 0, 5)
          #  enemy.veol = random.ranint(1, 5)

    player.draw_box()
    player.update()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()

