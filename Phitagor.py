import pygame
import random

pygame.init()

X = 600
Y = 680

SP=0.5

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("mon jeux")

player = pygame.image.load("assets/player.png").convert_alpha()
player = pygame.transform.scale(player, (55, 55))

player_X = 250
player_Y = 620

Enemy1 = pygame.image.load("assets/Enamie_X.png").convert_alpha()
Enemy1 = pygame.transform.scale(Enemy1, (35, 35))

Enemy1_X = 250
Enemy1_Y = -2

Enemy2 = pygame.image.load("assets/Enamie_Y.png").convert_alpha()
Enemy2 = pygame.transform.scale(Enemy2, (35, 35))

Enemy2_X = 250
Enemy2_Y = -2

arrow = pygame.image.load("assets/tiro.png").convert_alpha()
arrow = pygame.transform.scale(arrow, (40, 40))

arrow_X = 250
arrow_Y = 620

marche = True

def respawn():
    X = random.randint(1, 550)
    Y = -10
    return [Y, X]

def respawn_arrow():
    global arrow_Y
    triggered = False
    respawn_arrow_X = arrow_X
    respawn_arrow_Y = arrow_Y
    arrow_Y = -2
    return (respawn_arrow_X, respawn_arrow_Y, arrow_Y)

while marche:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            marche = False

    screen.fill((255, 255, 255))

    triggered = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        triggered = True
        arrow_Y += -1

    if Enemy1_Y == 680 and Enemy2_Y == 680:
        Enemy1_Y, Enemy1_X = respawn()
        Enemy2_Y, Enemy2_X = respawn()

    if arrow_Y == -2:
        arrow_X, arrow_Y = respawn_arrow()

    Enemy1_Y += SP
    Enemy2_Y += SP

    screen.blit(arrow, (arrow_X, arrow_Y))

    screen.blit(player, (player_X, player_Y))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_X > 1:
        player_X -= SP
        if not triggered:
            arrow_X -= SP
    if keys[pygame.K_RIGHT] and player_X < 550:
        player_X += SP
        if not triggered:
            arrow_X += SP
    if keys[pygame.K_UP] and player_Y > 1:
        player_Y -= SP
        if not triggered:
            arrow_Y -= SP
    if keys[pygame.K_DOWN] and player_Y < 630:
        player_Y += SP
        if not triggered:
            arrow_Y += SP

    screen.blit(Enemy1, (Enemy1_X, Enemy1_Y))
    screen.blit(Enemy2, (Enemy2_X, Enemy2_Y))

    pygame.display.update()