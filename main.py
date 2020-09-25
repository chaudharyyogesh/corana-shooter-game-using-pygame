import pygame
import random

# initialize the pygame
pygame.init()

# creating the screen
screen = pygame.display.set_mode((800, 500))

# title and icon
pygame.display.set_caption("Covid Shooter")
icon = pygame.image.load("coronavirus.png")
pygame.display.set_icon(icon)

# background

background = pygame.image.load("earth.jpg")
background = pygame.transform.scale(background, (800, 500))

# player
playerimg = pygame.image.load("battleship.png")
playerimg = pygame.transform.scale(playerimg, (68, 68))
playerx = 370
playery = 380
playerx_change = 0
playery_change = 0

enemyimg = pygame.image.load("virus.png")
enemyimg = pygame.transform.scale(enemyimg, (52, 52))
enemyx = random.randint(0, 756)
enemyy = random.randint(20, 150)
enemyx_change = 4
enemyy_change = 30

# bullet

bulletimg = pygame.image.load("bullet.png")
bulletimg = pygame.transform.scale(bulletimg, (25, 25))
bulletx = playerx + 22
bullety = playery - 25
bulletx_change = 0
bullety_change = -5
fire = 0


def palyer(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


def bullet(x, y):
    screen.blit(bulletimg, (x, y))


# game loop
running = True
while running:

    # background color

    screen.fill((255, 255, 0))

    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # key strokes event
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerx_change = -5
            bullety_change = -5
        if event.key == pygame.K_RIGHT:
            playerx_change = 5
            bullety_change = -5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerx_change = 0

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            playery_change = -5
        if event.key == pygame.K_DOWN:
            playery_change = 5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            playery_change = 0

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            fire = 1
            bulletx = playerx + 22
            bullety = playery - 25
            bullet(bulletx, bullety)

    playerx += playerx_change
    playery += playery_change

    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    if playery <= 0:
        playery = 0
    elif playery >= 436:
        playery = 436

    enemyx += enemyx_change

    if enemyx <= 0:
        enemyx_change = 4
        enemyy += enemyy_change
    elif enemyx >= 736:
        enemyx_change = -4
        enemyy += enemyy_change

    palyer(playerx, playery)
    enemy(enemyx, enemyy)

    bullety += bullety_change
    if fire is 1:
        bullet(bulletx, bullety)

    pygame.display.update()
