import pygame
import helper as h
import constants as c
from platform_1 import Platform as p
import globals as g

def file_read(level, room):
    g.platform_list = []
    g.starting_platform_list = []

    file_path = "level_definitions/level-"+level+"/room-"+room+".txt"

    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, 1):
                words = line.split()
                temp_rect = pygame.Rect(int(words[0]), int(words[1]), int(words[2]), int(words[3]))
                temp_platform = p(temp_rect, int(words[4]), words[5], words[6])
                if int(words[4]) == 4:
                    g.starting_platform_list.append(temp_platform)
                g.platform_list.append(temp_platform)
            
    except FileNotFoundError:
        print("This level/room doesn't exist", file_path)



def render(screen, player_position):
    #Background
    screen.fill("black")

    if(g.new_level):
        file_read(g.level, g.room)

    for platform in g.platform_list:
        platform.draw_platform(screen)

    #Draw player
    pygame.draw.circle(screen, "white", player_position, c.PLAYER_SIZE)


