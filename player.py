import pygame


class Player:
    def __init__(self,x,y,width,height, speed):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = (255,0,0)
        self.speed = speed
        self.in_defense_cd = False
        self.in_defense_cd_end_time = 0

    # fucntion to check what keys are pressed and move accordingly
    def handle_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Move left
            self.rect.x -= self.speed
        if keys[pygame.K_d]:  # Move right
            self.rect.x += self.speed
        if keys[pygame.K_w]:  # Move up
            self.rect.y -= self.speed
        if keys[pygame.K_s]:  # Move down
            self.rect.y += self.speed
      # Function to change color when the 'R' key is pressed
    def useDef_Cd(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r] and not self.in_defense_cd:
              self.color = (0, 0, 255)
              self.in_defense_cd = True
              # Set the end time of the cooldown to 5 seconds from now
              self.in_defense_cd_end_time = pygame.time.get_ticks() + 5000
              

        # Check if the defense mode should be turned off
        if self.in_defense_cd and pygame.time.get_ticks() > self.in_defense_cd_end_time:
            self.color = (255, 0, 0)
            self.in_defense_cd = False
        #check if the player hits the wall
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
                
          
           
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect )

 
