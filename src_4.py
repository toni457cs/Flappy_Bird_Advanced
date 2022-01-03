
import pygame, sys, random, time
pygame.init()

#set screen size and game speed
screen = pygame.display.set_mode((800,700))
game_speed = pygame.time.Clock()

bird_fly_up = 0 #0

#This helps with making the opening message disappear after the first time the space bar is hit.
space_hit = False

#set background photo
background_img = pygame.image.load('background.png')
background_img = pygame.transform.scale(background_img, (800, 700))

#set opening image
opening_logo = pygame.image.load('game_logo.png')
start_message = pygame.image.load('get_ready.png')
start_message = pygame.transform.scale(start_message, (300,150))
   
#set death floor
death_floor = pygame.image.load('floor.png')
death_floor = pygame.transform.scale(death_floor, (800, 300))

class pipes:
    pipe = pygame.image.load('single_pipe_up.png')
    pipe = pygame.transform.scale(pipe, (100,500))
    pipe_x_value1 = 800 
    pipe_x_value2 = 1200 
    pipe_x_value3 = 1600
    pipe_up_y1 = 450
    pipe_up_y2 = 550
    pipe_up_y3 = 350
    pipe_down_y1 = -300
    pipe_down_y2 = -200
    pipe_down_y3 = -400
    pipe_up = pipe
    pipe_down = pygame.transform.rotate(pipe, 180)
    
    def __init__(self, pipes):
        self.pipes = pipes

    def print_pipe1():
        pipes.pipe_x_value1 -= 0.2
        pipe_up1 = screen.blit(pipes.pipe_up,(pipes.pipe_x_value1,pipes.pipe_up_y1)) #500,450
        pipe_down1 = screen.blit(pipes.pipe_down,(pipes.pipe_x_value1,pipes.pipe_down_y1)) #500,-300

    def print_pipe2():
        pipes.pipe_x_value2 -= 0.2
        # print(pipes.pipe_x_value2)
        pipe_up2 = screen.blit(pipes.pipe_up,(pipes.pipe_x_value2,pipes.pipe_up_y2)) #300,550
        pipe_down2 = screen.blit(pipes.pipe_down,(pipes.pipe_x_value2,pipes.pipe_down_y2)) #300,-200
    
    def print_pipe3():
        pipes.pipe_x_value3 -= 0.2
        pipe_up3 = screen.blit(pipes.pipe_up, (pipes.pipe_x_value3, pipes.pipe_up_y3))
        pipe_down3 = screen.blit(pipes.pipe_down, (pipes.pipe_x_value3, pipes.pipe_down_y3))
    

class bird:       
    bird_x_value = 400
    bird_y_value = 400
    gravity = 0.6 #0.6
    bird = pygame.image.load('flappy_bird_img_yellow.png')
    bird = pygame.transform.scale(bird, (50,50))

    def __init__(self, bird):
        self.bird = bird

class collision:
    # if the bird hits the floor, display "Game Over", display the score - end game
    #same for pipes
    #this ends the game if the bird hits the floor
    def quit():
        black = (0, 0, 0)
        t_end = time.time() + 5
        while time.time() < t_end:
            game_over = screen.blit(game_end.game_over, (200, 200))
            myFont = pygame.font.SysFont("Arial", 64)
            scoreDisplay = myFont.render("Score:" + str(scoreboard.points), 1, black)
            screen.blit(scoreDisplay, (250, 400))
            pygame.display.flip()
        pygame.quit() #ends game, closes screen
    
    def floor_collision():
        if bird.bird_y_value >= 550:
            collision.quit()

    def pipe_collision(): #if things are normal
        #pipe up 1
        if pipes.pipe_x_value1 <= 450 and pipes.pipe_x_value1 >= 400:
            if bird.bird_y_value >= 900:
                # print("Detected")
                collision.quit()

        #pipe down 1
        if pipes.pipe_x_value1 <= 450 and pipes.pipe_x_value1 >= 400:
            if bird.bird_y_value <= 0:
                # print("Detected")
                collision.quit()
        
        #pipe up 2
        if pipes.pipe_x_value2 <= 450 and pipes.pipe_x_value2 >= 400:
            if bird.bird_y_value >= 550:
                # print("Detected")
                collision.quit()

        #pipe down 2
        if pipes.pipe_x_value2 <= 450 and pipes.pipe_x_value2 >= 400:
            if bird.bird_y_value <= 300:
                # print("Detected")
                collision.quit()

        #pipe up 3
        if pipes.pipe_x_value3 <= 450 and pipes.pipe_x_value3 >= 400:
            if bird.bird_y_value >= 350:
                # print("Detected")
                collision.quit()

        #pipe down 3
        if pipes.pipe_x_value3 <= 450 and pipes.pipe_x_value3 >= 400:
            if bird.bird_y_value <= 100:
                # print("Detected")
                collision.quit()

class scoreboard:
    points = 0
    points_incr = 1
    def incr_points():
        scoreboard.points += scoreboard.points_incr

    def counter():
        if pipes.pipe_x_value1 <= 425.2 and pipes.pipe_x_value1 >= 425:
            if bird.bird_y_value > pipes.pipe_down_y1:
                scoreboard.incr_points()
                print(scoreboard.points)

        if pipes.pipe_x_value2 <= 400.2 and pipes.pipe_x_value2 >= 400:
            if bird.bird_y_value > pipes.pipe_down_y2:
                scoreboard.incr_points()
                print(scoreboard.points)

        if pipes.pipe_x_value3 <= 450.2 and pipes.pipe_x_value3 >= 450:
            if bird.bird_y_value > pipes.pipe_down_y3:
                scoreboard.incr_points()
                print(scoreboard.points)

class game_end:
    game_over = pygame.image.load('game_over.jpg')
    game_over = pygame.transform.scale(game_over, (300, 150))
                
class power_up:
    good_fruit = pygame.image.load('red_apple.png')
    gf_x_value = 0 #2000 #pipes.pipe_x_value5
    gf_y_value =  400
    good_fruit = pygame.transform.scale(good_fruit,(75,75))
    power_up_time = time.time() + 15

    def print_good_fruit():
        power_up.gf_x_value -= 0.2
        # if power_up.gf_x_value <= 450 and power_up.gf_x_value >= 400:
        screen.blit(power_up.good_fruit, (power_up.gf_x_value, power_up.gf_y_value))

    def power_set():
        #reset pipes
        pipes.pipe_up_y1 = 550
        pipes.pipe_up_y2 = 550
        pipes.pipe_up_y3 = 550
        pipes.pipe_down_y1 = -200
        pipes.pipe_down_y2 = -200
        pipes.pipe_down_y3 = -200

    def activate_power_up():
        if power_up.gf_x_value <= 450 and power_up.gf_x_value >= 400:
            if bird.bird_y_value <= 450 and bird.bird_y_value >= 400:
                print("here")
                power_up.power_set()

        if pipes.pipe_x_value3 >= 2400:
            pipes.pipe_up_y1 = 450
            pipes.pipe_up_y2 = 550
            pipes.pipe_up_y3 = 350
            pipes.pipe_down_y1 = -300
            pipes.pipe_down_y2 = -200
            pipes.pipe_down_y3 = -400

class obstacle:
    bad_fruit = pygame.image.load('rotten_fruit.jpg')
    bad_fruit = pygame.transform.scale(bad_fruit, (75,75))
    bad_fruit_x_value = 2400
    bad_fruit_y_value = 400
    rotation = 0

    def launch_bad_fruit():
        obstacle.bad_fruit_x_value -= 0.4
        display_bad_fruit = screen.blit(obstacle.bad_fruit, (obstacle.bad_fruit_x_value, obstacle.bad_fruit_y_value))
        
    def poisoned():
        if obstacle.bad_fruit_x_value <= 450 and obstacle.bad_fruit_x_value >= 400:
            if bird.bird_y_value <= 450 and bird.bird_y_value >= 400:
                print("poisoned!!!!")
                pipes.pipe_up_y1 -= 0.5
                if pipes.pipe_up_y1 <= 300:
                    pipes.pipe_up_y1 += 0.5
                if pipes.pipe_up_y1 == 450:
                    pipes.pipe_up_y1 -= 0.5
                pipes.pipe_up_y2 -= 0.5
                if pipes.pipe_up_y2 <= 400:
                    pipes.pipe_up_y2 += 0.5
                if pipes.pipe_up_y2 == 550:
                    pipes.pipe_up_y2 -= 0.5
                pipes.pipe_up_y3 -= 0.5
                if pipes.pipe_up_y3 <= 200:
                    pipes.pipe_up_y3 += 0.5
                if pipes.pipe_up_y3 == 350:
                    pipes.pipe_up_y3 -= 0.5
                
                pipes.pipe_down_y1 -= 0.5
                if pipes.pipe_down_y1 <= -300:
                    pipes.pipe_down_y1 += 0.5
                if pipes.pipe_down_y1 == -450:
                    pipes.pipe_down_y1 -= 0.5
                pipes.pipe_down_y2 -= 0.5
                if pipes.pipe_down_y2 <= -200:
                    pipes.pipe_down_y2 += 0.5
                if pipes.pipe_down_y2 == -350:
                    pipes.pipe_down_y2 -= 0.5
                pipes.pipe_down_y3 -= 0.5
                if pipes.pipe_down_y3 <= -400:
                    pipes.pipe_down_y3 += 0.5
                if pipes.pipe_down_y3 == -550:
                    pipes.pipe_down_y3 -= 0.5
            if pipes.pipe_x_value3 >= 2400:
                pipes.pipe_up_y1 = 450
                pipes.pipe_up_y2 = 550
                pipes.pipe_up_y3 = 350
                pipes.pipe_down_y1 = -300
                pipes.pipe_down_y2 = -200
                pipes.pipe_down_y3 = -400
while True:
    #set background using info from above
    screen.blit(background_img, (0,-40))

    #set death_floor on screen
    screen.blit(death_floor,(0,600))

    #set start message
    if not space_hit:
        screen.blit(opening_logo,(200,200))
        screen.blit(start_message, (200,300))

    #set good fruit
    power_up.print_good_fruit()
    if not power_up.gf_x_value > -100:
        power_up.gf_x_value = 800
        power_up.print_good_fruit()
    power_up.activate_power_up()

    # set imposter
    obstacle.launch_bad_fruit()

    if not obstacle.bad_fruit_x_value > -100:
        obstacle.bad_fruit_x_value = 2500
        obstacle.launch_bad_fruit() 
    obstacle.poisoned()

    #set pipes
    pipes.print_pipe1()
    pipes.print_pipe2()
    pipes.print_pipe3()

    #set pipe collision
    collision.pipe_collision()

    #set pipe game loop
    if not pipes.pipe_x_value1 > -100:
        pipes.pipe_x_value1 = 800
        pipes.print_pipe1()
    if not pipes.pipe_x_value2 > -100:
        pipes.pipe_x_value2 = 800
        pipes.print_pipe2()
    if not pipes.pipe_x_value3 > -100:
        pipes.pipe_x_value3 = 800
        pipes.print_pipe3()

    #set bird
    bird.bird_y_value += bird.gravity
    screen.blit(bird.bird,(bird.bird_x_value, bird.bird_y_value))

    if bird_fly_up > 200: #200
        # bird_fly_up = 0 #0
        bird.gravity = 0.2 # 0.2
    else:
        bird_fly_up += 0.8 #0.8

    #set counter
    scoreboard.counter()

    #set floor collision
    if collision.floor_collision() == True:
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(), sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                space_hit = True
                bird.gravity = -0.2 #-1
                bird_fly_up = 0

    # print(bird.bird_y_value)
    screen.blit(bird.bird,(bird.bird_x_value, bird.bird_y_value))
    
    #this keeps the game running - essential, game breaker if removed
    pygame.display.update()
    time.sleep(0.001) #timer to ensure flap consistency




        



