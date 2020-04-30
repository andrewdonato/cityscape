import math 

verticalStreetEdges = []
horizontalStreetEdges = []

streets = [verticalStreetEdges, horizontalStreetEdges]

buildings = []
buildingArrays = []
buildings1 = []
buildings2 = []
buildings3 = []
buildings4 = []

mapTop = 0
mapBottom = 0
mapleft = 0
mapRight = 0
alleyway = 5

def setup():
    global mapTop, mapBottom, mapleft, mapRight, streets, verticalStreetEdges, horizontalStreetEdges, buildings
    size(601, 601, P3D)
    mapTop = -height
    mapBottom = height
    mapleft = 0
    mapRight = width
    
    lineLeft = (width/2 - width/40, 0, 0, width/2 - width/40, 0, height)
    lineRight = (width/2 + width/40, 0,  0, width/2 + width/40, 0, height)
    verticalStreetEdges = [lineLeft, lineRight]

    lineUp = (0, 0, height/2 - height/40, width, 0, height/2 - height/40)
    lineDown = (0, 0, height/2 + height/40, width, 0, height/2 + height/40)
    horizontalStreetEdges = [lineUp, lineDown]



    camera(width/2.0, -height, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/10.0, 0, 0, 1, 0)
    
    for i in range(len(verticalStreetEdges)):
        buildings.append([])
        createBuildings(verticalStreetEdges[i], "vertical", buildings[i])
        
    for i in range(len(horizontalStreetEdges)):
        buildings.append([])
        createBuildings(horizontalStreetEdges[i], "horizontal", buildings[i])
        
    # createBuildings(verticalStreetEdges[0], "vertical", buildings1, 20)
    # createBuildings(verticalStreetEdges[0], "vertical", buildings2, 20)
    # createBuildings(horizontalStreetEdges[0], "horizontal", buildings3, 20)
    # createBuildings(horizontalStreetEdges[0], "horizontal", buildings4, 20)

    
    


    
    
def draw():
    global buildings, buildings1, streets, verticalStreetEdges, horizontalStreetEdges, buildings
    background(255)
    stroke(0)

    # draw grid
    strokeWeight(1)
    showGrid()
    
    # draw street
    strokeWeight(5)
    line(*verticalStreetEdges[0])
    line(*verticalStreetEdges[1])
    line(*horizontalStreetEdges[0])
    line(*horizontalStreetEdges[1])
    
    # draw buildings
    strokeWeight(5)
    drawBuildings(verticalStreetEdges[0], buildings1, "left")
    drawBuildings(verticalStreetEdges[1], buildings2, "right")
    drawBuildings(horizontalStreetEdges[0], buildings3, "above")
    drawBuildings(horizontalStreetEdges[1], buildings4, "below")

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
    
    
def createBuildings(lineSegment, orientation, buildingArray):
    global buildings
    print orientation
    print buildingArray
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
        
        if orientation == "horizontal" :
            buildingMagnitude += boxX + alleyway
        elif orientation == "vertical" :
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
    
    
    
    
    
   
    
    
