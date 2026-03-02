import pygame
import constants as c
import globals as g

#Generates platforms (per room? probably should take in array of platforms)
# def render_platforms(platform_list, screen):
#     for rect in platform_list:
#         pygame.draw.rect(screen, "cyan", rect)
#     return platform_list

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

#TODO: POSSIBLY MAKE A PART OF PLAYER CLASS
def reset_position():
    for start_platform in g.starting_platform_list:
        if start_platform.level == g.prev_level and start_platform.room == g.prev_room:
            player_position = pygame.Vector2(start_platform.rect.x, start_platform.rect.top - c.PLAYER_SIZE)
            player_hitbox = pygame.Rect(player_position.x, player_position.y, c.PLAYER_SIZE, c.PLAYER_SIZE)
            return player_position, player_hitbox
        
    return KeyError

def text_input(event, text):
    continue_input = True

    if event.type == pygame.KEYDOWN:
        if event.key == 8:
            text = text[:-1]
        elif event.key == 13:
            continue_input = False
        else:
            text += event.unicode
    
    return continue_input, text
