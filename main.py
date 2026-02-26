import pygame
import movement
import main_menu
import constants as c
import render_level
import esc_menu
import helper as h


def main():
    pygame.init()

    #Setup Variables
    font = pygame.font.Font(None, 55)

    level = 0
    room = 0

    player_position = pygame.Vector2(c.SCREEN_WIDTH/2, 0)
    player_velocity = pygame.Vector2(0, 0)
    player_acceleration = pygame.Vector2(0, 0)
    player_hitbox = pygame.Rect(player_position.x, player_position.y, c.PLAYER_SIZE, c.PLAYER_SIZE)


    mouse_position = pygame.Vector2(0, 0)
    mouse_hitbox = pygame.Rect(mouse_position.x, mouse_position.y, c.MOUSE_SIZE, c.MOUSE_SIZE)
    pygame.mouse.set_visible(False)

    dt = 0
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
        
        if level == 0:
            level = main_menu.main_menu(mouse_hitbox, screen, font)

            if level != 0:
                player_position, player_velocity, player_acceleration = h.reset_position(1)

            pygame.display.flip()
            dt = clock.tick(60) / 1000
            continue

        if menu_open:
            platform_list = render_level.render(level, player_hitbox, screen, player_position)
            menu_open, level = esc_menu.esc_menu(mouse_hitbox, screen, font, menu_open, level)
            pygame.display.flip()
            dt = clock.tick(60) / 1000
            if menu_open == -1:
                running = False
                break
            continue

        platform_list = render_level.render(level, player_hitbox, screen, player_position)
        player_hitbox, player_position, player_velocity, player_acceleration = movement.movement_handling(platform_list, player_hitbox, player_position, player_velocity, player_acceleration, dt)

        #Display and update clock
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
    pygame.quit()