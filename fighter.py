import pygame

pygame.init()

class Fighter():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))
        self.speed = 10
        
    def move(self):
        dx = 0
        dy = 0
        
        # get keypresses
        key = pygame.key.get_pressed()

        # movement
        if key[pygame.K_a]:
            dx = -self.speed
        if key[pygame.K_d]:
            dx = self.speed

        # update player position
        self.rect.x += dx
        self.rect.y += dy
    
def draw(self, surface):
    pygame.draw.rect(surface, (255,0,0), self.rect)


        