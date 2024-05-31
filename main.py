import pygame
import button

from dashboard import Dashboard
from tilemap import Tile
from button import Button
from player import Sprite_One
from player import Sprite_Two

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comis Sans', 15)

title = "Castle Defender"
message = "Welcome to Castle Defender! Click play to being!"
display_title = my_font.render(message, True, (255, 255, 255))
display_message = my_font.render(message, True, (255, 255, 255))

b_play = pygame.image.load("playbutton.png")
b_one = pygame.image.load("onebutton.png")
b_two = pygame.image.load("twobutton.png")
b_three = pygame.image.load("threebutton.png")
b_four = pygame.image.load("fourbutton.png")
p_one = pygame.image.load("spriteone.png")
p_two = pygame.image.load("spritetwo.png")


# set up variables for the display
SCREEN_HEIGHT = 640
SCREEN_WIDTH = 1000
LOWER_MARGIN = 50
SIDE_MARGIN = 300
screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT + LOWER_MARGIN)
ROWS = 16
MAX_COLS = 25
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 7
current_tile = 0

world_data = []
for row in range(ROWS):
	r = [-1] * MAX_COLS
	world_data.append(r)

img_list = []
for x in range(TILE_TYPES):
	img = pygame.image.load(f'img/tile/{x}.png').convert_alpha()
	img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
	img_list.append(img)

save_img = pygame.image.load('img/save_btn.png').convert_alpha()
load_img = pygame.image.load('img/load_btn.png').convert_alpha()


PRIMARY_BG = pygame.image.load('background.png').convert_alpha()
BG_ONE = pygame.image.load('').convert_alpha()
BG_TWO = pygame.image.load('').convert_alpha()
BG_THREE = pygame.image.load('').convert_alpha()
BG_FOUR = pygame.image.load('').convert_alpha()

chosen_bg = 0

not_play = True
dashboard = False
lvl_one = False
lvl_two = False
lvl_three = False
create_map = False

button_play = Dashboard("playbutton.png", 40, 40)
button_one = Dashboard("onebutton.png", 40, 40)
button_two = Dashboard("twobutton.png", 40, 40)
button_three = Dashboard("threebutton.png", 40, 40)
button_four = Dashboard("fourbutton.png", 40, 40)

def draw_bg(chosen_bg):
    if chosen_bg == 1:
        screen.blit(BG_ONE, (0, 0 - LOWER_MARGIN))
    elif chosen_bg == 2:
        screen.blit(BG_TWO, (0, 0 - LOWER_MARGIN))
    elif chosen_bg == 3:
        screen.blit(BG_THREE, (0, 0 - LOWER_MARGIN))
    elif chosen_bg == 4:
        screen.blit(BG_FOUR, (0, 0 - LOWER_MARGIN))
    dashboard = False

def draw_grid():
	#vertical lines
	for c in range(MAX_COLS + 1):
		pygame.draw.line(screen, (255, 255, 255), (c * TILE_SIZE, 0), (c * TILE_SIZE, SCREEN_HEIGHT))
	#horizontal lines
	for c in range(ROWS + 1):
		pygame.draw.line(screen, (255, 255, 255), (0, c * TILE_SIZE), (SCREEN_WIDTH, c * TILE_SIZE))

def draw_world():
	for y, row in enumerate(world_data):
		for x, tile in enumerate(row):
			if tile >= 0:
				screen.blit(img_list[tile], (x * TILE_SIZE, y * TILE_SIZE))

save_button = button.Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT + LOWER_MARGIN - 50, save_img, 1)
load_button = button.Button(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT + LOWER_MARGIN - 50, load_img, 1)

button_list = []
button_col = 0
button_row = 0
for i in range(len(img_list)):
	tile_button = button.Button(SCREEN_WIDTH + (75 * button_col) + 50, 75 * button_row + 50, img_list[i], 1)
	button_list.append(tile_button)
	button_col += 1
	if button_col == 3:
		button_row += 1
		button_col = 0


# -------- Main Program Loop -----------
while run:
    while not not_play:
        if keys[pygame.K_RIGHT]:
            p_one.move_direction("right")
        elif keys[pygame.K_LEFT]:
            p_one.move_direction("left")
        elif keys[pygame.K_UP]:
            p_one.move_direction("up")
        elif keys[pygame.K_DOWN]:
            p_one.move_direction("down")

        if keys[pygame.K_d]:
            p_two.move_direction("right")
        elif keys[pygame.K_a]:
            p_two.move_direction("left")
        elif keys[pygame.K_w]:
            p_two.move_direction("up")
        elif keys[pygame.K_s]:
            p_two.move_direction("down")

# --- Main event loop --- #
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        elif not_play:
            if event.type == pygame.MOUSEBUTTONUP and button_play.rect.collidepoint(event.pos):
                dashboard = True
            if dashboard:
                if pygame.MOUSEBUTTONUP and b_one.rect.collidepoint(event.pos):
                    bg = 1
                    draw_bg(bg)
                    not_play = False
                    lvl_one = True
                if pygame.MOUSEBUTTONUP and b_two.rect.collidepoint(event.pos):
                    bg = 2
                    draw_bg(bg)
                    not_play = False
                    lvl_two = True
                if pygame.MOUSEBUTTONUP and b_three.rect.collidepoint(event.pos):
                    bg = 3
                    draw_bg(bg)
                    not_play = False
                    lvl_level = False
                if pygame.MOUSEBUTTONUP and b_four.rect.collidepoint(event.pos):
                    bg = 4
                    draw_bg(bg)
                    create_map = True
                    not_play = False
        elif not not_play and create_map:
            pygame.draw.rect(screen, (0, 255, 0), (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))

            button_count = 0
            for button_count, i in enumerate(button_list):
                if i.draw(screen):
                    current_tile = button_count

            pygame.draw.rect(screen, (255, 0, 0), button_list[current_tile].rect, 3)

            pos = pygame.mouse.get_pos()
            x = (pos[0]) // TILE_SIZE
            y = pos[1] // TILE_SIZE

            # check that the coordinates are within the tile area
            if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
                # update tile value
                if pygame.mouse.get_pressed()[0] == 1:
                    if world_data[y][x] != current_tile:
                        world_data[y][x] = current_tile
                if pygame.mouse.get_pressed()[2] == 1:
                    world_data[y][x] = -1

    pygame.display.update()

if not_play:
    screen.fill('background.png')
    screen.blit(display_title, (0, 0))
    screen.blit(display_message, (0, 0))
    screen.blit(button_play.image, button_play.rect)
if dashboard:
    screen.blit(button_one.image, button_one.rect)
    screen.blit(button_two.image, button_two.rect)
    screen.blit(button_three.image, button_three.rect)
    screen.blit(button_four.image, button_four.rect)
if lvl_one:
    screen.fill('background.png')
if lvl_two:
    screen.fill('background.png')
if lvl_three:
    screen.fill('background.png')

pygame.display.update()
