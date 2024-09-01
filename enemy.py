import pygame

class Enemy:
    def __init__(self,x,y,width,height, speed):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = (255,0,0)
        self.width = width
        self.height = height
        self.speed = speed * 0.8 
        self.direction_x = 1
        self.direction_y = 1
    
    def automated_movement(self, ball_position, screen_width, screen_height):
    
     #check ifi the ball is to the right or left of the enemy
    
     if self.rect.centery < ball_position.y:
        self.direction_y = 1
     elif self.rect.centery > ball_position.y:
        self.direction_y = -1
     elif self.rect.centerx < ball_position.x:
        self.direction_y = 1
     else:
        self.direction_y = 0  # Stay still if the ball is in line with the enemy

     self.rect.y += self.direction_y * self.speed

    # Keep the enemy within the screen 
     if self.rect.top < 0:
        self.rect.top = 0
     if self.rect.bottom > screen_height:
        self.rect.bottom = screen_height
     if self.rect.left < 0:
        self.rect.left = 0
     if self.rect.right > screen_width:
        self.rect.right = screen_width






    
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)
