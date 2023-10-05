from math import trunc
import sys
import pygame
import random
pygame.init()

# results: 
# 646, 607, 778, 754, 1355, 872, 822, 1030, 645, 854

# display setup and font parameters
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Button Latency Test")
font = pygame.font.SysFont("Times new Roman", 28)
c_black = pygame.Color("black")
c_green = pygame.Color("green")
c_red = pygame.Color("red")
c_white = pygame.Color("white")
center = screen.get_rect().center

# display messages
start_text = font.render("WORD LATENCY: PRESS ANY BUTTON", 0, c_black)
continue_text = font.render("Interaction",0,c_green)
waiting_text = font.render("Get Ready...",0,c_red)
word_list = ["Achievement", "Appreciated", "Belligerent", "Calculation", "Development", "Examination", "Flourishing", "Interaction"]

# time parameters
get_prev = None
get_avg = None
get_total = None
get_words = None
initial_time = 0
average_time = 0

# initial loop parameters
current_state = "start_state"
num_tested = 0
testing = True
times = []
four_words = []
words_string = ""

# main loop 
while testing:
    # get initial iteration time in milliseconds
    current_time = pygame.time.get_ticks()

    # handle events
    for event in pygame.event.get():
        # if red x on the window tab is pressed
        if event.type == pygame.QUIT:
            testing = False
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        # if a key is pressed 
        if event.type == pygame.KEYDOWN:
            # exits app when esc key is pressed 
            if event.key == pygame.K_ESCAPE:
                testing = False
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            
            if event.key == pygame.K_RIGHT and current_state == "reaction_state":
                reaction_time = (current_time - initial_time) / 1000
                flag = False
                for i in range(4):
                    if four_words[i] == "Interaction":
                        flag = True
                if flag == True:
                    num_tested += 1
                    times.append(reaction_time*1000)
                get_total = font.render(f"Total Test(s): {num_tested}", 0, c_black)
                initial_time = current_time + random.randint(1000, 2500) # generate random wait times
                current_state = "wait_state" 

            if event.key == pygame.K_LEFT and current_state == "reaction_state":
                reaction_time = (current_time - initial_time) / 1000
                flag = False
                for i in range(4):
                    if four_words[i] == "Interaction":
                        flag = True
                if flag == False:
                    num_tested += 1
                    times.append(reaction_time*1000)
                get_total = font.render(f"Total Test(s): {num_tested}", 0, c_black)
                initial_time = current_time + random.randint(1000, 3000) # generate random wait times
                current_state = "wait_state" 

            # changes state from start to wait when any key is pressed
            if num_tested >= 10:
                testing = False
                for i in range(10):
                    print(f"{trunc(times[i])}", end=", ")
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if current_state == "start_state":
                current_state = "wait_state" 
                initial_time = current_time + random.randint(1000, 3000) # generate random wait times

    if current_state == "wait_state":
        if current_time >= initial_time:
            current_state = "reaction_state"  
            four_words = random.sample(word_list, 4)
            words_string = " | ".join(four_words)
            get_words = font.render(words_string, 0, c_black)
    
    # sets the canvas to background white
    screen.fill(c_white)

    # Start State
    if current_state == "start_state":
        pygame.draw.rect(screen, c_black, (0, 0, 700, 500), 0)
        pygame.draw.rect(screen, c_white, (25, 25, 650, 450), 0)
        screen.blit(start_text, start_text.get_rect(center = center))
    # On Hold State
    if current_state == "wait_state":
        pygame.draw.rect(screen, c_red, (0, 0, 700, 500), 0)
        pygame.draw.rect(screen, c_white, (25, 25, 650, 450), 0)
        screen.blit(waiting_text, waiting_text.get_rect(center = center))
        if get_prev:
            screen.blit(get_prev, get_prev.get_rect(center = (center[0], 350)))
        if get_avg:
            screen.blit(get_avg, get_avg.get_rect(center = (center[0], 400)))
        if get_total:
            screen.blit(get_total, get_total.get_rect(center = (center[0], 450)))

    if current_state == "reaction_state":
        pygame.draw.rect(screen, c_green, (0, 0, 700, 500), 0)
        pygame.draw.rect(screen, c_white, (25, 25, 650, 450), 0)
        screen.blit(continue_text, continue_text.get_rect(center = center))
        if get_prev:
            screen.blit(get_prev, get_prev.get_rect(center = (center[0], 350)))
        if get_avg:
            screen.blit(get_avg, get_avg.get_rect(center = (center[0], 400)))
        if get_total:
            screen.blit(get_total, get_total.get_rect(center = (center[0], 450)))
        if get_words:
            screen.blit(get_words, get_words.get_rect(center = (center[0], 200)))

    pygame.display.flip()