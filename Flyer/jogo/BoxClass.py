from random import randint
from pgzero.actor import Actor

import sys
sys.path.append("/home/leonardo/Leonardo/GIT/Flyer/Flyer/jogo")

import MenuPrincipal as MP

# Classe Box
class Box:


#Construtor da Box
    def __init__(self , name , speed0=0):
        self.TIME_SLOWMOTION = 7
        self.initialPos = (randint(MP.WIDTH - 40, MP.WIDTH- 20) , randint(75 , MP.HEIGHT - 25))
        self.sprite = Actor(name.lower() ,  pos=(self.initialPos[0] , self.initialPos[1]) )
        self.speed = speed0
        self.initialSpeed = speed0
        self.pos = self.initialPos
        self.tempo = 0
        self.slowMotion = False
        self.tempoSlowMotion = 0
        self.storeSpeed = None

#Atualiza o estados dos frames
    def update(self, dt):
        self.tempo += dt
        self.evaluateSpeed(dt)
        self.evaluatePos(dt)
        self.defineSprite()

#Desenha frames na tela
    def draw(self):
        self.sprite.draw()

#Define a velocidade
    def evaluateSpeed(self , dt):
        if self.slowMotion == False:
            if self.storeSpeed != None:
                self.speed = self.storeSpeed
                self.storeSpeed = None
            if self.pos[0] < 0:
                self.tempo = 0
                self.speed -= 0.5
        else:
            if self.storeSpeed == None:
                self.storeSpeed = self.speed
            self.speed = -0.15
            self.tempoSlowMotion += dt


            if self.tempoSlowMotion >= self.TIME_SLOWMOTION:
                self.tempoSlowMotion = 0
                self.slowMotion = False

#Define a pos
    def evaluatePos(self , dt):
        if self.pos[0] < 0:
            self.pos = (MP.WIDTH + 25 , randint(75 , MP.HEIGHT - 25))
        else:
            self.pos = (self.pos[0]  + self.speed * self.tempo , self.pos[1] )

#Define sprite
    def defineSprite(self):
        self.sprite.x = self.pos[0]
        self.sprite.y = self.pos[1]









