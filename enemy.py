import pygame

class Enemy:
    def __init__(self,x,y,width,height, speed):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = (255,0,0)
        self.width = width
        self.height = height
        self.speed = speed
    
    def automated_movement(self,screen_width, screen_height):
        self.rect.y += self.direction_y * self.speed
        self.rect.x += self.direction_x * self.speed





    
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)
