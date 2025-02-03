# Creating Viewport
import pygame
import random
import time

pygame.init()
time.time()

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption('Tileset Test')
pygame.display.Info() 

# Setting default Variables
zoom_level = 5
current_tile_processed = 0

level_height = 10
level_width = 10

print_tile_xpos = 0
print_tile_ypos = 0

# Importing Textures
tile1 = pygame.image.load('tiles/tile1.png')
tile2 = pygame.image.load('tiles/tile2.png')
tile3 = pygame.image.load('tiles/tile3.png')
tile4 = pygame.image.load('tiles/tile4.png')
tile5 = pygame.image.load('tiles/tile5.png')
tile6 = pygame.image.load('tiles/tile6.png')
tile7 = pygame.image.load('tiles/tile7.png')
tile8 = pygame.image.load('tiles/tile8.png')
tile9 = pygame.image.load('tiles/tile9.png')
tile10 = pygame.image.load('tiles/tile10.png')
tile11 = pygame.image.load('tiles/tile11.png')
tile12 = pygame.image.load('tiles/tile12.png')
tile13 = pygame.image.load('tiles/tile13.png')
tile14 = pygame.image.load('tiles/tile14.png')
tile15 = pygame.image.load('tiles/tile15.png')
tile16 = pygame.image.load('tiles/tile16.png')

player_img = pygame.image.load('characters/character.png')

font_PixelReborne = pygame.font.Font('fonts/PixelReborne.ttf', 32)

# Preparing colors
color_bg = (36, 21, 39)
color_white = (255, 255, 255)

# Preparing Display Surface
screen.fill(color_bg)
pygame.display.flip()

# Functions
# Get atlas type from coords
def get_atlas_tile_type(atlasX, atlasY):
    with open('rooms/tilemap.txt') as file:
        data = file.read()
        raw_tiles = list(data)

    raw_tile_number = ((atlasY - 1) * (level_width + 1)) + atlasX
    return raw_tiles[raw_tile_number]

#Print base tiles
while current_tile_processed < ((level_height * level_width) - 2):
    with open('rooms/tilemap.txt') as file:
        data = file.read()
        raw_tiles = list(data)

    if current_tile_processed > ((level_height * level_width) - 2):
        current_tile_processed = 0
        print_tile_ypos = 0
        print_tile_xpos = 0

    if raw_tiles[current_tile_processed] == '0':

        tile_type = pygame.transform.scale(tile13, (16 * zoom_level, 16 * zoom_level))
        screen.blit(tile_type, (print_tile_xpos, print_tile_ypos))

        current_tile_processed += 1
    else:
        if raw_tiles[current_tile_processed] == '1':

            tile_type = pygame.transform.scale(tile7, (16 * zoom_level, 16 * zoom_level))
            screen.blit(tile_type, (print_tile_xpos, print_tile_ypos))

            current_tile_processed += 1
        else:

            print_tile_ypos += 16 * zoom_level
            print_tile_xpos = -16 * zoom_level
            current_tile_processed += 1

    print_tile_xpos += 16 * zoom_level

# game loop
running = True
while running:



    # for loop through the event queue
    for event in pygame.event.get():

        # Keypresses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F3:
                if debug_mode:
                    debug_mode = False
                else:
                    debug_mode = True
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False

        # Check for QUIT event
        if event.type == pygame.QUIT: 
            pygame.quit()
            running = False

    pygame.display.flip()