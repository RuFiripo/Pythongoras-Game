import pygame
import random

pygame.init()

X = 600
Y = 680
keys = pygame.key.get_pressed()
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
Vel_arrow_Y = 0

marche = True
triggered = False

Solid_player = player.get_rect()
Solid_Enemy1 = Enemy1.get_rect()
Solid_Enemy2 = Enemy2.get_rect()
Solid_arrow = arrow.get_rect()

def respawn():
    X = random.randint(1, 550)
    Y = -10
    return [Y, X]

def respawn_arrow():
    triggered = False
    arrow_X = player_X
    arrow_Y = player_Y
    Vel_arrow_Y = 0
    return (arrow_X,arrow_Y,triggered,Vel_arrow_Y)

def colisionsE1():
    global score
    if Solid_player.colliderect(Solid_Enemy1) or Solid_Enemy1.y == 670:
        score -=1
        return True
    elif Solid_arrow.colliderect(Solid_Enemy1):
        score += 1
        return True
    else:
        return False
def colisionsE2():
    global score
    if Solid_player.colliderect(Solid_Enemy2) or Solid_Enemy2.y == 670:
        score -=1
        return True
    elif Solid_arrow.colliderect(Solid_Enemy2):
        score += 1
        return True
    else:
        return False

while marche:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            marche = False

    screen.fill((255, 255, 255))


    if keys[pygame.K_SPACE]:
        triggered = True
        Vel_arrow_Y = -1


    if Enemy1_Y == 680 and Enemy2_Y == 680:
        Enemy1_Y, Enemy1_X = respawn()
        Enemy2_Y, Enemy2_X = respawn()

    Enemy1_Y += SP
    Enemy2_Y += SP

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


    if arrow_Y == 1:
        arrow_X, arrow_Y, triggered, Vel_arrow_Y = respawn_arrow()

    arrow_Y += Vel_arrow_Y


    pygame.draw.rect(screen, (255, 0, 0), Solid_Enemy1, 4)
    pygame.draw.rect(screen, (255, 0, 0), Solid_Enemy2, 4)
    pygame.draw.rect(screen, (255, 0, 0), Solid_arrow, 4)
    pygame.draw.rect(screen, (255, 0, 0), Solid_player, 4)


    screen.blit(Enemy1, (Enemy1_X, Enemy1_Y))
    screen.blit(Enemy2, (Enemy2_X, Enemy2_Y))
    screen.blit(arrow, (arrow_X, arrow_Y))
    screen.blit(player, (player_X, player_Y))

    Solid_Enemy1.x = Enemy1_X
    Solid_Enemy1.y = Enemy1_Y
    Solid_Enemy2.x = Enemy2_X
    Solid_Enemy2.y = Enemy2_Y
    Solid_arrow.x = arrow_X
    Solid_arrow.y = arrow_Y
    Solid_player.x = player_X
    Solid_player.y = player_Y

    pygame.display.update()
