import pygame
import sys

pygame.init()

lar = 550
hut = 700

screen = pygame.display.set_mode((lar, hut))
pygame.display.set_caption("Menu")

Lock = pygame.image.load("assets/lock.png").convert_alpha()
Lock = pygame.transform.scale(Lock, (55, 55))
Lock_X = 220
Lock_Y = 125

win = False

fonte = pygame.font.Font(None, 30)
texto_game2 = fonte.render("Space invaders", True, (0, 0, 0))
texto_game1 = fonte.render("Quiz", True, (0, 0, 0))
texto_info = fonte.render("Montrez que vous avez ", True, (255, 255, 255))
texto_info1 = fonte.render("les connaissances nécessaires ", True, (255, 255, 255))
def mostrar_menu():
    frame_index = 0
    clock = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if batom_game1.collidepoint(evento.pos):
                    import Quiz

                elif batom_game2.collidepoint(evento.pos):
                    if win == False:
                        batom_info1 = pygame.Rect(100, 500 + 50, 150, 50)
                        pos_text_info = texto_info.get_rect(center=batom_info1.center)
                        screen.blit(texto_info, pos_text_info)
                        batom_info1 = pygame.Rect(100, 520 + 50, 150, 50)
                        pos_text_info1 = texto_info1.get_rect(center=batom_info1.center)
                        screen.blit(texto_info1, pos_text_info1)
                    
                    elif win == True:
                        import Phitagor


        batom_game2 = pygame.Rect(40, 80 + 50, 150, 50)
        pygame.draw.rect(screen, (255, 255, 255), batom_game2)
        pos_text_game2 = texto_game2.get_rect(center=batom_game2.center)
        screen.blit(texto_game2, pos_text_game2)

        if batom_game2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (200, 200, 200), batom_game2)

        batom_game1 = pygame.Rect(40, 40, 150, 50)
        pygame.draw.rect(screen, (255, 255, 255), batom_game1)
        pos_text_game1 = texto_game1.get_rect(center=batom_game1.center)
        screen.blit(texto_game1, pos_text_game1)

        if batom_game1.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (200, 200, 200), batom_game1)

        screen.blit(Lock, (Lock_X, Lock_Y))

        pygame.display.flip()


def iniciar_jogo():
    print("O jogo começou!")
    import Chose

mostrar_menu()