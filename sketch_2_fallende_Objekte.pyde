yPos = 50
offset = 5

def setup():
    size(600, 600)

def draw():
    global yPos
    global offset
    
    print yPos
    background(255, 255, 255)
    
    ellipse(width/2, yPos, 50, 50)
    ellipse(width/2 + 150, yPos, 50, 50)
    
    if yPos > height - 25 or yPos < 25:
        offset = 0
    
    yPos = yPos + offset
