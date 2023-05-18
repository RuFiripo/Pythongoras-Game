import pygame
import random
import sys

pygame.init()

X = 550
Y = 700
keys = pygame.key.get_pressed()
SP = 0.5

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

explosion_gif = pygame.image.load("assets/explosion.gif").convert_alpha()
explosion_gif = pygame.transform.scale(explosion_gif, (30, 30))

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

score = 0
game_over = False

font = pygame.font.Font(None, 36)  
timer_font = pygame.font.Font(None, 48)  

start_ticks = pygame.time.get_ticks() 
game_duration = 2 * 60 * 1000  

def respawn():
    X = random.randint(1, 500)
    Y = -10
    return [X, Y]  

def respawn_arrow():
    triggered = False
    arrow_X = player_X
    arrow_Y = player_Y
    Vel_arrow_Y = 0
    return (arrow_X, arrow_Y, triggered, Vel_arrow_Y)

def colisionsE1():
    global score
    if Solid_player.colliderect(Solid_Enemy1) or Solid_Enemy1.y == 670:
        score -= 1
        return True
    elif Solid_arrow.colliderect(Solid_Enemy1):
        score += 1
        return True
    else:
        return False

def colisionsE2():
    global score
    if Solid_player.colliderect(Solid_Enemy2) or Solid_Enemy2.y == 670:
        score -= 1
        return True
    elif Solid_arrow.colliderect(Solid_Enemy2):
        score += 1
        return True
    else:
        return False

def format_time(milliseconds):
    seconds = milliseconds // 1000
    minutes = seconds // 60
    seconds %= 60
    return f"{minutes:02}:{seconds:02}"  

while marche:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            marche = False

    screen.fill((255, 255, 255))

    if Enemy1_Y == 660 or Enemy2_Y == 660:
        game_over = True

    if keys[pygame.K_SPACE]:
        triggered = True
        Vel_arrow_Y = -2

        if arrow_Y <= 1:
            arrow_X, arrow_Y, triggered, Vel_arrow_Y = respawn_arrow()

    player_X, player_Y = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_X > 1:
        player_X -= SP
        if not triggered:
            arrow_X -= pygame.mouse.get_pos()
    if keys[pygame.K_RIGHT] and player_X < 550:
        player_X += SP
        if not triggered:
            arrow_X += pygame.mouse.get_pos()
    if keys[pygame.K_UP] and player_Y > 1:
        player_Y -= SP
        if not triggered:
            arrow_Y -= pygame.mouse.get_pos()
    if keys[pygame.K_DOWN] and player_Y < 630:
        player_Y += SP
        if not triggered:
            arrow_Y += pygame.mouse.get_pos()
    
    
    Solid_Enemy1.x = Enemy1_X
    Solid_Enemy1.y = Enemy1_Y

    Solid_Enemy2.x = Enemy2_X
    Solid_Enemy2.y = Enemy2_Y

    Solid_arrow.x = arrow_X
    Solid_arrow.y = arrow_Y

    Solid_player.x = player_X
    Solid_player.y = player_Y

    Enemy1_Y += SP
    Enemy2_Y += SP
    
    
    if Enemy1_Y == 670 or colisionsE1():
        screen.blit(explosion_gif, (Enemy1_X, Enemy1_Y))
        Enemy1_X, Enemy1_Y = respawn() 
    
    if Enemy2_Y == 670 or colisionsE2():
        screen.blit(explosion_gif, (Enemy2_X, Enemy2_Y))
        Enemy2_X, Enemy2_Y = respawn()  
        
    
    if arrow_Y == 1:
        arrow_X, arrow_Y, triggered, Vel_arrow_Y = respawn_arrow()

    arrow_Y += Vel_arrow_Y

    

    pygame.draw.rect(screen, (0, 0, 0), Solid_Enemy1, 4)
    pygame.draw.rect(screen, (0, 0, 0), Solid_Enemy2, 4)
    pygame.draw.rect(screen, (0, 0, 0), Solid_arrow, 4)
    pygame.draw.rect(screen, (0, 0, 0), Solid_player, 4)

    screen.blit(Enemy1, (Enemy1_X, Enemy1_Y))
    screen.blit(Enemy2, (Enemy2_X, Enemy2_Y))
    screen.blit(arrow, (arrow_X, arrow_Y))
    screen.blit(player, (player_X, player_Y))


    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    
    elapsed_time = pygame.time.get_ticks() - start_ticks
    remaining_time = max(0, game_duration - elapsed_time)
    timer_text = timer_font.render(format_time(remaining_time), True, (0, 0, 0))
    screen.blit(timer_text, (X - 120, 10))

    pygame.display.update()

    if game_over:
        screen.fill((0, 0, 0))  

        game_over_text = font.render("Game Over", True, (255, 255, 255))
        text_rect = game_over_text.get_rect(center=(X // 2, Y // 2))
        screen.blit(game_over_text, text_rect)

        pygame.display.flip()

        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
