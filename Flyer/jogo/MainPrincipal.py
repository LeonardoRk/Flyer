import sys
sys.path.append("/home/leonardo/Leonardo/jogos digitais/Flyer/jogo")

import ClasseDrone as Cd
import WorldClass as Wc
import BoxClass as Box

WIDTH = 1000
HEIGHT = 400


#Main principal
background = Actor("back" , pos=(500 , 200) )
world = Wc.World( Cd.Drone("jamaica" ,mass=100, position=(24 , 200)) ,
                  [Box.Box("box" , speed0=-0.08) , Box.Box("box" ,speed0=-1.30006) , Box.Box("box" , speed0=-1.00001)])

def draw():
    screen.clear()
    background.draw()
    world.draw()

def update(dt):
    world.update(dt)

