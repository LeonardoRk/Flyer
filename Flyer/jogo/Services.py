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

    def showMessageOnScreen(self , points):
        POINTS = "POINTS : "
        stringPoints = str(points)
        myfont = pygame.font.SysFont("Arial", 25)

        label = myfont.render(POINTS + stringPoints, 1, (0,255,0))
        return label

    def createWorld(self):
        SPEED_BOX1 = -0.81
        SPEED_BOX2 = -1.1
        SPEED_BOX3 = -1.003
        world = Wc.World(Cd.Drone("jamaica", mass=100, position=(24, 200)),
                         [Box.Box("box", speed0=SPEED_BOX1), Box.Box("box", speed0=SPEED_BOX2),
                          Box.Box("box", speed0=SPEED_BOX3)],
                         Lc.Losangle("losango"),
                         Bg.Background("back", 500, 200),
                         Gc.Gravity("gravitychange"))
        return world