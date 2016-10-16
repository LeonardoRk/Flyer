import pygame


class Services():

    def __init__(self):
        ...

    def showMessageOnScreen(self , points):
        POINTS = "POINTS : "
        stringPoints = str(points)
        myfont = pygame.font.SysFont("Arial", 25)

        label = myfont.render(POINTS + stringPoints, 1, (0,255,0))
        return label
