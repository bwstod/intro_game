import pygame

print( "hello")

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_vel = pygame.Vector2(0, 0)
player_acc = pygame.Vector2(0, 0)

speed = 7000

player_size = 20

dt = 0

player_disabled = 0
stun_time = 30

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    


    pygame.draw.circle(screen, "white", player_pos, player_size)    
    
    player_acc.x = -player_vel.x*5
    player_acc.y = -player_vel.y*5

    keys = pygame.key.get_pressed()
    if player_disabled == 0:
        if keys[pygame.K_w]:
            player_acc.y += -speed 
        if keys[pygame.K_s]:
            player_acc.y += speed 
        if keys[pygame.K_a]:
            player_acc.x += -speed 
        if keys[pygame.K_d]:
            player_acc.x += speed
    else:
        player_disabled -= 1

    if player_pos.x < player_size or player_pos.x > screen.get_width() - player_size:
        player_vel.x = -player_vel.x
        player_disabled = stun_time
    if player_pos.y < player_size or player_pos.y > screen.get_height() - player_size:
        player_vel.y = -player_vel.y
        player_disabled = stun_time

    # if abs(player_vel.x) > 0:
    #     player_vel.x += -1
    # else:
    #     player_vel.x = 0

    # if player_vel.y > 0:
    #     player_acc.y += -3
    # else: 
    #     player_acc.y = 0

    player_vel.x += player_acc.x * dt
    player_vel.y += player_acc.y * dt
        

    player_pos.x += player_vel.x * dt
    player_pos.y += player_vel.y * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000


pygame.quit()