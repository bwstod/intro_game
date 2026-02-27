import pygame
import constants as c

#Generates platforms (per room? probably should take in array of platforms)
def render_platforms(platform_list, screen):
    # platform_list = []
    # for i in range(3):
    #     platform_list.append(pygame.Rect(c.SCREEN_WIDTH/(i+1)- 50, c.SCREEN_HEIGHT-50, 50, 50))
    for rect in platform_list:
        pygame.draw.rect(screen, "cyan", rect)
    return platform_list

#create text object with hitbox
def text_create(x, y, w, h, text, text_color, font):
    button = pygame.Rect(x, y, w, h)
    text_surf = font.render(text, True, text_color)

    return button, text_surf

#draw text object
def text_render(colors, buttons, text_surfs, text_offset_x, text_offset_y, screen):
    for i, button in enumerate(buttons):
        pygame.draw.rect(screen, colors[i], button)
        screen.blit(text_surfs[i], (button.x + text_offset_x[i], button.y + text_offset_y[i]))

def mouse_handle(mouse_hitbox, screen, mouse_size):
    mouse_position = pygame.mouse.get_pos()
    mouse_hitbox.update(mouse_position[0] - mouse_size, mouse_position[1] - mouse_size, mouse_size*2, mouse_size*2)
    pygame.draw.rect(screen, "red", mouse_hitbox)
    return mouse_hitbox

def reset_position(level, room):
    player_position = pygame.Vector2(c.SCREEN_WIDTH/2, 0)
    player_velocity = pygame.Vector2(0, 0)
    player_acceleration = pygame.Vector2(0, 0)
    return player_position, player_velocity, player_acceleration
