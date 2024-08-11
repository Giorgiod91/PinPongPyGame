import pygame
import random
from player import Player
from Objects import Objects
from balls import Ball
from Goals import Goals

# pygame setup
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()
running = True

# Initialize player, objects, and ball
player = Player(screen_width // 2, screen_height // 2, 22, 50, 5)
objects = Objects(100, 100, random.randint(1, 100), random.randint(1, 100), 5)
ball = Ball(player.rect.x, player.rect.y, 7, 7, 5)
current_color = "purple"

# Initialize speed boost variables
speedBoost = False
pygame.mixer.init()
goals = Goals(screen_width, screen_height)
randomColors = ["green", "blue", "red", "yellow", "orange", "purple", "pink", "brown", "black", "white"]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(current_color)

    # Handle player movement and abilities
    player.handle_movement()
    player.useDef_Cd()
    player.draw(screen)
    
    # Draw objects and goals
    objects.draw(screen)
    goals.draw(screen)
    goals.drawGoalLine(screen, screen_width, screen_height)

    if goals.speedBoostAvailable:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            ball.speed = 10  # Activate the speed boost
            speedBoost = True
            goals.speedBoostAvailable = False
            print("Speed Boost Activated!")

    # Check if a goal was scored
    goal_scored = goals.check_goal(ball, screen_width, screen_height)
    if goal_scored:
        current_color = random.choice(randomColors)
        if current_color == "red":
            ball.color = (255, 255, 255)
            player.color = (255, 255, 255)
        elif current_color == "white":
            ball.color = (0, 0, 255)
            player.color = (0, 0, 255)

        print(f"Goal scored! Changing color to {current_color}")

        # Reset ball speed if the boost was activated
        if speedBoost:
            ball.speed = 5
            speedBoost = False

    # Handle ball movement and collision
    ball.automated_movement(screen_width, screen_height)
    ball.check_collision(player)
    ball.check_collision(objects)

    
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
