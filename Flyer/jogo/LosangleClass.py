from pgzero.actor import Actor
from random import randint

import MenuPrincipal as MP

class Losangle:

    def __init__(self , name=None ):
        self.tempo = 0
        self.pos = (randint(MP.WIDTH - 40, MP.WIDTH- 20) , randint(20 , MP.HEIGHT - 25))
        self.sprite = Actor(name.lower() , self.pos)

    def draw(self ):
        self.sprite.draw()


    def update(self, dt):
        self.tempo = self.tempo + dt




