from pygame_functions import *
import math, random, time, pickle

screenSize(1000,1000)
setBackgroundColour("black")



mass_multiplier = 0.5

rotation_speed = 1
min_speed = 1
max_speed = 10

game_active = True

class Creature:
    def __init__(self,x,y,image,  size):
        self.x = x
        self.y = y
        self.size = size   # size is a percentage of the full size image
        self.sprite = makeSprite(image)
        
        
        moveSprite(self.sprite,self.x,self.y,centre=True)
        transformSprite(self.sprite, 0, self.size/100)
        showSprite(self.sprite)
    
        
        
        

class Enemy(Creature):
    def __init__(self,x,y,image,  size):
        super().__init__(x,y,image,  size)
        
        self.direction = random.randint(0,359)
        self.speed = random.randint(min_speed, max_speed)
    
    def move(self):
        
        self.y += math.sin( ( self.direction/180 ) * math.pi) * self.speed
        self.x += math.cos( ( self.direction/180 ) * math.pi) * self.speed
        
        self.y = self.y % 1000
        self.x = self.x % 1000
        
        moveSprite(self.sprite, self.x, self.y)
        
    def update(self):
    
        self.move()
        
    
    
class Player(Creature):
    def __init__(self,x,y,image,  size):
        super().__init__(x,y,image,  size)
        
        self.speed = 2
        self.direction = 0
        
    def move(self):
        
        self.y += math.sin(math.radians(self.direction)) * self.speed
        self.x += math.cos(math.radians(self.direction)) * self.speed
        
        if keyPressed("a"):
            direction = 365 % (direction - rotation_speed)
            
        if keyPressed("d"):
            direction = 365 % (direction + rotation_speed)
        
        moveSprite(self.sprite, self.x, self.y)
        transformSprite(self.sprite,self.direction,self.size/100)
    
    def update(self):
        self.move()
    
setAutoUpdate(False)
 

enemy_list = [Enemy(random.randint(0,1000),random.randint(0,1000), "enemy.png", random.randint(10,100)) for i in range(10)]
player = Player(500,500,"player.png",100)

while game_active:
    
    for enemy in enemy_list:
        enemy.update()
    player.move()
    
    
    updateDisplay()
    tick(50)
        
endWait()
