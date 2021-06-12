# Fill me in!

### Name: Connor Flynn
### Project Name: !!!PLANET DEFENSE!!!

### Description: the goal of planet defense is to project the earth from an oncoming meteor storm.
### you must destroy 40 meteors in order to win the game but if 3 meteors hit the earth you will lose.
### Title screen will have a messege telling the user to press I in order to open up the info screen for the buttons,
### pressing I again on the Info button will bring you back to the Title screen.  pressing P will bring you to
### the gaming screen.  using the controls provided from the info screen or the instructions comment down below, you can aim the
### barrel and fire the lasers at the meteors in order to remove them and decrease the remaining meteors left.  
### if the ground, laser cannon or the barrel get hit, you will loose a life.  if lives reaches zero, you will be presented
### with a lose screen, if the remaining meteors left is zero, you will win the game.  for both screens you will see
### a text box that will instruct you to press R to reset the game.  if you do you can replay the game as many times as you want.

### Instructions: when first running the program, there are two things that you can do right at the beginning.
### the first thing which you can do is to press I to open up the info menu which will explain the controls of the game, you can
### then press I again if you wish to go back to the main menu screen.  once back there you can do the other thing which is
### to open up the game menu.  you can do that by pressing P.  you will then be shown to a screen with a laser cannon and meteors
### falling from the sky.  you can use A to move the laser's barrel left, D to move the laser's barrel right and K to fire the laser.
### you will want to point the end of the barrel towards the meteors in order to remove them when the laser hits.  when a laser does hit
### a meteor, it will remove that meteor and the laser that hit it and remove one from the remaining meteors you need to
### remove.  If the barrel, the laser gun, or the ground gets hit by a meteor, it will decrease 1 from the remaining lives.
### Once all the meteors have been destroyed, you will be shown to a win screen, if no remaining lives are left you will
### be shown to a lose screen.  For either screen, if you press R, it will return you to the main menu and alow you to replay
### the code as many times as you want.

### Functions: 396 to 423, 440 to 453
### Objects: 70 to 73, 77 to 80, 139 to 141, 148 to 158, 167 to 175, 215, 219, 225, 231, 235, 239 and 242
### Events: 263 and 396
### Complex conditionals: 268, 318, 339, 358, 374, 411 and 417
### properties & methods: 49, 273, 344, 363, 379, 492 and 541
### Loops: 127, 209, 296, 442, 459, 497, 511, 546, 550 and 560

### peer review: restart program button (maybe 'r')(added peer feedback of restart on lines, smaller clusters
### peer review changes on lines 302, 311, 374 to 390, 504 and 557

### Iterations: ###
### Iteration #1: creates the title screen with info and the game screen, the user is able to shoot down meteors
### with the laser cannon.  There is no win or lose parameters so it is just an endless wave of fast moving asteroids.
### Iteration #2: win parameters are created, the user now needs to shoot down 40 asteroids to win the game.  if 3
### asteroids hit the ground, laser cannon or the barrel, the user will lose.  there is no reset button to go
### back to the main menu so if the player wants to play again they need to rerun the program.
### Iteration #3: a reset method is made, now when the user clicks on R on either the win or lose screens,
### it will send the user back to the main menu so they can replay the game.

#sets the background to black when the user runs the code
### Properties & Methods
app.background = 'Black'
#creates the randomStars value
app.randomStars = 0
#creates the starGroup
starGroup = Group()
#creates the meteor amount value
app.meteors = 0
#creates the meteor Group
meteorGroup = Group()
#creates the laser group
app.lasers = Group()
#sets the state of the screen to Title
app.state = 'Title'
#creates the amount of lives the user has
livesAmount = 5
#creates the amount of meteors the user needs to destroy before winning
meteorNumberAmount = 40


#creates the text which will be used when the user wins the game
### Objects
winScreen = Group(
Label('!WINNER!', 200, 200, size = 40, fill='white'))
#sets the winScreens visiblity to False
winScreen.visible=False    

#creates the text which will be used when the user loses the game
### Objects
loseScreen = Group(
Label('You Lose', 200, 200, size= 40,))
#sets the loseScreens visibility to False
loseScreen.visible=False


#creates all the sounds used on the Title screen
titleScreenSound1 = Sound('https://sounds-mp3.com/mp3/0011903.mp3')
titleScreenSound2 = Sound('https://sounds-mp3.com/mp3/0011926.mp3')
titleScreenSound3 = Sound('https://sounds-mp3.com/mp3/0004810.mp3')

#creates the background music for the game screen
gameScreenSound = Sound('https://www.fesliyanstudios.com/download-link.php?src=i&id=618')

#creates the noise of the laser firing
pewPew = Sound('https://www.soundfishing.eu/download.php?id=11881')

#creates the winning sound effect
winSound = Sound('http://soundbible.com/grab.php?id=1003&type=mp3')
#creates the losing sound effect
loseSound = Sound('http://soundbible.com/grab.php?id=1830&type=mp3')

#as long as the app.state is Title, it will play the titleScreen sound effects
if (app.state == 'Title'):
    titleScreenSound1.play(loop=True)
    titleScreenSound2.play(loop=True)
    titleScreenSound3.play(loop=True)
    
#creates the values for the background stars on the Title screen
def drawRandomStars():
    #sets the Size and Opacity of the star between a random range of 8 to 20
    randomSizeAndOpacity = randrange(8,20)
    #randomises the stars centerX
    starCenterX = randrange(0, 400)
    #randomises the stars centerY
    starCenterY = randrange(0,400)
    #imputs the randomised values for the stars
    theStar = Star(starCenterX, starCenterY, randomSizeAndOpacity/2, 4, fill='gold', opacity=randomSizeAndOpacity*5)
    #adds the newly created stars to the star group
    starGroup.add(theStar)
    #sets all the stars to the back of the screen
    theStar.toBack()
    #adds one to the total value of random stars
    app.randomStars += 1

#places the stars from drawRandomStars on screen
def drawStarsInSpace():
    #as long as app.randomStars value is less than or equal to 50, it will
    #continue to add more stars
    ### Loops
    while(app.randomStars <= 50):
        drawRandomStars()
#calls the drawStarsInSpace function
drawStarsInSpace()

#creates the centerX value of the return label on the win and lose screens
menuCenterX = 200
#creates the centerY value of the return label on the win and lose screens
menuCenterY = 300

#creates the return label and text box with the random menu centerX and centerY
### Objects
menuReturn = Group(
Rect(menuCenterX-150, menuCenterY-20, 300, 40, fill='gray', border = 'black'),
Label('Press R to play again', menuCenterX, menuCenterY, size=20))

#sets the menuReturn's visibility to False
menuReturn.visible = False

#creates all the text and text boxes for the Title screen
### Objects
beginningScreen = Group(
Label('!!!PLANET DEFENSE!!!', 200, 80, size=30, bold=True, fill=gradient('white', rgb(120, 120, 120), start='top')),
Label('Earth is being attacked by a meteor storm.', 200, 150, size = 15,  bold=True, fill=gradient('white', rgb(120, 120, 120), start='top')),
Label('you are tasked with destroying', 200, 170, size = 15,  bold=True, fill=gradient('white', rgb(120, 120, 120), start='top')),
Label('the Meteors before they hit earth.', 200, 190, size = 15,  bold=True, fill=gradient('white', rgb(120, 120, 120), start='top')),
Label('if too many meteors hit earth, you will lose.', 200, 210, size = 15,  bold=True, fill=gradient('white', rgb(120, 120, 120), start='top')),
Label('Destroy as many meteors as you can to win.', 200, 230, size = 15,  bold=True, fill=gradient('white', rgb(120, 120, 120), start='top')),
Rect(30, 300, 160, 35, fill='red'),
Rect(210, 300, 160, 35, fill='green'),
Label('press i for info', 110, 317, size = 20, bold=True, fill='white'),
Label('press p to play', 290, 317, size = 20, bold=True, fill='white'))

#creates the text boxes centerX value
rectCenterX = 200
#creates the text boxes centerY value
rectCenterY = 330

#creates the labels and rectangle for the info Screen
### Objects
infoScreen = Group(
Label('-Press p to start the game-', 200, 150, size=20),
Label('-Press a to move the barrel left-', 200, 180, size=20),
Label('-Press d to move the barrel right-', 200, 210, size=20),
Label('-Press k to fire the laser-', 200, 240, size=20),
Rect(rectCenterX-120, rectCenterY, 240, 50, fill='white', border='black'),
Label('press i to return to main menu', rectCenterX, rectCenterY+23, size=16, bold=True))
#sets the infoScreen group to false
infoScreen.visible = False

#gets the values for the meteors
def drawRandomMeteors():
    #as long as the app.state is equal to Game, it will creates
    if (app.state == 'Game'):
        #grabs the image of the meteor
        app.meteorImage = 'https://docs.google.com/drawings/d/e/2PACX-1vSMcLhlkrCQfyUhGJPHb1wCtiOEj-iWKmNEk6sc4MdT3utDpPb0C9ubS3PqNrE9mxsyolEcH69l_jaN/pub?w=322&h=319'
        #gets a random centerX value for each meteor
        meteorCenterX = randrange(15, 375)
        #gets a random centerY value for each meteor
        meteorCenterY = randrange(-2800, -60)
        #imputs the values of the meteor image and centerX and centerY
        meteor = Image(app.meteorImage, meteorCenterX, meteorCenterY)
        #randomizes the rotation angle of each meteor
        meteor.rotation = randrange(-10, 10)
        #gets a random value for the meteors width and height
        meteorWidthAndHeight = randrange(40, 80)
        #imputs the meteor width equal to the random value of meteorWidthAndHeight
        meteor.width = meteorWidthAndHeight
        #imputs the meteor height equal to the random value of meteorWidthAndHeight
        meteor.height = meteorWidthAndHeight
        #adds each meteor created to the meteor group
        meteorGroup.add(meteor)
        #adds 1 to the meteor value
        app.meteors += 1

#creates all the meteors when the game screen is shown
def drawMeteorsInSpace():
    # if the app.state is equal to Game, and app.meteors is less than or equal to 10,
    #drawMeteorsInSpace will keep adding meteors
    if (app.state == 'Game'):
        #while app.meteors is less than or equal to 10, it will add meteors
        ### Loops
        while(app.meteors <= 10):
            #draws the meteor
            drawRandomMeteors()

#creates the ground that will be displayed on the game screen
### Objects
ground = Rect(0, 380, 400, 20, fill='forestGreen')

#creates the lazerGun that will be displayed on the game screen
### Objects
laserGun = Group(
Polygon(50, 400, 100, 350, 300, 350, 350, 400, fill='lightGray'),
Arc(200, 350, 40, 40, -90, 180, fill='dimGray', border='lightGray'))

#creates the barrel that will be displayed on the game screen
### Objects
barrel = Line(200, 350, 200, 300, fill='dimGray', lineWidth = 10)
#moves the barrel to the back of all shapes
barrel.toBack()

#creates the lives and meteors left group that will be displayed on the game screen
### Objects
livesAndMeteorsLeftGroup = Group(
Rect(100, 350, 100, 50, fill=None, border='black'),
Rect(200, 350, 100, 50, fill=None, border='black'),
Label('lives', 150, 385, size=16),
Label('meteors left', 250, 385, size=16))

#the value of how many lives remain before you lose
### Objects
lives = Label(livesAmount, 150, 365, size=18)
#the value of how many meteors remain before you win
### Objects
meteorNumber = Label(meteorNumberAmount, 250, 365, size=18)

#sets the barrel's visibility to False
barrel.visible = False
#sets the laserGun's visibility to False
laserGun.visible = False
#sets the laserGun's visibility to False
ground.visible = False
#sets the lives and meteors left group visibility to False
livesAndMeteorsLeftGroup.visible = False
#sets the lives counter visibility to False
lives.visible = False
#sets the meteor number's visibility to False
meteorNumber.visible = False



#on keyPress function will very depending on the key pressed and the state of app.state.  
#better description for each on key press on each if and elif conditional
### Functions
### Events
def onKeyPress(key):
    
    #if the key that is pressed is P and the app.state is Title,
    #the screen will display the Game Screen
    ### Complex Conditionals
    if (key == 'p' and app.state == 'Title'):
        #sets the app.state to Game
        app.state = 'Game'
        #the app.background is changed to a gradient that looks like the earths atmosphere
        ### Properties & Methods
        app.background = gradient('black', 'navy', 'deepSkyBlue', 'skyBlue', start='top')
        #sets the barrel visibility to True
        barrel.visible = True
        #sets the laser gun visibility to True
        laserGun.visible = True
        #sets the ground's visibility to True
        ground.visible = True
        #sets the beginning screen's visibility to False
        beginningScreen.visible = False
        #sets the star groups visibility to False
        starGroup.visible = False
        #pauses the title screens sound effects
        drawMeteorsInSpace()
        titleScreenSound1.pause()
        titleScreenSound2.pause()
        titleScreenSound3.pause()
        #plays the games screen sound and loops it
        gameScreenSound.play(loop=True, restart=True)
        #draws the meteors in space
        #app.meteors is set to 0
        app.meteors = 0
        #for each meteor, it will set their visibility to True
        ### Loops
        for meteor in meteorGroup.children:
            meteor.visible = True
        #meteor.visible = True
            meteor.toFront()
            meteor.centerX = randrange(15, 375)
            ###peer feedback: make smaller clusters (increased the random range of the meteors from -2400, -60 to -2800, -60) (line 302)
            meteor.centerY = randrange(-2800, -60)
        #sets the visibility of the lives and meteors left label and text boxes to True
        livesAndMeteorsLeftGroup.visible = True
        #sets the lives value visibility to True
        lives.visible = True
        #sets the meteor number's visibility to True
        meteorNumber.visible = True
        ### Peer feedback: restart program button (this part will restart the game screens win/lose values and the barrels placement) (line 311)
        #creates the amount of lives the user has
        lives.value = livesAmount
        #creates the amount of meteors the user needs to destroy before winning
        meteorNumber.value = meteorNumberAmount
        barrel.toBack()
        
    #else if the key is equal to k and the app.state is Game, it will fire the laser from the end of the barrel
    ### Complex Conditionals
    elif (key == 'k' and app.state == 'Game'):
        #sets x1 equal to barrel.x1
        x1 = barrel.x1
        #sets y1 equal to barrel.y1
        y1 = barrel.y1
        #sets x2 equal to barrel.x2
        x2 = barrel.x2
        #sets y2 equal to barrel.y2
        y2 = barrel.y2 
        #finds the angle between x1, y1, and x2, y2
        barrelAngle = angleTo(x1, y1, x2, y2)
        #gets an x and x value based on x1, y1, the angle of the barrel, and 50 pixels away form the x1 and y1.
        #it also sets the lasers length to 20
        x, y = getPointInDir(x1, y1, barrelAngle, 50+20)
        #adds a laser to app.lasers and imputs the x2, y2, x, and y values
        app.lasers.add(Line(x2, y2, x, y, fill='red', lineWidth = 6))
        #the pewPew sound effect will be played and will restart if k is pressed again on app.state equal to Game
        pewPew.play(restart=True)
        
    #else if key is equal to i and app.state is equal to Title, it will display the information screen
    ### Complex Conditionals
    elif (key == 'i' and app.state == 'Title'):
        #app.state is set to Info
        app.state = 'Info'
        #the app.bakcground becomes light Gray
        ### Properties & Methods
        app.background = 'lightGray'
        #the beginning Screen's visibility is set to False
        beginningScreen.visible = False
        #the star group's visibility is set to False
        starGroup.visible = False
        #pauses the title screens sound effects
        titleScreenSound1.pause()
        titleScreenSound2.pause()
        titleScreenSound3.pause()
        #info screen's visibility is set to True
        infoScreen.visible = True
        
    #else if key is equal to I and the app.state is equal to Info, the info screen will return to the main menu
    ### Complex Conditionals
    elif (key == 'i' and app.state == 'Info'):
        #the app.state becomes Title
        app.state = 'Title'
        #the app.background is set to black
        ### Properties & Methods
        app.background = 'black'
        #the beginningScreens visiblity is set to True
        beginningScreen.visible = True
        starGroup.visible = True
        titleScreenSound1.play()
        titleScreenSound2.play()
        titleScreenSound3.play()
        infoScreen.visible = False
        
    ### Peer: restart program button (this part will change the screen back to the main menu screen) (lines 374 to 390)
    ### Complex Conditionals
    elif (key == 'r' and app.state == 'Lose' or key == 'r' and app.state == 'Win'):
        #the app.state becomes Title
        app.state = 'Title'
        #the app.background is set to black
        ### Properties & Methods
        app.background = 'black'
        #the beginningScreens visiblity is set to True
        beginningScreen.visible = True
        starGroup.visible = True
        menuReturn.visible = False
        if (winScreen.visible == True):
            winScreen.visible = False
        elif (loseScreen.visible == True):
            loseScreen.visible = False
        titleScreenSound1.play()
        titleScreenSound2.play()
        titleScreenSound3.play()


#on key hold function
### Functions
### Events
def onKeyHold(keys):
    #sets x1 equal to barrel.x1
    x1 = barrel.x1
    #sets y1 equal to barrel.y1
    y1 = barrel.y1
    #sets x2 equal to barrel.x2
    x2 = barrel.x2
    #sets y2 equal to barrel.y2
    y2 = barrel.y2
    #finds the angle between x1, y1, and x2, y2
    barrelAngle = angleTo(x1, y1, x2, y2)
    
    #as long as A is pressed down and the app.state == 'Game', and the barrelAngle is greater
    #than or equal to 270 or is less than or equal to 96, it would decrease the barrel degree. (move left)
    ### Complex Conditionals
    if ('a' in keys and app.state == 'Game' and (barrelAngle >= 270 or barrelAngle <= 96)):
        barrelAngle -= 6
        
    #as long as D is prssed down and the app.state == 'Game', and the barrelAngle is less
    #than or equal to 90 or is greater than or equal to 263, it would increase the barrel degree. (move right)
    ### Complex Conditionals
    elif ('d' in keys and app.state == 'Game' and (barrelAngle <= 90 or barrelAngle >= 263)):
        barrelAngle += 6
        
    #if the y2 is greater than or equal to 350, its angle will increase
    if y2 >= 350:
        barrelAngle += 1
        
    #if the y2 is less than or equal to 350, its angle will decrease
    if y2 >= 350:
        barrelAngle -= 1
    #get an x and a y value based on the x1 value, y1 value, the angle of the barrel, and a distance of 50
    x, y = getPointInDir(x1, y1, barrelAngle, 50)
    #the barrels x2 value becomes equal to the new x value
    barrel.x2 = x
    #the barrels y2 value becomes equal to the new x value
    barrel.y2 = y


#on step function
def onStep():
    
    #if the app.state is equal to Title, it will move the stars to right in a constant loop
    if (app.state == 'Title'):
        #all individual stars move at different speeds based on their opacity
        ### Loops
        for theStar in starGroup.children:
            #a opacity divided by 100 will be added to the stars centerX value
            theStar.centerX += theStar.opacity/100
            
            #moves a star all the way past the left side of the screen in
            #case the star goes off the right side of the screen
            if (theStar.centerX > 410):
                #the stars centerX will have a random range between -30 and -10
                theStar.centerX = randrange(-30, -10)
                #the stars centerY will have a random range between 0 and 400
                theStar.centerY = randrange(0, 400)
                
    #if the app.state is equal to Game, it will start to move the meteors to the bottom of the screen   
    if (app.state == 'Game'):
        #for each individual meteor in meteor Group, it will rotate using the meteor.ration and it will
        #move each meteor down by 5
        ### Loops
        for meteor in meteorGroup.children:
            meteor.rotateAngle += meteor.rotation
            meteor.centerY += 5
            
            #if a meteor hits the ground, the barrel, or the laser gun, it will decrease the lives value by 1
            if (meteor.hitsShape(ground) or meteor.hitsShape(barrel) or meteor.hitsShape(laserGun) == True ):
                lives.value -= 1
                
                #if the value of lives is less than or equal to 0, it will set the screen to the losing screen
                if (lives.value <= 0):
                    # loosing spot
                    #sets the app.state to Lose
                    app.state = 'Lose'
                    #the menu return's visibility is True
                    menuReturn.visible = True
                    #the lose screen's visibility is set to True
                    loseScreen.visible = True
                    #the barrel's visibility is set to False
                    barrel.visible = False
                    #the laser Gun's visibility is set to False
                    laserGun.visible = False
                    #the ground's visibility is set to False
                    ground.visible = False
                    #the lives and meteors visibility is set to False
                    livesAndMeteorsLeftGroup.visible = False
                    #the visiblity of the label for the remaining amount of lives is set to False
                    lives.visible = False
                    #the visibility of the label for the remaining amount of meteors left is set to False
                    meteorNumber.visible = False
                    #the losing sound is played
                    loseSound.play()
                    #the app.background is changed to red
                    ### Properties & Methods
                    app.background = 'red'
                    #pauses the background music of the gameScreen
                    gameScreenSound.pause()
                    #sets the visibility of a single meteor to false if it hits a laser
                    ### Loops
                    for meteor in meteorGroup.children:
                        meteor.visible = False
                #moves the centerX of a meteor when hit by a laser
                meteor.centerX = randrange(15, 375)
                #moves the centerY of a meteor when hit by a laser
                ### Peer feedback: make smaller clusters (increased the random range of the meteors from -2400, -60 to -2800, -60) (line 504)
                meteor.centerY = randrange(-2800, -60)
                
            #if a meteor hits a laser, it will remove that laser and decrease 
            #the meteor value by one
            if (meteor.hitsShape(app.lasers) == True):
                #for every individual laser, if it hits a meteor it will remove a
                #laser from the app.lasers group and decrease the meteor needed to destroy by one
                ### Loops
                for laser in app.lasers.children:
                    if laser.hitsShape(meteor):
                        app.lasers.remove(laser)
                        meteorNumber.value -= 1
                        #if the meteors that you need to destroy is less than or equal to 0,
                        #then the win screen will be displayed
                        
                        if (meteorNumber.value <= 0):
                            #the app.state is set to Win
                            app.state = 'Win'
                            #menu Return group's visibility is set to True
                            menuReturn.visible = True
                            #sets the win screen group's visibility is set to True
                            winScreen.visible = True
                            #sets the barrel group's visibility is set to True
                            barrel.visible = False
                            #sets the laser gun's visibility to False
                            laserGun.visible = False
                            #sets the ground's visibility to False
                            ground.visible = False
                            #sets the lives and meteor's left group's visiblity to False
                            livesAndMeteorsLeftGroup.visible = False
                            #sets the lives visibility to False
                            lives.visible = False
                            #sets the meteor number's visiblity to False
                            meteorNumber.visible = False
                            #plays the win sound effect
                            winSound.play()
                            #sets the app.background to green
                            ### Properties & Methods
                            app.background = 'green'
                            #pauses the game screen sound effect
                            gameScreenSound.pause()
                            #every laser that is still on screen when you win will become invisible
                            ### Loops
                            for laser in app.lasers.children:
                                laser.visible = False
                            #every meteor that is still on screen will become invisible
                            ### Loops
                            for meteor in meteorGroup.children:
                                meteor.visible = False
                #sets the centerX of individual meteors to a random range between 15 to 375
                meteor.centerX = randrange(15, 375)
                #sets the centerY of individual meteors to a random range between -2800 to -60
                ### Peer feedback: make smaller clusters (increased the random range of the meteors from -2400, -60 to -2800, -60) (line 557)
                meteor.centerY = randrange(-2800, -60)
    #moves every laser in the direction the barrel is facing
    
    ### Loops
    for laser in app.lasers.children:
        #x1 equals the lasers x1
        x1 = laser.x1
        #y1 equals the lasers y1
        y1 = laser.y1
        #x2 equals the lasers x2
        x2 = laser.x2
        #y2 equals the lasers y2
        y2 = laser.y2
        #sets the laser angle between x1, y1 and x2, y2
        laserAngle = angleTo(x1, y1, x2, y2)
        #x3 and y3 points are determined based on x1, y1, the laser angle, and 10 points infront of x1 and y1
        x3, y3 = getPointInDir(x1, y1, laserAngle, 10)
        #x4 and y4 points are determined based on x2, y2, the laser angle, and 10 points infront of x2 and y2
        x4, y4 = getPointInDir(x2, y2, laserAngle, 10)
        
        #if the laser hits the edge of the screen in any direction, it will be removed, else it will continue moving
        if (x3 >= 400 or x3 <= 0 or y3 >= 400 or y3 <= 0):
            #removes the laser from the laser group
            app.lasers.remove(laser)
            
        else:
            #laser x1 becomes equal to x3
            laser.x1 = x3
            #laser y1 becomes equal to y3
            laser.y1 = y3
            #laser x4 becomes equal to x4
            laser.x2 = x4
            #laser y4 becomes equal to y4
            laser.y2 = y4


        



