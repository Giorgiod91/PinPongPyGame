import pygame  

class Ball:
    def __init__(self,x,y,width,height, speed):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = (244,44,14)
        self.speed = speed
        self.direction = 0
        self.width = 20
        self.height = 20

    def automated_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.direction = -1

        self.rect.y += self.direction * self.speed

        


            
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)

