import math 

streets = []
curbs = []
buildings = []

mapWidth = None
mapHeight = None
mapDepth = None
mapTop = None
mapBottom = None
mapleft = None
mapRight = None



tileWall = 600
desiredStreets = [   
    (1*tileWall/8, 0*tileWall/8, 0, 1*tileWall/8, 8*tileWall/8, 0),
    (0*tileWall/8, 4*tileWall/8, 0, 4*tileWall/8, 4*tileWall/8, 0),
    (4*tileWall/8, 4*tileWall/8, 0, 8*tileWall/8, 8*tileWall/8, 0),
    (2*tileWall/8, 0*tileWall/8, 0, 2*tileWall/8, 8*tileWall/8, 0),
    (3*tileWall/8, 0*tileWall/8, 0, 3*tileWall/8, 8*tileWall/8, 0),
    (0*tileWall/8, 5*tileWall/8, 0, 3*tileWall/8, 5*tileWall/8, 0),
    (0*tileWall/8, 6*tileWall/8, 0, 6*tileWall/8, 6*tileWall/8, 0),
    (0*tileWall/8, 7*tileWall/8, 0, 3*tileWall/8, 7*tileWall/8, 0),
    (0*tileWall/8, 2*tileWall/8, 0, 8*tileWall/8, 2*tileWall/8, 0),
    (4*tileWall/8, 2*tileWall/8, 0, 8*tileWall/8, 6*tileWall/8, 0),
    (4*tileWall/8, 0*tileWall/8, 0, 4*tileWall/8, 2*tileWall/8, 0),
    (5*tileWall/8, 2*tileWall/8, 0, 8*tileWall/8, 5*tileWall/8, 0),
    (5*tileWall/8, 3*tileWall/8, 0, 8*tileWall/8, 3*tileWall/8, 0),
    (6*tileWall/8, 4*tileWall/8, 0, 8*tileWall/8, 4*tileWall/8, 0),
    (6*tileWall/8, 2*tileWall/8, 0, 8*tileWall/8, 4*tileWall/8, 0),
    (4*tileWall/8, 1*tileWall/8, 0, 1*tileWall/8, 1*tileWall/8, 0),
    (5*tileWall/8, 2*tileWall/8, 0, 5*tileWall/8, 0*tileWall/8, 0),
    (6*tileWall/8, 2*tileWall/8, 0, 6*tileWall/8, 0*tileWall/8, 0),
    (5*tileWall/8, 1*tileWall/8, 0, 8*tileWall/8, 1*tileWall/8, 0),
    (5*tileWall/8, 3*tileWall/8, 0, 4*tileWall/8, 4*tileWall/8, 0),]


def setup():
    global mapTop, mapBottom, mapleft, mapRight, streets, curbs, buildings
    size(601, 601, P3D)
    
    mapWidth = width
    mapHeight = height
    mapDepth = height
    mapTop = None
    mapBottom = None
    mapleft = None
    mapRight = None
    
    
    for i in range(0, len(desiredStreets)):
        streetLine = desiredStreets[i]
        createStreet(streetLine[0], streetLine[1], streetLine[2], streetLine[3], streetLine[4], streetLine[5], i, 30, "both", "two-way")

    # for street in streets:
    #     if street.visited == False:
    #         street.findIntersections()
        
        
    for street in streets:
        street.drawStreet()
        
                
    # print streets[0].streetWidth
    # print streets[0].buildingOrientation
    # print streets[0].directionality
    
    


# def createStreet(xStart, yStart, zStart, xEnd, yEnd, zEnd, index, streetWidth=30, buildingOrientation="both", directionality="two-way"):
def createStreet(xStart, yStart, zStart, xEnd, yEnd, zEnd, index, streetWidth, buildingOrientation, directionality):
    global streets
    newStreet = Street(xStart, yStart, zStart, xEnd, yEnd, zEnd, index, streetWidth, buildingOrientation, directionality)
    streets.append(newStreet)
    


class Street:
    # def __init__(self, xStart, yStart, zStart, xEnd, yEnd, zEnd, streetCreationIndex, streetWidth, buildingOrientation = "both", directionality = "two-way"):
    def __init__(self, xStart, yStart, zStart, xEnd, yEnd, zEnd, streetCreationIndex, streetWidth, buildingOrientation, directionality):
        self.xStart = xStart 
        self.yStart = yStart 
        self.zStart = zStart 
        self.xEnd = xEnd 
        self.yEnd = yEnd 
        self.zEnd = zEnd
        self.streetIndex = streetCreationIndex
        self.streetWidth = streetWidth 
        self.buildingOrientation = buildingOrientation
        self.curbs = []
        self.intersections = []
        self.intersectsWith = []
        self.angle = None
        self.directionality = directionality
        # self.visited = False
        self.lookedForIntersections = False

    def createCurbs(self):
        pass

    def connectStreet(self, street):
        pass

    def getBuildings(self):
        pass

    def findIntersections(self, streets):
        pass            

    def findCorners(self):
        pass        

    def findAngle(self):
        pass

    def findVelocity(self):
        pass
        
    def drawStreet(self):
        line(self.xStart, self.yStart, self.zStart, self.xEnd, self.yEnd, self.zEnd)


class Curb:
    def __init__(self, xStart, yStart, zStart, xEnd, yEnd, zEnd, buildingOrientation, curbCreationIndex, streetIndex):
        self.xStart = xStart
        self.yStart = yStart
        self.zStart = zStart
        self.xEnd = xEnd
        self.yEnd = yEnd
        self.zEnd = zEnd
        self.buildingOrientation = buildingOrientation
        self.curbIndex = curbCreationIndex
        self.streetIndex = streetIndex
        self.buildings = []
        self.angle = None

    def createBuildings(self):
        pass

    def findAngle(self):
        pass


class Intersection:
    def __init__(self, streets, intersectionCreationIndex):
        self.streets = []
        self.intersectionIndex = intersectionCreationIndex
        self.address = []

    # def findAddress():
    #     pass


class Building:
    def __init__(self, xCoordinate, yCoordinate, zCoordinate, xSize, ySize, zSize, buildingCreationIndex, curbIndex, streetIndex):
        
        self.x = xCoordinate
        self.y = yCoordinate 
        self.z = zCoordinate
        self.xSize = xSize
        self.ySize = ySize
        self.zSize = zSize
        self.buildingIndex = buildingCreationIndex
        self.address = [xCoordinate, yCoordinate, zCoordinate]
        self.curbIndex = curbIndex
        self.streetIndex = streetIndex
