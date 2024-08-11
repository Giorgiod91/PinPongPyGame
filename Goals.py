import pygame
import random
from player import Player
from Objects import Objects
from balls import Ball


class Goals:
    def __init__(self, screen_width, screen_height):
        self.player1Goals = []
        self.player2Goals = []
        self.goal_One_Position = pygame.Rect(0, 0, 5, screen_height)  # Left side goal area
        self.goal_Two_Position = pygame.Rect(screen_width - 5, 0, 5, screen_height)  # Right side goal area
        self.goal_scored = False

    def drawGoalLine(self, screen, screen_width, screen_height):
        pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 600), 5)
        pygame.draw.line(screen, (255, 255, 255), (0, 0), (0, screen_height), 5)
        pygame.draw.line(screen, (255, 255, 255), (screen_width - 5, 0), (screen_width - 5, screen_height), 5)
    
    def check_goal(self, ball, screen_width, screen_height):
        self.goal_scored = False
        if ball.rect.colliderect(self.goal_One_Position):
            self.player2Goals.append(1)
            
            ball.direction_x *= -1
            
            self.goal_scored = True
            
        if ball.rect.colliderect(self.goal_Two_Position):
            self.player1Goals.append(1)    
           
            ball.direction_x *= -1
            self.goal_scored = True

        return self.goal_scored
        

        
    
       


    def draw(self, screen):
        font = pygame.font.Font(None, 36)
        player1_score = font.render(str(len(self.player1Goals)), True, (255, 255, 255))
        player2_score = font.render(str(len(self.player2Goals)), True, (255, 255, 255))
        screen.blit(player1_score, (50, 50))
        screen.blit(player2_score, (750, 50))
             