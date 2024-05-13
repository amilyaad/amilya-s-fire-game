import pygame

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comis Sans', 15)

title = "Castle Defender"
message = "Welcome to Castle Defender! Click play to being!"
display_title = my_font.render(message, True, (255, 255, 255))
display_message = my_font.render(message, True, (255, 255, 255))

self.image = pygame.image.load("playbutton.png")
self.image = pygame.image.load("onebutton.png")
self.image = pygame.image.load("twobutton.png")
self.image = pygame.image.load("threebutton.png")
self.image_size = self.image.get_size()


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

not_play = True
dashboard = False
# -------- Main Program Loop -----------
while run:

    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        elif not_play:
            if event.type == pygame.MOUSEBUTTONUP:
                not_play = False
                dashboard = True

    pygame.display.update()
    ##  ----- NO BLIT ZONE END  ----- ##



screen.fill(('background.png'))
if not_play:
    screen.blit(display_title, (0,0))
    screen.blit(display_message, (0, 0))
    screen.blit(self.play_botton, (0,0))
if dashboard:


pygame.display.update()
