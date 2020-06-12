
##############################################################################################################################

#### don't ask me why i use so weird variables :) :)
#
#
# enjoy
# by @hakim.kim77

import pygame
import time
import random


pygame.init()

# Variables

gv = False

width = 800
height = 600

x1 = 50
y1 = 500

x = random.randint(1, 100)
y = 0

x2 = random.randint(1, 100)
y2 = 0

rs = random.randint(5, 30)
rs2 = random.randint(5, 30)

e_x = 800
e_y = 500
e2_x = 700
e2_y = 500

b_x = 0
b_y = 500
b_s = 40

X = 580
Y = 550

b2_x = 0
b2_y = 50

clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (47, 141, 255)
blue1 = (0, 0, 255)
green = (0, 255, 0)
gray1 = (192, 192, 192)
yellow = (255, 255, 50)
gray = (128, 128, 128)

play = False

mc = False

cod = 1
cod2 = 1
cod3 = 1
cod4 = 1

state = "ready"
state2 = "ready"

e_lives = 10
e2_lives = 10

health = 50

col = gray1

mw = False

playa = False
mdc = False

cood = 1

mod = 1
mod2 = 1

wn = pygame.display.set_mode((width, height))
pygame.display.set_caption("Adventure Game")

font = pygame.font.SysFont(None, 60)
fontt = pygame.font.SysFont(None, 20)


# image load

background = pygame.image.load("background.png")
Key = pygame.image.load("key.png")
b = pygame.image.load("bullet1.png")
icon = pygame.image.load("key2.png")
pygame.mixer.music.load("m.mp3")


pygame.display.set_icon(icon)

# messages

def message(msg, color):
    txt = font.render(msg, True, color)
    wn.blit(txt, [320, 300])

def mess(m, color):
    t = font.render(m + str(health), True, color)
    wn.blit(t, [250, 40])

def m(msg, color):
    txt = font.render(msg, True, color)
    wn.blit(txt, [300, 300])

def m2(msg, color):
    txt = font.render(msg, True, color)
    wn.blit(txt, [300, 300])

def help1(msg, color):
    txt = fontt.render(msg, True, color)
    wn.blit(txt, [10, 500])
    

# firing

def fire(x, y):
    global state
    state = "fire"
    wn.blit(b, (x + 16, y + 10))

def fire2(x, y):
    global state2
    state2 = "fire"
    wn.blit(b2, (x + 16, y + 10))
    
# win menu

def win_menu():
    global mw
    global gv
    global play
    
    while not mw:
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                m = True
                gv = True
                play = False
               

        wn.fill(white)
        m2("You WON!", green)

        pygame.display.update()
        

# die menu

def die_menu():
    global play
    global mdc
    global health
    global gv
    
    while not mdc:
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                mdc = True
                gv = True
                play = False
        



        wn.fill(gray1)
        m("You Lost!", red)
      

        pygame.display.update()
        
# menu

def menu():
    global play
    global mc
    global col
    while not mc:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mc = True
                play = False
        
            Mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and 300 + 150 > Mouse[0] > 300 and 280 + 80 > Mouse[1] > 280:    
                pygame.mixer.music.play(0)       
                play = True
                mc = True
                
        if 300 + 150 > Mouse[0] > 300 and 280 + 80 > Mouse[1] > 280:
            col = gray
        else:
            col = gray1
        
              
        wn.fill(blue)
        pygame.draw.rect(wn, col, [300, 280, 150 ,80])
        message("PLAY", red)
        help1("move with d and a , space to kill red blocks and avoid reds from the sky once you finish go and get the key", white)

        pygame.display.update()
        
    
# run function

def run():
    global gv
    global x1
    global y1
    global x2
    global y2
    global cod
    global state
    global state2
    global b_x
    global b_y
    global b_s
    global e_x
    global e_y
    global e2_x
    global e2_y
    global cod2
    global cod3
    global cood
    global X
    global Y
    global cod4
    global e_lives
    global e2_lives
    global health
    global play
    global b2_x
    global b2_y
    global x
    global y
    global rs
    global rs2
    global mod
    global mod2

    while not gv:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gv = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and state != "fire":
                    b_x = x1
                    fire(b_x, y1)
                    
        wn.blit(background, (0, 0))
        pygame.draw.rect(wn, blue, [x1, y1, 40, 40])
        pygame.draw.rect(wn, red, [e_x, e_y, 30, 30])
        pygame.draw.rect(wn, red, [e2_x, e2_y, 30, 30])
        pygame.draw.rect(wn, black, [X, Y, 80, 20])
        pygame.draw.rect(wn, red, [x, y, 30, 30])
        pygame.draw.rect(wn, red, [x2, y2, 30, 30])
        wn.blit(Key, (600, 30))
        
        # player movement

        key = pygame.key.get_pressed()
        if key[pygame.K_d] and x1 + 40 < 799: x1 += 10
        if key[pygame.K_a] and x1 + 5 > 0: x1 += -10

        # enemies mouvenment

        if cod2 < 2:
            e_x += -15
            if e_x >= 0 and (x1 <= e_x and x1 >= e_x + 30 or x1 + 40 > e_x + 30):
                health += -25
                cod2 += 1
            if cod2 == 2:
                e_x = 800
                cod2 += -1

        if cod3 < 2:
            e2_x += -15
            if e2_x >= 0 and (x1 <= e2_x and x1 >= e2_x + 30 or x1 + 40 > e2_x + 30):
                health += -25
                cod3 += 1
            if cod3 == 2:
                e2_x = 700
                cod3 += -1

        # platform movement

        if cod4 < 2:
            Y += -8
            if Y <= 20:
                cod4 += 1
        if cod4 == 2:
            Y += 8
            if Y >= 550:
                cod4 += 3
        if cod4 == 5:
            if Y >= y1 and Y <= y1 + 40 or Y + 20 >= y1 and Y + 20 < y1 + 40:
                if x1 >= X and x1 <= X + 80 or x1 + 40 >= X and x1 + 40 < X + 80:
                    y1 += -8
                    Y += -8
                    if Y <= 50 and y1 <= 50:
                        cod4 += -4
            else:
                Y += -8
                if Y <= 50:
                    cod4 += -4
            
                
        # bullet movement

        if b_x >= width:
            b_x = x1
            state = "ready"
        if state == "fire":
            fire(b_x, y1)
            b_x += b_s

        # enm2 movement

        if mod < 2:
            y += rs
            if y >= height:
                mod += 1
        if mod == 2:
            x = random.randint(1, 100)
            y = 0
            mod += -1

        if mod2 < 2:
            y2 += rs2
            if y2 >= height:
                mod2 += 1
        if mod2 == 2:
            x2 = random.randint(1, 100)
            y2 = 0
            mod2 += -1

        # collisions checking

        if y >= y1 and y <= y1 + 40 or y + 30 >= y1 and y + 30 < y1 + 40:
            if x >= x1 and x <= x1 + 40 or x + 30 >= x1 and x + 30 < x1 + 40:
                x = random.randint(1, 100)
                y = 0
                health += -10

        if y2 >= y1 and y2 <= y1 + 40 or y2 + 30 >= y1 and y2 + 30 < y1 + 40:
            if x2 >= x1 and x2 <= x1 + 40 or x2 + 30 >= x1 and x2 + 30 < x1 + 40:
                x2 = random.randint(1, 100)
                y2 = 0
                health += -10

        # collisions with enm  and bullet

        if b_x >= e_x and b_x  <= e_x + 30 or b_x + 30 >= e_x and b_x + 30 < e_x + 30:
            e_lives += -1
            e_x = 800
            b_x = x1
            state = "ready"
            

        if b_x >= e2_x and b_x  <= e2_x + 30 or b_x + 30 >= e2_x and b_x + 30 < e2_x + 30:
            e2_lives += -1
            e2_x = 700                    
            b_x = x1
            state = "ready"
            


        if health <= 0:
            pygame.mixer.music.stop()
            die_menu()

        if y1 <= 30:
            pygame.mixer.music.stop()
            win_menu()


        if e_lives == 0:
            e_x = 1000000
            e_y = 1000000
        if e2_lives == 0:
            e2_x = 1000000
            e2_y = 1000000            
                            
        mess("Health: ", white)
        
        pygame.display.update()

        clock.tick(60)

    pygame.quit()
    quit()


# run the game

menu()
if play == True:
    run()

