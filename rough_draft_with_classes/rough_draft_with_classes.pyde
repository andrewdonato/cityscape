import math 

curbs = []
streets = []

def setup():
    global mapTop, mapBottom, mapleft, mapRight, streets, verticalStreetEdges, horizontalStreetEdges, buildings
    size(601, 601, P3D)
    

def createStreet(xStart, yStart, zStart, xEnd, yEnd, zEnd, width=30):
    global streets
    newStreet = Street(xStart, yStart, zStart, xEnd, yEnd, zEnd, width)
    streets.append(newStreet)
    


class Street:
    def __init__(self, xStart, yStart, zStart, xEnd, yEnd, zEnd, width, streetCreationIndex, buildingOrientation = "both", directionality = "two-way"):
        self.xStart = xStart 
        self.yStart = yStart 
        self.zStart = zStart 
        self.xEnd = xEnd 
        self.yEnd = yEnd 
        self.zEnd = zEnd
        self.width = width
        self.streetIndex = streetCreationIndex 
        buildingOrientation = buildingOrientation
        # self.i = index
        self.curbs = []
        self.intersections = []
        self.angle = None
        self.directionality = ""
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

