import pygame
# from tilemap import make_tile_map

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Shoot the Fruit!")

# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

file1 = 'tile1.png'
image = pygame.image.load(file1)
rect1 = image.get_rect()

screen.fill((0, 0, 0))
screen.blit(image, rect1)
pygame.display.update()
