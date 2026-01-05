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
pygame.init()

# *********SETUP**********

windowWidth = 1280
windowHeight = 720
window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()  #will allow us to set framerate

#*********COLOR*************

GREEN = (0,255,0)
RED = (128, 22, 13)
BLACK = (0,0,0)
WHITE = (250,250,250)
DUST = (146, 173, 171)

#********** GAME STATES ******

state = "HOME"

#***********IMAGES**************

HomePageBG2 = pygame.image.load ("images/HomePageBG2.png")
InstructionsButton = pygame.image.load ("images/InstructionsButton.png")
CharacterButton = pygame.image.load ("images/CharactersButton.png")
PlayButton = pygame.image.load("images/PlayButton.png")
InstructionsBG = pygame.image.load("images/InstructionsBG.png")
CharactersBG = pygame.image.load("images/CharactersBG.png")
ElevenChar = pygame.image.load("images/ElevenFront.png")
MikeChar = pygame.image.load("images/MikeFront.png")

#***********SCALED IMAGES**************

scaled_image1 = pygame.transform.scale(InstructionsButton, (280,180))
scaled_image2 = pygame.transform.scale(CharacterButton, (304,274))
scaled_image3 = pygame.transform.scale(PlayButton, (280,180))
scaled_image4 = pygame.transform.scale(InstructionsBG, (1280, 720))
scaled_image5 = pygame.transform.scale(CharactersBG, (1280, 720))
scaled_image6 = pygame.transform.scale(ElevenChar, (225,330))
scaled_image7 = pygame.transform.scale(MikeChar, (225, 330))

#*********Fonts************

font = pygame.font.Font("Fonts/Benguiat Bold.ttf", 26)
font2 = pygame.font.Font("Fonts/Benguiat Bold.ttf", 46)
    
# *********BUTTONS**********

home_button = [

    pygame.Rect(500, 35, scaled_image1.get_width(), scaled_image1.get_height()),
    pygame.Rect(488, 70, scaled_image2.get_width(), scaled_image2.get_height()),
    pygame.Rect(464,220, scaled_image3.get_width(), scaled_image3.get_height())
    
]
back_button = pygame.Rect(30, 30, 150, 60)

# *********GAME LOOP**********

Running = True
while Running:

    # *********EVENTS**********

    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
   
    #**********MOUSE/KEYBOARD******

            if state == "HOME":
                if home_button[0].collidepoint(mx, my): #Checks if mouse clicks button
                    state = "INSTRUCTIONS"
                elif home_button[1].collidepoint(mx, my):
                    state = "CHARACTERS"
                elif home_button[2].collidepoint(mx, my):
                    state = "PLAY"

            else:
                if back_button.collidepoint(mx, my):
                    state = "HOME"

    #*********** STATES ****************

    if state == "INSTRUCTIONS":
        window.fill(BLACK)
        window.blit(scaled_image4, (0,0))
        
    elif state == "CHARACTERS":
        window.fill(BLACK)
        window.blit(scaled_image5, (0,0))
        window.blit(ElevenChar, (235,160))
        window.blit(MikeChar, (15,175))

    #if state == "PlAY":
    elif state == "HOME":
        Gamename = "The Upside Run"
        window.fill((0,0,0))
        window.blit(HomePageBG2,(40,23))
        window.blit(scaled_image1,(500,35))
        window.blit(scaled_image2,(488,90))
        window.blit(scaled_image3, (500,220))
        renderText2 =font2.render(Gamename, 1, pygame.Color(DUST))
        window.blit(renderText2, (426,380))

    
    # *********GAME LOGIC**********

    #PUT YOUR DRAWING, IMAGE PLACEMENT, BLIT ETC.. COMMANDS HERE FOR EACH GAMESTATE

    # *********SHOW THE FRAME TO THE USER**********

    pygame.display.flip()
    clock.tick(60) #Force frame rate to 60fps or lower


pygame.quit()

#fix button ranges