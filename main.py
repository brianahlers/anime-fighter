import pygame

pygame.init()

window_width = 800
window_height = 600
window_title = "Anime Fighter"

# Create the window
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        # Check if the user closed the window
        if event.type == pygame.QUIT:
            running = False

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

