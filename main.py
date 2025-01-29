from pygame_functions import *
import math, random, time, pickle

screenSize(1000,1000)
setBackgroundColour("black")

mass_multiplier = 0.5

min_speed = 1
max_speed = 50

class Creature:
    def __init__(self,x,y,image,  size):
        self.x = x
        self.y = y
        self.size = size   # size is a percentage of the full size image
        self.sprite = makeSprite(image)
        self.direction = random.randint(0,359)
        self.speed = random.randint(min_speed, max_speed)
        moveSprite(self.sprite,self.x,self.y,centre=True)
        transformSprite(self.sprite, 0, self.size/100)
        showSprite(self.sprite)
    
        
        
        
        
        

class Player(Creature):
    def __init__(self):
        super().__init__()
        self.direction = 0
        
    def move(self):
        
        self.y += math.sin(math.radians(self.direction)) * self.speed
        self.x += math.cos(math.radians(self.direction)) * self.speed
        
        
    

setAutoUpdate(False)
c1 = Creature(random.randint(0,1000),random.randint(0,1000), "enemy.png", random.randint(10,100)) 

updateDisplay()
        
endWait()
