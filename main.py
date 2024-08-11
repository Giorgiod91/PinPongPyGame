import pygame
import sys
from player import Player
from Objects import Objects
from balls import Ball
from Goals import Goals
import random

# pygame setup
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()
running = True
#initialize player, boss, and balls
player = Player(screen_width // 2, screen_height // 2, 22, 50, 5)
objects = Objects(100, 100, random.randint(1, 100), random.randint(1, 100), 5)

ball = Ball(player.rect.x, player.rect.y,  7, 7, 5)
current_color = "purple"

pygame.mixer.init()


goals = Goals(screen_width, screen_height)
new_Objects = []
randomColors = ["green", "blue", "red", "yellow", "orange", "purple", "pink", "brown", "black", "white"]


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    
       

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(current_color)

    


    # RENDER YOUR GAME HERE
     # Handle player movement
    player.handle_movement()
    # Handle player ability
    player.useDef_Cd()

    # Draw the player
    player.draw(screen)

   

    objects.draw(screen)
    goals.draw(screen)
    goals.drawGoalLine(screen, screen_width, screen_height)
    goal_scored = goals.check_goal(ball, screen_width, screen_height)


    if goals.check_goal(ball, screen_width, screen_height):
        current_color = random.choice(randomColors)
        if(current_color == "red"):
         ball.color = (255,255,255)
         player.color = (255,255,255)
        elif(current_color == "white"):
         ball.color = (0,0,255)
         player.color = (0,0,255)
         
           
        print(f"Goal scored! Changing color to {current_color}")
    
   
                 
 
       

    ball.automated_movement(800, 600)
    ball.check_collision(player)
    #if(collisionHappened):
     #  pygame.mixer.music.load("bounce.wav")
   
       
        
                

    ball.draw(screen)
   


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()