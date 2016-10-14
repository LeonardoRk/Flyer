import sys
sys.path.append("/home/leonardo/Leonardo/GIT/Flyer/Flyer/jogo")

import ClasseDrone as Cd
import WorldClass as Wc
import BoxClass as Box
import LosangleClass as Lc
import Background as Bg
import Services


WIDTH = 1000
HEIGHT = 400

SPEED_BOX1 = -0.81
SPEED_BOX2 = -1.1
SPEED_BOX3 = -1.003

#MAIN PRINCIPAL
world = Wc.World( Cd.Drone("jamaica" ,mass=100, position=(24 , 200)) ,
                  [Box.Box("box" ,speed0= SPEED_BOX1 ), Box.Box("box" ,speed0= SPEED_BOX2) ,
                   Box.Box("box" , speed0= SPEED_BOX3)] ,
                   Lc.Losangle("losango") ,
                   Bg.Background("back", 500, 200))

services = Services.Services()

points = 0

def draw():
    global  points
    points += 1
    screen.clear()
    world.draw()

    screen.blit(services.showMessageOnScreen(points), (800, 20))

def update(dt):

    world.update(dt)




