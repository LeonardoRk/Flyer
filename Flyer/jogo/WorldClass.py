from pgzero.keyboard import keyboard

import Services as Sv
from pgzero.actor import Actor
from random import randint

#Classe mundo
class World:

    colision = False
#Construtor do mundo
    def __init__(self , drone , boxes=[] , background=0 ):
        self.TIME_TO_CREATE_ITEM = 8
        self.drone = drone
        self.boxes = list(boxes)
        self.losango = None
        self.background = background
        self.gravityChange = None
        self.timeToCreateItem = 0
        self.services = Sv.Services()
        self.starItem = None


#Atualiza o estados dos frames
    def update(self, dt):
        global colision
        colisionLimits = self.drone.update(dt)
        for box in self.boxes:
            box.update(dt)
        colisionBox = self.defineTouchOnBox()
        if self.losango == None or self.gravityChange == None or self.starItem == None:
            self.defineWhenCreateItem(dt)

        if self.losango != None :
            self.losango.update(dt)
            self.defineTouchOnLosange()

        if self.gravityChange != None:
            self.defineTouchOnGravityChange()

        if self.starItem != None:
            self.defineTouchOnStar()

        if keyboard.x and self.drone.containsItemGravity :
            self.gravityChange = None
            self.drone.containsGravityInverted = True
            self.drone.gravity = -self.drone.gravity
            self.drone.containsItemGravity = False

        if keyboard.z and self.drone.containsItemSlowMotion:
            self.losango = None
            self.boxes[0].slowMotion = True
            self.boxes[1].slowMotion = True
            self.boxes[2].slowMotion = True
            self.drone.containsItemSlowMotion = False

        if keyboard.c and self.drone.containsItemStar:
            self.starItem = None
            self.drone.containsStartActivated = True
            self.drone.containsItemStar = False

        if colisionBox == True or colisionLimits == True:
            return False
        else:
            return True

#Desenha frames na tela
    def draw(self):
        self.background.draw()
        self.drone.draw()

        for box in self.boxes:
            box.draw()

        if self.losango != None :
            self.losango.draw()

        if self.gravityChange != None:
            self.gravityChange.draw()

        if self.starItem != None:
            self.starItem.draw()


#Define contato entre drone e caixa
    def defineTouchOnBox(self):
        for box in self.boxes:

            if self.drone.sprite.right -10 >= box.sprite.left and self.drone.sprite.left + 1 <= box.sprite.right:
                if self.drone.sprite.bottom -8 >= box.sprite.top and self.drone.sprite.top + 8 <= box.sprite.bottom:
                    if self.drone.containsStartActivated:
                        print("toquei, mas ta ativado")
                        return False
                    else:
                        return True

    def defineTouchOnLosange(self):
        if  self.drone.sprite.right - 5 >= self.losango.  sprite.left:
            if self.drone.sprite.bottom -10  >= self.losango.sprite.top and self.drone.sprite.top <= self.losango.sprite.bottom:
                self.losango.sprite = Actor("losango" , pos=(320 , 23))
                self.drone.containsItemSlowMotion = True


    def defineTouchOnGravityChange(self):
        if self.drone.sprite.right - 5 >= self.gravityChange.sprite.left:
            if self.drone.sprite.bottom - 10 >= self.gravityChange.sprite.top and \
                            self.drone.sprite.top <= self.gravityChange.sprite.bottom:
                self.drone.containsItemGravity = True
                self.gravityChange.sprite = Actor("gravitychange" , pos=(570 , 23))

    def defineTouchOnStar(self):
        if self.drone.sprite.right - 7 >= self.starItem.sprite.left:
            if self.drone.sprite.bottom - 12 >= self.starItem.sprite.top and \
                            self.drone.sprite.top <= self.starItem.sprite.bottom:
                self.drone.containsItemStar = True
                self.starItem.sprite = Actor("star" , pos=(750 , 23))


    def defineWhenCreateItem(self , dt):
        self.timeToCreateItem += dt
        if self.timeToCreateItem >= self.TIME_TO_CREATE_ITEM:
            self.timeToCreateItem = 0

            if self.losango == None and self.gravityChange == None and self.starItem == None:
                aleatorio = randint(0, 2)

            elif self.losango == None and self.gravityChange == None:
                aleatorio = randint(0 , 1)

            elif self.gravityChange == None and self.starItem == None:
                aleatorio = randint(1 , 2)
            elif self.starItem == None and self.losango == None:
                aleatorio = randint(0,1)
                if aleatorio == 1:
                    aleatorio = 2
            elif self.gravityChange == None:
                aleatorio = 1
            elif self.starItem == None:
                aleatorio = 2
            else:
                aleatorio = 0

            if aleatorio == 0:
                self.losango =  self.services.createItemLosangle()
            if aleatorio == 1:
                self.gravityChange = self.services.createItemGravityChange()
            if aleatorio == 2:
                self.starItem = self.services.createItemStart()








