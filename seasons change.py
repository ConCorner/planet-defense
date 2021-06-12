### This file was copied from CS 1 '19-'20 on 2021-04-06.

# Fill me in!
app.background = gradient('lightSkyBlue', 'paleGoldenrod', start='bottom')

#sun
sun = Circle(200, 100, 50, fill='yellow')



#rainbow 
Purple = Circle(120, 340, 120, fill=None, border='Purple', borderWidth=5, visible = False)
Blue = Circle(120, 340, 115, fill=None, border='blue', borderWidth=5, visible = False)
Green = Circle(120, 340, 110, fill=None, border='green', borderWidth=5, visible = False)
Yellow = Circle(120, 340, 105, fill=None, border='yellow', borderWidth=5, visible = False)
Orange = Circle(120, 340, 100, fill=None, border='orange', borderWidth=5, visible = False)
Red = Circle(120, 340, 95, fill=None, border='red', borderWidth=5, visible = False)

#cloud #1
cloud11 = Circle(100, 140, 20, fill='white', opacity=40, visible = False)
cloud12 = Circle(120, 150, 20, fill='white', opacity=40, visible = False)
cloud13 = Circle(85, 146, 20, fill='white', opacity=40, visible = False)
cloud14 = Circle(98, 155, 20, fill='white', opacity=40, visible = False)

#Cloud #2
cloud21 = Circle(290, 120, 20, fill='white', opacity=40, visible = False)
cloud22 = Circle(310, 130, 20, fill='white', opacity=40, visible = False)
cloud23 = Circle(275, 126, 20, fill='white', opacity=40, visible = False)
cloud24 = Circle(288, 135, 20, fill='white', opacity=40, visible = False)

#cloud #3
cloud31 = Circle(175, 62, 20, fill='white', opacity=40, visible = False)
cloud32 = Circle(195, 72, 20, fill='white', opacity=40, visible = False)
cloud33 = Circle(160, 68, 20, fill='white', opacity=40, visible = False)
cloud34 = Circle(173, 77, 20, fill='white', opacity=40, visible = False)

#ground
ground = Rect(0, 330, 400, 70, fill='forestGreen')
#wheat feilds
Rect(12, 340, 20, 50, fill='brown')
plant1 = Rect(15, 345, 14, 10, fill='wheat')
plant2 = Rect(15, 360, 14, 10, fill='wheat')
plant3 = Rect(15, 375, 14, 10, fill='wheat')

Rect(40, 340, 20, 50, fill='brown')
plant4 = Rect(43, 345, 14, 10, fill='wheat')
plant5 = Rect(43, 360, 14, 10, fill='wheat')
plant6 = Rect(43, 375, 14, 10, fill='wheat')

Rect(68, 340, 20, 50, fill='brown')
plant7 = Rect(71, 345, 14, 10, fill='wheat')
plant8 = Rect(71, 360, 14, 10, fill='wheat')
plant9 = Rect(71, 375, 14, 10, fill='wheat')

Rect(96, 340, 20, 50, fill='brown')
plant10 = Rect(99, 345, 14, 10, fill='wheat')
plant11 = Rect(99, 360, 14, 10, fill='wheat')
plant12 = Rect(99, 375, 14, 10, fill='wheat')

#house
Polygon(200, 380, 345, 380, 345, 315, 305, 305, 200, 315, fill='maroon')
roof = Polygon(200, 315, 200, 320, 305, 310, 345, 320, 345, 315, 305, 305, fill= rgb(80, 0, 0))
Rect(190, 375, 10, 5, fill='darkGrey')

#window #1
Rect(230, 340, 25, 25, fill= rgb(80, 0, 0))
Rect(234, 344, 17, 17, fill='white')
Rect(230, 350, 25, 5, fill= rgb(80, 0, 0))
Rect(240, 340, 5, 25, fill= rgb(80, 0, 0))

#window #2
Rect(280, 340, 25, 25, fill= rgb(80, 0, 0))
Rect(284, 344, 17, 17, fill='white')
Rect(280, 350, 25, 5, fill= rgb(80, 0, 0))
Rect(290, 340, 5, 25, fill= rgb(80, 0, 0))

def onKeyPress(key):
    #rain and rainbow
    if (key == 't'):
        Purple.visible = True
        Blue.visible = True
        Green.visible = True
        Yellow.visible = True
        Orange.visible = True
        Red.visible = True
        cloud11.visible = True
        cloud12.visible = True
        cloud13.visible = True
        cloud14.visible = True
        cloud21.visible = True
        cloud22.visible = True
        cloud23.visible = True
        cloud24.visible = True
        cloud31 .visible = True
        cloud32.visible = True
        cloud33.visible = True
        cloud34 .visible = True
        app.background = gradient('lightSkyBlue', 'paleGoldenrod', start='bottom')
        plant1.visible = True
        plant2.visible = True
        plant3.visible = True
        plant4.visible = True
        plant5.visible = True
        plant6.visible = True
        plant7.visible = True
        plant8.visible = True
        plant9.visible = True
        plant10.visible = True
        plant11.visible = True
        plant12.visible = True
        ground.fill = 'forestGreen'
        roof.fill = rgb(80, 0, 0)
        
    #clear sky
    if (key == 'y'):
        Purple.visible = False
        Blue.visible = False
        Green.visible = False
        Yellow.visible = False
        Orange.visible = False
        Red.visible = False
        cloud11.visible = False
        cloud12.visible = False
        cloud13.visible = False
        cloud14.visible = False
        cloud21.visible = False
        cloud22.visible = False
        cloud23.visible = False
        cloud24.visible = False
        cloud31 .visible = False
        cloud32.visible = False
        cloud33.visible = False
        cloud34 .visible = False
        app.background = gradient('lightSkyBlue', 'paleGoldenrod', start='bottom')
        plant1.visible = True
        plant2.visible = True
        plant3.visible = True
        plant4.visible = True
        plant5.visible = True
        plant6.visible = True
        plant7.visible = True
        plant8.visible = True
        plant9.visible = True
        plant10.visible = True
        plant11.visible = True
        plant12.visible = True
        ground.fill = 'forestGreen'
        roof.fill = rgb(80, 0, 0)
    
    #snow
    if (key == 'u'):
        Purple.visible = False
        Blue.visible = False
        Green.visible = False
        Yellow.visible = False
        Orange.visible = False
        Red.visible = False
        cloud11.visible = True
        cloud12.visible = True
        cloud13.visible = True
        cloud14.visible = True
        cloud21.visible = True
        cloud22.visible = True
        cloud23.visible = True
        cloud24.visible = True
        cloud31 .visible = True
        cloud32.visible = True
        cloud33.visible = True
        cloud34 .visible = True
        app.background = gradient('lightSkyBlue', 'white', start='bottom')
        plant1.visible = False
        plant2.visible = False
        plant3.visible = False
        plant4.visible = False
        plant5.visible = False
        plant6.visible = False
        plant7.visible = False
        plant8.visible = False
        plant9.visible = False
        plant10.visible = False
        plant11.visible = False
        plant12.visible = False
        ground.fill = 'white'
        roof.fill = 'white'