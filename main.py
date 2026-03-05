import pygame
# import Old.movement as movement
import Menus.main_menu as main_menu
import constants as c
import render_level
import Menus.esc_menu as esc_menu
import helper as h
import globals as g
from Class_Definitions.player_ import Player as p


def main():
    pygame.init()

    #Setup Variables
    font = pygame.font.Font(None, 55)

    main_player = p()

    mouse_position = pygame.Vector2(0, 0)
    mouse_hitbox = pygame.Rect(mouse_position.x, mouse_position.y, c.MOUSE_SIZE, c.MOUSE_SIZE)
    pygame.mouse.set_visible(False)

    menu_open = 0

    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == 27:
                menu_open = (menu_open+1)%2
            if event.type == pygame.QUIT:
                running = False
        
        if g.level == "main":
            g.new_level = True
            g.level = main_menu.main_menu(mouse_hitbox, screen, font)

            if g.level != "main":
                g.level = "0"
                g.room = "0"

            pygame.display.flip()
            g.dt = clock.tick(60) / 1000
            continue

        if menu_open:
            render_level.render(screen, main_player.pos)
            menu_open, g.level = esc_menu.esc_menu(mouse_hitbox, screen, font, menu_open, g.level)
            pygame.display.flip()
            g.dt = clock.tick(60) / 1000
            if menu_open == -1:
                running = False
                break
            continue

        render_level.render(screen, main_player.pos)

        if g.new_level:
            main_player.reset_position()
            print("reset position new level", main_player.pos)

        g.new_level = False

        main_player.movement_handle()

        #Display and update clock
        pygame.display.flip()
        g.dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
    pygame.quit()