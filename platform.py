import pygame
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
import constants as c

class Platform:
    def __init__(self, rect, type):
        self.rect = rect
        self.type = type
        # self.screen = screen
        pass

    type_colors = {1: c.PLATFORM_COLOR, 2: c.DANGER_COLOR, 3: c.GOAL_COLOR, 4: c.START_COLOR}

    def draw_platform(self, screen):
        pygame.draw.rect(screen, self.type_colors[self.type], self.rect)

    def collide_platform(self, player_hitbox, player_position, player_velocity, player_acceleration):
        ground_level = c.SCREEN_HEIGHT
        if player_hitbox.bottom - 20 < self.rect.top and player_velocity.y >= 0:
            ground_level = self.rect.top +1
        elif player_hitbox.x < self.rect.left:
            player_velocity.x = 0
            player_acceleration.x = 0
            player_position.x = self.rect.left - c.PLAYER_SIZE
        elif player_hitbox.x < self.rect.right:
            player_velocity.x = 0
            player_acceleration.x = 0
            player_position.x = self.rect.right + c.PLAYER_SIZE

        # return ground_level, player_position, player_velocity, player_acceleration
        return ground_level

    
    def text_output(self):
        # output_string = ""

        left = self.rect.left
        top = self.rect.top
        width = self.rect.width
        height = self.rect.height

        output_string = str(left) + " " + str(top) + " " + str(width) + " " + str(height) + " " + str(self.type) + "\n"

        return output_string
    
