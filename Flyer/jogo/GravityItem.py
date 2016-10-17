from pgzero.actor import Actor
from random import randint
import ClasseDrone as Cd

class Gravity:

    def __init__(self , name ):
        self.pos = (randint(950, 980) , randint(20 , 390))
        self.sprite = Actor(name.lower() , self.pos)
        self.tempo = 0


    def draw(self):
        self.sprite.draw()


