from Character import Char
from Walls import Wall
from Floor import Floor
from flying import Flying
import random

def setup():
    global stage
    stage = 1
    global collide
    collide = [[0 for x in range(1500)] for y in range(2000)] #giant boolean 2d array used for collision
    addCollision(450,0,100,50)
    addCollision(1000,0, 100,50)
    
    #LVL 1 IMAGES BELOW-------------------------------
    global a #top and bottom wall image
    global b #side wall image
    global c #floor image
    global d #stairs image
    global titleDisplay
    a = loadImage("topwall.png")       
    b = loadImage("sidewall.png")
    c = loadImage("floor.png")
    d = loadImage("Stairs.png")
    titleDisplay = loadImage("Title.png")
    #-------------------------------------------------
    
    #LVL 2 THINGS-------------------------------------
    global flying #array of the flying objects in stage 2
    global flyingSize #the size of the flying array
    flying = []
    flyingSize = 10
    for g in range (flyingSize):
        flying.append(Flying())
    #--------------------------------------------------
    
    global Keys #array to track key presses
    global Me #character
    global walls #used to draw walls
    global i #counter used in addCollision()
    global j #counter used in addCollision()
    global k
    global ground #used to draw floor
    ground = Floor()
    Keys = [False] * 5 #sets keys to be an array of 4 falses
    i = 0
    j = 0
    k = 0
    size(1500, 1000) #screen size
    Me = Char()
    walls = Wall()
    ground.drawFloor(c) # (floor image)
    walls.drawWall(a,a,b,b,d) # (topwall image, botwall image, leftwall image, rightwall image)
    Me.drawChar()
                        

#----------------------------------------DRAW-------------------------------------------------                
def draw():
    global stage
    if (stage == 1):#Title screen draw cycle
        image(titleDisplay,0,0)
        if(mousePressed == True):
            stage = stage + 1
    if (stage == 2):#level 1 draw cycle (SUMMONING ROOM)
        move()
        ground.drawFloor(c)
        walls.drawWall(a,a,b,b,d)
        Me.drawChar()
        if (Keys[4] == True):
            rect(400,200,700,600)
        if (Me.y <= 0):#Transfering to next level
            stage = stage + 1
            removeCollision()
            Me.x = 750
            Me.y = 960
            addCollision(0,0,1000,500)
            addCollision(1000,0, 1000,500)

    if (stage == 3):#Level 2 (STAIRCASE)
 
        move()
        background(50,50,50)#placeholder for staircase image
        rect(0,0,500,1000)#placeholder for left wall
        rect(1000,0,500,1000)#placeholder for right wall
        
        for g in range (flyingSize): #moves and draws the flying objects in stage 3
            flying[g].moveFlying()
            flying[g].drawFlying()
            if(flying[g].y > 990 and Me.y > 300):
                flying[g].y = 0
                flying[g].x = random.randrange(500, 950)
                flying[g].dy = random.randrange(5, 9)
        i = 0
        j = 0
        k = 0

        while(j<20):
            while(k<20):
                for g in range (flyingSize):
                    if(Me.x == flying[g].x + k and Me.y == flying[g].y + 30 + j):
                        death()
                        stage = 1
                k = k + 1
            k = 0
            j = j + 1
            
                    
        Me.drawChar()
        
        if(Me.y < 20):
            stage = stage + 1
            removeCollision()
            Me.x = 150
            Me.y = 900
    if(stage == 4):
        move()
        background(50,50,50)
        Me.drawChar()
        



#----------------------------------------FUNCTIONS----------------------------------------------------        
def death():
    clear()
    removeCollision()
    Me.x = 750
    Me.y = 900
    for g in range (flyingSize):
        flying[g].y=0

    
def keyPressed():#registers all key presses
    if(key == 'a'):
        Keys[0] = True
    if(key == 'd'):
        Keys[1] = True
    if(key == 'w'):
        Keys[2] = True
    if(key == 's'):
        Keys[3] = True
    if(key == 'p'):
        if(Keys[4] == True):
               Keys[4] = False
        else:
            Keys[4] = True

def keyReleased():
    if(key == 'a'):
        Keys[0] = False
    if(key == 'd'):
        Keys[1] = False
    if(key == 'w'):
        Keys[2] = False
    if(key == 's'):
        Keys[3] = False

    
def addCollision(x, y, w, h): #takes in an objects x and y coordinates and its width and height and sets up the objects collision with character
    i = 0
    j = 0

    while(i < h):
        while(j < w):
            collide[x+i][y+j] = True
            j= j+1
        j = 0
        i = i+1
        
def removeCollision():
    i = 0
    j = 0
    
    while(i<1500):
        while(j<1000):
            collide[i][j] = False
            j = j+1
        j=0
        i = i + 1
    
def checkCollision(x, y): #takes in the characters x and y coordinates and checks if you are colliding with an object
    if(collide[x-1][y-1] == True):
        return(True)
    else:
        return(False)

def move(): #movement and collision checks Left, Right, Up, Down respectively
    if(checkCollision((Me.x - 2), (Me.y+2)) == False and checkCollision((Me.x - 2), (Me.y + 42)) == False):
        if(Keys[0] == True):
            if(Me.x >= 55 and stage==2):
                Me.moveChar(-4,0)
            else: 
                if(stage == 3):
                    Me.moveChar(-4, 0)
    if(checkCollision((Me.x +2), (Me.y+42)) == False and checkCollision((Me.x + 2), (Me.y + 42)) == False and checkCollision((Me.x + 24), (Me.y)) == False and checkCollision((Me.x + 24), (Me.y + 42)) == False):
        if(Keys[1] == True):
            if(Me.x <= 1425 and stage == 2):
                Me.moveChar(4, 0)
            else:
                if(stage == 3):
                    Me.moveChar(4, 0)
    if(checkCollision((Me.x+2), (Me.y-2)) == False and checkCollision((Me.x + 22), (Me.y - 2)) == False):
        if(Keys[2] == True):
            if(((Me.y >=106) or (Me.x <1000 and Me.x >500)) and stage == 2):
                Me.moveChar(0, -4)
            else: 
                if(stage == 3):
                    Me.moveChar(0, -4)
    if(checkCollision((Me.x+2), (Me.y+2)) == False and checkCollision((Me.x + 22), (Me.y + 2)) == False and checkCollision((Me.x + 2), (Me.y + 43)) == False and checkCollision((Me.x + 22), (Me.y + 43)) == False):
        if(Keys[3] == True):
            if(Me.y <= 905 and stage == 2):
                Me.moveChar(0, 4)
            else:
                if(stage == 3):
                    Me.moveChar(0, 4)


 