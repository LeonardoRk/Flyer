from pgzero.actor import Actor
from random import randint

import MenuPrincipal as MP

class Gravity:

    def __init__(self , name ):
        self.pos = (randint(MP.WIDTH - 40, MP.WIDTH- 20) , randint(20 , MP.HEIGHT - 25))
        self.sprite = Actor(name.lower() , self.pos)
        self.tempo = 0


    def draw(self):
        self.sprite.draw()


