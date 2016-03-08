class Wall(object):

    def __init__(self):
        self.x = 750
        self.y = 950
        self.h = 40
        self.w = 20    
    
    def drawWall(self, b, c, d, e, f):


        image(b, 0, 0)
       
        image(c, 0, 950)

        image(d, 0, 0)

        image(e, 1450, 0)
        
        image(f, 500, 0)