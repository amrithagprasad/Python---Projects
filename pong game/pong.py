import pygame
import sys
import random

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.x = screen_width/2 - 10
    ball.y = random.randint(10, 100)
    ball_speed_x *= random.choice([-1, 1])
    ball_speed_y *= random.choice([-1, 1])


def point_won(winner):
    global cpu_points, player_points

    if winner == "cpu":
        cpu_points += 1
    if winner == "player":
        player_points += 1

    reset_ball()

def animate_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.bottom >= screen_height or ball.top <= 0: #checking if the bottom of the ball rectangle is more than or equal to the screen height. Similarly for top
        ball_speed_y *= -1 #changing direction of the ball in vertical axis

    if ball.right >= screen_width:
        point_won("cpu")
    if ball.left <= 0:
        point_won("player")

    #ball collisions
    if ball.colliderect(player) or ball.colliderect(cpu):
        ball_speed_x *= -1

def animate_player():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def animate_cpu():
    #for this a simple AI algorithm has been used.
    #Check if the center y of the ball is above the center y  of the paddle.
    #If it is, we move it up, else we move it down. 

    global cpu_speed
    cpu.y += cpu_speed

    if ball.centery <= cpu.centery:
        cpu_speed = -6
    if ball.centery >= cpu.centery:
        cpu_speed = 6

    #collisions
    if cpu.top <= 0:
        cpu.top = 0
    if cpu.bottom >= screen_height:
        cpu.bottom = screen_height

pygame.init()

screen_width = 1280
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

ball = pygame.Rect(0, 0, 30, 30)
ball.center = (screen_width/2, screen_height/2)

cpu = pygame.Rect(0, 0, 20, 100)
cpu.centery = screen_height/2

player = pygame.Rect(0, 0 ,20, 100)
player.midright = (screen_width, screen_height/2)

ball_speed_x = 6
ball_speed_y = 6
player_speed = 0
cpu_speed = 6

cpu_points, player_points = 0, 0

score_font = pygame.font.Font(None, 100) #font family and size

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: #keydown means a player has pressed a key
            if event.key == pygame.K_UP: #using the event.key attribute to check which key was pressed
                player_speed = -6 #the speed is negative as we need to move the paddle up
            if event.key == pygame.K_DOWN: #using the event.key attribute to check which key was pressed
                player_speed = 6 #the speed is positive as we need to move the paddle down
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: #K_UP means the key has been released and is not being pressed anymore
                player_speed = 0 #resetting the player speed to zero
            if event.key == pygame.K_DOWN: 
                player_speed = 0
            

    animate_ball()
    animate_player()
    animate_cpu()
    
    

    screen.fill('black')

    cpu_score_surface = score_font.render(str(cpu_points), True, "white")
    player_score_surface = score_font.render(str(player_points), True, "white")
    screen.blit(cpu_score_surface, (screen_width/4, 20))
    screen.blit(player_score_surface, (3*screen_width/4, 20))
    #blit - block image transfer

    pygame.draw.aaline(screen, 'white', (screen_width/2, 0), (screen_width/2, screen_height))
    pygame.draw.ellipse(screen, 'white', ball)
    pygame.draw.rect(screen, 'red', cpu)
    pygame.draw.rect(screen, 'blue', player)

    pygame.display.update()
    clock.tick(60)
