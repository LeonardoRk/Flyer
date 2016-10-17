import pygame
import ClasseDrone as Cd
import WorldClass as Wc
import BoxClass as Box
import LosangleClass as Lc
import Background as Bg
import GravityItem as Gc


class Services():

    def __init__(self):
        ...

    def showPontuation(self , points , gravityActivated=False):
        pointsString = ""

        if gravityActivated == False:
            pointsString = "POINTS : "
        else:
            pointsString = "X2 POINTS : "
        stringPoints = str(points)
        myfont = pygame.font.SysFont("Arial", 25)

        label = myfont.render(pointsString + stringPoints, 1, (0,255,0))
        return label

    def showHighestPointsOnMenu(self, highpoints):
        HIGHPOINTS = "HIGH POINTS: "
        stringPoints = str(highpoints)
        myfont = pygame.font.SysFont("Arial", 30)

        label = myfont.render(HIGHPOINTS + stringPoints, 1, (255, 255, 255))
        return label

    def showActualPointsOnMenu(self, points):
        HIGHPOINTS = "Your last one: "
        stringPoints = str(points)
        myfont = pygame.font.SysFont("Arial", 25)
        label = myfont.render(HIGHPOINTS + stringPoints, 1, (255, 255, 255))
        return label

    def createWorld(self):
        SPEED_BOX1 = -0.81
        SPEED_BOX2 = -1.1
        SPEED_BOX3 = -1.003
        world = Wc.World(Cd.Drone("jamaica", mass=100, position=(24, 200)),
                         [Box.Box("box", speed0=SPEED_BOX1), Box.Box("box", speed0=SPEED_BOX2),
                          Box.Box("box", speed0=SPEED_BOX3)],
                         Lc.Losangle("losangle"),
                         Bg.Background("back", 500, 200),
                         Gc.Gravity("gravityChange"))
        return world