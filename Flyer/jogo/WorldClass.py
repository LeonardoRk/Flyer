from pgzero.actor import Actor

#Classe mundo
class World:

#Construtor do mundo
    def __init__(self , drone , boxes=[] , losango=0):
        self.drone = drone
        self.boxes = list(boxes)
        self.losango = losango

#Atualiza o estados dos frames
    def update(self, dt):
        self.drone.update(dt)
        self.losango.update(dt)
       
        for box in self.boxes:
            box.update(dt)
        self.defineTouchOnBox()
        self.defineTouchOnLosange()


#Desenha frames na tela
    def draw(self):
        self.drone.draw()
        self.losango.draw()
        for box in self.boxes:
            box.draw()

#Define contato entre drone e caixa
    def defineTouchOnBox(self):
        for box in self.boxes:

            if self.drone.sprite.right -10 >= box.sprite.left and self.drone.sprite.left + 1 <= box.sprite.right:
                if self.drone.sprite.bottom -8 >= box.sprite.top and self.drone.sprite.top + 8 <= box.sprite.bottom:
                	exit()

    def defineTouchOnLosange(self):
        if  self.drone.sprite.right - 9 >= self.losango.  sprite.left:
            if self.drone.sprite.bottom  >= self.losango.sprite.top and self.drone.sprite.top <= self.losango.sprite.bottom:
                print("deixa invisivel a imagem")










