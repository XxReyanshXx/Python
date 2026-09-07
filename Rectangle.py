class Rectangle():
    def __init__(self,leanth,width):
        self.lenght=  leanth
        self.width = width
        
 
    
    def rectangle_area(self):
        return self.lenght*self.width
        
        
newRectangle = Rectangle(12,10)  
print("Area of rectangle:",newRectangle.rectangle_area())