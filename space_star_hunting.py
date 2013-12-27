# This is my first game demonstration in python

import pygame, sys
from pygame.locals import *
import random

pygame.init()

def game():
    # make window called screen and initialize the background
    width, height = 1000, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('my star catcher game')
    background = pygame.image.load('sprite/bg.jpg')
    background = pygame.transform.scale(background,(width,height))

    

    # load targets in array
    targetnum = 10
    target = []
    for i in range(targetnum):
        targetimage = pygame.image.load('sprite/star.png')
        targetimage = pygame.transform.scale(targetimage,(20,20))
        target.append([])
        target[i] = targetimage
        
    targetpos = []
    targetspace = height/targetnum-10
    for i in range(targetnum):
        targetpos.append([])
        for j in range(2):
            targetpos[i].append(i*j*targetspace+50)

    # target visible set up of the array
    targetvisible = []
    for i in range(targetnum):
        targetvisible.append(True)

    player = pygame.image.load('sprite/spaceship.png')
    player = pygame.transform.scale(player,(50,40))
    px,py = (width-50)/2, (height-40)/2

    # speed of game and other variables initiated
    clock = pygame.time.Clock()
    gamespeed = 100
    movex = movey = 0

    speed = []
    for i in range(targetnum):
        speed.append([])
        for j in range(2):
            speed[i].append(gamespeed*random.randint(1,5))

    score = 0

    # this is the score text loading
    gamefont = pygame.font.Font(None,30)
    scoretext = gamefont.render("player score: "+str(score), 2, [255,0,0])
    boxsize = scoretext.get_rect()
    scoreXpos = (width-boxsize[2])/2
    
    # running of the game loop
    while True:
        # image display updates
        seconds = clock.tick()/1000.0
        screen.blit(background,(0,0))
        screen.blit(player,(px,py))
        scoretext = gamefont.render("player score: "+str(score), 2, [255,0,0])
        if score == 100:
            font = pygame.font.Font(None,100)
            text = font.render("You Won !!!",True,(0,255,0))
            screen.blit(text,[width/2,height/2])
        screen.blit(scoretext,[scoreXpos,20])

        # target blited through a for loop
        for i in range(targetnum):
            if targetvisible[i]:
                targetpos[i][0] += seconds*speed[i][0]
                targetpos[i][1] += seconds*speed[i][1]
                targetimage = target[i]
                x = targetpos[i][0]
                y = targetpos[i][1]
                screen.blit(targetimage, (x,y))
            else:
               targetimage = target[i]
               x = width - 50
               y = height-(i+1)*targetspace
               screen.blit(targetimage, (x,y))


        pygame.display.update()
        # keyboard and/or mouse movements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    movex = 12
                if event.key == K_LEFT:
                    movex = -12
                if event.key == K_UP:
                    movey = -12
                if event.key == K_DOWN:
                    movey = 12
            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    movex = 0
                if event.key == K_LEFT:
                    movex = 0
                if event.key == K_UP:
                    movey = 0
                if event.key == K_DOWN:
                    movey = 0
                    
        px = px + movex
        py += movey

        # test for the sides of the screens
        for i in range(targetnum):
            if targetpos[i][0] > width or targetpos[i][0] < 0:
                speed[i][0] = -speed[i][0]
                targetpos[i][0] += seconds*speed[i][0]
            if targetpos[i][1] > height or targetpos[i][1] < 0:
                speed[i][1] = -speed[i][1]
                targetpos[i][1] += seconds*speed[i][1]

        # this is the collision test
        for i in range(targetnum):
            if abs(targetpos[i][0]-px) < 20 and abs(targetpos[i][1]-py) < 20:
                targetvisible[i] = False
                score += 10
                targetpos[i] = [width+100,height+100]
            
# python's way of running the main rutine
if __name__ == '__main__':
    game()
