import pygame,time,sys,pygbutton,random,time
from pygame.locals import *

pygame.init()
mainclock = pygame.time.Clock()
width = 1024
height = 768
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption('Quiz')
background = pygame.image.load("tv2.png").convert()
background_poistion = [0,0]
screen.blit(background,background_poistion)
pygame.display.flip()

######tester
def tester_Function():
    i = 0

    questionUNanswered = 1
    Section1Q = [0]*5
    Section1Ques = open('questions1.txt','r')
    with open('questions1.txt','r') as file:
        Section1Q = file.readlines()

    Section1A = [0]*5
    Section1Ans = open('answer1.txt','r')
    with open('answer1.txt','r') as file:
        Section1A = file.readlines()
    num1 = str(random.randint(0,5))
    num2 = str(random.randint(0,5))
    question = pygbutton.PygButton((100,40,200,30),Section1Q[i])
    tester2 = pygbutton.PygButton((100,70,200,30),'Clicl Here')
    Ranswer = pygbutton.PygButton((100,110,200,30),Section1A[i])
    Wanswer1 = pygbutton.PygButton((100,150,200,30),num1)
    Wanswer2 = pygbutton.PygButton((100,190,200,30),num2)
    winner = pygbutton.PygButton((500,190,200,30),'')

    question.draw(screen)
    tester2.draw(screen)
    Ranswer.draw(screen)
    Wanswer1.draw(screen)
    Wanswer2.draw(screen)
    winner.draw(screen)
    buttonEvent = Ranswer.handleEvent(event)
    buttonEvent2= Wanswer1.handleEvent(event)
    buttonEvent3= Wanswer2.handleEvent(event)



    if 'click' in buttonEvent:
            winner = pygbutton.PygButton((500,190,200,30),'Winner')
            winner.draw(screen)
            i = i+1
    if 'click' in buttonEvent2 :
            winner = pygbutton.PygButton((500,190,200,30),'Lose')
            winner.draw(screen)
            i = i+1
    if 'click' in buttonEvent3 :
            winner = pygbutton.PygButton((500,190,200,30),'Lose')
            winner.draw(screen)
            i= i +1


    question.draw(screen)
    tester2.draw(screen)
    Ranswer.draw(screen)
    Wanswer1.draw(screen)
    Wanswer2.draw(screen)
    winner.draw(screen)


while True: # main game loop
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    tester_Function()

    pygame.display.update()
