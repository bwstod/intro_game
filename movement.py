import pygame
import pygame._sdl2.video as video
import helper as h
import constants as c

pygame.init()

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

def movement_handling(platform_list, player_hitbox, player_position, player_velocity, player_acceleration, dt, level, room):
    rect_list = []
    for platform in platform_list:
        rect_list.append(platform.rect)

    collision_platforms = player_hitbox.collidelistall(rect_list)

    ground_level = c.SCREEN_HEIGHT

    if collision_platforms != -1:
        for collision_platform in collision_platforms:
            if platform_list[collision_platform].type == 2:
                player_position, player_velocity, player_acceleration = h.reset_position(level, room)

            ground_level = platform_list[collision_platform].collide_platform(player_hitbox, player_position, player_velocity, player_acceleration)

    on_ground = physics(player_position, player_velocity, player_acceleration, ground_level)
    keys = pygame.key.get_pressed()
    player_input(player_velocity, player_acceleration, keys, on_ground)

    update_position(player_position, player_velocity, player_acceleration, dt)
    player_hitbox.update(player_position.x - c.PLAYER_SIZE, player_position.y - c.PLAYER_SIZE, c.PLAYER_SIZE*2, c.PLAYER_SIZE*2)

    return player_hitbox, player_position, player_velocity, player_acceleration
