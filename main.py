import pygame
import random
import math
from pygame import mixer

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

# background music
mixer.music.load('background.wav')
mixer.music.play(-1)

# player
playerimg = pygame.image.load("battleship.png")
playerimg = pygame.transform.scale(playerimg, (68, 68))
playerx = 370
playery = 390
playerx_change = 0
playery_change = 0

enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 3
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("virus.png"))
    enemyimg[i] = pygame.transform.scale(enemyimg[i], (52, 52))
    enemyx.append(random.randint(0, 735))
    enemyy.append(random.randint(20, 150))
    enemyx_change.append(4)
    enemyy_change.append(30)

# bullet

bulletimg = pygame.image.load("bullet.png")
bulletimg = pygame.transform.scale(bulletimg, (25, 25))
bulletx = playerx + 22
bullety = 400
bulletx_change = 0
bullety_change = -5
fire = 0

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 28)
textx = 10
texty = 10

# game over text
over_font = pygame.font.Font('freesansbold.ttf', 60)
overx = 280
overy = 220


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255, 0.5))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def bullet(x, y):
    screen.blit(bulletimg, (x, y))


def isCollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt(math.pow((enemyx - bulletx), 2) + math.pow((enemyy - bullety), 2))
    if distance < 27:
        return True
    else:
        return False


# game over fun
def game_over_text(x, y):
    over_text = over_font.render("Game Over. ", True, (255, 255, 255))
    screen.blit(over_text, (x, y))

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
        if event.key == pygame.K_RIGHT:
            playerx_change = 5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerx_change = 0

    # if event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_UP:
    #         playery_change = -5
    #     if event.key == pygame.K_DOWN:
    #         playery_change = 5
    # if event.type == pygame.KEYUP:
    #     if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
    #         playery_change = 0

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            if fire == 0:
                mixer.Sound('laser.wav').play()
                bulletx = playerx + 22
                bullety = 400
                fire = 1

    playerx += playerx_change
    # playery += playery_change

    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    # if playery <= 0:
    #     playery = 0
    # elif playery >= 436:
    #     playery = 436

    for i in range(num_of_enemies):

        # game over
        if enemyy[i] > 350:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
            game_over_text(overx, overy)
            break

        enemyx[i] += enemyx_change[i]

        if enemyx[i] <= 0:
            enemyx_change[i] = 4
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -4
            enemyy[i] += enemyy_change[i]

        collision = isCollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            mixer.Sound('explosion.wav').play()
            bullety = 400
            fire = 0
            score_value += 1
            enemyx[i] = random.randint(0, 735)
            enemyy[i] = random.randint(20, 150)

        enemy(enemyx[i], enemyy[i], i)

    # moving bullet up
    if fire is 1:
        bullety += bullety_change
        bullet(bulletx, bullety)
        if bullety <= 0:
            bullety = 450
            fire = 0

    player(playerx, playery)
    show_score(textx, texty)

    pygame.display.update()
