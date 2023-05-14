import pygame
import sys
import random


def mov_player(player_X, player_Y):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_X > 1:
        player_X -= 1
    if keys[pygame.K_RIGHT] and player_X < 550:
        player_X += 1
    if keys[pygame.K_UP] and player_Y > 1:
        player_Y -= 1
    if keys[pygame.K_DOWN] and player_Y < 630:
        player_Y += 1
    return player_X, player_Y


pygame.init()

X = 600
Y = 680

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("mon jeux")

player = pygame.image.load("assets/player.png").convert_alpha()
player = pygame.transform.scale(player, (50, 50))

player_X = 250
player_Y = 600

Enemy1 = pygame.image.load("assets/Enamie_X.png").convert_alpha()
Enemy1 = pygame.transform.scale(Enemy1, (50, 50))

Enemy1_X = 250
Enemy1_Y = -50

Enemy2 = pygame.image.load("assets/Enamie_Y.png").convert_alpha()
Enemy2 = pygame.transform.scale(Enemy2, (50, 50))

Enemy2_X = 250
Enemy2_Y = -50

marche = True


def respawn():
    X = random.randint(1, 550)
    Y = 1
    return [Y, X]


while marche:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            marche = False

    screen.fill((255, 255, 255))

    if Enemy1_Y == 680 and Enemy2_Y == 680:
        Enemy1_Y, Enemy1_X = respawn()
        Enemy2_Y, Enemy2_X = respawn()

    Enemy1_Y += 1
    Enemy2_Y += 1

    player_X, player_Y = mov_player(player_X, player_Y)
    screen.blit(player, (player_X, player_Y))
    screen.blit(Enemy1, (Enemy1_X, Enemy1_Y))
    screen.blit(Enemy2, (Enemy2_X, Enemy2_Y))

    pygame.display.update()