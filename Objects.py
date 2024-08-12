import pygame
from balls import Ball

class Objects:
    def __init__(self,x,y,width,height, speed):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = (0,0,0)
        self.speed = speed
        self.direction = 1 # 1 is right, -1 is left
        self.patrol_range = 200
        self.start_x = x
        self.end_x = x + self.patrol_range
        self.destroy = False
        self.objects_life = 100


    def automated_movement(self):
        if self.rect.x >= self.end_x:
            self.direction = -1
        elif self.rect.x <= self.start_x:
            self.direction = 1

        self.rect.x += self.speed * self.direction

    def shootProjectiles(self):
        self.color = (3,44,55)

    
    def destroy_object(self, ball):
            self.objects_life -=50
            if self.objects_life <=0:
                    print("life at 0")
                    self.destroy = True
                    self.rect.width = 0
                    self.rect.height = 0
           
                


    

       

        
        



    
    def draw(self, screen):
          if self.destroy == False:
            pygame.draw.rect(screen, self.color, self.rect)
        
