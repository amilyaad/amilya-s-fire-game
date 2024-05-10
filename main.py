import pygame

pygame.init()

# set up variables for the display
SCREEN_HEIGHT = 640
SCREEN_WIDTH = 1100
LOWER_MARGIN = 50
screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT + LOWER_MARGIN)

PRIMARY_BG = pygame.image.load('background.png').convert_alpha()
BG_ONE = pygame.image.load('').convert_alpha()
BG_TWO = pygame.image.load('').convert_alpha()
BG_THREE = pygame.image.load('').convert_alpha()
BG_FOUR = pygame.image.load('').convert_alpha()

chosen_bg = 0

def draw_bg(chosen_bg):
    if chosen_bg == 1
        screen.blit(BG_ONE, (0,0 - LOWER_MARGIN))
    elif chosen_bg == 2:
        screen.blit(BG_TWO, (0, 0 - LOWER_MARGIN))
    elif chosen_bg == 3:
        screen.blit(BG_THREE, (0, 0 - LOWER_MARGIN))
    elif chosen_bg == 4:
        screen.blit(BG_FOUR, (0, 0 - LOWER_MARGIN))

# -------- Main Program Loop -----------
while run:

    draw_bg()

    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        elif event.type == KEYDOWN:
            if event.key == K_1:
                self.load_image(file)
    pygame.display.update()
    ##  ----- NO BLIT ZONE END  ----- ##



screen.fill((0, 0, 0))
screen.blit(image, rect1)
pygame.display.update()
