
#Classe mundo
class World():

#Construtor do mundo
    def __init__(self , drone , boxes=[] ):
        self.drone = drone
        self.boxes = list(boxes)

#Atualiza o estados dos frames
    def update(self, dt):
        self.drone.update(dt)
        for box in self.boxes:
            box.update(dt)
        self.defineTouch()

#Desenha frames na tela
    def draw(self):
        self.drone.draw()
        for box in self.boxes:
            box.draw()

#Define contato entre drone e caixa
    def defineTouch(self):
        for box in self.boxes:

            if self.drone.sprite.right -1 >= box.sprite.left and self.drone.sprite.left + 1 <= box.sprite.right:
                if self.drone.sprite.bottom -8 >= box.sprite.top and self.drone.sprite.top +8 <= box.sprite.bottom:
                	exit()


