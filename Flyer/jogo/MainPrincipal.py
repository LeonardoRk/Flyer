import sys
sys.path.append("/home/leonardo/Leonardo/GIT/Flyer/Flyer/jogo")

import pygame
import ClasseDrone as Cd
import WorldClass as Wc
import BoxClass as Box
import Services as Svs
import LosangleClass as Lc


WIDTH = 1000
HEIGHT = 400


#Main principal
background = Actor("back" , pos=(500 , 200) )
world = Wc.World( Cd.Drone("jamaica" ,mass=100, position=(24 , 200)) ,
                  [Box.Box("box" , speed0=-0.48) , Box.Box("box" ,speed0=-1.30006) , Box.Box("box" , speed0=-1.00001)] ,
                  Lc.Losangle("losango"))
services = Svs.Services()


points = 0

def draw():
    global  points
    points += 1
    screen.clear()
    background.draw()
    world.draw()

    screen.blit( services.showMessageOnScreen(points), (800, 20))

def update(dt):

    world.update(dt)




