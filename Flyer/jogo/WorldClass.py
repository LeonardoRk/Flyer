import Services

#Classe mundo
class World:

#Construtor do mundo
    def __init__(self , drone , boxes=[] , losango=0 , background=0 , gravityChange=0):
        self.drone = drone
        self.boxes = list(boxes)
        self.losango = losango
        self.background = background
        self.gravityChange = gravityChange

#Atualiza o estados dos frames
    def update(self, dt):
        self.drone.update(dt)
        for box in self.boxes:
            box.update(dt)
        self.defineTouchOnBox()

        if self.losango != None and self.losango != 0:
            self.losango.update(dt)
            self.defineTouchOnLosange()

        if self.gravityChange != None and self.gravityChange != 0:
            self.defineTouchOnGravityChange()

#Desenha frames na tela
    def draw(self):
        self.background.draw()
        self.drone.draw()

        for box in self.boxes:
            box.draw()

        if self.losango != None and self.losango != 0:
            self.losango.draw()

        if self.gravityChange != None and self.gravityChange != 0:
            self.gravityChange.draw()

#Define contato entre drone e caixa
    def defineTouchOnBox(self):
        for box in self.boxes:

            if self.drone.sprite.right -10 >= box.sprite.left and self.drone.sprite.left + 1 <= box.sprite.right:
                if self.drone.sprite.bottom -8 >= box.sprite.top and self.drone.sprite.top + 8 <= box.sprite.bottom:
                	exit()

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
                if self.drone.containsSlowMotion == False:
                    self.gravityChange.gravityInverted = True
                    self.gravityChange = None
                    self.drone.gravity = -self.drone.gravity









