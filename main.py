import pygame
import random

#initialize pygame
pygame.init()

###SETUP###
#display window
widthWindow = 600
heigthWindow = 650
window = pygame.display.set_mode((widthWindow,heigthWindow))

#title and icon of the window
pygame.display.set_caption("Sci Matto Fiero Mhanz")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#start_image
startImg = pygame.image.load('start.png')
startImg = pygame.transform.scale(startImg, (50, 50))
posStartX = 40
posStartY = 30

#skier image
skierImg = pygame.image.load('skier.png')
skierImg = pygame.transform.scale(skierImg, (50, 50))
posSkierX = 275
posSkierY = 30
posSkierX_change = 0
posSkierY_change = 0

#tree image
treeImg = pygame.image.load('pine-tree.png')
treeImg = pygame.transform.scale(treeImg, (30, 30))

treePos = [[50,200],[300,400]]

###END SETUP###

def skier(x,y):
    window.blit(skierImg,(x,y))

def tree(x,y):
    window.blit(treeImg,(x,y))
    window.blit(treeImg,(x+100,y))

def isOut(skierX, skierY, tree1X, tree2X, treeY):
    if skierY == treeY:
        if skierX <= tree1X+50 or skierX >= tree2X:
            return True
        else:
            return False
    else:
        False


#game loop
running = True
while running:
    #background color
    window.fill((230,230,230))

    #show start
    window.blit(startImg,(posStartX,posStartY))
    posStartY += -2

    for event in pygame.event.get():
        #if exit button pressed
        if event.type == pygame.QUIT:
            running = False
        #if pressed ...
        if event.type == pygame.KEYDOWN:
            #left arrow
            if event.key == pygame.K_LEFT:
                posSkierX_change = -1
            #rigth arrow
            if event.key == pygame.K_RIGHT:
                posSkierX_change = 1
        #when released
        if event.type == pygame.KEYUP:
            #left arrow
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                posSkierX_change = 0

    #show skier
    posSkierX += posSkierX_change
    if posSkierX <= 0:
        posSkierX = 0
    elif posSkierX >= widthWindow-50:
        posSkierX = widthWindow-50
    skier(posSkierX,posSkierY)

    #show tree
    tree(treePos[0][0],treePos[0][1])
    tree(treePos[1][0],treePos[1][1])

    #is out?
    flagIsOut = isOut(posSkierX,posSkierY,treePos[0][0],treePos[0][0]+100,treePos[0][1])

    if flagIsOut == True:
        print("Perso")
        #running = False

    treePos[0][1] += -0.1
    treePos[1][1] += -0.1

    pygame.display.update()