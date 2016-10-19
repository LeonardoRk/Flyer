import sys
sys.path.append("/home/leonardo/Leonardo/GIT/Flyer/Flyer/jogo")

from pgzero.actor import Actor
from pgzero.keyboard import keyboard
import MenuPrincipal as Mp

DISTANCE_BETWEEN_CENTER_TO_LEFT_BORDER = 24
DISTANCE_BETWEEN_CENTER_TO_TOP_BORDER = 68
DISTANCE_BETWEEN_CENTER_TO_BOTTOM_BORDER = 20

#Classe drone
class Drone:

#Construtor do Drone
    def __init__(self , name , mass=0 ,  aceleration=(0,0)  ,position=(0,0)  ):
        self.sprite = Actor(name.lower() , pos=(position[0] , position[1]) )
        self.MAX_INVERTED_GRAVITY = 6
        self.gravity = 80
        self.mass = mass
        self.aceleration = aceleration
        self.speed = (0,0)
        self.position = position
        self.fr = (0,0)
        self.gravityTime = 0
        self.tempo = 0
        self.containsItemSlowMotion = False
        self.containsItemGravity = False
        self.containsSlowMotion = False
        self.containsGravityInverted = False
        self.jumpforce = 0
        self.downforce = 0


#Desenha frames
    def draw(self):
        self.sprite.draw()

#atualiza o estados dos frames
    def update(self, dt):
        self.tempo = dt
        colidiu = self.evaluateResultantForce()
        self.evaluatePosition()
        self.evaluateSpeed(0)
        self.evaluateAceleration()
        self.evaluateSprite()
        self.countTimeOfInvertedGravity(dt)

        if colidiu == True:
            return True
        else:
            return False

#Calcula a força Resultante
    def evaluateResultantForce(self):

        if self.position[1] >= Mp.HEIGHT - DISTANCE_BETWEEN_CENTER_TO_BOTTOM_BORDER or \
                        self.position[1] <= DISTANCE_BETWEEN_CENTER_TO_TOP_BORDER:  #indica que morreu
            return True
        else:
            self.jumpforce = 0
            self.downforce = 0
            if keyboard.up:
                self.sprite.image = "drone_up"
                self.jumpforce = 500
                self.downforce = 0
            elif keyboard.down:
                self.sprite.image = "drone_down"
                self.jumpforce = 0
                self.downforce = 200
            self.fr = ( self.fr[0] ,
                     (-self.jumpforce * self.mass) + (self.mass * self.gravity) + (self.mass * self.downforce))


#Calcula a aceleração
    def evaluateAceleration(self):
        self.aceleration = (self.fr[0] / self.mass  , self.fr[1] / self.mass)

#Calcula a velocidade
    def evaluateSpeed(self , dy ):
        DRONE_SPEED = 180
        DRONE_STOPPED = 0
        if keyboard.left:
            self.sprite = Actor("drone_left" , self.position)
            dy = -DRONE_SPEED
            if self.position[0] < DISTANCE_BETWEEN_CENTER_TO_LEFT_BORDER:
                dy = DRONE_STOPPED
        if keyboard.right:
            self.sprite = Actor("drone_right", self.position)
            dy = DRONE_SPEED
            if self.position[0] >= Mp.WIDTH - DISTANCE_BETWEEN_CENTER_TO_LEFT_BORDER :
                dy = DRONE_STOPPED
        self.speed = (dy ,   self.speed[1] + self.aceleration[1] * self.tempo)

#Calcula a posição
    def evaluatePosition(self):
        self.position = (self.position[0] + (self.speed[0] * self.tempo) ,
                         self.position[1] + self.speed[1] * self.tempo + (self.aceleration[1] * (self.tempo ** 2 )/ 2 ) )

#Define o sprite
    def evaluateSprite(self):
        self.sprite.x = self.position[0]
        self.sprite.y = self.position[1]

    def countTimeOfInvertedGravity(self , dt):

        if self.containsGravityInverted == True:
            self.gravityTime += dt

            if self.gravityTime >= self.MAX_INVERTED_GRAVITY:
                self.gravityTime = 0
                self.containsGravityInverted = False
                self.gravity = - self.gravity


