

#Classe mundo
class World:



#Construtor do mundo
    def __init__(self , drone , boxes=[] , losango=0 , background=0):
        self.drone = drone
        self.boxes = list(boxes)
        self.losango = losango
        self.background = background

#Atualiza o estados dos frames
    def update(self, dt):
        self.drone.update(dt)
        print(self.boxes[0].speed)
        for box in self.boxes:
            box.update(dt)
        self.defineTouchOnBox()

        if self.losango != None and self.losango != 0:
            self.losango.update(dt)
            self.defineTouchOnLosange()

#Desenha frames na tela
    def draw(self):
        self.background.draw()
        self.drone.draw()

        for box in self.boxes:
            box.draw()
        if self.losango != None and self.losango != 0:
            self.losango.draw()

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










