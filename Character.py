class Char(object):
    def __init__(self):
        self.x = 750
        self.y = 900
        self.w = 20
        self.h = 40
    
    def drawChar(self):
        global a
        a = loadImage("sprite.png")
        image(a, self.x, self.y, self.w, self.h)
        
    
    def moveChar(self, a, b):
        self.x = (self.x + a)
        self.y = (self.y + b)