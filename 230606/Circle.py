import math

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    
    def calcArea(self):
        return math.pi * self.r * self.r
        
if __name__ == "__main__":
    c = Circle(10, 10, 10)
    print(c.calcArea())