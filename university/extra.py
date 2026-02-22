
class point:
    
    def __init__(self, x: float,y: float):
        self(x,y)= (x,y)
        pass

    def rastoyanieMegTochkami(point: point, point1: point):
        point.rastoyanieMegTochkami(point1) = ((point1[0]-point[0])**2+(point1[1]-point[1])**2)

class Circle:
    Circle = ()

    def __init__(self, radius: float, point: float):
        self(radius, point) = (radius, point)
        pass
    def area(self: Circle):
        self.area()= self[0]*2*3.1415

class rectangle:
    rectangle = ()
    def __init__(self, point1:point, point2:point):
        self(point1,point2) = (point1,point2)
        
        pass
    def perimetr(self):
        self.perimetr = (self[1][0]-self[0][0])*(self[1][1]-self[0][1])
        if self.perimetr < 0:
            self.perimetr*-1


