import math 

streets = []
curbs = []
buildings = []

mapWidth = 1200
mapHeight = 1200
mapDepth = 1200



tileWall = mapWidth
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
    
    
    for i in range(0, len(desiredStreets)):
        streetLine = desiredStreets[i]
        createStreet(streetLine[0], streetLine[1], streetLine[2], streetLine[3], streetLine[4], streetLine[5], i, 30, "both", "two-way")

                
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
        # self.i = index
        self.curbs = []
        self.intersections = []
        self.angle = None
        self.directionality = directionality
        self.visited = False

    def createCurbs(self):
        pass

    def connectStreet(self, street):
        pass

    def getBuildings():
        pass

    def findIntersections(self, streets):
        pass

    def findAngle():
        pass

    def findVelocity():
        pass
        
    def drawStreet():
        pass


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

    def findAngle():
        pass


class Intersection:
    def __init__(self, streets, intersectionCreationIndex):
        self.streets = []
        self.intersectionIndex = intersectionCreationIndex
        self.address = []

    def findAddress():
        pass


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
