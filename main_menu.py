import movement
import pygame
import constants as c
import helper as h

def main_menu(mouse_hitbox, screen, font):
    screen.fill("black")
    level = 0

    play_color = "white"
    play_button, play_text = h.text_create(c.SCREEN_WIDTH/2-200, c.SCREEN_HEIGHT/2 - 100, 400, 50, "Play!", "Black", font)

    if(play_button.colliderect(mouse_hitbox)):
        play_color = "pink"
        if(pygame.mouse.get_pressed(num_buttons=3)[0]):
            level = 1


    h.text_render([play_color], [play_button], [play_text], [100], [5], screen)

    #Mouse handling
    mouse_hitbox = h.mouse_handle(mouse_hitbox, screen)



    return level

    