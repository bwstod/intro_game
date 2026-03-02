import pygame

import constants as c
import globals as g
import helper as h

class Player:
    def __init__(self, position, velocity, acceleration, hitbox):
        self.pos = position
        self.vel = velocity
        self.acc = acceleration
        self.hit = hitbox
        self.on_ground = True

        self.x_speed = c.SPEED

        self.size = c.PLAYER_SIZE



    def update_position(self):
        self.vel.x += self.acc.x * g.dt
        self.vel.y += self.acc.y * g.dt

        if self.vel.x > 500:
            self.vel.x = 500
            
        self.pos.x += self.pos.x * g.dt
        self.pos.y += self.pos.y * g.dt

        if self.pos.x < 0:
            self.pos.x = 0
        
        if self.pos.x > c.SCREEN_WIDTH:
            self.pos.x = c.SCREEN_WIDTH

    def input(self, keys):
        if self.on_ground:
            if keys[pygame.K_w]:
                self.vel.y += -400
        if keys[pygame.K_a]:
            self.acc.x += -self.x_speed
        if keys[pygame.K_d]:
            self.acc.x += self.x_speed

    def physics(self):
        self.acc.x = -self.vel.x*5

        jump = True

        if(self.pos.y < g.ground_level - self.size):
            self.acc.y = 1000
            jump = False
        else:
            self.acc.y = 0
            self.vel.y = 0
            self.pos.y = g.ground_level - self.size

        return jump
    
    def movement_handle(self):
        #TODO: UPDATE RECT_LIST TO BE GLOBAL
        rect_list = []
        for platform in g.platform_list:
            rect_list.append(platform.rect)

        collision_platforms = self.hit.collidelistall(rect_list)

        g.ground_level = c.SCREEN_HEIGHT

        if collision_platforms != -1:
            for collision_platform in collision_platforms:
                if g.platform_list[collision_platform].type == 2:
                    print("dead", self.pos)
                    self.pos, self.hit = h.reset_position()
                    
                if g.platform_list[collision_platform].type == 3:
                    print("new level", self.pos)
                    g.prev_level = g.level
                    g.prev_room = g.room
                    g.level = g.platform_list[collision_platform].level
                    g.room = g.platform_list[collision_platform].room
                    g.new_level = True
                    

                g.ground_level = g.platform_list[collision_platform].collide_platform(self.hit, self.pos, self.vel, self.acc)

        self.on_ground = self.physics(self.pos, self.vel, self.acc, g.ground_level)
        keys = pygame.key.get_pressed()
        self.player_input(keys)

        self.update_position()
        self.hit.update(self.pos.x - self.size, self.pos.y - self.size, self.size*2, self.size*2)

        # return player_hitbox, player_position, player_velocity, player_acceleration

