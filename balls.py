import pygame  

class Ball:
    def __init__(self,x,y,width,height, speed):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = (244,44,14)
        self.speed = speed
        self.direction_y = 0  
        self.direction_x = 1  
        self.width = 20
        self.height = 20


    def automated_movement(self, screen_width, screen_height):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.direction = -1

        self.rect.y += self.direction_y * self.speed
        self.rect.x += self.direction_x * self.speed

     
        if self.rect.top < 0:
            self.rect.top = 0
            self.direction_y = 1  # Bounce down if the ball hits the top edge
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.direction_y = -1  # Bounce up if the ball hits the bottom edge
        if self.rect.left < 0:
            self.rect.left = 0
            self.direction_x = 1  # Bounce right if the ball hits the left edge
        if self.rect.right > screen_width:
            self.rect.right = screen_width
            self.direction_x = -1  # Bounce left if the ball hits the right edge


        


            
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)

