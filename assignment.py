'''
-----------------------------------------------------------------------------
Program Name: The Upside Run
Program Description: A 2 player maze game inspired by Stranger Things where Eleven
tries to collect eggos and the demogorgon tries to get to her before she can eat all 8 eggos. 
The game end when Eleven succesffuly eats all 8 eggos or when the demogorgon catches up to her.
-----------------------------------------------------------------------------
References:
- https://www.pygame.org/docs/ref/mask.html  (understood how to mask)
- https://www.youtube.com/watch?v=Po_7E1GQOpw (understood how relates to my maze)
- https://www.youtube.com/watch?v=tJiKYMQJnYg (understood what masking does)
- https://www.openai.com/. (helped understand the concepts of coding masks and how to reset a list)

-----------------------------------------------------------------------------

Additional Libraries/Extensions:

Pygame Library
Sound Library
Random Library

-----------------------------------------------------------------------------

Known bugs:

-

----------------------------------------------------------------------------


Program Reflection:
I think this project deserves a level 4+ because ...

 Level 3 Requirements Met:
• Game uses user event
• Uses Loop Structures
• Has multiple states 
• Has Collision Detection 
• Uses Appropriate DataTypes 
• Has Conditional Statements

Features Added Beyond Level 3 Requirements:
• Masking the Maze and Player Sprites
• Checking for collision in a masked environment 
• Random Locations for Eggo generation 
• Two Player Game Play 
• Uses Lists 
-----------------------------------------------------------------------------
'''
# *********SETUP**********

import pygame
import random
from pygame import mixer 
pygame.init()

#***CREATING WINDOW******

windowWidth = 1280
windowHeight = 720
window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()  #will allow us to set framerate

#*****DIMENSIONS AND COORDINATES******

PlayerX = 61
PlayerY = 659
Speed = 5

DemoX = 900
DemoY = 100
DemoSpeed = 5

#Sets a set of coordinates for eggo which are randomly selected with the random library in a list
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

#creates a function that stores the values for player/demo coordinates and current score along with coordinates. Meant to resent the game after playing once
def reset_game ():
    return 61, 659, 900, 100, 0, None, EggoCoordinates.copy()

# *********MUSIC************

BackgroundSound = pygame.mixer.Sound("Sound/StrangerThings.mp3") #loads the sound
BackgroundSound.set_volume(1.0) # sets volume of background music
BackgroundSound.play(-1) # creates a forever loop for the backgorund music to play for

#*********COLORs*************

GREEN = (0,255,0)
RED = (128, 22, 13)
BLACK = (0,0,0)
WHITE = (250,250,250)
DUST = (146, 173, 171)

#********** GAME STATE ******

state = "HOME"

#***********LOADING IMAGES**************

#Home BG
HomePageBG2 = pygame.image.load ("images/HomePageBG2.png")
#Buttons
InstructionsButton = pygame.image.load ("images/InstructionsButton.png")
CharacterButton = pygame.image.load ("images/CharactersButton.png")
PlayButton = pygame.image.load("images/PlayButton.png")
#State BG
InstructionsBG = pygame.image.load("images/InstructionsBG.png")
CharactersBG = pygame.image.load("images/CharactersBG.png")
Maze = pygame.image.load("images/Maze.png")
ElevenSprite = pygame.image.load("images/ElevenSprite.png")
DemoSprite = pygame.image.load("images/DemoSprite.png")
#Eggos
Eggos = pygame.image.load("images/Eggo.png")
#Quit BG
LOSS_SCREEN = pygame.image.load("images/QuitBg.png")
back_button = pygame.image.load("images/BackButton.png")

#**********MAZE SECTION***************

Maze = Maze.convert_alpha() # keeps the transparent section in the maze transparent () (https://www.youtube.com/watch?v=Po_7E1GQOpw)
maze_rect = Maze.get_rect(topleft=(-225,0)) # creates a rectangle with the dimensions of the maze and puts makes the image 225 px of the screen
maze_mask = pygame.mask.from_surface(Maze, 127) # Create a masked mask that says any section that is over 127 px as solid and anything under is a path
player_mask = pygame.mask.Mask((5,5), fill=True) # Creates a small hitbox for the player that says that the rectangle is solid
demo_mask = pygame.mask.Mask((5,5), fill=True) # Creates a small hitbox for the Demo that says that the rectangle is solid

CurrentEggo = None
RemainingEggos = EggoCoordinates.copy()
CurrentScore = 0

#***********SCALED IMAGES**************

scaled_image1 = pygame.transform.scale(InstructionsButton, (280,180))
scaled_image2 = pygame.transform.scale(CharacterButton, (280,360))
scaled_image3 = pygame.transform.scale(PlayButton, (280,180))
scaled_image4 = pygame.transform.scale(InstructionsBG, (1280, 720))
scaled_image5 = pygame.transform.scale(CharactersBG, (1280, 720))
scaled_image6 = pygame.transform.scale(back_button, (600,360))

#*********Fonts************

font = pygame.font.Font("Fonts/Benguiat Bold.ttf", 26) # loads the font with a sie of 26
font2 = pygame.font.Font("Fonts/Benguiat Bold.ttf", 46) # loads the font with a sie of 46
font3 = pygame.font.Font("Fonts/Benguiat Bold.ttf", 16) # loads the font with a sie of 16

# *********BUTTONS**********

#Sets a set of rectangles that allign with the actual buttons
home_button = [

    pygame.Rect(523, 101, 234, 47),
    pygame.Rect(562, 288, 155, 37)
    
]
# *********GAME LOOP**********

Running = True
while Running:

    # *********Sprite Movement**********

    mx, my = pygame.mouse.get_pos()
    print(mx, my) # Used to get mouse position while coding

    key = pygame.key.get_pressed() # Checks to see if keys are pressed


    ''' Checks to see if the l key is pressed while in the play state and creates a rectangle that store the future location of the sprite if it were to be moved.
        The differnece between the x coordinate of the rectnagle for the player and the X coordinate of the maze malls are calculated. If the demo_mask and the 
        maze_mask collide, then the returnt he coordinates which prevents the sprite from moving in that direction, but if none is returned then the the Demo Speed
        is added to DemoX allowing the sprite to move to the right.
    '''

    if key[pygame.K_l] and state == "PLAY":
        test_rect = pygame.Rect(DemoX + DemoSpeed, DemoY, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(demo_mask, offset) is None: # (https://www.youtube.com/watch?v=tJiKYMQJnYg) 
            DemoX += DemoSpeed

    ''' Follows the same code as the l key but is run to check for the j key instead. One difference is, if none is returned, then the DemoSpeed is subtracted from 
        DemoX which allows the sprite to move towards the left.
    '''

    if key[pygame.K_j] and state == "PLAY":
        test_rect = pygame.Rect(DemoX - DemoSpeed, DemoY, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(demo_mask, offset) is None:
            DemoX -= DemoSpeed

    ''' Follows the same code as the l key but is run to check for the k key instead. One difference is, if none is returned, then the DemoSpeed is added to 
        DemoY which allows the sprite to move downwards.
    '''

    if key[pygame.K_k] and state == "PLAY":
        test_rect = pygame.Rect(DemoX, DemoY + DemoSpeed, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(demo_mask, offset) is None:
            DemoY += DemoSpeed

    ''' Follows the same code as the l key but is run to check for the i key instead. One difference is, if none is returned, then the DemoSpeed is subtracted from 
        Demoy which allows the sprite to go upwards.
    '''

    if key[pygame.K_i] and state == "PLAY":
        test_rect = pygame.Rect(DemoX, DemoY - DemoSpeed, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(demo_mask, offset) is None:
            DemoY -= DemoSpeed

    ''' Follows the same code as the l key but is run to check for the d key instead. One difference is, if none is returned, then the Speed is added to 
        PlayerX which allows the sprite to move towards the right.
    '''

    if key[pygame.K_d] and state == "PLAY":
        test_rect = pygame.Rect(PlayerX + Speed, PlayerY, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(player_mask, offset) is None:
                PlayerX = PlayerX + Speed

    ''' Follows the same code as the l key but is run to check for the a key instead. One difference is, if none is returned, then the Speed is subtracted from 
        PlayerX which allows the sprite to move towards the left.
    '''

    if key[pygame.K_a] and state == "PLAY":
        test_rect = pygame.Rect(PlayerX - Speed, PlayerY, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(player_mask, offset) is None:
            PlayerX = PlayerX - Speed

    ''' Follows the same code as the l key but is run to check for the s key instead. One difference is, if none is returned, then the Speed is added to 
        Playery which allows the sprite to move downwards.
    '''

    if key[pygame.K_s] == True and state == "PLAY":
        test_rect = pygame.Rect(PlayerX, PlayerY + Speed, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(player_mask, offset) is None:
            PlayerY = PlayerY + Speed

    ''' Follows the same code as the l key but is run to check for the w key instead. One difference is, if none is returned, then the Speed is subtracted from 
        PlayerX which allows the sprite to go upwards.
    '''

    if key[pygame.K_w] == True and state == "PLAY":
        test_rect = pygame.Rect(PlayerX, PlayerY - Speed, 20, 20)
        offset = (test_rect.x - maze_rect.x, test_rect.y - maze_rect.y)
        if maze_mask.overlap(player_mask, offset) is None:
            PlayerY = PlayerY - Speed

    # *********EVENTS******************************************************

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Allows the window to close if the x button was clicked
            Running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Checks to see if the left button was cicked
            click_pos = event.pos 
   
    #**********MOUSE********************

            if state == "HOME":
                if home_button[0].collidepoint(click_pos): #Checks if mouse clicks instructions buttton
                    state = "INSTRUCTIONS"
                elif home_button[1].collidepoint(click_pos): #Checks if mouse clicks play button
                    PlayerX, PlayerY, DemoX, DemoY, CurrentScore, CurrentEggo, RemainingEggos = reset_game() # Makes it so the Player/Demo coordinate reset after each game
                    state = "PLAY"

    #*********** STATES ****************

    #Instructions State

    if state == "INSTRUCTIONS": #checks to see if the player wants to be in the Instructions State
        window.fill(BLACK)
        window.blit(scaled_image4, (0,0))
    
        button_rect = pygame.Rect(55,24, 191, 63) #creates hitbox for the back button which allows player to go back to the home state
        window.blit(scaled_image6, (-150,-125))

        #Checks to see if user clicks back button to go to the Home State
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = event.pos
            if button_rect.collidepoint(click_pos):
                state = "HOME"
        
        #Creates Instructions header
        InstructionsHeader = "INSTRUCTIONS "

        #Renders Instructions Header
        renderText5 = font.render (InstructionsHeader,1, pygame.Color (DUST))

        #Blits Instructions Header onto the window
        window.blit(renderText5, (180,125))

        #Creates Summary of Game
        InstructionsCaption1 = " The goal is for the player to collect as"
        InstructionsCaption2 = " many eggo without the "
        InstructionsCaption3 = " demogrogron catching them"

        #Renders Text for Summary
        renderText6 = font3.render (InstructionsCaption1,1, pygame.Color (DUST))
        renderText7 = font3.render (InstructionsCaption2,1, pygame.Color (DUST))
        renderText8 = font3.render (InstructionsCaption3,1, pygame.Color (DUST))
        
        #Blits Text for Summary onto the Window
        window.blit(renderText6, (114,225))
        window.blit(renderText7, (184,250))
        window.blit(renderText8, (156,275))

        #Creates Instruction for game
        InstructionsCaption4 = " - Use WASD key to move player"
        InstructionsCaption5 = " - Collect the eggos as they appear"
        InstructionsCaption6 = " - Each eggo is worth 100 points"
        InstructionsCaption7 = " - If you wish to quit, exit the maze"
        InstructionsCaption8 = " - You lose if the demogorgon catches you"
        InstructionsCaption9 = " - The demogorgon's goal is to catch the player"
        InstructionsCaption10 = " - Use IJKL key to move demogorgon"
        InstructionsCaption11 = " - The game ends if the demogorgon catches the player"
        InstructionsCaption12 = " - or if the player gains 800 points"

        #Renders Instructions for Game
        renderText9 = font3.render (InstructionsCaption4,1, pygame.Color (DUST))
        renderText10 = font3.render (InstructionsCaption5,1, pygame.Color (DUST))
        renderText11 = font3.render (InstructionsCaption6,1, pygame.Color (DUST))
        renderText12 = font3.render (InstructionsCaption7,1, pygame.Color (DUST))
        renderText13 = font3.render (InstructionsCaption8,1, pygame.Color (DUST))
        renderText14 = font3.render (InstructionsCaption9,1, pygame.Color (DUST))
        renderText15 = font3.render (InstructionsCaption10,1, pygame.Color (DUST))
        renderText16 = font3. render(InstructionsCaption11,1,pygame.Color (DUST))
        renderText17 = font3. render(InstructionsCaption12,1, pygame.Color (DUST))

        #Blits Instructions for game onto the window
        window.blit(renderText9, (114,390))
        window.blit(renderText10, (114,420))
        window.blit(renderText11, (114,460))
        window.blit(renderText12, (114,495))
        window.blit(renderText13, (114,530))
        window.blit(renderText14, (114,565))
        window.blit(renderText15, (114,600))
        window.blit(renderText16, (114,635))
        window.blit(renderText17, (114,670))

    #Play State

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
        window.blit(ElevenSprite, (x - offset1, y - offset2)) # centres the Eleven Sprite image to the rectangle which is used for collision detection
        window.blit(DemoSprite, (a - offset1, b - offset2)) ## centres the Demo Sprite image to the rectangle which is used for collision detection
   
        #Checks to see if the Eleven sprite leaves the maze and if it does the state changes to QUIT
        if player_rect.right < 0:
            state = "QUIT"
        elif player_rect.left > windowWidth:
            state = "QUIT"

        #Checks to see if the Demo sprite leaves the maze and if it does the state changes to QUIT
        if demo_rect.right < 0:
            state = "QUIT"
        elif demo_rect.left > windowWidth:
            state = "QUIT"

        if CurrentEggo is None: #Checks to see if there are curenlty no eggos on the screen
            if not RemainingEggos: #Checks to see if there are any unused coordinates for the eggos
                RemainingEggos = EggoCoordinates.copy() #If there are no more unused eggos, then the list is regenerated (https://www.openai.com/)
            EggoLocation = random.choice(RemainingEggos) #EggoLocoation chooses a random location from the coordinates that have been reset
            CurrentEggo = True #Now there is an active egg on the screen
        if CurrentEggo == True: #Checks to see if there is an eggo on the screen
            window.blit(Eggos, EggoLocation) #Blits the eggo onto the wondow
            EggoRect = pygame.Rect(EggoLocation[0], EggoLocation[1], Eggos.get_width(), Eggos.get_height()) #Creates a rectangle in the same location of the eggo on the screen with the same dimensions
            if player_rect.colliderect(EggoRect): #Checks to see if the player collided with the eggo
                CurrentEggo = None # if the player did collide then there are no active eggos on the screen so the loop starts again but the coordinates do not need to be reset as the list is not empty yet
                RemainingEggos.remove(EggoLocation) # Removes the used up coordinates from the list so EggoLocation[0]/[1] are the next set of coordinates in the list
                CurrentScore += 100 #100 points add to the player's score as they collect eggos
                if CurrentScore == 800:
                    state = "PLAYER_WON" # The state changes to Player_Won if the current score becomes 100

        demo_rect = pygame.Rect(DemoX, DemoY, 20, 20) # Creates a rectangle for the demogorgon 
        if player_rect.colliderect(demo_rect): #Checks to see if the player and the demo collide and if they do then the state changes. 
            state = "DEMO_WON" 

    #Quit State

    elif state == "QUIT": #Checks to see if the state is QUIT
        window.fill((0,0,0))
        window.blit(LOSS_SCREEN, (0,0)) #blits the Quit screen backgorund image

        #Same code as before used for back button to go back to the haome screen
        button_rect = pygame.Rect(55,24, 191, 63)
        window.blit(scaled_image6, (-150,-125))

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = event.pos
            if button_rect.collidepoint(click_pos):
                state = "HOME"

        #notifies the player of their current score and that they have quit the game
        QuitCaption1 = "You have quit the Game! Better luck next time!"
        renderText3 = font.render (QuitCaption1,1, pygame.Color (DUST))
        window.blit(renderText3, (500,650))
        QuitCaption2 = "Your Current Score is: "
        renderText4 = font.render (QuitCaption2 + str(CurrentScore),1, pygame.Color (RED))
        window.blit(renderText4, (300,150))

    #Demo_win State

    elif state == "DEMO_WON": #Checks to see if the state is Demo_Won
        window.fill(BLACK)
        window.blit(LOSS_SCREEN, (0,0)) #Blits the Demo_Won screen BG which is the same as the player won and quit screen but it has different text on it

        #Same code as before used for back button to go back to the haome screen
        button_rect = pygame.Rect(55,24, 191, 63)
        window.blit(scaled_image6, (-150,-125))

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = event.pos
            if button_rect.collidepoint(click_pos):
                state = "HOME"

        #Tells the players that the demogorgon won and allows the player to go back to the home screen if they want to
        PlayerLossCaption = "The Demo got you!"
        PlayerLossCaption1 = "Better Luck Next Time!"
        renderText18 = font.render (PlayerLossCaption, 1, pygame.Color (RED))
        window.blit(renderText18, (300,150))
        renderText19 = font.render (PlayerLossCaption1, 1, pygame.Color (DUST))
        window.blit(renderText19, (500,650))

    #Player_Win State

    elif state == "PLAYER_WON": #Checks to see if the state is Player_Won
        window.fill(BLACK)
        window.blit(LOSS_SCREEN, (0,0)) #Blits the player_won screen BG which is the same as the demo_won and quit screen but it has different text on it

        #Same code as before used for back button to go back to the haome screen
        button_rect = pygame.Rect(55,24, 191, 63)
        window.blit(scaled_image6, (-150,-125))

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = event.pos
            if button_rect.collidepoint(click_pos):
                state = "HOME"
        #Tells the players that Eleven won and allows the player to go back to the home screen to play again 
        PlayerLossCaption = "The Player Won!"
        PlayerLossCaption1 = "Better Luck Next Time Demo!"
        renderText18 = font.render (PlayerLossCaption, 1, pygame.Color (RED))
        window.blit(renderText18, (300,150))
        renderText19 = font.render (PlayerLossCaption1, 1, pygame.Color (DUST))
        window.blit(renderText19, (500,650))

    #Home State

    elif state == "HOME": #Checks tif the state is HOME

        #Bg Placement and images Placement on scree
        window.fill((0,0,0))
        window.blit(HomePageBG2,(40,23))
        window.blit(scaled_image1,(500,35))
        window.blit(scaled_image3, (500,220))

        #Create Game Header
        Gamename = "The Upside Run"
        renderText2 =font2.render(Gamename, 1, pygame.Color(DUST))
        window.blit(renderText2, (426,380))

        #Create Current Score report for players that choose to continue playing
        QuitCaption2 = "ELEVEN'S CURRENT SCORE: "
        renderText4 = font.render (QuitCaption2 + str(CurrentScore),1, pygame.Color (DUST))
        window.blit(renderText4, (430,200))

    

    # *********SHOW THE FRAME TO THE USER**********

    pygame.display.flip()
    clock.tick(60) #Force frame rate to 60fps or lower


pygame.quit()
