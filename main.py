from pygame_functions import *
import math, random, time, pickle




screen_x_size = 1000
screen_y_size = 1000
screenSize(screen_x_size,screen_y_size)
setBackgroundColour("black")

mass_multiplier = 0.2

rotation_speed = 10
min_speed = 1
max_speed = 10

game_active = True

class Creature:
    
    def __init__(self, global_x, global_y, image, size):
        
        self.global_x = global_x
        self.global_y = global_y
        self.size = size 
        self.sprite = makeSprite(image)
        self.speed = 0
    
        
        
        
        transformSprite(self.sprite, 0, self.size/100)
        showSprite(self.sprite)
    
        

class Enemy(Creature):
    def __init__(self,global_x, global_y,image,  size):
        super().__init__(global_x, global_y, image,  size)
        
        self.direction = random.randint(0,359)
        self.speed = random.randint(min_speed, max_speed)
        
        hideSprite(self.sprite)
        
        transformSprite(self.sprite,self.direction,self.size/100)
        
        #self.relative_player_x_speed = 0
        #self.relative_player_x_speed = 0
        
    
    def move(self):
        
        
        
        self.global_y += math.sin( ( self.direction/180 ) * math.pi) * self.speed
        self.global_x += math.cos( ( self.direction/180 ) * math.pi) * self.speed
        
        self.global_y = self.global_y % 10000
        self.global_x = self.global_x % 10000



        
    def update(self):
    
        self.move()
        
def draw_boundary(player):
    clearShapes()
    drawRect((screen_x_size/2)-player.global_x,(screen_y_size)-player.global_y, 10000, 10000, (0,0,40), 0)
    drawRect((screen_x_size/2)-player.global_x,(screen_y_size)-player.global_y, 10000, 10000, (255,255,255), 5)
    
    
class Player(Creature):
    def __init__(self,global_x, global_y, image, size):
        
        super().__init__(global_x, global_y, image, size)
        self.direction = 0
        moveSprite(self.sprite, screen_x_size/2, screen_y_size/2 ,centre=True)
        transformSprite(self.sprite,self.direction,self.size/100)
        
    def move(self):
        
        #if keyPressed("w"):
        
        self.global_y += math.sin(math.radians(self.direction)) * self.speed
        self.global_x += math.cos(math.radians(self.direction)) * self.speed
        
        self.global_y = self.global_y % 10000
        self.global_x = self.global_x % 10000
        
        dy = mouseY() - screen_y_size / 2
        dx = mouseX() - screen_x_size / 2
        
        distance = math.sqrt(dy*dy + dx*dx)
        
        self.speed = (distance/200) * 10
        if self.speed > max_speed:
            self.speed = max_speed

        self.direction = math.degrees(math.atan2(dy,dx))
        
        for c in enemy_list:
            if touching(self.sprite,c.sprite):
                
                if self.size > c.size:
                    enemy_list.remove(c)
                    hideSprite(c.sprite)
                    self.size += c.size * mass_multiplier
                    
        moveSprite(self.sprite, screen_x_size/2, screen_y_size/2 ,centre=True)
        transformSprite(self.sprite,self.direction,self.size/100)
        self.check_display()
        
    def check_display(self):
        
        for c in enemy_list:
            
            if abs(dx := (self.global_x - c.global_x)) < screen_x_size/2 and abs(dy := (self.global_y - c.global_y)) < screen_y_size/2:
                
                moveSprite(c.sprite, (screen_x_size/2)- dx , (screen_y_size/2) - dy ,centre=True)
                showSprite(c.sprite)
            
            else:
                hideSprite(c.sprite)
        
   
        
        
    
    def update(self):
        self.move()
    
setAutoUpdate(False)
 

enemy_list = [Enemy(random.randint(0,10000),random.randint(0,10000), "enemy.png", random.randint(10,100)) for i in range(200)]
player = Player(5000,5000,"player.png",20)

while game_active:
    
    for enemy in enemy_list:
        enemy.update()
    player.update()
    draw_boundary(player)
    
    updateDisplay()
    tick(50)
        
endWait()
