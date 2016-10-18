import Services as Sv
from random import randint

#Classe mundo
class World:

    colision = False
#Construtor do mundo
    def __init__(self , drone , boxes=[] , background=0 ):
        self.TIME_TO_CREATE = 17
        self.drone = drone
        self.boxes = list(boxes)
        self.losango = None
        self.background = background
        self.gravityChange = None
        self.timeToCreateItem = 0
        self.services = Sv.Services()


#Atualiza o estados dos frames
    def update(self, dt):
        global colision
        colisionLimits = self.drone.update(dt)
        for box in self.boxes:
            box.update(dt)
        colisionBox = self.defineTouchOnBox()
        if self.losango == None and self.gravityChange == None:
            self.defineWhenCreateItem(dt)

        if self.losango != None :
            self.losango.update(dt)
            self.defineTouchOnLosange()

        if self.gravityChange != None:
            self.defineTouchOnGravityChange()

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

        if self.gravityChange != None and self.gravityChange != 0:
            self.gravityChange.draw()

#Define contato entre drone e caixa
    def defineTouchOnBox(self):
        for box in self.boxes:

            if self.drone.sprite.right -10 >= box.sprite.left and self.drone.sprite.left + 1 <= box.sprite.right:
                if self.drone.sprite.bottom -8 >= box.sprite.top and self.drone.sprite.top + 8 <= box.sprite.bottom:
                    return True

    def defineTouchOnLosange(self):
        if  self.drone.sprite.right - 5 >= self.losango.  sprite.left:
            if self.drone.sprite.bottom -10  >= self.losango.sprite.top and self.drone.sprite.top <= self.losango.sprite.bottom:
                if self.drone.containsSlowMotion == False:
                    self.losango = None
                    self.boxes[0].slowMotion = True
                    self.boxes[1].slowMotion = True
                    self.boxes[2].slowMotion = True


    def defineTouchOnGravityChange(self):
        if self.drone.sprite.right - 5 >= self.gravityChange.sprite.left:
            if self.drone.sprite.bottom - 10 >= self.gravityChange.sprite.top and \
                            self.drone.sprite.top <= self.gravityChange.sprite.bottom:
                self.drone.containsGravityInverted = True
                self.gravityChange = None
                self.drone.gravity = -self.drone.gravity


    def defineWhenCreateItem(self , dt):
        self.timeToCreateItem += dt
        if self.timeToCreateItem >= self.TIME_TO_CREATE:
            self.timeToCreateItem = 0
            aleatorio = randint(0, 1)
            if aleatorio == 0 and self.gravityChange == None:
                self.losango =  self.services.createItemLosangle()
                print("criou losango")
            if aleatorio == 1 and self.losango == None:
                self.gravityChange = self.services.createItemGravityChange()
                print("criou gravity inverter")
            #if aleatorio == 2:
                """ create star"""







