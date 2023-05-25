import pygame
import sys
import pygbutton
import random
from pygame.locals import *

pygame.init()
mainclock = pygame.time.Clock()
width = 1024
height = 768
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Quiz')

def tester_Function(event, i):
    questionUNanswered = 1
    Section1Ques = open('questions1.txt', 'r')
    with open('questions1.txt', 'r') as file:
        Section1Q = file.readlines()

    Section1Ans = open('answer1.txt', 'r')
    with open('answer1.txt', 'r') as file:
        Section1A = file.readlines()

    num1 = str(random.randint(0, 5))
    num2 = str(random.randint(0, 5))
    question = pygbutton.PygButton((100, 40, 200, 30), Section1Q[i])
    tester2 = pygbutton.PygButton((100, 70, 200, 30), 'Click Here')
    Ranswer = pygbutton.PygButton((100, 110, 200, 30), Section1A[i])
    Wanswer1 = pygbutton.PygButton((100, 150, 200, 30), num1)
    Wanswer2 = pygbutton.PygButton((100, 190, 200, 30), num2)
    winner = pygbutton.PygButton((500, 190, 200, 30), '')

    while True:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            buttonEvent = Ranswer.handleEvent(event)
            buttonEvent2 = Wanswer1.handleEvent(event)
            buttonEvent3 = Wanswer2.handleEvent(event)

            if 'click' in buttonEvent:
                winner = pygbutton.PygButton((500, 190, 200, 30), 'Winner')
                i += 1
            if 'click' in buttonEvent2:
                winner = pygbutton.PygButton((500, 190, 200, 30), 'Lose')
                i += 1
            if 'click' in buttonEvent3:
                winner = pygbutton.PygButton((500, 190, 200, 30), 'Lose')
                i += 1

        question.draw(screen)
        tester2.draw(screen)
        Ranswer.draw(screen)
        Wanswer1.draw(screen)
        Wanswer2.draw(screen)
        winner.draw(screen)

        pygame.display.update()
        mainclock.tick(60)

        if i >= len(Section1Q):
            break

i = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    tester_Function(event, i)

    pygame.display.update()
    mainclock.tick(60)