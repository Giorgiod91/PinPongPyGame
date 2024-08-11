import pygame
import random

class Ball:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (244, 44, 14)
        self.speed = speed
        self.direction_y = 0
        self.direction_x = 1
        self.width = 20
        self.height = 20

        

    def automated_movement(self, screen_width, screen_height):
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

    
    def check_collision(self, player):
        pygame.mixer.init()
        if self.rect.colliderect(player.rect):
            pygame.mixer.music.load('bounce1.Wav')
            

            # Determine where the ball hit the paddle
            distance_from_center = (player.rect.centery - self.rect.centery)
            bounce_direction = distance_from_center / (player.rect.height / 2)

            # Adjust the ball's direction based on the hit position
            bounce_angle = bounce_direction * 75  # Adjust angle based on collision point
            self.direction_x = -self.direction_x  # Reverse the horizontal direction
            self.direction_y = -bounce_direction  # Set the vertical direction based on the collision point

            

           

                    
           
         
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)
