import pygame
from fighter import Fighter

pygame.init()

# create game window
screen_width = 800
screen_height = 600
screen_title = "Anime Fighter"

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(screen_title)

# set framerate
clock = pygame.time.Clock()
FPS = 60

# load bg image
bg_image = pygame.image.load("./assets/images/matterhorn.jpg").convert_alpha()

# function to draw bg
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height))
    screen.blit(scaled_bg, (0,0))
    
draw_bg()

# create fighters
fighter1 = Fighter(200, 310)
fighter2 = Fighter(700, 310)

# game loop
running = True
while running:
    clock.tick(FPS)
    
        # event handler
    for event in pygame.event.get():
        # Check if the user closed the window
        if event.type == pygame.QUIT:
            running = False

    # move fighters
    fighter1.move()
    fighter2.move()

    # draw fighters
    screen.fill((0,0,0))
    fighter1.draw(screen)
    fighter2.draw(screen)

    # update display
    pygame.display.flip()
    
    pygame.quit()

    # handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        print("A key pressed")
    if keys[pygame.K_d]:
        print("D key pressed")
    if keys[pygame.K_w]:
        print("W key pressed")
    if keys[pygame.K_s]:
        print("S key pressed")
    if keys[pygame.K_SPACE]:
        print("Spacebar pressed")    

    # Update the display
    pygame.display.update()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        print("Left arrow pressed")
    if keys[pygame.K_RIGHT]:
        print("Right arrow pressed")
    if keys[pygame.K_SPACE]:
        print("Spacebar pressed")    

