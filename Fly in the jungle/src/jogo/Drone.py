import sys
sys.path.append(os.path.dirname(__file__))
from pygame.locals import *

import pygame.mixer
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
import Main as main
import pygame
DISTANCE_BETWEEN_CENTER_TO_LEFT_BORDER = 24
DISTANCE_BETWEEN_CENTER_TO_TOP_BORDER = 68
DISTANCE_BETWEEN_CENTER_TO_BOTTOM_BORDER = 20

# Drone class
class Drone:

    # Constructor of Drone
    def __init__(self,name,mass = 0,aceleration = (0,0),position = (0,0)):
        self.sprite = Actor(name.lower(),pos = (position[0],position[1]))
        self.MAX_INVERTED_GRAVITY = 6
        self.gravity = 80
        self.mass = mass
        self.aceleration = aceleration
        self.speed = (0,0)
        self.position = position
        self.resultantForce = (0,0)
        self.gravityTime = 0
        self.starTime = 0
        self.time = 0
        self.containsItemSlowMotion = False
        self.containsItemGravity = False
        self.containsItemStar = False
        self.containsSlowMotion = False
        self.containsGravityInverted = False
        self.containsStartActivated = False
        self.jumpforce = 0
        self.downforce = 0
        self.flySound = True
        
        


    # Draw frames
    def draw(self):
        self.sprite.draw()

    # Update the states of frames
    def update(self, dt):
        self.time = dt
        colision = self.evaluateResultantForce()
        self.evaluatePosition()
        self.evaluateSpeed(0)
        self.evaluateAceleration()
        self.evaluateSprite()
        self.countTimeOfInvertedGravity(dt)
        self.countTimeOfStarItem(dt)

        if colision == True:
            return True
        else:
            return False

    # Calculates the resultant force
    def evaluateResultantForce(self):

        if self.position[1] >= main.HEIGHT - DISTANCE_BETWEEN_CENTER_TO_BOTTOM_BORDER or \
                        self.position[1] <= DISTANCE_BETWEEN_CENTER_TO_TOP_BORDER:  # It indicates that died
            return True
        else:
            self.jumpforce = 0
            self.downforce = 0
            self.detectUpOrDownMovement()
            self.resultantForce = ( self.resultantForce[0] ,
                     (-self.jumpforce * self.mass) + (self.mass * self.gravity) + (self.mass * self.downforce))


    # Calculates the acceleration
    def evaluateAceleration(self):
        self.aceleration = (self.resultantForce[0] / self.mass,self.resultantForce[1] / self.mass)

    # Calculates the speed
    def evaluateSpeed(self , dy ):
    
        self.detectLeftOrRightMovement()
        

    # Calculates the position
    def evaluatePosition(self):
        self.position = (self.position[0] + (self.speed[0] * self.time) ,
                         self.position[1] + self.speed[1] * self.time + (self.aceleration[1] * (self.time ** 2)/2))

    # Setting the sprite
    def evaluateSprite(self):
        self.sprite.x = self.position[0]
        self.sprite.y = self.position[1]

    def detectUpOrDownMovement(self):
        clickedUpOrDown = False
        if keyboard.up:
            clickedUpOrDown = True
            if self.containsStartActivated:
                self.sprite.image = "drone_up_red"
            else:
                self.sprite.image = "drone_up"
            self.jumpforce = 500
            self.downforce = 0
        elif keyboard.down:
            clickedUpOrDown = True
            if self.containsStartActivated:
                self.sprite.image = "drone_down_red"
            else:
                self.sprite.image = "drone_down"
            self.jumpforce = 0
            self.downforce = 200
        return clickedUpOrDown

    def detectLeftOrRightMovement(self):
        DRONE_SPEED = 180
        DRONE_STOPPED = 0
        clickedLeftOrRight = False
        dy = 0
        if keyboard.left:
            clickedLeftOrRight = True
            if self.containsStartActivated:
                self.sprite = Actor("drone_left_red",self.position)
            else:
                self.sprite = Actor("drone_left",self.position)
            dy = -DRONE_SPEED
            if self.position[0] < DISTANCE_BETWEEN_CENTER_TO_LEFT_BORDER:
                dy = DRONE_STOPPED

        if keyboard.right:
            clickedLeftOrRight = True
            if self.containsStartActivated:
                self.sprite = Actor("drone_right_red",self.position)
            else:
                self.sprite = Actor("drone_right",self.position)
            dy = DRONE_SPEED
            if self.position[0] >= main.WIDTH - DISTANCE_BETWEEN_CENTER_TO_LEFT_BORDER :
                dy = DRONE_STOPPED
        self.speed = (dy,self.speed[1] + self.aceleration[1] * self.time)
        return clickedLeftOrRight

    # count the time of gravity item
    def countTimeOfInvertedGravity(self , dt):

        if self.containsGravityInverted == True:
            self.gravityTime += dt

            if self.gravityTime >= self.MAX_INVERTED_GRAVITY:
                self.gravityTime = 0
                self.containsGravityInverted = False
                self.gravity = - self.gravity

    def countTimeOfStarItem(self , dt):

            if self.containsStartActivated == True:
                self.starTime += dt

                if self.starTime >= self.MAX_INVERTED_GRAVITY:
                    self.starTime = 0
                    self.containsStartActivated = False

    
        
        
       
            
             
       



