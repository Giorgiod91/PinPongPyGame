
import random
from player import Player
from Objects import Objects
from balls import Ball
from Goals import Goals
from enemy import Enemy

# pygame setup
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()
running = True

# Initialize player, objects, and ball
player = Player(screen_width // 2, screen_height // 2, 22, 50, 5)
enemy = Enemy(screen_width // 3, screen_height // 2, 22, 50, 5)
objects = []

for i in range(6):
   
    x = random.randint(0, screen_width -10)
    y = random.randint(0, screen_height -10)
    height = random.randint(0, 30)
    width = random.randint(0,60)
    new_object = Objects(x, y, width, height, 0)
    objects.append(new_object)


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
    player.get_smaller_if_hit(ball)
    
 
    # Draw objects and goals
      # Draw objects and goals
    for obj in objects:
        obj.draw(screen)

    # Draw enemy
    enemy.draw(screen)
    enemy.automated_movement(ball.rect, screen_width, screen_height)
    # check if enemy collides with the ball
    ball.check_collision(enemy)
        
        
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
    goal_scored = goals.check_goal(ball, screen_width, screen_height,player)
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

    
   
    for obj in objects:
        ball.check_collision(obj)
        
         
   
   
        
   
        
    
        

    
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
