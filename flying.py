import random

class Flying(object):
    def __init__(self):
        
        self.x = random.randrange(500, 950)
        self.y = 0
        self.w = 50
        self.h = 50
        self.dy = random.randrange(5, 9)
        
        
    def drawFlying(self):
        rect(self.x, self.y, self.w, self.h)
        
    def moveFlying(self):
        self.y = self.y + self.dy