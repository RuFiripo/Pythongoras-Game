import pygame
import sys
from moviepy.editor import VideoFileClip
from PIL import Image

pygame.init()

music_background = pygame.mixer.music.load("assets/LostCompanionTomboFry.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)

lar = 550
hut = 700

screen = pygame.display.set_mode((lar, hut))
pygame.display.set_caption("Menu")




gif_path = "assets/bg.gif"
clip = VideoFileClip(gif_path)
fps = clip.fps

frames = []
for t in range(0, int(clip.duration * fps)):
    frame = clip.get_frame(t / fps)
    pil_image = Image.fromarray((frame * 255).astype('uint8'))
    pil_image = pil_image.resize((lar, hut))
    pygame_image = pygame.image.fromstring(pil_image.tobytes(), pil_image.size, pil_image.mode)
    frames.append(pygame_image)

# Carregar recursos do menu antecipadamente
fonte = pygame.font.Font(None, 30)
texto_play = fonte.render("Play", True, (0, 0, 0))
texto_quit = fonte.render("Quit", True, (0, 0, 0))
Title = fonte.render("Pythongoras-Game", True, (255, 255, 255))

def mostrar_menu():
    frame_index = 0
    clock = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if batom_play.collidepoint(evento.pos):
                    pygame.time.delay(100)
                    iniciar_jogo()
                elif batom_quit.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(frames[frame_index], (0, 0))
        
        batom_Title = pygame.Rect(190, 100 + 50, 150, 50)
        pos_text_Title = Title.get_rect(center=batom_Title.center)
        screen.blit(Title, pos_text_Title)

        batom_play = pygame.Rect(lar/2 - 75, hut/2 + 50, 150, 50)
        pygame.draw.rect(screen, (255, 255, 255), batom_play)
        pos_text_play = texto_play.get_rect(center=batom_play.center)
        screen.blit(texto_play, pos_text_play)

        if batom_play.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (200, 200, 200), batom_play)

        batom_quit = pygame.Rect(lar/2 - 75, hut/2 + 140, 150, 50)
        pygame.draw.rect(screen, (255, 255, 255), batom_quit)
        pos_text_quit = texto_quit.get_rect(center=batom_quit.center)
        screen.blit(texto_quit, pos_text_quit)

        if batom_quit.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (200, 200, 200), batom_quit)

        pygame.display.flip()

        frame_index = (frame_index + 1) % len(frames)

        clock.tick(fps)

def iniciar_jogo():
    print("O jogo começou!")
    import Chose

mostrar_menu()