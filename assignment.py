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
#***********BG**************

HomePageBG2 = pygame.image.load ("images/HomePageBG2.png")
InstructionsButton = pygame.image.load ("images/InstructionsButton.png")
scaled_image1 = pygame.transform.scale(InstructionsButton, (280,180))
CharacterButton = pygame.image.load ("images/CharactersButton.png")
scaled_image2 = pygame.transform.scale(CharacterButton, (280,180))

#*********Fonts************

font = pygame.font.Font("Fonts/Benguiat Bold.ttf", 26)
font2 = pygame.font.Font("Fonts/Benguiat Bold.ttf", 46)
    
# *********BUTTONS**********



# *********GAME LOOP**********
while True:
    # *********EVENTS**********
    for event in pygame.event.get():
        if event.type== pygame.MOUSEMOTION:
            print(pygame.mouse.get_pos())
        if event.type == pygame.QUIT: # windowow close button clicked?
            exit()
    #pygame.display.update()
   
    #**********MOUSE/KEYBOARD******


    # *********GAME LOGIC**********
    
    ChooseChar = "CHARACTERS"
    Play = "PLAY"
    Gamename = "The Upside Run"
    #PUT YOUR GAME LOGIN HERE FOR EACH GAMESTATE
    
    
    #*************BG**************

    window.fill((0,0,0))
    window.blit(HomePageBG2,(40,23))
    window.blit(scaled_image1,(500,35))
    window.blit(scaled_image2,(500,135))
    
    # *********DRAW THE FRAME**********

    

    #pygame.draw.rect(window, WHITE, (500,175,280,70))

    pygame.draw.rect(window, WHITE, (500,275,280,70))



    #pygame.draw.rect(window, BLACK, (520,185,240,50))

    pygame.draw.rect(window, BLACK, (520,285,240,50))

    pygame.draw.rect(window, BLACK, (420,370,454,85))



    #renderText =font.render(ChooseChar, 1, pygame.Color("red"))
    #window.blit(renderText, (527,194))

    renderText =font.render(Play, 1, pygame.Color("red"))
    window.blit(renderText, (598,294))

    renderText2 =font2.render(Gamename, 1, pygame.Color("red"))
    window.blit(renderText2, (426,380))

    #PUT YOUR DRAWING, IMAGE PLACEMENT, BLIT ETC.. COMMANDS HERE FOR EACH GAMESTATE

    # *********SHOW THE FRAME TO THE USER**********
    pygame.display.flip()
    clock.tick(60) #Force frame rate to 60fps or lower


pygame.quit()

#Finish uploading home page images 