# Fill me in!

### Name: Connor Flynn
###Project name: Alien space trip

###Description:  when the User runs the program, it will ask the user to imput the names of 5 colors of their choice.
### Once the colors are imputed, it will set the circles to the colors you imputed and the labels down below it from left to right by
### the first imputed color to the last imputed color.
### it will also create 50 stars in the background at random X and Y values with a random opacity and ships which move constantly to the right by one.
### when a ship reaches an X value of 430 or greater, it will be sent all the way to X value -480.
### When the user clicks on a Colored circle, it will then assign a value called app.color to that circles color.  Then when the User clicks a ship,
### it will assign that individual ships color to the color of the previous circle that the user clicked.

###Instructions:  
### step 1: Imput 5 color names of built in colors.  (built in colors can be found under the Docs + Colors tab)
### step 2: once you have imputed the 5 colors, a screen displaying circles with the colors you
### chose and labels underneath those circles with the names of the colors should be shown at the bottom of the canvas.  
### right above the ciricles, there should be a group of ships moving to the right of your canvas with a collection of stars behind them.
### step 3: click on one of the color Circles at the bottom of the canvas.  once done you can click the ships to change their colors
### to the color of the circle you had just clicked before.  you will also see at this time that the ships loop back when they reach too
### far to the right of the canvas as they get moved to the left side of the canvas.

### String List (located on line 60)
### functions and return loops (located on lines 87, 100, 127, 142, and 146)
### while loops (located on lines 58 and 89)


#sets the app.color equal to gray.  this is the color used by the ship base layer
app.color = 'gray'

#sets the canvas background to black
app.background = 'black'

#creates the group used for the circles fill at the bottom of the canvas
colorCircles = Group()

#creates the group used for the ships on the canvas
grayShips = Group()

#creates the group of designs for each Ship
shipsDesign = Group()

#sets the app.star value to 0
app.stars = 0

#sets the app.colorListNum value to 1
colorListNum = 1

#creates a list of colors
colors = []





#as long as colorListNum is less than or equal to 5, it will send a getTextInput
#to the user so they can add a color.  once they imput a color it is added to the end of the colors list
### While Loop
while (colorListNum <= 5):
    ###String list
    color = app.getTextInput('Add a color. please make sure the color you choose if available from the color doc in CMU.')
    colors.append(color)
    #adds one to the colorListNum
    colorListNum += 1



#creates the X, Y and opacity values for the stars and the stars themselfs
def drawStars():
    #sets the stars centerX value to a random range between 0 to 400
    starCenterX = randrange(0, 400)
    #sets the stars centerY value to a random range between 0 to 320
    starCenterY = randrange(0, 320)
    #sets the stars opacity to a random value between 40 to 100
    randomOpacity = randrange(40, 100)
    #creates an individual star using the starCenterX, starCenterY, and randomOpacity
    theStar = Star(starCenterX, starCenterY, 10, 4, fill='gold', opacity=randomOpacity)
    #sets all the stars in theStar to the back of the canvas behind the ships
    theStar.toBack()
    #adds 1 to the app.stars value
    app.stars += 1



### Function with Return & For Loop
#places a maximum of 50 stars on the canvas
def drawStarsInSpace():
    #as long as the app.stars value is less than or equal to 50, it will keep adding stars
    ### While Loop
    while(app.stars <= 50):
        #calls the drawStars function
        drawStars()
#returns the drawStarsInSpace function
drawStarsInSpace()



### Function with Return & For Loop
#places the colors in circles at the bottom of the canvas and adds a label below the circles telling what color it is
def drawColorCircles():
    
    #assigns the X value to the first circle in the colorCircles group
    colorX = 30
    #assigns the Y value to the first circle in the colorCircles group
    colorY = 350

    #creates enough circles for all the values in the colors list
    for i in range(len(colors)):
        #creates labels using the vlues from the colors list.
        #places the label on the colorX and then 85 pixels to the right for the next circle
        #places the label on the colorY with an additional 35 pixels down
        Label(colors[i], colorX+ i * 85, colorY+35, fill='white', bold = True, size=14)
        #adds a circle to colorCircles group which displays the color presented to the colors List
        #places the circle on the colorX and then 85 pixels to the right for the next circle
        #places the circle on the colorY with an additional 35 pixels down
        colorCircles.add(
            Circle(colorX+ i * 85, colorY, 25, fill=colors[i], border='white',
                   borderWidth=3)
            )
#returns the drawColorCircles function
drawColorCircles()



### Function with Return & For Loop
#places all the ships on the screen
def drawGrayShips():
    #places all the ships in a range between 30 and 480 in intervals of 80 on the X axis 
    for centerX in range(30, 481, 80):
        #places all the ships in a range between 40 and 280 in intervals of 80 on the Y axis 
        for centerY in range(40, 281, 80):
            #adds each shape on the centerX and centerY values for the ranges above
            grayShips.add(Group(Oval(centerX, centerY, 60, 30, fill='gray'), Circle(centerX, centerY-10, 15, fill='gray')))
            
#returns the drawGrayShips function
drawGrayShips()



### Function with Return & For Loop
#places the design of the ships on the screen
def drawShipsDesign():
    #assigns the circleDesign to 'dimGray' fill
    circleDesign = 'dimGray'
    #places all the ship designs in a range between 30 and 480 in intervals of 80 on the X axis 
    for centerX in range(30, 481, 80):
        #places all the ship designs in a range between 40 and 280 in intervals of 80 on the Y axis
        for centerY in range(40, 281, 80):
            #adds shapes to the shipsDesign group
            shipsDesign.add(
            #creates a circle to the left of centerX by 22 and down 2 from centerY
            #uses circleDesign for the circles fill
            Circle(centerX-22, centerY+2, 4, fill=circleDesign),
            #creates a circle to the left of centerX by 12 and down 5 from centerY
            #uses circleDesign for the circles fill
            Circle(centerX-12, centerY+5, 4, fill=circleDesign),
            #creates a circle to the right of centerX by 12 and down 5 from centerY
            #uses circleDesign for the circles fill
            Circle(centerX+12, centerY+5, 4, fill=circleDesign),
            #creates a circle to the right of centerX by 22 and down 2 from centerY
            #uses circleDesign for the circles fill
            Circle(centerX+22, centerY+2, 4, fill=circleDesign),
            #creates a circleusing centerX and down 8 from centerY
            #uses circleDesign for the circles fill
            Circle(centerX, centerY+8, 6, fill=circleDesign),
            #creates an arc using centerX and down 12 from centerY
            Arc(centerX, centerY-12, 20, 20, -90, 180, fill=gradient('white', 'yellow', 'gold')))

#returns the drawShipsDesign function 
drawShipsDesign()



### Function with Return & For Loop
#on step moves the ships and the ship designs
def onStep():
        
        #selects every individual ship from grayShips
        for Ship in grayShips.children:
            #moves all the ship's to the right by 1
            Ship.centerX += 1
            #when an individual ship's centerX reaches 430, that ship will return its centerX to -480 
            if (Ship.centerX >= 430):
                Ship.centerX -= 480
        #selects every individual ship design from shipsDesign
        for design in shipsDesign.children:
            #moves all the ship's design to the right by 1
            design.centerX += 1
            #when an individual ship design's centerX reaches 430, that ship design will return its centerX to -480
            if (design.centerX >= 430):
                design.centerX -= 480
                
#returns the onStep function
onStep()




#onMousePress works when the mouse is clicked
def onMousePress(mouseX, mouseY):

    #when the user clicks on one of the color circles,
    #it will assign it to the app.color fill
    changeColorCircles = colorCircles.hitTest(mouseX, mouseY)
    #as long as the mouse clicks something from the changeColorCircles, it will make the changeColorCircles fill equal to app.color
    if(changeColorCircles != None):
        app.color = changeColorCircles.fill
    #prints out the value of app.color to the console
    print(app.color)
    
    #when the user clicks an individual ship, it will change its color to whatever,
    #is assigned to app.color
    fillShip = grayShips.hitTest(mouseX, mouseY)
    #as long as the mouse clicks something from the fillship, it will make the turn the ships fill that the user clicks equal to app.color
    if (fillShip != None):
        fillShip.fill = app.color
        
        
        
