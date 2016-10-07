from random import randint
from pgzero.actor import Actor

import sys
sys.path.append("/home/leonardo/Leonardo/jogos digitais/Flyer/jogo")

import MainPrincipal as Mp

# Classe Box
class Box():

#Construtor da Box
    def __init__(self , name , speed0=0):
        self.initialPos = (randint(500 , 1000), randint(0 , 400))
        self.sprite = Actor(name.lower() ,  pos=(self.initialPos[0] , self.initialPos[1]) )
        self.speed = speed0
        self.initialSpeed = speed0
        self.pos = self.initialPos
        self.tempo = 0


#Atualiza o estados dos frames
    def update(self, dt):
        self.tempo += dt
        self.evaluateSpeed()
        self.evaluatePos(dt)
        self.defineSprite()

#Desenha frames na tela
    def draw(self):
        self.sprite.draw()

#Define a velocidade
    def evaluateSpeed(self):
        if self.pos[0] < 0:
            self.tempo = 0
            self.speed -= 0.5

#Define a pos
    def evaluatePos(self , dt):
        if self.pos[0] < 0:
            self.pos = (Mp.WIDTH + 25, randint(0 , Mp.HEIGHT))
        else:
            self.pos = (self.pos[0]  + self.speed * self.tempo , self.pos[1] )

#Define sprite
    def defineSprite(self):
        self.sprite.x = self.pos[0]
        self.sprite.y = self.pos[1]






