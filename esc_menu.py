import pygame
import helper as h
import constants as c

def esc_menu(mouse_hitbox, screen, font, menu_open, level):
    continue_color = "white"
    continue_button, continue_text = h.text_create(c.SCREEN_WIDTH/2 - 200, c.SCREEN_HEIGHT/2 - 100, 400, 50, "Continue", "Black", font)
    if(continue_button.colliderect(mouse_hitbox)):
        continue_color = "pink"
        if(pygame.mouse.get_pressed(num_buttons=3)[0]):
            menu_open = (menu_open+1)%2
    
    main_menu_color = "white"
    main_menu_button, main_menu_text = h.text_create(c.SCREEN_WIDTH/2 - 200, c.SCREEN_HEIGHT/2, 400, 50, "Menu", "Black", font)
    if(main_menu_button.colliderect(mouse_hitbox)):
        main_menu_color = "pink"
        if(pygame.mouse.get_pressed(num_buttons=3)[0]):
            level = 0
            menu_open = (menu_open+1)%2

    quit_color = "white"
    quit_button, quit_text = h.text_create(c.SCREEN_WIDTH/2 - 200, c.SCREEN_HEIGHT/2 + 100, 400, 50, "Quit", "Black", font)
    if(quit_button.colliderect(mouse_hitbox)):
        quit_color = "pink"
        if(pygame.mouse.get_pressed(num_buttons=3)[0]):
            menu_open = -1

    esc_menu_buttons = [continue_button, main_menu_button, quit_button]
    esc_menu_texts = [continue_text, main_menu_text, quit_text]
    esc_menu_colors = [continue_color, main_menu_color, quit_color]
    esc_menu_text_x = [100, 150, 150]
    esc_menu_text_y = [5, 5, 5]
    h.text_render(esc_menu_colors, esc_menu_buttons, esc_menu_texts, esc_menu_text_x, esc_menu_text_y, screen)
    
    #Mouse handling
    mouse_hitbox = h.mouse_handle(mouse_hitbox, screen)

    return menu_open, level
