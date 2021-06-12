### This file was copied from CS 1 '19-'20 on 2021-04-06.

# Fill me in!

#the sky and its lighting
Sky = Rect(0, 0, 400, 400, fill=gradient('darkBlue', 'blue'), opacity=60)
Rect(0, 0, 400, 400, fill=gradient('gold', 'navy'), opacity=30)
Sky2 = Rect(0, 0, 400, 400, opacity=10)

#the sun
Sun = Star(200, 270, 50, 90, roundness=70, fill=gradient('gold', 'yellow', 'maroon'))
leftEye = Circle(185, 255, 5, fill='yellow')
rightEye = Circle(215, 255, 5, fill='yellow')
mouth = Rect(185, 280, 30, 5, fill='yellow')

#the stars
Star1 = Star(50, 15, 10, 4, fill='yellow', opacity=40)
Star2 = Star(260, 85, 10, 4, fill='yellow', opacity=40)
Star3 = Star(110, 125, 10, 4, fill='yellow', opacity=40)
Star4 = Star(25, 150, 10, 4, fill='yellow', opacity=40)
Star5 = Star(350, 115, 10, 4, fill='yellow', opacity=40)
Star6 = Star(360, 40, 10, 4, fill='yellow', opacity=40)
Star7 = Star(170, 60, 10, 4, fill='yellow', opacity=40)
Star8 = Star(220, -10, 10, 4, fill='yellow', opacity=40)




#the ground
Ground = Rect(0, 300, 400, 100, fill=gradient('darkGreen', 'green'), opacity=100)

#trees and apples
treetrunk1 = Rect(70, 250, 10, 50, fill=rgb(130, 40, 0))
treeTrunk2 = Rect(245, 250, 10, 50, fill=rgb(130, 40, 0))
treeTrunk3 = Rect(350, 250, 10, 50, fill=rgb(130, 40, 0))
treeLeafs1 = Circle(75, 240, 20, fill='green')
treeLeafs2 = Circle(250, 240, 20, fill='green')
treeLeafs3 = Circle(355, 240, 20, fill='green')
Circle(70, 230, 4, fill='red')
Circle(85, 240, 4, fill='red')
Circle(65, 245, 4, fill='red')
Circle(75, 252, 4, fill='red')
Circle(240, 235, 4, fill='red')
Circle(245, 250, 4, fill='red')
Circle(255, 242, 4, fill='red')
Circle(260, 230, 4, fill='red')
Circle(355, 230, 4, fill='red')
Circle(345, 242, 4, fill='red')
Circle(360, 250, 4, fill='red')
Circle(365, 240, 4, fill='red')

#the grounds lighting
Ground2 = Rect(0, 300, 400, 100, opacity=10)


def onMousePress(mouseX, mouseY):
    
    #the suns movement based on Y axis
    Sun.centerY = mouseY
    leftEye.centerY = mouseY-15
    rightEye.centerY = mouseY-15
    mouth.centerY = mouseY+12
    
    #ground opacity
    Ground.opcaity = mouseY / 10 + 5
    Ground2.Opacity = mouseY / 10 + 12
     
    #all stars movement and opacity based on the Y axis when clicked with mouse
    Star1.opacity = mouseY / 10 + 25
    Star1.centerY = mouseY-260
    Star2.opacity = mouseY / 10 + 25
    Star2.centerY = mouseY-185
    Star3.opacity = mouseY / 10 + 25
    Star3.centerY = mouseY-145
    Star4.opacity = mouseY / 10 + 25
    Star4.centerY = mouseY-120
    Star5.opacityY = mouseY / 10 + 25
    Star5.centerY = mouseY-155
    Star6.opacityY = mouseY / 10 + 25
    Star6.centerY = mouseY-240
    Star7.opacityY = mouseY / 10+25
    Star7.centerY = mouseY-210
    Star8.opacitY = mouseY / 10+25
    Star8.centerY = mouseY-280
    
    #sky opacity
    Sky.opacity = mouseY / 4.5 + 1
    Sky2.opacity = mouseY / 10 + 12