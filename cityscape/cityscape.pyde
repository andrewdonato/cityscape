import math 

buildings = {}
buildings1 = []
buildings2 = []
buildings3 = []
buildings4 = []

streetSegments = {}

mapTop = 0
mapBottom = 0
mapleft = 0
mapRight = 0
alleyway = 5




def setup():
    global mapTop, mapBottom, mapleft, mapRight, streetSegments, buildings
    size(601, 601, P3D)
    mapTop = -height
    mapBottom = height
    mapleft = 0
    mapRight = width
    
    camera(width/2.0, -height, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/10.0, 0, 0, 1, 0)
    
    # createStreets()
    
    # createBuildings(middleVerticalStreet()[0], "vertical", buildings1, 20)
    # createBuildings(middleVerticalStreet()[0], "vertical", buildings2, 20)
    # createBuildings(middleHorizontalStreet()[0], "horizontal", buildings3, 20)
    # createBuildings(middleHorizontalStreet()[0], "horizontal", buildings4, 20)
    
    streetSegments = {
                    (width/2 - width/40, 0, 0, width/2 - width/40, 0, height) : "left",
                    (width/2 + width/40, 0,  0, width/2 + width/40, 0, height) : "right",
                    (0, 0, height/2 - height/40, width, 0, height/2 - height/40) : "above",
                    (0, 0, height/2 + height/40, width, 0, height/2 + height/40) : "below"
    }
    
    ## Create building arrays. Call createBuildings.
    lineSegments = streetSegments.keys()
    # for lineSegment in lineSegments :
    for i in range(len(lineSegments)):
        lineSegment = lineSegments[i]
        buildings[lineSegment] = []
        createBuildings(lineSegment, streetSegments[lineSegment], buildings[lineSegment])
    
    
def draw():
    global buildings, buildings1
    background(255)
    stroke(0)

    # draw grid
    strokeWeight(1)
    showGrid()
    
    # draw street
    drawStreets()
    
    # strokeWeight(5)
    # line(*middleVerticalStreet()[0])
    # line(*middleVerticalStreet()[1])
    # line(*middleHorizontalStreet()[0])
    # line(*middleHorizontalStreet()[1])
    
    # draw buildings
    strokeWeight(5)
    drawBuildings(middleVerticalStreet()[0], buildings1, "left")
    drawBuildings(middleVerticalStreet()[1], buildings2, "right")
    drawBuildings(middleHorizontalStreet()[0], buildings3, "above")
    drawBuildings(middleHorizontalStreet()[1], buildings4, "below")

    # camera
    camera(3*mouseX - width , 2*mouseY - height, 1*(height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/10.0, height/2, 0, 1, 0)


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

# def createStreets():
#     global streetSegments, buildings
#     # strokeWeight(5)
#     streetLines = streetSegments.keys()
#     streetOrientation = streetSegments.values()
    
#     for i in range(len(streetLines)):
#         line(*streetLines[i])
#         buildings.append([])
        
#     createBuildings(middleVerticalStreet()[0], "vertical", buildings1, 20)
                        
        
    
def drawStreets():
    global streetSegments
    strokeWeight(5)
    lineSegments = streetSegments.keys()
    # streetOrientation = lineSegments.values()
    for i in range(len(lineSegments)):
        line(*lineSegments[i])

def middleVerticalStreet():
    lineLeft = (width/2 - width/40, 0, 0, width/2 - width/40, 0, height)
    lineRight = (width/2 + width/40, 0,  0, width/2 + width/40, 0, height)
    return lineLeft, lineRight

def middleHorizontalStreet():
    lineUp = (0, 0, height/2 - height/40, width, 0, height/2 - height/40)
    lineDown = (0, 0, height/2 + height/40, width, 0, height/2 + height/40)
    return lineUp, lineDown    
    
# def createBuildings(lineSegment, orientation, buildingArray=buildings1, amount=15):
def createBuildings(lineSegment, orientation, buildingArray):
    global buildings
    
    print lineSegment 
    print orientation
    print buildingArray
    #     createBuildings(middleVerticalStreet()[0], "vertical", buildings1, 20)
    # createBuildings(streetSegments)
    
    
    # lineSegments = streetSegment.keys()

    # for i in range(len(lineSegments)):
    #     lineSegment = lineSegments[i]
    #     # lineSegments = streetSegments.key()
    #     buildings[lineSegment] = []
    
    # buildingArray = buildings.values()
    
    # streetOrientation = lineSegments.values()
    
    # for i in range(len(lineSegments)):
        # lineSegment = lineSegments[i]
    
    strokeWeight(5)

    # determine magnitude of line    
    xAbsolute = abs(lineSegment[0]-lineSegment[3])
    yAbsolute = abs(lineSegment[1]-lineSegment[4])
    zAbsolute = abs(lineSegment[2]-lineSegment[5])
    lineMagnitude = math.sqrt(xAbsolute**2 + yAbsolute**2 + zAbsolute**2)

    buildingMagnitude = 0    
    while buildingMagnitude < lineMagnitude :
        
        boxX = int(random(10, height/10))
        boxY = int(random(10, height/10))
        boxZ = int(random(10, height/10))
        # boxX = 50
        # boxY = 50
        # boxZ = 50
        
        if orientation == "above" or orientation == "below" :
            buildingMagnitude += boxX + alleyway
        elif orientation == "left" or orientation == "right":
            buildingMagnitude += boxZ + alleyway
        
        if buildingMagnitude < lineMagnitude :
            building = [boxX, boxY, boxZ]
            buildingArray.append(building)    
        
    # make skyscraper
    skyscraper = len(buildingArray)/2
    buildingArray[skyscraper][1] = int(random(60, height/2.5))
    
                      
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
    
    
    
# thisdict =  {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdictK = thisdict.keys()
# for i in range(len(thisdictK)):
#     print(thisdictK[i])

# thisdictV = thisdict.values()
# for i in range(len(thisdictV)):
#     print(thisdictV[i])
    
# for x in thisdict:
#     print(thisdict[x])

    

    
   
    
    
