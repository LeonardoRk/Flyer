import pygame

def showMessageOnScreen(string1):
    POINTS = "POINTS : "
    string1 = str(string1)
    myfont = pygame.font.SysFont("Arial", 25)

    label = myfont.render(POINTS + string1 , 1, (0,255,0))
    return label
