### This file was copied from CS 1 '19-'20 on 2021-04-06.

# Fill me in!

#background
Rect(0, 0, 400, 400, fill='white')

#background of the fruit
innerCircle = Circle(180, 180, 150, fill=gradient('darkOrange', 'darkOrange', 'white'))

#all gears
Gear1 = Star(100, 130, 40, 7, fill='grey', roundness=40)
Circle(100, 130, 10)
Gear2 = Star(160, 160, 40, 7, fill='grey', roundness=40)
Circle(160, 160, 10)
Gear3 = Star(220, 190, 40, 7, fill='grey', roundness=40)
Circle(220, 190, 10)
Gear4 = Star(125, 225, 40, 7, fill='grey', roundness=40, rotateAngle=-20)
Circle(125, 225, 10)
Gear5 = Star(250, 260, 40, 7, fill='grey', roundness=40, rotateAngle=-20)
Circle(250, 260, 10)
Gear6 = Star(275, 150, 40, 7, fill='grey', roundness=40, rotateAngle=-20)
Circle(275, 150, 10)
Gear7 = Star(170, 280, 40, 7, fill='grey', roundness=40, rotateAngle=-30)
Circle(170, 280, 10)
Gear8 = Star(215, 115, 40, 7, fill='grey', roundness=40, rotateAngle=-28)
Circle(215, 115, 10)




#green stems of the fruit
Rect(185, 8, 20, 60, fill='green', rotateAngle=30)
Rect(180, 12, 15, 60, fill='green', rotateAngle=-20)

#the border of the fruit
outerCircle = Circle(180, 180, 150, fill=None, border='orange', borderWidth=50)


#turns orange into Apple when pressed
def onMousePress(mouseX, mouseY):
    innerCircle.fill = gradient('crimson', 'crimson', 'white')
    outerCircle.border = 'red'
    pass

#turns apple back into an Orange when pressed
def onMouseRelease(mouseX, mouseY):
    pass
    innerCircle.fill = gradient('darkOrange', 'darkOrange', 'white')
    outerCircle.border = 'orange'


#Turns all Gears when mouse moves
def onMouseMove(mouseX, mouseY):
    pass
    Gear1.rotateAngle +=2
    Gear2.rotateAngle -=2
    Gear3.rotateAngle +=2
    Gear4.rotateAngle +=2
    Gear5.rotateAngle -=2
    Gear6.rotateAngle -=2
    Gear7.rotateAngle -=2
    Gear8.rotateAngle +=2