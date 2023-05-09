import math
import time

while True:

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
        time.sleep(5)

    elif RES == 2:

        X1: float = float(input('Côté opposé: '))
        X2 = float(input('hypoténuse: '))

        P0 = math.sqrt(X2 ** 2 - X1 ** 2)

        print("....................................................")

        print("La valeur de l'hypoténuse est: {}".format(P0))
        time.sleep(5)

    elif RES == 3:

        X1: float = float(input('Côté adjacent: '))
        X2 = float(input('hypoténuse: '))

        P0 = math.sqrt(X2 ** 2 - X1 ** 2)

        print("....................................................")

        print("La valeur de l'hypoténuse est: {}".format(P0))
        time.sleep(5)
        
    else:
        print('réponse invalide voulez-vous réessayer')
        print("1 - Oui")
        print("2 - No")

        Souo = int(input(" "))

        if Souo == 1:
                continue

        elif Souo == 2:
                break
                time.sleep(2)
        else:
                print("option invalide!")
                print("Est seulement possible de répondre avec un numéro")
                time.sleep(4)
                
                
                
                
                
                import pygame

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
WIDTH, HEIGHT = 800, 600

# Define as cores a serem usadas
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Cria a janela do jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define o título da janela
pygame.display.set_caption("Menu do Jogo")

# Loop principal do jogo
running = True
while running:

    # Verifica se algum evento ocorreu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenche a tela com a cor branca
    screen.fill(WHITE)

    # Cria um retângulo para o botão "Iniciar"
    start_button = pygame.Rect(300, 200, 200, 50)
    pygame.draw.rect(screen, BLACK, start_button)
    font = pygame.font.Font(None, 36)
    text = font.render("Iniciar", True, WHITE)
    text_rect = text.get_rect(center=start_button.center)
    screen.blit(text, text_rect)

    # Cria um retângulo para o botão "Sair"
    quit_button = pygame.Rect(300, 300, 200, 50)
    pygame.draw.rect(screen, BLACK, quit_button)
    text = font.render("Sair", True, WHITE)
    text_rect = text.get_rect(center=quit_button.center)
    screen.blit(text, text_rect)

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
