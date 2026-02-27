import pygame
import helper as h
import constants as c
from platform_1 import Platform as p

def render(level, room, player_hitbox, screen, player_position):
    #Background
    screen.fill("black")

    #NEED TO MAKE LEVEL SPECIFIC PLATFORM GENERATION
    # platform_list = []
    # for i in range(3):
    #     platform_list.append(pygame.Rect(c.SCREEN_WIDTH/(i+1)- 50, c.SCREEN_HEIGHT-50, 50, 50))
    # platform_list = h.render_platforms(platform_list, screen)

    platform_list = file_read(level, room)
    for platform in platform_list:
        platform.draw_platform(screen)

    #Draw player
    pygame.draw.circle(screen, "white", player_position, c.PLAYER_SIZE)

    return platform_list

def file_read(level, room):
    platform_list = []

    file_path = "level_definitions/level-"+level+"/room-"+room+".txt"

    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, 1):
                words = line.split()
                temp_rect = pygame.Rect(int(words[0]), int(words[1]), int(words[2]), int(words[3]))
                temp_platform = p(temp_rect, int(words[4]))
                platform_list.append(temp_platform)

            
    except FileNotFoundError:
        print("This level/room doesn't exist", file_path)



    return platform_list