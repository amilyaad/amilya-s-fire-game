import pygame

pygame.init()

# set up variables for the display
SCREEN_HEIGHT = 640
SCREEN_WIDTH = 1100
LOWER_MARGIN = 50
screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT + LOWER_MARGIN)

BG_ONE = pygame.image.load('').convert_alpha()
BG_TWO = pygame.image.load('').convert_alpha()
BG_THREE = pygame.image.load('').convert_alpha()
BG_FOUR = pygame.image.load('').convert_alpha()

def draw_bg(# inputted bg by user):
    if
    screen.blit(BG_ONE, (0,0 - LOWER_MARGIN))

# -------- Main Program Loop -----------
while run:

    draw_bg()

    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    pygame.display.update()
    ##  ----- NO BLIT ZONE END  ----- ##



screen.fill((0, 0, 0))
screen.blit(image, rect1)
pygame.display.update()
