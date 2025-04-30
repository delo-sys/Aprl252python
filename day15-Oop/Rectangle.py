class Rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def calaarea(self):
        return self.length * self.width

    def calaperimeter(self):
        return ((self.length + self.width)*2)
