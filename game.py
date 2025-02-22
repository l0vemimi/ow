import pygame
import sys
import random

# initialize Pygame
pygame.init()

# set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("game")

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
MAROON = (128, 0, 0)
BROWN = (165, 42, 42)
CRIMSON = (220, 20, 60)
TOMATO = (255, 99, 71)
ORANGE = (255, 165, 0)
GOLD = (255, 215, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
LIME = (0, 255, 0)
AQUAMARINE = (127, 255, 212)
TURQUOISE = (64, 224, 208)
CYAN = (0, 255, 255)
AQUA = (0, 255, 255)
TEAL = (0, 128, 128)
BLUE = (0, 0, 255)  
INDIGO = (75, 0, 130)
PURPLE = (128, 0, 128)
THISTLE = (216, 191, 216)
PLUM = (221, 160, 221)
VIOLET = (238, 130, 238)
MAGENTA = (255, 0, 255)
ORCHID = (218, 112, 214)
FUCHSIA = (255, 0, 255)
LAVENDER = (230, 230, 250)
PINK = (255, 192, 203)
BEIGE = (245, 245, 220)
BISQUE = (255, 228, 196)
WHEAT = (245, 222, 179)
SIENNA = (160, 82, 45)
PERU = (205, 133, 63)
TAN = (210, 180, 140)
MOCCASIN = (255, 228, 181)
LINEN = (250, 240, 230)
BISQUE = (255, 228, 196)
MOCCASIN = (255, 228, 181)
CORNSILK = (255, 248, 220)
IVORY = (255, 255, 240)

# player image
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()
player_rect.topleft = (screen_width // 2, screen_height // 2)
player_speed = 5

# enemy image
enemy_image = pygame.image.load("enemy.png")
enemy_rect = enemy_image.get_rect()
enemy_rect.topleft = (random.randint(0, screen_width), random.randint(0, screen_height))
enemy_speed = 3

# obstacle image
obstacle_image = pygame.image.load("obstacle.png")
obstacle_rect = obstacle_image.get_rect()
obstacle_rect.topleft = (random.randint(0, screen_width), random.randint(0, screen_height))

# Camera position
camera_x = 0
camera_y = 0

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # get the set of keys pressed and check for user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # move the enemy
    if player_rect.x < enemy_rect.x:
        enemy_rect.x -= enemy_speed
    if player_rect.x > enemy_rect.x:
        enemy_rect.x += enemy_speed
    if player_rect.y < enemy_rect.y:
        enemy_rect.y -= enemy_speed
    if player_rect.y > enemy_rect.y:
        enemy_rect.y += enemy_speed
        
    # check for collision with the enemy
    if player_rect.colliderect(enemy_rect):
        print("Collision with enemy!")
        running = False
        
    # check for collision with the obstacle
    if player_rect.colliderect(obstacle_rect):
        print("Collision with obstacle!")
        running = False

    # clear the screen
    screen.fill(BEIGE)

    # draw the player
    screen.blit(player_image, player_rect)
    
    # draw the enemy
    screen.blit(enemy_image, enemy_rect)
    
    # draw the obstacle
    screen.blit(obstacle_image, obstacle_rect)
    
    # update the display
    pygame.display.flip()

    # cap the frame rate
    pygame.time.Clock().tick(60)

# quit
pygame.quit()
sys.exit()