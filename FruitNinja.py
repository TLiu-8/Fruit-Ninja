#########################################
# File Name: FruitNinja.py
# Description: My version of fruit ninja, for the ISU, Thanks Mr. G :)
# Author: Theo Liu
# Date: 05/30/2018
#########################################

#---------------------------------------------------------------------------------#
# Introductory Initializations                                                    #
#---------------------------------------------------------------------------------#

from random import randint
from math import sqrt
import time
import pygame

# Pygame Window Initialization----------------------#
WIDTH = 800
HEIGHT = 600
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))



# Colours------------------------------------------# 
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
YELLOW = (255,255,  0)
GREEN = ( 57,225,20)
BLUE   = (  0,  0,255)
RED = (255,  0,  0)

# Boolean Operators Initializations-----------------#

#Major Screen Drawings
inPlay = True
inMenu = True
inSelect = False
inGame = False
inGameOver = False

# Modes
classicMode = False
arcadeMode = False

# Deaths
timeUp = False
livesOut = False

#Power ups and Bombs and Combos
bombSpawn = True

specialBoostCondition = False
specialBoostDisplay = False
specialBoost = False
doublePoints = False
powerupSpawn = True

comboDisplay = False
comboScore = False

waveSpawn = False       #wave of fruit

oneTimeUse = True  #one time use of countdown


# Select Screen Properties--------------------------# (Sets the properties of the buttons for the select screens, choiceColour indices can be change to yellow or white when the player clicks one or the other)

buttonX = [200,400,600]
buttonY = [220,420]
BUTTON_R = 75

choiceColour = [WHITE,WHITE,WHITE,WHITE,WHITE,WHITE]

# Other Variables ----------------------------------#

check = 0             #used for delay after a wave of fruit
checkNum = 45
counter = 0     

extra = 0        #adding extra fruit each time
timerModifier = 0  #adding time after a powerup
timerCondition = 1  #one time use condition

point = 1          #points added each time
score = 0
lives = 10

fruitSpawn = randint(1,2)
goneFruit = 0      #fruits that have been swiped or fallen

explosionPic = [0]*6  #animation
explosionPicNum = 0

GRAVITY = 2

bombY = 620              #bomb initializations
bombVy = randint(-45,-38)
bombX = randint(0,700)

powerupY = 640              #power up initializations
powerupX = randint(40,720)
powerupVy = randint(-48,-32)
powerupR = 35

position = (0,0)
press = 0  #whether mouse is held down or not


# Main Lists

objectX = []
objectY = []
objectJumpSpeed =[]
objectVy = []
drawing = []
objectR = []
typeFruit = []
conditionA= []
conditionB= []
conditionC=[]
explosionX = []
explosionY =[]
explosion = []
comboCheck = []
positioncopy = []

for count in range(fruitSpawn):
    objectX.append(randint(0,700))
    objectY.append(600)
    objectJumpSpeed.append(randint(-40,-30))
    typeFruit.append(randint(1,5))
    objectVy.append(0)
    drawing.append(1)
    objectR.append(0)
    positioncopy.append(0)
    conditionA.append(0)
    conditionB.append(1)
    conditionC.append(1)
    explosion.append(0)
    explosionX.append(0)
    explosionY.append(0)
    comboCheck.append(0)


#---------------------------------------------------------------------------------#
# Functions                                                                       # (sorted alphabetically)
#---------------------------------------------------------------------------------#

def sword(position):
    pygame.draw.circle(gameWindow,YELLOW,position,3,0)

def drawMenu():                             # Displays all features of the main Menu
    gameWindow.fill(BLACK)
    

    gameWindow.blit(titlePicture,(110,30))

    gameWindow.blit(logo,(325,250))

    rulesControlHeading = inGameFont.render("Check Shell for Rules and Controls",1,RED)
    gameWindow.blit(rulesControlHeading,(200,500))

    startPrompt = inGameFont.render("Press Space to Begin",1,GREEN)
    gameWindow.blit(startPrompt,(280,420))

    pygame.display.update()
    pygame.time.delay(40)

def selectScreen():                     # displays everything in select screen

    gameWindow.fill(BLACK)
    
    bambooSetting = inGameFont.render(" BAMBOO",1,choiceColour [0])
    yinyangSetting = inGameFont.render("  WAVE ",1,choiceColour [1])
    waveSetting = inGameFont.render("YINYANG",1,choiceColour [2])

    classicLevel = inGameFont.render("CLASSIC",1,choiceColour [3])
    arcadeLevel = inGameFont.render("ARCADE",1,choiceColour [4])

    modeHeading = inGameFont.render("Input choice of mode:",1,YELLOW)
    courseHeading = inGameFont.render("Input background of course:",1,YELLOW)
    startPrompt = inGameFont.render("Press Right Shift to Start Game",1,GREEN)
    
    gameWindow.blit(startPrompt,(100,500))

    gameWindow.blit(modeHeading,(100,295))
    gameWindow.blit(courseHeading,(100,80))

    gameWindow.blit(classicLevel,(150,400))
    gameWindow.blit(arcadeLevel,(550,400))

    gameWindow.blit(bambooSetting,(160,200))
    gameWindow.blit(yinyangSetting,(360,200))
    gameWindow.blit(waveSetting,(560,200))

    pygame.draw.circle(gameWindow, WHITE, (buttonX [0],buttonY [0]),BUTTON_R,5)
    pygame.draw.circle(gameWindow, WHITE, (buttonX [1],buttonY [0]),BUTTON_R,5)
    pygame.draw.circle(gameWindow, WHITE, (buttonX [2],buttonY [0]),BUTTON_R,5)

    pygame.draw.circle(gameWindow, WHITE, (buttonX [0],buttonY [1]),BUTTON_R,5)
    pygame.draw.circle(gameWindow, WHITE, (buttonX [2],buttonY [1]),BUTTON_R,5)


    pygame.display.update()
    pygame.time.delay(20)
    
def countdown():
    count = [3,2,1]
    for i in range(3):
        gameWindow.fill(BLACK)
        countdown= font.render(str(count [i]),1,WHITE)
        gameWindow.blit(countdown,(380,280))
        pygame.display.update()
        pygame.time.delay(1000)

def background():
    if backgroundInput == 1:
        gameWindow.blit(background1,(0,0))
    elif backgroundInput == 2:
        gameWindow.blit(background2,(0,0))
    else:
        gameWindow.blit(background3,(0,0))

def drawScoreboard(seconds):
    
    scoreBoard = inGameFont.render(str(score),1,WHITE)
    gameWindow.blit(scoreBoard,(100,20))

    scoreHeading = inGameFont.render("Score:",1,WHITE)
    gameWindow.blit(scoreHeading,(20,20))

    if classicMode == True:

        livesHeading = inGameFont.render("Lives:",1,WHITE)
        gameWindow.blit(livesHeading,(560,20))

        livesDisplay = inGameFont.render(str(lives),1,WHITE)
        gameWindow.blit(livesDisplay,(630,20))

    if comboDisplay == True:
        comboHeading = inGameFont.render("+1 Combo!",1,WHITE)
        gameWindow.blit(comboHeading, (150,20))

    if arcadeMode == True:    
        if seconds > 100:
            seconds = 100
        timeLeft = 103 - seconds
        countingDisplay = inGameFont.render(str(timeLeft),1,WHITE)
        gameWindow.blit(countingDisplay,(680,20))

def bombAndExplosion():
    for i in range(fruitSpawn):
        if explosion [i] == 1:
            gameWindow.blit(explosionPic[explosionPicNum], (explosionX [i], explosionY [i]))

    gameWindow.blit(bomb,(bombX,bombY))

def powerup():
    if powerupD == 1:
        pygame.draw.circle(gameWindow,powerupCLR,(powerupX,powerupY),powerupR,0)
        powerupSymbol = inGameFont.render("P",1,BLACK)
        gameWindow.blit(powerupSymbol,(powerupX-5,powerupY-20))
        
    if doublePoints == True:
            doublePointStatement = inGameFont.render("DOUBLE POINTS",1,YELLOW)
            gameWindow.blit(doublePointStatement,(320,20))

    if specialBoostCondition == True:
        if arcadeMode == True:
            specialBoostStatement = inGameFont.render("+1 10 Seconds",1,YELLOW)
        if classicMode == True:
            specialBoostStatement = inGameFont.render("+1 Life",1,YELLOW)
            gameWindow.blit(specialBoostStatement,(260,20))

def fruit():
    for i in range(fruitSpawn):
        if drawing [i] == 1:
            if typeFruit [i] == 1:
                gameWindow.blit(apple,(objectX [i],objectY [i]))
                objectR [i] = 25
            if typeFruit [i] == 2:
                gameWindow.blit(orange,(objectX [i],objectY [i]))
                objectR [i] = 30
            if typeFruit [i] == 3:
                gameWindow.blit(watermelon,(objectX [i],objectY [i]))
                objectR [i] = 50
            if typeFruit [i] == 4:
                gameWindow.blit(cabbage,(objectX [i],objectY [i]))
                objectR [i] = 40
            if typeFruit [i] == 5:
                gameWindow.blit(tomato,(objectX [i], objectY [i]))
                objectR [i] = 50

def distance_A((x1, y1), (x2, y2)):
    return (sqrt((x1-x2)**2 + (y1-y2)**2))

def distance_B((x1, y1), x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)     #different variations of the same distance calculator
                                             # ex: cursor and cursor vs two points and cursor
def distance_C(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def endGame():
    if timeUp == True:
        timeUpStatement = inGameFont.render("Time's Up!",1,WHITE)
        gameWindow.blit(timeUpStatement,(380,280))
    if livesOut == True:
        livesOutStatement = inGameFont.render("No More Lives!",1,WHITE)
        gameWindow.blit(livesOutStatement,(360,280))


def redrawGameWindow():
    gameWindow.fill(WHITE)
    background()
    if oneTimeUse == True:
        countdown()


    drawScoreboard(seconds)
    
    fruit()          
    bombAndExplosion()
    powerup()

    endGame()

    
    sword(position)
    
    pygame.display.update()

            
def gameOver(seconds):                  # Displays all gameover screen  drawings
    gameWindow.fill(BLACK)
    
    gameOverWord = titleFont.render("GAME OVER",1,YELLOW)
    copyRight = inGameFont.render("By: Theodore Liu Copyright 2018 " , 1, WHITE)
    gameWindow.blit(gameOverWord,(190,400))

    scoreBoard = inGameFont.render(str(score),1,WHITE)
    gameWindow.blit(scoreBoard,(740,20))

    scoreHeading = inGameFont.render("Score:",1,WHITE)
    gameWindow.blit(scoreHeading,(640,20))

    if arcadeMode == True:

        timerHeading = inGameFont.render("Time in Game:",1,WHITE)
        gameWindow.blit(timerHeading,(20,20))

        countingDisplay = inGameFont.render(str(seconds),1,WHITE)
        gameWindow.blit(countingDisplay,(220,20))
    
    gameWindow.blit(titlePicture,(180,200))
    gameWindow.blit(copyRight,(190,520))
    
    pygame.display.update()
    pygame.time.delay(20)

#-------------------------------------------------------------------------------------#
# the main program begins here                                                        #
#-------------------------------------------------------------------------------------#


# Pygame Initialization------------------------------#    
pygame.init()

# Fonts
titleFont = pygame.font.SysFont("Impact",80)
inGameFont = pygame.font.SysFont("Impact",30)
font = pygame.font.SysFont("Impact",60)

# Sounds
sliceFruit = pygame.mixer.Sound("Slice.wav")
sliceFruit.set_volume(0.6)
death = pygame.mixer.Sound("EndGame.wav")
death.set_volume(0.4)


# Pictures
titlePicture = pygame.image.load("titlePicture.png")
logo = pygame.image.load("logo.png")

background1 = pygame.image.load("background1.png")
background2 = pygame.image.load("background2.png")
background3 = pygame.image.load("background3.png")

apple = pygame.image.load("apple.png")
orange = pygame.image.load("orange.png")
watermelon = pygame.image.load("watermelon.png")
cabbage = pygame.image.load("cabbage.png")
tomato = pygame.image.load("tomato.png")

bomb = pygame.image.load("bomb.png")


#Music
pygame.mixer.music.load("theme.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

# Main Loop-----------------------------------------#

print "Fruit Ninja - Controls: "
print ""
print "1. Move your sword with the cursor"
print ""
print "2. Hold down to perform swipes, you can hold for as long"
print "   as you want, you can't go off screen."

print ""
print "Fruit Ninja - Rules: "
print ""
print "1. Swipe fruit with your sword to earn points."
print "2. Do not touch bombs, which end the game instantly"
print "3. Along with fruit, bombs, and powerups all of these"
print "   spawn from the bottom of the gameWindow and fall back down"
print "3. There is a 10 second doubling powerup that is labelled P"
print "4. And a increase of time or lives powerup."
print "5. Two Main game modes are Arcade and Classic."
print "   In Classic, when a fruit falls back down that results in a lost life"
print "   You have 10 lives to start"
print "   In arcade, there are no lives and no penalty for dropping fruit"
print "   However, as a result there is a time limit to 100 seconds"
print ""
print "   Overall classic is harder, and arcade is better for beginners"
print "   Note: Yin Yang Stage is faster and the hardest stage."
print "   The other two stages are the same difficulty"
print "6. Good Luck and Have Fun!"
print ""
print "Click ESC to exit the game at any point in time"


while inPlay:

    while inMenu:
        
        pygame.event.get()
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_ESCAPE]:
            inMenu = False
            inPlay = False
            
        elif keys[pygame.K_SPACE]:
            inMenu = False
            inSelect = True
            
        else:
            drawMenu()

    while inSelect:

        selectScreen()

        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                (cursorX,cursorY)=pygame.mouse.get_pos()
                
                for i in range(3):  #check if on-screen buttons ahve been clicked
                    
                    if distance_C(cursorX, cursorY, buttonX [i], buttonY [1] ) <= BUTTON_R and i != 1:                       
                        if i == 0:
                            classicMode = True
                            choiceColour [3] = YELLOW
                            choiceColour [4] = WHITE
                        elif i == 2:
                            arcadeMode = True
                            choiceColour [4] = YELLOW
                            choiceColour [3] = WHITE
                        else:
                            classicMode = True      #just incase they don't select anything

                    if distance_C(cursorX, cursorY, buttonX [i], buttonY [0] ) <= BUTTON_R:

                        choiceColour [i] = YELLOW

                        if i == 0:
                            backgroundInput = 1
                            choiceColour [1] = WHITE
                            choiceColour [2] = WHITE
                        elif i == 1:
                            backgroundInput = 2
                            choiceColour [0] = WHITE                            # Conditions for when checking each of the three buttons based on their x values (bottom buttons (buttonY [1])
                            choiceColour [2] = WHITE                            # and checking if they have been clicked or not, resets if a player clicks hard then changes mind to easy
                        else:
                            backgroundInput = 3
                            choiceColour [0] = WHITE
                            choiceColour [1] = WHITE


        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            inSelect = False
            inPlay = False
        if keys[pygame.K_RSHIFT]:
            inSelect = False
            inGame = True

        
    
    BEGIN = time.time()
    while inGame:

        
        seconds = round((time.time()-BEGIN),2)

        #Event Checks-------#       
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                press = 1

            if event.type == pygame.MOUSEBUTTONUP:
                press = 0

            if event.type == pygame.MOUSEMOTION:
                position = pygame.mouse.get_pos()
                me = True
        

                for i in range(fruitSpawn):     #checking if cursor is in fruit radius
                    if distance_B(position,objectX [i] +objectR [i],objectY [i]+objectR [i]) < objectR [i] and press == 1:
                        if conditionB [i] == 1:     #one copy is created based on condition
                            positioncopy [i] = pygame.mouse.get_pos()
                            conditionB [i] = 0
                            conditionA [i] = 1
                
                    if conditionA [i] == 1 and press == 1:  # check if new position of cursor is 10 pixels away (ie: decently large cut)
                        position = pygame.mouse.get_pos()
                        if distance_A(position,positioncopy [i]) >= 10:
                            
                            if distance_B(position,objectX [i]+ objectR [i] ,objectY [i]+objectR [i]) > objectR [i]:    #check if cursor has left
                                drawing [i] = 0
                                comboCheck [i] = seconds
                                if comboScore == False:     #check for combos (ie: fruit that have been sliced within 0.25 seconds)
                                    for k in range(fruitSpawn):
                                        if  0 < comboCheck [i] - comboCheck [k] < 0.25:
                                            comboScore = True
                                
                                explosionX [i] = objectX [i]
                                explosionY [i] = objectY [i]
                                if conditionC [i] == 1:         #one time use,add points and reset variables
                                    goneFruit = goneFruit+1
                                    conditionC [i] = 0
                                    score = score+point
                                    sliceFruit.play()
                                    conditionB [i] = 1
                                    conditionA [i] = 0
                                    explosion [i] = 1
                                    comboCheck [i] = seconds
                                    if comboScore == True:              #add extra points for combos        
                                        score = score+point
                                        comboScore = False
                                        comboDisplay = True
                                        conditionD = 1
           

                    if press == 1 and distance_B(position,powerupX,powerupY) < 35:  #power up check
                        powerupY = 640
                        powerupX = randint(40,760)
                        powerupD = 2
                        if powerupCLR == YELLOW:
                            doublePoints = True
                        else:
                            specialBoost = True        
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inGame = False
                    inPlay = False
        #Event Checks-------#

        #Game Mechanics

        for i in range(fruitSpawn):     #Explosion animation

            if explosion [i] == 1:
                explosionAnimation = [1,2,3,4,5]
                for j in range(6):
                    explosionPic [j] = pygame.image.load("explosion" +str(j) + ".png")
                explosionPicNum = explosionAnimation [explosionPicNum]
                if explosionPicNum == 5:
                    explosionPicNum = 0
                    explosion [i] = 0

        if bombSpawn == True:           #random bomb generator
            bombD = randint(1,200)

        if bombD == 1:
            bombSpawn = False
            bombVy = bombVy + GRAVITY
            bombY = bombY + bombVy
            if bombY > 620:
                bombY = 620
                bombX = randint(0,740)
                bombVy = randint(-48,-38)
                bombSpawn = True


        if powerupSpawn == True:                    #power up generator
            powerupD = randint(1,200)

            powerupCustom = randint(1,2)
            powerupVy = randint(-40,-30)
            if powerupCustom == 1:
                powerupCLR = YELLOW
            else:
                powerupCLR = BLUE
                
        if powerupD == 1:
            powerupSpawn = False
            powerupVy = powerupVy + GRAVITY
            powerupY = powerupY + powerupVy
            if powerupY > 640:
                powerupY = 640
                powerupX = randint(40,760)
                powerupVy = randint(-48,-38)
                powerupSpawn = True

        if doublePoints == True:                # 10 second doubling point conditions
            point = 2
            if timerCondition == 1:
                timerStart = seconds
                timerCondition = 0
            if  seconds >= timerStart + 10:

                point = 1
                doublePoints = False
                timerCondition = 1
                powerupSpawn = True

                                            #either increases time or increases lives
        if specialBoost == True:
            lives = lives+ 1
            timerModifier = timerModifier + 1
            specialBoostCondition = True
            specialBoost = False

        for i in range(timerModifier):          #will allow timer to add 10 seconds
            seconds = seconds - 10

        if specialBoostCondition == True:
            counter = counter+1
            if counter > 20:
                specialBoostCondition =  False
                powerupSpawn = True
        
        for i in range(fruitSpawn):                 #Fruit generator
            objectVy [i] = objectJumpSpeed [i]
            objectJumpSpeed [i] = objectJumpSpeed [i] + GRAVITY
            objectY [i] = objectY [i] + objectVy [i]
            if objectY [i] >= 600 and drawing [i] == 1:
                goneFruit = goneFruit + 1
                drawing [i] = 0
                lives = lives - 1
                
        if goneFruit == (fruitSpawn):           #check if all fruit are gone start new wave
            goneFruit = 0
            waveSpawn = True

        if waveSpawn == True:
            
            check = check+1             #slight delay allowing player to be prepared for next wave
            if check == checkNum:
                
                extra = randint(1,3)
                fruitSpawn = fruitSpawn + extra
                if fruitSpawn > 10:
                    fruitSpawn = randint(6,9)

                objectX = []
                objectY = []
                objectJumpSpeed =[]
                objectVy = []
                drawing = []
                objectR = []
                typeFruit = []
                conditionA= []
                conditionB= []
                conditionC=[]
                explosionX = []
                explosionY =[]
                explosion = []
                comboCheck = []
                positioncopy = []

                for count in range(fruitSpawn+1):
                    objectX.append(randint(0,700))
                    objectY.append(600)
                    objectJumpSpeed.append(randint(-45,-30))
                    typeFruit.append(randint(1,5))
                    objectVy.append(0)
                    drawing.append(1)
                    objectR.append(0)
                    positioncopy.append(0)
                    conditionA.append(0)
                    conditionB.append(1)
                    conditionC.append(1)
                    explosion.append(0)
                    explosionX.append(0)
                    explosionY.append(0)
                    comboCheck.append(0)

                waveSpawn = False

                check = 0
                checkNum = checkNum - 5
                if checkNum <= 30:
                    checkNum = 20

        #Death conditions-------------#
        
        if lives <= 0 and classicMode == True:
            livesOut = True
            
        if seconds >= 103 and arcadeMode == True:
            timeUp = True

        if press == 1 and distance_B(position,bombX+33,bombY+65) < 33:
            pygame.mixer.music.pause()
            death.play()
            pygame.time.delay(2000)
            inGame = False
            inGameOver = True
            
       
        pygame.time.delay(40)
        
        redrawGameWindow()      #Display everything
        
        oneTimeUse = False

        #Death Displays and combos

        if (lives <= 0 and classicMode == True) or (seconds >= 100 and arcadeMode == True):
            pygame.mixer.music.pause()
            death.play()
            pygame.time.delay(2000)
            inGame = False
            inGameOver = True

        if comboDisplay == True:
            conditionD = conditionD + 1
            if conditionD == 10:
                comboDisplay = False
                comboScore = False

    while inGameOver:               #End Screen
        pygame.mixer.music.unpause()
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            inGameOver = False
            inPlay = False
        else:
            gameOver(seconds)

                
pygame.quit()

# End of Program --------------------------------------------------------------------------------#


        


