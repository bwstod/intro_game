import pygame
import sys
import os

# from ..platform import Platform as p


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
import constants as c
import helper as h

from platform_1 import Platform as p




def main(): 
    pygame.init()

    txt_file = None

    mouse_position = pygame.Vector2(0, 0)
    mouse_hitbox = pygame.Rect(mouse_position.x, mouse_position.y, 1, 1)
    pygame.mouse.set_visible(False)

    start_bounding_box = 0
    bounding_box_1 = None
    # bounding_box_2 = None

    platform_bounding_rect = pygame.Rect(0,0,0,0)
    platform_list = []

    dt = 0

    platform_type = 1

    level_input = False
    level = "0"
    room_input = False
    room = "0"

    save = False

    screen = pygame.display.set_mode((c.SCREEN_WIDTH + 400, c.SCREEN_HEIGHT + 100), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_hitbox.centerx < c.SCREEN_WIDTH and mouse_hitbox.centery < c.SCREEN_HEIGHT:
                    if(start_bounding_box):
                        temp_platform = p(platform_bounding_rect.copy(), platform_type)
                        platform_list.append(temp_platform)
                    else:
                        bounding_box_1 = mouse_hitbox.center
                    start_bounding_box = (start_bounding_box + 1)%2
            if level_input:
                if event.type == pygame.KEYDOWN:
                    if event.key == 8:
                        level = level[:-1]
                    elif event.key == 13:
                        level_input = False
                        break
                    else:
                        level += event.unicode
            if room_input:
                if event.type == pygame.KEYDOWN:
                    if event.key == 8:
                        room = room[:-1]
                    elif event.key == 13:
                        room_input = False
                        break
                    else:
                        room += event.unicode


        screen.fill("black")
        pygame.draw.line(screen, "white", pygame.Vector2(c.SCREEN_WIDTH, 0), pygame.Vector2(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 3)
        pygame.draw.line(screen, "white", pygame.Vector2(0, c.SCREEN_HEIGHT), pygame.Vector2(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 3)

        #Buttons creation
        font = pygame.font.Font(None, 55)

        exit_button, exit_text = h.text_create(10, c.SCREEN_HEIGHT + 10, 100, 80, "Exit", "Black", font)
        save_button, save_text = h.text_create(150, c.SCREEN_HEIGHT + 10, 120, 80, "Save", "Black", font)
        clear_button, clear_text = h.text_create(300, c.SCREEN_HEIGHT + 10, 150, 80, "Clear", "Black", font)
        level_input_button, level_input_text = h.text_create(c.SCREEN_WIDTH - 150, c.SCREEN_HEIGHT + 10, 250, 80, "Level Input", "Black", font)
        room_input_button, room_input_text = h.text_create(c.SCREEN_WIDTH + 110, c.SCREEN_HEIGHT + 10, 250, 80, "Room Input", "Black", font)

        platform_button, platform_text = h.text_create(c.SCREEN_WIDTH + 10, 50, 380, 100, "Platform", c.PLATFORM_COLOR, font)
        danger_button, danger_text = h.text_create(c.SCREEN_WIDTH + 10, 200, 380, 100, "Danger", c.DANGER_COLOR, font)
        goal_button, goal_text = h.text_create(c.SCREEN_WIDTH + 10, 350, 380, 100, "Goal", c.GOAL_COLOR, font)
        start_button, start_text = h.text_create(c.SCREEN_WIDTH + 10, 500, 380, 100, "Start", c.START_COLOR, font)
        
        texts = [exit_text, save_text, clear_text, level_input_text, room_input_text, platform_text, danger_text, goal_text, start_text]
        colors = ["white"] * len(texts)
        buttons = [exit_button, save_button, clear_button, level_input_button, room_input_button, platform_button, danger_button, goal_button, start_button]
        text_offset_x = [10, 10, 10, 10, 10, 100, 100, 100, 100]
        text_offset_y = [25, 25, 25, 25, 25, 30, 30, 30, 30]

        colors[platform_type+4] = (255,192,150)
        colors[3] = (255,192,150) if level_input else "white"
        colors[4] = (255,192,150) if room_input else "white"

        level_button, level_text = h.text_create(500, c.SCREEN_HEIGHT + 10, 50, 50, "Level: " + level, "White", font)
        room_button, room_text = h.text_create(500, c.SCREEN_HEIGHT + 50, 50, 50, "Room: " + room, "White", font)
        h.text_render(["black", "black"], [level_button, room_button], [level_text, room_text], [0, 0], [0, 0], screen)


        for i, text_button in enumerate(buttons):
            if text_button.colliderect(mouse_hitbox):
                colors[i] = "pink"

                if(pygame.mouse.get_pressed(num_buttons=3)[0]):
                    if i == 0:
                        running = False
                    elif i == 1:
                        save = True
                    elif i == 2:
                        platform_list = []
                    elif i == 3:
                        level_input = True
                        room_input = False
                    elif i == 4:
                        level_input = False
                        room_input = True
                    else:
                        platform_type = i - 4
                            
                        
        h.text_render(colors, buttons, texts, text_offset_x, text_offset_y, screen)


        #Creating platforms
        
        if(start_bounding_box):
            left = bounding_box_1[0]
            top = bounding_box_1[1]
            temp_width = min(mouse_hitbox.centerx, c.SCREEN_WIDTH) - bounding_box_1[0]
            temp_height = min(mouse_hitbox.centery, c.SCREEN_HEIGHT) - bounding_box_1[1]

            if(temp_width < 0):
                left = bounding_box_1[0] + temp_width
                temp_width = -temp_width
            
            if(temp_height < 0):
                top = bounding_box_1[1] + temp_height
                temp_height = -temp_height

            platform_bounding_rect.update(left, top, temp_width, temp_height)
            pygame.draw.rect(screen, "white", platform_bounding_rect)

        
        for platform in platform_list:
            platform.draw_platform(screen)

        mouse_hitbox = h.mouse_handle(screen=screen, mouse_hitbox=mouse_hitbox, mouse_size=1) 

        if save:
            main_folder = "level_definitions"
            try:
                os.mkdir(main_folder+"/level-"+level)
                print("Created new Level folder, adding room file")
            except:
                print("Level Folder already exists, adding room file")
            file_name = main_folder+"/level-"+level+"/room-"+room+".txt"
            with open(file_name, 'w') as file:
                for platform in platform_list:
                    file.write(platform.text_output())

            running = False

        #Display and update clock
        pygame.display.flip()
        dt = clock.tick(60) / 1000


    pygame.quit()

    return txt_file

if __name__ == "__main__":
    room_definition = main()

    #turn txt to file?
    if room_definition:
        print("yay")
    else:
        print("none")