class Point:
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y
 
    def __str__ (self):
        return "({0},{1})".format(self.x,self.y)
 
    def distance_from_origin (self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
print(Point(4,3).distance_from_origin())
