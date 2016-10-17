from pgzero.actor import Actor
from random import randint
import pygame.sprite

class Losangle:

    def __init__(self , name=None ):
        self.tempo = 0
        self.pos = (randint(950, 980) , randint(20 , 390))
        self.sprite = Actor(name.lower() , self.pos)

    def draw(self ):
        self.sprite.draw()


    def update(self, dt):
        self.tempo = self.tempo + dt




