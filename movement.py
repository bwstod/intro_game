import pygame
import pygame._sdl2.video as video

print( "hello")

pygame.init()

#Setup Variables
screen_width = 1280
screen_height = 720
speed = 1500
player_size = 20
# player_disabled = 0
# stun_time = 30

font = pygame.font.Font(None, 55)

#Runtime Variables
level = 0
player_position = pygame.Vector2(screen_width/2, 0)
player_velocity = pygame.Vector2(0, 0)
player_acceleration = pygame.Vector2(0, 0)
player_hitbox = pygame.Rect(player_position.x, player_position.y, player_size, player_size)

ground_level = screen_height
on_ground = True

mouse_size = 10
mouse_position = pygame.Vector2(0, 0)
mouse_hitbox = pygame.Rect(mouse_position.x, mouse_position.y, mouse_size, mouse_size)
pygame.mouse.set_visible(False)


dt = 0

menu_open = 0

#Setup
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

#Takes in key presses
def player_input(player_vel, player_acc, keys, on_ground):
    # pygame.key.set_repeat()
    if on_ground:
        if keys[pygame.K_w]:
            player_vel.y += -400
    if keys[pygame.K_a]:
        player_acc.x += -speed 
    if keys[pygame.K_d]:
        player_acc.x += speed
        
#Defines "friction" and "gravity"
def physics(player_pos, player_vel, player_acc, ground_level):
    player_acc.x = -player_vel.x*5

    jump = True

    if(player_pos.y < ground_level - player_size):
        player_acc.y = 1000
        jump = False
    else:
        player_acc.y = 0
        player_vel.y = 0
        player_pos.y = ground_level - player_size

    return jump

#Updates player position on screen
def update_position(player_pos, player_vel, player_acc):
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
    
    if player_pos.x > screen_width:
        player_pos.x = screen_width

#Generates platforms (per room?)
def generate_platforms(room_id):
    platform_list = []
    for i in range(3):
        platform_list.append(pygame.Rect(screen_width/(i+1)- 50, screen_height-50, 50, 50))
    for rect in platform_list:
        pygame.draw.rect(screen, "cyan", rect)
    return platform_list

#Collision detection with platform objects
def platform_handling(collision_rect, player_hitbox, player_position, player_velocity, player_acceleration, rect_list):
    ground_level = screen_height
    if collision_rect != -1:
        platform = rect_list[collision_rect]

        if player_hitbox.bottom - 20 < platform.top and player_velocity.y >= 0:
            ground_level = platform.top +1
            # ground_level = player_hitbox.bottom
        elif player_hitbox.x < platform.left:
            # print("player bot: ", player_hitbox.bottom, ", box top: ", rect_list[collision_rect].top, ", box right: ", rect_list[collision_rect].right)

            player_velocity.x = 0
            player_acceleration.x = 0
            player_position.x = platform.left - player_size
        elif player_hitbox.x < platform.right:
            # print("player bot: ", player_hitbox.bottom, ", box top: ", rect_list[collision_rect].top, ", box right: ", rect_list[collision_rect].right)

            player_velocity.x = 0
            player_acceleration.x = 0
            player_position.x = platform.right + player_size
        
    return ground_level


def text_create(x, y, w, h, text, text_color):
    button = pygame.Rect(x, y, w, h)
    text_surf = font.render(text, True, text_color)

    return button, text_surf

def text_render(colors, buttons, text_surfs, text_offset_x, text_offset_y):
    for i, button in enumerate(buttons):
        pygame.draw.rect(screen, colors[i], button)
        screen.blit(text_surfs[i], (button.x + text_offset_x[i], button.y + text_offset_y[i]))


#Main Runtime loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == 27:
            menu_open = (menu_open+1)%2
        if event.type == pygame.QUIT:
            running = False

    #Background
    screen.fill("black")

    if level == 0:
        play_color = "white"
        play_button, play_text = text_create(screen_width/2-200, screen_height/2 - 100, 400, 50, "Play!", "Black")

        if(play_button.colliderect(mouse_hitbox)):
            play_color = "pink"
            if(pygame.mouse.get_pressed(num_buttons=3)[0]):
                level = 1

                #restart game
                player_position = pygame.Vector2(screen_width/2, 0)
                player_velocity = pygame.Vector2(0, 0)
                player_acceleration = pygame.Vector2(0, 0)
                player_hitbox = pygame.Rect(player_position.x, player_position.y, player_size, player_size)

        text_render([play_color], [play_button], [play_text], [100], [5])

        #Mouse handling
        mouse_position = pygame.mouse.get_pos()
        mouse_hitbox.update(mouse_position[0] - mouse_size, mouse_position[1] - mouse_size, mouse_size*2, mouse_size*2)
        pygame.draw.rect(screen, "red", mouse_hitbox)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        continue

    #Platform handling
    platform_list = generate_platforms(1)

    collision_platform = player_hitbox.collidelist(platform_list)
    ground_level = platform_handling(collision_platform, player_hitbox, player_position, player_velocity, player_acceleration, platform_list)

    #Draw player
    pygame.draw.circle(screen, "white", player_position, player_size)

    

    if menu_open:
        continue_color = "white"
        continue_button, continue_text = text_create(screen_width/2 - 200, screen_height/2 - 100, 400, 50, "Continue", "Black")
        if(continue_button.colliderect(mouse_hitbox)):
            continue_color = "pink"
            if(pygame.mouse.get_pressed(num_buttons=3)[0]):
                menu_open = (menu_open+1)%2
        
        main_menu_color = "white"
        main_menu_button, main_menu_text = text_create(screen_width/2 - 200, screen_height/2, 400, 50, "Menu", "Black")
        if(main_menu_button.colliderect(mouse_hitbox)):
            main_menu_color = "pink"
            if(pygame.mouse.get_pressed(num_buttons=3)[0]):
                level = 0
                menu_open = (menu_open+1)%2

        quit_color = "white"
        quit_button, quit_text = text_create(screen_width/2 - 200, screen_height/2 + 100, 400, 50, "Quit", "Black")
        if(quit_button.colliderect(mouse_hitbox)):
            quit_color = "pink"
            if(pygame.mouse.get_pressed(num_buttons=3)[0]):
                break

        esc_menu_buttons = [continue_button, main_menu_button, quit_button]
        esc_menu_texts = [continue_text, main_menu_text, quit_text]
        esc_menu_colors = [continue_color, main_menu_color, quit_color]
        esc_menu_text_x = [100, 150, 150]
        esc_menu_text_y = [5, 5, 5]
        text_render(esc_menu_colors, esc_menu_buttons, esc_menu_texts, esc_menu_text_x, esc_menu_text_y)
        
        #Mouse handling
        mouse_position = pygame.mouse.get_pos()
        mouse_hitbox.update(mouse_position[0] - mouse_size, mouse_position[1] - mouse_size, mouse_size*2, mouse_size*2)
        pygame.draw.rect(screen, "red", mouse_hitbox)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        continue


    #Main gameplay loop
    on_ground = physics(player_position, player_velocity, player_acceleration, ground_level)
    keys = pygame.key.get_pressed()
    player_input(player_velocity, player_acceleration, keys, on_ground)

    update_position(player_position, player_velocity, player_acceleration)
    player_hitbox.update(player_position.x - player_size, player_position.y - player_size, player_size*2, player_size*2)

    

    #Display and update clock
    pygame.display.flip()
    dt = clock.tick(60) / 1000


pygame.quit()