'''
-----------------------------------------------------------------------------
Program Name: (never put your personal name or information on the Internet)
Program Description:

-----------------------------------------------------------------------------
References:

(put a link to your reference here but also add a comment in the code below where you used the reference)

-----------------------------------------------------------------------------

Additional Libraries/Extensions:

(put a list of required extensions so that the user knows that they need to download extra features)

-----------------------------------------------------------------------------

Known bugs:

(put a list of known bugs here, if you have any)

----------------------------------------------------------------------------


Program Reflection:
I think this project deserves a level XXXXXX because ...

 Level 3 Requirements Met:
• 
•  
•  
•  
•  
• 

Features Added Beyond Level 3 Requirements:
• 
•  
•  
•  
•  
• 
-----------------------------------------------------------------------------
'''

import pygame
from pygame import mixer 
pygame.init()

# *********SETUP**********

windowWidth = 1280
windowHeight = 720
window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()  #will allow us to set framerate
PlayerX = 61
PlayerY = 659
Speed = 5

# *********MUSIC************

BackgroundSound = pygame.mixer.Sound("Sound/StrangerThings.mp3")
BackgroundSound.set_volume(1.0) 
BackgroundSound.play(-1)

#*********COLOR*************

GREEN = (0,255,0)
RED = (128, 22, 13)
BLACK = (0,0,0)
WHITE = (250,250,250)
DUST = (146, 173, 171)

#********** GAME STATES ******

state = "HOME"

#***********IMAGES**************

#Home BG
HomePageBG2 = pygame.image.load ("images/HomePageBG2.png")
#Buttons
InstructionsButton = pygame.image.load ("images/InstructionsButton.png")
CharacterButton = pygame.image.load ("images/CharactersButton.png")
PlayButton = pygame.image.load("images/PlayButton.png")
#State BG
InstructionsBG = pygame.image.load("images/InstructionsBG.png")
CharactersBG = pygame.image.load("images/CharactersBG.png")
#Character State Images
ElevenChar = pygame.image.load("images/ElevenFront.png")
MikeChar = pygame.image.load("images/MikeFront.png")
DustinChar = pygame.image.load("images/DustinFront.png")
WillChar = pygame.image.load("images/WillFront.png")
LucasChar = pygame.image.load("images/LucasFront.png")
#Play State Images
Maze = pygame.image.load("images/Maze.png")

#**********MAZE SECTION***************

Maze = Maze.convert_alpha()
maze_rect = Maze.get_rect(topleft=(-310, -40))
maze_mask = pygame.mask.from_surface(Maze, 127)
player_mask = pygame.mask.Mask((20, 20), fill=True)

#***********SCALED IMAGES**************

scaled_image1 = pygame.transform.scale(InstructionsButton, (280,180))
scaled_image2 = pygame.transform.scale(CharacterButton, (280,360))
scaled_image3 = pygame.transform.scale(PlayButton, (280,180))
scaled_image4 = pygame.transform.scale(InstructionsBG, (1280, 720))
scaled_image5 = pygame.transform.scale(CharactersBG, (1280, 720))

#*********Fonts************

font = pygame.font.Font("Fonts/Benguiat Bold.ttf", 26)
font2 = pygame.font.Font("Fonts/Benguiat Bold.ttf", 46)
    
# *********BUTTONS**********

home_button = [

    pygame.Rect(523, 101, 234, 47),
    pygame.Rect(545, 188, 191, 56),
    pygame.Rect(562, 288, 155, 37)
    
]
back_button = pygame.Rect(30, 30, 150, 60)

# *********GAME LOOP**********

Running = True
while Running:

    # *********Sprite Movement**********

    mx, my = pygame.mouse.get_pos()
    print(mx, my)

    key = pygame.key.get_pressed()

    if key[pygame.K_d] == True and state == "PLAY":
        test_rect = pygame.Rect(PlayerX + Speed, PlayerY, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(player_mask, offset) is None:
            PlayerX = PlayerX + Speed

    #if key[pygame.K_d] == True:
        #PlayerX = PlayerX + 1

    if key[pygame.K_a] == True and state == "PLAY":
        test_rect = pygame.Rect(PlayerX - Speed, PlayerY, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(player_mask, offset) is None:
            PlayerX = PlayerX - Speed

    #if key[pygame.K_a] == True:
        #PlayerX = PlayerX - Speed

    if key[pygame.K_s] == True and state == "PLAY":
        test_rect = pygame.Rect(PlayerX, PlayerY + Speed, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(player_mask, offset) is None:
            PlayerY = PlayerY + Speed

    #if key[pygame.K_s] == True:
        #PlayerY = PlayerY + Speed

    if key[pygame.K_w] == True and state == "PLAY":
        test_rect = pygame.Rect(PlayerX, PlayerY - Speed, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(player_mask, offset) is None:
            PlayerY = PlayerY - Speed

   #if key[pygame.K_w] == True:
        #PlayerY = PlayerY - Speed

    PlayerX += (key[pygame.K_RIGHT] - key[pygame.K_LEFT])*Speed
    PlayerY += (key[pygame.K_DOWN] - key[pygame.K_UP])*Speed
    # *********EVENTS**********

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = event.pos 
   
    #**********MOUSE/KEYBOARD******

            if state == "HOME":
                if home_button[0].collidepoint(click_pos): #Checks if mouse clicks button
                    state = "INSTRUCTIONS"
                elif home_button[1].collidepoint(click_pos):
                    state = "CHARACTERS"
                elif home_button[2].collidepoint(click_pos):
                    state = "PLAY"

            else:
                if back_button.collidepoint(click_pos):
                    state = "HOME"

    #*********** STATES ****************

    if state == "INSTRUCTIONS":
        window.fill(BLACK)
        window.blit(scaled_image4, (0,0))
        
    elif state == "CHARACTERS":
        window.fill(BLACK)
        window.blit(scaled_image5, (0,0))
        window.blit(ElevenChar, (375,345))
        window.blit(MikeChar, (170,340))
        window.blit(DustinChar, (-50,290))
        window.blit(WillChar, (570,170))
        window.blit(LucasChar, (750, 190))


    elif state == "PLAY":
        window.fill(BLACK)
        window.blit (Maze, (-310,-40))
        pygame.draw.rect(window, GREEN, (PlayerX,PlayerY,20,20))


    elif state == "HOME":
        Gamename = "The Upside Run"
        window.fill((0,0,0))
        window.blit(HomePageBG2,(40,23))
        window.blit(scaled_image1,(500,35))
        window.blit(scaled_image2,(500,50))
        window.blit(scaled_image3, (500,220))
        renderText2 =font2.render(Gamename, 1, pygame.Color(DUST))
        window.blit(renderText2, (426,380))

    
    # *********GAME LOGIC**********

    #PUT YOUR DRAWING, IMAGE PLACEMENT, BLIT ETC.. COMMANDS HERE FOR EACH GAMESTATE

    # *********SHOW THE FRAME TO THE USER**********

    pygame.display.flip()
    clock.tick(60) #Force frame rate to 60fps or lower


pygame.quit()

#Get Sprite