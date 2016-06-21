import math, sys, os, pygame, random, time

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Tester.')
pygame.mouse.set_visible(0)
white = ( 255, 255, 255)

def smileMove():
    screen.fill(white)
    smiley = pygame.image.load('Content/car.png')
    random.seed()
    xMove = random.randrange(1,501)
    yMove = random.randrange(1,501)

    screen.blit(smiley,(xMove,yMove))

c = 0
done = False
while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    screen.fill(white)
    while c <5:
        smileMove()
        pygame.display.flip()
        c = c + 1
        time.sleep(3)
pygame.quit()