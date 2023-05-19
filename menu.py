import pygame
import sys
from moviepy.editor import VideoFileClip
from PIL import Image

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

        screen.blit(frames[frame_index], (0, 0))

        batom_play = pygame.Rect(lar/2 - 75, hut/2 + 50, 150, 50)
        pygame.draw.rect(screen, (255, 255, 255), batom_play)
        fonte = pygame.font.Font(None, 30)
        text_play = fonte.render("Jogar", True, (0, 0, 0))
        pos_text_play = text_play.get_rect(center=batom_play.center)
        screen.blit(text_play, pos_text_play)

        if batom_play.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (200, 200, 200), batom_play)

        pygame.display.flip()

        frame_index = (frame_index + 1) % len(frames)

        clock.tick(fps)

def iniciar_jogo():
    print("O jogo começou!")
    import Phitagor
    

pygame.init()

lar= 550
hut = 700

screen = pygame.display.set_mode((lar, hut))
pygame.display.set_caption("Menu Principal")

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

mostrar_menu()
