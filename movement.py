import pygame
import pygame._sdl2.video as video
import helper as h
import constants as c

pygame.init()

#Setup Variables
# screen_width = 1280
# screen_height = 720
# speed = 1500
# player_size = 20
# # player_disabled = 0
# # stun_time = 30

# font = pygame.font.Font(None, 55)

# #Runtime Variables
# level = 0
# player_position = pygame.Vector2(screen_width/2, 0)
# player_velocity = pygame.Vector2(0, 0)
# player_acceleration = pygame.Vector2(0, 0)
# player_hitbox = pygame.Rect(player_position.x, player_position.y, player_size, player_size)

# ground_level = screen_height
# on_ground = True

# mouse_size = 10
# mouse_position = pygame.Vector2(0, 0)
# mouse_hitbox = pygame.Rect(mouse_position.x, mouse_position.y, mouse_size, mouse_size)
# pygame.mouse.set_visible(False)


# dt = 0

# menu_open = 0

# #Setup
# screen = pygame.display.set_mode((screen_width, screen_height))
# clock = pygame.time.Clock()
# running = True

#Takes in key presses
def player_input(player_vel, player_acc, keys, on_ground):
    # pygame.key.set_repeat()
    if on_ground:
        if keys[pygame.K_w]:
            player_vel.y += -400
    if keys[pygame.K_a]:
        player_acc.x += -c.SPEED 
    if keys[pygame.K_d]:
        player_acc.x += c.SPEED
        
#Defines "friction" and "gravity"
def physics(player_pos, player_vel, player_acc, ground_level):
    player_acc.x = -player_vel.x*5

    jump = True

    if(player_pos.y < ground_level - c.PLAYER_SIZE):
        player_acc.y = 1000
        jump = False
    else:
        player_acc.y = 0
        player_vel.y = 0
        player_pos.y = ground_level - c.PLAYER_SIZE

    return jump

#Updates player position on screen
def update_position(player_pos, player_vel, player_acc, dt):
    player_vel.x += player_acc.x * dt
    player_vel.y += player_acc.y * dt

    if player_vel.x > 500:
        player_vel.x = 500
    
    # if player_vel.y > 500:
    #     player_vel.y = 500

        
    player_pos.x += player_vel.x * dt
    player_pos.y += player_vel.y * dt

    if player_pos.x < 0:
        player_pos.x = 0
    
    if player_pos.x > c.SCREEN_WIDTH:
        player_pos.x = c.SCREEN_WIDTH


#Collision detection with platform objects
def platform_handling(collision_rect, player_hitbox, player_position, player_velocity, player_acceleration, rect_list):
    ground_level = c.SCREEN_HEIGHT
    if collision_rect != -1:
        platform = rect_list[collision_rect]

        if player_hitbox.bottom - 20 < platform.top and player_velocity.y >= 0:
            ground_level = platform.top +1
            # ground_level = player_hitbox.bottom
        elif player_hitbox.x < platform.left:
            # print("player bot: ", player_hitbox.bottom, ", box top: ", rect_list[collision_rect].top, ", box right: ", rect_list[collision_rect].right)

            player_velocity.x = 0
            player_acceleration.x = 0
            player_position.x = platform.left - c.PLAYER_SIZE
        elif player_hitbox.x < platform.right:
            # print("player bot: ", player_hitbox.bottom, ", box top: ", rect_list[collision_rect].top, ", box right: ", rect_list[collision_rect].right)

            player_velocity.x = 0
            player_acceleration.x = 0
            player_position.x = platform.right + c.PLAYER_SIZE
        
    return ground_level

def movement_handling(platform_list, player_hitbox, player_position, player_velocity, player_acceleration, dt):
    collision_platform = player_hitbox.collidelist(platform_list)
    ground_level = platform_handling(collision_platform, player_hitbox, player_position, player_velocity, player_acceleration, platform_list)

    on_ground = physics(player_position, player_velocity, player_acceleration, ground_level)
    keys = pygame.key.get_pressed()
    player_input(player_velocity, player_acceleration, keys, on_ground)

    update_position(player_position, player_velocity, player_acceleration, dt)
    player_hitbox.update(player_position.x - c.PLAYER_SIZE, player_position.y - c.PLAYER_SIZE, c.PLAYER_SIZE*2, c.PLAYER_SIZE*2)

    return player_hitbox, player_position, player_velocity, player_acceleration
