import pygame
import random
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('rocketship.gif')
starImg = pygame.image.load('Star.png')

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    
def star(x,y):
    gameDisplay.blit(starImg, (x,y))

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('You Crashed')

def game_loop():

    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    star_x = random.randrange(0, display_width)
    star_y = 0
    star_height = 50
    star_width = 50
    star_speed = 7

    gameExit = False

    rocket_width = 30

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
        x+=x_change
        gameDisplay.fill(black)
        #things(thing_startx, thing_starty, thing_width, thing_height, black)
        #thing_starty += thing_speed
        star(star_x,star_y)
        star_y += star_speed
        car(x,y)

        if x > display_width - car_width or x < 0:
            crash()

        if star_y > display_height:
            star_y = 0
            star_x = random.randrange(0,display_width)
            
        if y < star_y + star_height:
          print('y crossover')
          if x > star_x and x < star_x + star_width or x + rocket_width > star_x and x + star_width < star_x+star_width:
            print('x crossover')
            crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()