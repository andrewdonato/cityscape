import math 

curbs = []
streets = []

def setup():
    global mapTop, mapBottom, mapleft, mapRight, streets, verticalStreetEdges, horizontalStreetEdges, buildings
    size(601, 601, P3D)
    

def createStreet(xStart, yStart, zStart, xEnd, yEnd, zEnd, width):
    global streets
    newStreet = Street(xStart, yStart, zStart, xEnd, yEnd, zEnd, width)
    streets.append(newStreet)
    


class Street:
    def __init__(self, xStart, yStart, zStart, xEnd, yEnd, zEnd, width):
        self.xStart = xStart, 
        self.yStart = yStart, 
        self.zStart = zStart, 
        self.xEnd = xEnd, 
        self.yEnd = yEnd, 
        self.zEnd = zEnd,
        self.width = width 
        # self.i = index
        self.intersectsWith = []

    def findIntersections():
        pass

    def createCurbs():
        pass



class Curb:
    def __init__(self, xStart, yStart, zStart, xEnd, yEnd, zEnd, buildingOrientation):
        self.xStart = xStart, 
        self.yStart = yStart, 
        self.zStart = zStart, 
        self.xEnd = xEnd, 
        self.yEnd = yEnd, 
        self.zEnd = zEnd, 
        self.buildingOrientation = buildingOrientation
        self.buildings = []
