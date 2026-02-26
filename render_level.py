import pygame
import helper as h
import constants as c

def render(level, player_hitbox, screen, player_position):
    #Background
    screen.fill("black")

    #NEED TO MAKE LEVEL SPECIFIC PLATFORM GENERATION
    platform_list = []
    for i in range(3):
        platform_list.append(pygame.Rect(c.SCREEN_WIDTH/(i+1)- 50, c.SCREEN_HEIGHT-50, 50, 50))
    platform_list = h.render_platforms(platform_list, screen)

    #Draw player
    pygame.draw.circle(screen, "white", player_position, c.PLAYER_SIZE)

    return platform_list