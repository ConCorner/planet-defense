# Fill me in!

### Name: Connor Flynn
#### project name: the 1, 2, 3 project (or the angle and Distance project) 
###When the user starts up the program, it will send the origin shape, also known as createShape, to a random X and Y position on the graph.  After they run
###the program the user can then click on the screen to create the second shape also known as shape2.  once they click on the screen to create shape2
###the third shape known as shape3 will appear at the same distance and angle as createShape is to shape2, only it will start at shape2 instead of createShape.
### how to control:
###click the run button to set a random centerX and centerY for the origin shape(createShape)
###click mouse on screen to create the second shape(shape2)
###once shape2 is created, the third shape(shape3) will be created at the same distance
###and angle of createShape and shape2 but starting from shape2 instead of createShape

#lines 15-18 creates the first shape which has a random centerX and centerY to it
#all shapes follow createShape's mouseX and mouseY
createShape = Circle(randrange(50,350), randrange(50,350), 20, fill=None, border='red')
Star(createShape.centerX, createShape.centerY, createShape.radius,3, fill=gradient('yellow', 'orange', 'red'), rotateAngle=180)
Star(createShape.centerX, createShape.centerY, createShape.radius,3, fill=gradient('yellow', 'orange', 'red'))
Label('Origin', createShape.centerX, createShape.centerY)

labelAlign = 84                                                                                         #aligns distance and angle labels

#lines 23-25 creates the Labels for distance and the distValue's alignment which is used to display the Distance title.
dist = Label('distance = ', 25, 10, align='left')
dist.right = labelAlign
distValue = Label('0', 85, 10)

#lines 28-30 creates the Labels for angle and the angleValue's alignment which is used to display the Angle title.
angle = Label('angle = ', 25,25, align='left')
angle.right = labelAlign
angleValue = Label ('0', 85,25)

#when the mouse button is clicked it will create the second shape known as shape2 followed by the third shape or shape3 which uses the same angle and distance between Origin and second shape
#in order to create the third shape followed after the second shape.
def onMousePress(mouseX, mouseY):
    
    #lines 38-46 create the second shape which is created on MouseX and Mouse Y when the mouse is clicked.
    #all shapes follow shape2's mouseX and mouseY.
    shape2 = Circle(mouseX, mouseY, createShape.radius, fill = 'pink')                                  
    Oval(shape2.centerX-10, shape2.centerY-5, 8, 12, fill='white')
    Oval(shape2.centerX+10, shape2.centerY-5, 8, 12, fill='white')
    Rect(mouseX-25, mouseY-12, 50, 5)
    Rect(mouseX-15, mouseY-27, 30, 20)
    Circle(mouseX-10, mouseY-3, 3, fill='brown')
    Circle(mouseX+10, mouseY-3, 3, fill='brown')
    Rect(mouseX-5, mouseY+11,10, 2)
    Label('Second', shape2.centerX, shape2.centerY+5)
    
    textAlign = 86                                                                                      #aligns distance and angle output    

    #gets the distance from the origin's shape centerX and centerY to the second shape's centerX and centerY and then prints that in the console.
    D = distance(createShape.centerX, createShape.centerY, shape2.centerX, shape2.centerY)
    print('distance', D)
    
    #gets the angle from the origin's shape centerX and centerY to the second shape's centerX and centerY and then prints that in the console.
    A = angleTo(createShape.centerX, createShape.centerY, shape2.centerX, shape2.centerY)
    print('angle', A)
    
    #lines 59-62 display the values of D(distance) and A(Angle) between the origin circle and second circle and aligns the distance and angle Labels to the left.
    distValue.value = D
    distValue.left = textAlign
    angleValue.value = A
    angleValue.left = textAlign
    
    #lines 69-73 creates the thrid shape known as shape3.  it calculates the centerX and centerY of the second shape(shape2) and its Angle and distance
    #from the first shape(createShape) to find the X and Y values for the third shape(shape3).  once the button is pressed and the second shape is created,
    #the third shape will be created at the same distance and angle as the second shape is from the first shape but instead of starting from the first shape,
    #the third shape will start from the second shape.
    #all shapes for shape3 use the X and Y values of getPointInDir
    x,y = getPointInDir(shape2.centerX, shape2.centerY, A, D)
    shape3 = Polygon(x-17, y-45, x-30, y+10, x, y+40, x+30, y+10, x+17, y-45, x+15, y, x-15, y)
    Circle(x,y,20, fill='white')
    Circle(x,y,15)
    Label('Third', shape3.centerX, shape3.centerY+5, fill='white')
    #end
    pass

    