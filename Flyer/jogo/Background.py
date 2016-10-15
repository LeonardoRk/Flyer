from pgzero.actor import Actor

class Background:

    def __init__(self , name , x , y):
        self.pos = (x , y)
        self.sprite = Actor(name.lower() , self.pos)

        # Desenha frames na tela
    def draw(self):
        self.sprite.draw()

