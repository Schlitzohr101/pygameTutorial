import pygame
import random
import time

#start the pygame engine
pygame.init()

#create the size of our games window, set as variables
display_width = 800
display_height = 600

#these are not included in pygame, so lets make some reference colors
#(#,#,#) each of these numbers applies to R G B values
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#Tell pygame to make the game window with the variables we made
gameDisplay = pygame.display.set_mode((display_width,display_height))
#give the window a name
pygame.display.set_caption('Star Collision')

#Save the game clock into a variable
clock = pygame.time.Clock()

#loading the images for the game, these are changeable 
carImg = pygame.image.load('rocketship.gif')
starImg = pygame.image.load('Star.png')

#Here we create useable objects for our images
#without this code, the images could not be used
def obstacle(x,y):
    gameDisplay.blit(starImg, (x,y))

def hero(x,y):
    #define the code for using the hero here 

#this is called boiler plate code, its a lot of code to create something rather simple
#in this case all this code is used to create a Text box we can see
#it is important, but not the focus
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

#this is the most important part of the boiler code, we run this to say when we have crashed, died, etc
def crash():
    message_display('You Crashed')

#here's the meat of the code, the actual game code
def game_loop():

    #x and y here will be used to track the position of our hero
    x =  (display_width * 0.45)
    y = (display_height * 0.8)

    #how much the x of our hero will change
    x_change = #

    #set up for the objects we will be avoiding
    obstacle_x = #
    obstacle_y = #
    #these may need to be changed given what your obstacle is
    obstacle_height = 50
    obstacle_width = 50
    obstacle_speed = #

    #this variable controls the cycle of the game
    gameExit = #

    hero_width = 30

    while not gameExit:

        #this is where the controls of the game are handled
        #mouse or keyboard input are considered events
        #this for ____ in _____ asks for every 'event' in the game
        #run the code indented
        for event in pygame.event.get():
            #here is if the event is to quit the game
            if event.type == pygame.QUIT:
                #
            #if a key is pressed
            if event.type == pygame.KEYDOWN:
                #left arrow key
                if event.key == pygame.K_LEFT:
                    #
                #right arrow key
                elif event.key == pygame.K_RIGHT:
                    #
            #if a key is released, aka you stop pushing it        
            if event.type == pygame.KEYUP:
                #which keys we stopped pressing
                if # or #:
                    x_change = 0
        
        x+=#
        gameDisplay.fill(black)

        obstacle(#,#)
        obstacle_y += #
        hero(x,y)

        
        #this check is to see if our hero and the obstacle are touching
        if y < obstacle_y + obstacle_height:
          print('y crossover')
          if x > obstacle_x and x < obstacle_x + obstacle_width or x + hero_width > obstacle_x and x + hero_width < obstacle_x+obstacle_width:
            print('x crossover')
            crash()
        #here we update our game window
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()