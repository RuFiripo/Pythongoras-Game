import math
import time
import pygame

pygame.init()


WIDTH, HEIGHT = 800, 600


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Menu de Jeux")


running = True
while running:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(WHITE)

   
    start_button = pygame.Rect(300, 200, 200, 50)
    pygame.draw.rect(screen, BLACK, start_button)
    font = pygame.font.Font(None, 36)
    text = font.render("Comonsé", True, WHITE)
    text_rect = text.get_rect(center=start_button.center)
    screen.blit(text, text_rect)


    print("           I \                                       ")
    print("           I   \                                     ")
    print("       3   I     \   1                               ")
    print("           I       \                                 ")
    print("           I_________\                               ")
    print("               2                                     ")

    print("De quel côté veux-tu calculer ?")
    print("1 - hypoténuse")
    print("2 - côté adjacent")
    print("3 - Côté opposé")

    RES = int(input('Saisissez l option souhaitée: '))

    if RES == 1:

        X1 = float(input('Côté opposé: '))
        X2 = float(input('côté adjacent: '))

        P0 = math.sqrt( X2 ** 2 + X1 ** 2)

        print("....................................................")

        print("O valor da hypoténuse é: {}".format(P0))
        time.sleep(2)

    elif RES == 2:

        X1: float = float(input('Côté opposé: '))
        X2 = float(input('hypoténuse: '))

        P0 = math.sqrt(X2 ** 2 - X1 ** 2)

        print("....................................................")

        print("La valeur du côté adjacent/opposé est: {}".format(P0))
        time.sleep(2)

    elif RES == 3:

        X1: float = float(input('Côté adjacent: '))
        X2 = float(input('hypoténuse: '))

        P0 = math.sqrt(X2 ** 2 - X1 ** 2)

        print("....................................................")

        print("La valeur du côté adjacent/opposé est: {}".format(P0))
        time.sleep(2)
         
           
    quit_button = pygame.Rect(300, 300, 200, 50)
    pygame.draw.rect(screen, BLACK, quit_button)
    text = font.render("sortir", True, WHITE)
    text_rect = text.get_rect(center=quit_button.center)
    screen.blit(text, text_rect)

  
    pygame.display.flip()


pygame.quit()

                
                
                
                
                
                
