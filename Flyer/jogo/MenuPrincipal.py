import sys
sys.path.append("/home/leonardo/Leonardo/GIT/Flyer/Flyer/jogo")

from pgzero.actor import Actor
import pygame
import Services


WIDTH = 1000
HEIGHT = 400

play = False
botaoPlay = Actor("botao_play" , pos=(WIDTH/2 , HEIGHT/2))
services = Services.Services()
points = 0
highpoints = 0
actualPoints = 0
savedPoints = False
world = None


def draw():
    global play, points , world , highpoints , actualPoints , savedPoints
    
    if pygame.mouse.get_pressed()[0] == 1:  # LEFT BUTTON CLICKED
        if pygame.mouse.get_pos()[0] >= botaoPlay.left and pygame.mouse.get_pos()[0] <= botaoPlay.right:
            if pygame.mouse.get_pos()[1] >= botaoPlay.top and pygame.mouse.get_pos()[1] <= botaoPlay.bottom:
                play = True
                world = services.createWorld()
                return world

    if play == False :
        screen.clear()
        if savedPoints == False:
            if points >= highpoints:
                highpoints = points
            actualPoints = points
            savedPoints = True


        points = 0
        botaoPlay.draw()
        screen.blit(services.showHighestPointsOnMenu(highpoints), (WIDTH/2.5, HEIGHT/8))
        screen.blit(services.showActualPointsOnMenu(actualPoints), (WIDTH / 2.5, HEIGHT / 4))


    if play == True :
        savedPoints = False
        screen.clear()
        if(world.drone.containsGravityInverted == True):
            points = points + 20
        else:
            points += 1
        world.draw()
        screen.blit(services.showPontuation(points , world.drone.containsGravityInverted), (800, 20) )


def update(dt):
    global world , play
    if world != None and play == True:
        play = world.update(dt)






