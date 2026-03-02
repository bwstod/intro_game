import pygame
import pygame._sdl2.video as video
import helper as h
import constants as c
import globals as g

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
def update_position(player_pos, player_vel, player_acc):
    player_vel.x += player_acc.x * g.dt
    player_vel.y += player_acc.y * g.dt

    if player_vel.x > 500:
        player_vel.x = 500
        
    player_pos.x += player_vel.x * g.dt
    player_pos.y += player_vel.y * g.dt

    if player_pos.x < 0:
        player_pos.x = 0
    
    if player_pos.x > c.SCREEN_WIDTH:
        player_pos.x = c.SCREEN_WIDTH

def movement_handling(player_hitbox, player_position, player_velocity, player_acceleration):
    rect_list = []
    for platform in g.platform_list:
        rect_list.append(platform.rect)

    collision_platforms = player_hitbox.collidelistall(rect_list)

    ground_level = c.SCREEN_HEIGHT

    if collision_platforms != -1:
        for collision_platform in collision_platforms:
            if g.platform_list[collision_platform].type == 2:
                print("dead", player_position)
                player_position, player_hitbox = h.reset_position()
                
            if g.platform_list[collision_platform].type == 3:
                print("new level", player_position)
                g.prev_level = g.level
                g.prev_room = g.room
                g.level = g.platform_list[collision_platform].level
                g.room = g.platform_list[collision_platform].room
                g.new_level = True
                

            ground_level = g.platform_list[collision_platform].collide_platform(player_hitbox, player_position, player_velocity, player_acceleration)

    on_ground = physics(player_position, player_velocity, player_acceleration, ground_level)
    keys = pygame.key.get_pressed()
    player_input(player_velocity, player_acceleration, keys, on_ground)

    update_position(player_position, player_velocity, player_acceleration)
    player_hitbox.update(player_position.x - c.PLAYER_SIZE, player_position.y - c.PLAYER_SIZE, c.PLAYER_SIZE*2, c.PLAYER_SIZE*2)

    return player_hitbox, player_position, player_velocity, player_acceleration
