import pygame

class DungeonBoss:
    def __init__(self,x,y,width,height, speed):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = (0,0,0)
        self.speed = speed
        self.direction = 1 # 1 is right, -1 is left
        self.patrol_range = 200
        self.start_x = x
        self.end_x = x + self.patrol_range


    def automated_movement(self):
        if self.rect.x >= self.end_x:
            self.direction = -1
        elif self.rect.x <= self.start_x:
            self.direction = 1

        self.rect.x += self.speed * self.direction

    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


