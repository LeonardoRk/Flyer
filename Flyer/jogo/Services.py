import pygame
from pgzero.actor import Actor
import Drone as drone
import World as worldClass
import Box as box
import Losangle as losangle
import Background as background
import GravityItem as gravityItem
import Main as main
import StarItem as starItem

# Service class
class Services():

    # Constructor of Services
    def __init__(self):
        ...

    # Show pontuation of player
    def showPontuation(self,points,gravityActivated=False):

        if gravityActivated == False:
            pointsString = "POINTS : "
        else:
            pointsString = "20X POINTS : "
        stringPoints = str(points)
        myfont = pygame.font.SysFont("Arial",25)

        label = myfont.render(pointsString + stringPoints,1,(0,255,0))
        return label

    # Show the hightest score of player
    def showHighestPointsOnMenu(self,highpoints):
        HIGHPOINTS = "HIGH POINTS: "
        stringPoints = str(highpoints)
        myfont = pygame.font.SysFont("Arial",30)

        label = myfont.render(HIGHPOINTS + stringPoints,1,(255,255,255))
        return label

    # Show the actual points of player
    def showActualPointsOnMenu(self,points):
        HIGHPOINTS = "Your last one: "
        stringPoints = str(points)
        myfont = pygame.font.SysFont("Arial",25)
        label = myfont.render(HIGHPOINTS + stringPoints,1,(255,255,255))
        return label

    # Create world
    def createWorld(self):

        SPEED_BOX1 = -0.81
        SPEED_BOX2 = -1.1
        SPEED_BOX3 = -1.003
        world = worldClass.World(drone.Drone("drone_right",mass = 100,position=(24,200)),
                         [box.Box("box",speed0 = SPEED_BOX1),box.Box("box",speed0 = SPEED_BOX2),
                          box.Box("box",speed0 = SPEED_BOX3)],
                         background.Background("background",main.WIDTH / 2,main.HEIGHT /2 + 25))

        return world

    # Create item losangle
    def createItemLosangle(self):
        return losangle.Losangle("losango")

    # Create item gravity
    def createItemGravityChange(self):
        return gravityItem.Gravity("gravitychange")

    # Create item star
    def createItemStart(self):
        return starItem.StarItem("star")

    # Draw keys in screen
    def drawKey(self):

        x = Actor("z" , pos = (370 , 23))
        y = Actor("x" , pos = (520 , 23))
        c = Actor("c" , pos= (700 , 27))
        key = (x , y , c)

        return key