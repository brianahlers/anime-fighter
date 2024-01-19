import pygame

pygame.init()

# create game window
screen_width = 800
screen_height = 600
screen_title = "Anime Fighter"

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(screen_title)

# load bg image
bg_image = pygame.image.load("./assets/images/matterhorn.jpg").convert_alpha()

# function to draw bg
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height))
    screen.blit(scaled_bg, (0,0))

# game loop
running = True
while running:

    # draw bg
    draw_bg()

    # event handler
    for event in pygame.event.get():
        # Check if the user closed the window
        if event.type == pygame.QUIT:
            running = False

    # update display
    pygame.display.update()

    # handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        print("Left arrow pressed")
    if keys[pygame.K_RIGHT]:
        print("Right arrow pressed")
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

