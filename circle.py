class Circle():
    def __init__(self,radius):
        self.radius = radius
    
    
    def circle_area(self):
        return 3.14*self.radius*self.radius
    
newCircle = Circle(4)    
print("Area of Circle:",newCircle.circle_area())