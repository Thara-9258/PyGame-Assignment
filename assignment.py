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
import random
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

DemoX = 900
DemoY = 100
DemoSpeed = 5

EggoCoordinates = [
    (145, 460),
    (456, 232),
    (452, 416),
    (766, 594),
    (688, 335),
    (846, 190),
    (1076, 445),
    (1158, 164)
]

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
ElevenSprite = pygame.image.load("images/ElevenSprite.png")
DemoSprite = pygame.image.load("images/DemoSprite.png")
#Eggos
Eggos = pygame.image.load("images/Eggo.png")
#Quit BG
QuitBG = pygame.image.load("images/QuitBg.png")

#**********MAZE SECTION***************

Maze = Maze.convert_alpha()
maze_rect = Maze.get_rect(topleft=(-225,0))
maze_mask = pygame.mask.from_surface(Maze, 127)
player_mask = pygame.mask.Mask((5,5), fill=True)
demo_mask = pygame.mask.Mask((5,5), fill=True)
CurrentEggo = None
RemainingEggos = EggoCoordinates.copy()
CurrentScore = 0

#***********SCALED IMAGES**************

scaled_image1 = pygame.transform.scale(InstructionsButton, (280,180))
scaled_image2 = pygame.transform.scale(CharacterButton, (280,360))
scaled_image3 = pygame.transform.scale(PlayButton, (280,180))
scaled_image4 = pygame.transform.scale(InstructionsBG, (1280, 720))
scaled_image5 = pygame.transform.scale(CharactersBG, (1280, 720))

#*********Fonts************

font = pygame.font.Font("Fonts/Benguiat Bold.ttf", 26)
font2 = pygame.font.Font("Fonts/Benguiat Bold.ttf", 46)
font3 = pygame.font.Font("Fonts/Benguiat Bold.ttf", 16)
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

    if key[pygame.K_l] and state == "PLAY":
        test_rect = pygame.Rect(DemoX + DemoSpeed, DemoY, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(demo_mask, offset) is None:
            DemoX += DemoSpeed

    if key[pygame.K_j] and state == "PLAY":
        test_rect = pygame.Rect(DemoX - DemoSpeed, DemoY, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(demo_mask, offset) is None:
            DemoX -= DemoSpeed

    if key[pygame.K_k] and state == "PLAY":
        test_rect = pygame.Rect(DemoX, DemoY + DemoSpeed, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(demo_mask, offset) is None:
            DemoY += DemoSpeed

    if key[pygame.K_i] and state == "PLAY":
        test_rect = pygame.Rect(DemoX, DemoY - DemoSpeed, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(demo_mask, offset) is None:
            DemoY -= DemoSpeed

    if key[pygame.K_d] and state == "PLAY":
        test_rect = pygame.Rect(PlayerX + Speed, PlayerY, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(player_mask, offset) is None:
                PlayerX = PlayerX + Speed


    if key[pygame.K_a] and state == "PLAY":
        test_rect = pygame.Rect(PlayerX - Speed, PlayerY, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(player_mask, offset) is None:
            PlayerX = PlayerX - Speed


    if key[pygame.K_s] == True and state == "PLAY":
        test_rect = pygame.Rect(PlayerX, PlayerY + Speed, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(player_mask, offset) is None:
            PlayerY = PlayerY + Speed


    if key[pygame.K_w] == True and state == "PLAY":
        test_rect = pygame.Rect(PlayerX, PlayerY - Speed, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(player_mask, offset) is None:
            PlayerY = PlayerY - Speed


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
        InstructionsHeader = "INSTRUCTIONS "
        renderText5 = font.render (InstructionsHeader,1, pygame.Color (DUST))

        window.blit(renderText5, (180,125))
        InstructionsCaption1 = " The goal of the game is to collect as"
        InstructionsCaption2 = " many eggos as possible without the "
        InstructionsCaption3 = " demogrogron catching you"

        renderText6 = font3.render (InstructionsCaption1,1, pygame.Color (DUST))
        renderText7 = font3.render (InstructionsCaption2,1, pygame.Color (DUST))
        renderText8 = font3.render (InstructionsCaption3,1, pygame.Color (DUST))
        
        window.blit(renderText6, (114,225))
        window.blit(renderText7, (114,250))
        window.blit(renderText8, (146,275))

        InstructionsCaption4 = " - Use WASD key to move"
        InstructionsCaption5 = " - Collect the eggos as the appear"
        InstructionsCaption6 = " - Each eggo is worth 100 points"
        InstructionsCaption7 = " - if you wish to quit, exit the maze"
        InstructionsCaption8 = " - You lose if the demogorgon catches you"
        InstructionsCaption9 = " - The demogorgons will get faster the longer you play"

        renderText9 = font3.render (InstructionsCaption4,1, pygame.Color (DUST))
        renderText10 = font3.render (InstructionsCaption5,1, pygame.Color (DUST))
        renderText11 = font3.render (InstructionsCaption6,1, pygame.Color (DUST))
        renderText12 = font3.render (InstructionsCaption7,1, pygame.Color (DUST))
        renderText13 = font3.render (InstructionsCaption8,1, pygame.Color (DUST))
        renderText14 = font3.render (InstructionsCaption9,1, pygame.Color (DUST))

        window.blit(renderText9, (136,375))
        window.blit(renderText10, (136,425))
        window.blit(renderText11, (136,475))
        window.blit(renderText12, (136,525))
        window.blit(renderText13, (136,575))
        window.blit(renderText14, (136,625))

        
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
        window.blit (Maze,(-225,0))
        player_rect = pygame.draw.rect(window, GREEN, (PlayerX,PlayerY,20,20))
        demo_rect = pygame.Rect(DemoX, DemoY, 20, 20)

        x = player_rect.x
        y = player_rect.y

        a = demo_rect.x
        b = demo_rect.y

        offset1 = 40
        offset2 = 40       
        window.blit(ElevenSprite, (x - offset1, y - offset2))
        window.blit(DemoSprite, (a - offset1, b - offset2))

        if player_rect.right < 0:
            state = "QUIT"
        elif player_rect.left > windowWidth:
            state = "QUIT"

        if demo_rect.right < 0:
            state = "QUIT"
        elif demo_rect.left > windowWidth:
            state = "QUIT"

        if CurrentEggo is None:
            if not RemainingEggos:
                RemainingEggos = EggoCoordinates.copy()
            EggoLocation = random.choice(RemainingEggos)
            CurrentEggo = True 
        if CurrentEggo == True:
            window.blit(Eggos, EggoLocation)
            EggoRect = pygame.Rect(EggoLocation[0], EggoLocation[1], Eggos.get_width(), Eggos.get_height())
            if player_rect.colliderect(EggoRect):
                CurrentEggo = None
                RemainingEggos.remove(EggoLocation)
                CurrentScore += 100

        demo_rect = pygame.Rect(DemoX, DemoY, 20, 20)
        if player_rect.colliderect(demo_rect):
            state = "QUIT" 

    elif state == "QUIT":
        window.fill((0,0,0))
        window.blit(QuitBG, (0,0))
        QuitCaption1 = "You have quit the Game! Better luck next time!"
        renderText3 = font.render (QuitCaption1,1, pygame.Color (DUST))
        window.blit(renderText3, (500,650))
        QuitCaption2 = "Your Current Score is: "
        renderText4 = font.render (QuitCaption2 + str(CurrentScore),1, pygame.Color (RED))
        window.blit(renderText4, (300,150))

    

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

#Comment, back button, Instructions