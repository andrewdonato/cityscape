import math 

buildings1 = []
buildings2 = []
buildings3 = []
buildings4 = []
buildings5 = []
buildings6 = []
buildings7 = []
buildings8 = []
buildings9 = []
buildings10 = []

mapTop = 0
mapBottom = 0
mapleft = 0
mapRight = 0
alleyway = 5

def setup():
    global mapTop, mapBottom, mapleft, mapRight
    size(701, 701, P3D)
    mapTop = -height
    mapBottom = height
    mapleft = 0
    mapRight = width
    
    camera(width/2.0, -height, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/10.0, 0, 0, 1, 0)
    
    seedValue = (int(random(2000)))
    print seedValue
    randomSeed(seedValue)
    
    createBuildings(middleVerticalStreet()[0], "vertical", buildings1, 20)
    createBuildings(middleVerticalStreet()[0], "vertical", buildings2, 20)
    createBuildings(middleHorizontalStreet()[0], "horizontal", buildings3, 20)
    createBuildings(middleHorizontalStreet()[0], "horizontal", buildings4, 20)
    createBuildings(leftVerticalStreet()[0], "vertical", buildings5, 20)
    createBuildings(leftVerticalStreet()[0], "vertical", buildings6, 20)
    createBuildings(rightVerticalStreet()[0], "vertical", buildings7, 20)
    createBuildings(rightVerticalStreet()[0], "vertical", buildings8, 20)
    createBuildings(outsideVerticalStreet()[0], "vertical", buildings9, 20)
    createBuildings(outsideVerticalStreet()[0], "vertical", buildings10, 20)
    
def draw():
    global buildings, buildings1
    frameRate(10)    
    # background(125)
    background(105,206,235)
    
    stroke(0)

    ## mouse

    # pushMatrix()
    # ellipse(mouseX,mouseY, 25, 10)
    # popMatrix()

    # pushMatrix()
    # fill(0,255,0)
    # translate(width/2, +1, height/2)
    # box(width,0,height)
    # fill(255)
    # popMatrix()
    
    # draw grid
    strokeWeight(1)
    showGrid()
    showSkyGrid()
    
    # draw street lines
    strokeWeight(5)
    line(*middleVerticalStreet()[0])
    line(*middleVerticalStreet()[1])
    # line(*middleHorizontalStreet()[0])
    # line(*middleHorizontalStreet()[1])
    line(*leftVerticalStreet()[0])
    line(*leftVerticalStreet()[1])
    line(*rightVerticalStreet()[0])
    line(*rightVerticalStreet()[1])
    line(*outsideVerticalStreet()[0])
    line(*outsideVerticalStreet()[1])
    
    
    
    # ground
    pushMatrix()
    fill(75,225,100)
    # fill(75,225,225)
    # fill(200)
    
    translate(width/2, +1, height/2)
    box(width,1,height)
    popMatrix()
    
    
    # draw streets box
    fill(50)
    pushMatrix()    
    translate(width/2, -1, height/2)
    box(width/22, 1, height)
    translate(width/2, 0, 0)
    box(width/22, 1, height)
    translate(-width, 0, 0)
    box(width/22, 1, height)
    translate(3*width/4, 0, 0)
    box(width/22, 1, height)
    translate(-width/2, 0, 0)
    box(width/22, 1, height)
    popMatrix()
    
    
    # stroke(0)
    # strokeWeight(40)

        
    # line(width/2, 0, 0, width/2, 0, height)
    # line(width/4, 0, 0, width/4, 0, height)
    # line(3*(width/4) , 0,  0, 3*(width/4) , 0, height)
    # line(0, 0, 0, 0, 0, height)
    # line(width, 0, 0, width, 0, height)
    
    # draw buildings
    strokeWeight(5)
    fill(225)
    drawBuildings(middleVerticalStreet()[0], buildings1, "left")
    drawBuildings(middleVerticalStreet()[1], buildings2, "right")
    # drawBuildings(middleHorizontalStreet()[0], buildings3, "above")
    # drawBuildings(middleHorizontalStreet()[1], buildings4, "below")
    drawBuildings(leftVerticalStreet()[0], buildings5, "left")
    drawBuildings(leftVerticalStreet()[1], buildings6, "right")
    drawBuildings(rightVerticalStreet()[0], buildings7, "left")
    drawBuildings(rightVerticalStreet()[1], buildings8, "right")
    drawBuildings(outsideVerticalStreet()[0], buildings9, "left")
    drawBuildings(outsideVerticalStreet()[1], buildings10, "right")
    
    pushMatrix()    
    # shipZ = 0
    # while shipZ < mapTop:
    #     translate(0,0,shipZ)
    #     drawShip()
    #     shipZ += 1
    drawShip()
    popMatrix()
    
    
    # camera
    camera(3*mouseX - 2*width , 3*mouseY - 2*height, 2*(height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/10.0, height/2, 0, 1, 0)


def showGrid():
    strokeWeight(1)
    x = 0
    while x < width :
        line(x, 0, 0, x, 0, height)
        x = x + 50
    
    z = 0
    while z < height :
        line(0, 0, z, width, 0, z)
        z = z + 50
    
    strokeWeight(5)
    line(mapleft, 0, 0, mapRight, 0 , 0)

def showSkyGrid():
    pushMatrix()
    translate(0, mapTop, 0)
    strokeWeight(1)
    x = 0
    while x < width :
        line(x, 0, 0, x, 0, height)
        x = x + 50
    
    z = 0
    while z < height :
        line(0, 0, z, width, 0, z)
        z = z + 50
    
    strokeWeight(5)
    line(mapleft, 0, 0, mapRight, 0 , 0)
    popMatrix()
    
    
def middleVerticalStreet():
    lineLeft = (width/2 - width/40, 0, 0, width/2 - width/40, 0, height)
    lineRight = (width/2 + width/40, 0,  0, width/2 + width/40, 0, height)
    return lineLeft, lineRight

def leftVerticalStreet():
    lineLeft = (width/4 - width/40, 0, 0, width/4 - width/40, 0, height)
    lineRight = (width/4 + width/40, 0,  0, width/4 + width/40, 0, height)
    return lineLeft, lineRight

def rightVerticalStreet():
    lineLeft = (3*(width/4) - width/40, 0, 0, 3*(width/4) - width/40, 0, height)
    lineRight = (3*(width/4) + width/40, 0,  0, 3*(width/4) + width/40, 0, height)
    return lineLeft, lineRight

def outsideVerticalStreet():
    lineLeft = (width - width/40, 0,  0, width - width/40, 0, height)
    lineRight = (0 + width/40, 0, 0, 0 + width/40, 0, height)
    return lineLeft, lineRight



def middleHorizontalStreet():
    lineUp = (0, 0, height/2 - height/40, width, 0, height/2 - height/40)
    lineDown = (0, 0, height/2 + height/40, width, 0, height/2 + height/40)
    return lineUp, lineDown    
    
    
    
def createBuildings(lineSegment, orientation, buildingArray=buildings1, amount=15):
    global buildings
    strokeWeight(5)

    # determine magnitude of line    
    xAbsolute = abs(lineSegment[0]-lineSegment[3])
    yAbsolute = abs(lineSegment[1]-lineSegment[4])
    zAbsolute = abs(lineSegment[2]-lineSegment[5])
    lineMagnitude = math.sqrt(xAbsolute**2 + yAbsolute**2 + zAbsolute**2)



    buildingMagnitude = 0    
    while buildingMagnitude < lineMagnitude :
        
        boxX = int(random(20, width/10))
        boxY = int(random(10, height/3))
        boxZ = int(random(10, height/10))
        # boxX = 50
        # boxY = 50
        # boxZ = 50
        
        difference = abs(buildingMagnitude - lineMagnitude)
        
        if orientation == "horizontal" :
            buildingMagnitude += boxX + alleyway
        elif orientation == "vertical" :
            buildingMagnitude += boxZ + alleyway
        
        if buildingMagnitude < lineMagnitude :
            building = [boxX, boxY, boxZ]
            buildingArray.append(building)
        # else:
        #     building = [[boxX - difference, boxY, boxZ - difference]]
        #     buildingArray.append(building)
        
    # make skyscraper
    skyscraper = len(buildingArray)/2
    buildingArray[skyscraper][1] = int(random(60, height/1.5))
    
                      
def drawBuildings(streetLine, buildingArray, side):
    buildings = buildingArray
    pushMatrix()
        
    for i in range(len(buildings)):
        
        if i == 0 :
            previousBuilding = [0, 0, 0]
        else:
            previousBuilding = buildings[i-1]
        
        building = buildings[i]
        
        boxX = building[0]
        boxY = building[1]
        boxZ = building[2]
        
        ## building color
        # fill(255)
        fill(0,135,219)
        
        # randomSeed(1000)
        # r=int(random(0,255))
        # randomSeed(1010)
        # g=int(random(0,255))
        # randomSeed(1020)
        # b=int(random(0,255))
        # # fill(r, g, b)
        # # randomSeed(1000)
        # fill(int(random(0,255)),int(random(0,255)),int(random(0,255)))

        
        
        
        
        if side == "left" or side == "right":
            
            # moves buildings along the Z axis down the street
            translate(0, 0, previousBuilding[2]/2+ boxZ/2 + alleyway )
        
            if side == "left":                                            
                pushMatrix()
                
                # moves buildings against the street and adjusts height
                translate(streetLine[0] - boxX/2, -boxY/2, 0)                                        
    
                box(building[0], building[1], building[2])
                popMatrix()
                    
            elif side == "right":
                pushMatrix()
                
                # moves buildings against the street and adjusts height
                translate(streetLine[0] + boxX/2, -boxY/2, 0)                        
                
                box(building[0], building[1], building[2])
                popMatrix()
                
        elif side == "above" or side == "below":
            
            # moves buildings along the X axis down the street
            translate(previousBuilding[0]/2+ boxX/2 + alleyway, 0, 0)
                            
            if side == "above":
                pushMatrix()
                
                # moves buildings against the street and adjusts height
                translate(0, -boxY/2, streetLine[2] - boxZ/2)                        
                
                box(building[0], building[1], building[2])
                popMatrix()
                
            elif side == "below":
                pushMatrix()
                
                # moves buildings against the street and adjusts height
                translate(0, -boxY/2, streetLine[2] + boxZ/2)                        
                
                box(building[0], building[1], building[2])
                popMatrix()            
    popMatrix()
    
    
    
def drawShip():
    # translate(width/2, -height, 0)
    translate(width/2, -height, height/2)
    fill(100)
    
    stroke(0)
    sphere(10)
    stroke(50)
    beginShape()
    vertex(0,0,80)
    vertex(20,0,0)
    vertex(-20,0,0)
    vertex(0,0,80)
    endShape()
    beginShape()
    vertex(0,0,30)
    vertex(40,0,-40)
    vertex(-40,0,-40)
    vertex(0,0,30)
    endShape()    
    
    # sphere(10)
    
    
        
    
   
    
    
