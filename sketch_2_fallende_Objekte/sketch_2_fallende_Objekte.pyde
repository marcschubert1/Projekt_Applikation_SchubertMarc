start = 125
yPos1 = 125
yPos2 = 125
offset1 = 0
offset2 = 0
v1 = 0
v2 = 0
a = 0
b = 0

def setup():
    size(600, 600)

def draw():
    global yPos1
    global yPos2
    global v1
    global v2
    global offset1
    global offset2


    frameRate(60)
    background(120,80,80)
    noStroke()
    fill(255)
    ellipse(width/2, yPos1, 50, 50)
    ellipse(width/2 + 150, yPos2, 50, 50)
    fill(0,255,0)
    rect(50,50,50,50)
    fill(255,0,0)
    rect(50,150,50,50)
    fill(255)
    rect(550,50,25,550)
    rect(250,50,300,25)
    stroke(255)
    strokeWeight(3)
    line(width/2,75,width/2,100)
    line(width/2+150,75,width/2+150,100)
    textSize(20)
    textAlign(CENTER)
    # Text in der Darstellung (int wegen Kommastellen!)
    text(str(int(v1))+ "m/s", width/2, yPos1+50)
    text(str(int(v2))+ "m/s", width/2+150, yPos2+50)
    text("100 Meter", width/2+75, 40)
    text("Start",75, 120)
    text("Reset", 75, 220)
    text("Links: Erde", 100, 300)
    text("Rechts: Mond", 100, 320)
    yPos1 = yPos1 + offset1
    yPos2 = yPos2 + offset2
    
    button_clicked()
    boden_erreicht()
    
            
def button_clicked():
    global a
    global b
    global v1
    global v2
    global offset1
    global offset2
    global yPos1
    global yPos2
    if mouseX in range(50,100) and mouseY in range(50,100) and mousePressed == True:
        a = 1
        b = 1

    # wenn grün gedrückt, bezogen auf linke Kugel
    if a == 1:
        v1 = v1 + 9.81/60
        offset1 = offset1 + 9.81/800
    # wenn grün gedrückt, bezogen auf rechte Kugel
    if b == 1:
        v2 = v2 + 1.62/60
        offset2 = offset2 + 1.62/800
    # Geschwindigkeit abgeschätzt, aufgrund unbekannter Anzahl Pixel
        
    if mouseX in range(50,100) and mouseY in range(150,200) and mousePressed == True:
        yPos1 = start
        yPos2 = start
        offset1 = 0
        offset2 = 0
        a = 0
        b = 0
        v1 = 0
        v2 = 0
        
def boden_erreicht():
    global offset1
    global v1
    global offset2
    global v2
    if yPos1 > height - 30:
            offset1 = 0
            v1 = 0
            
    if yPos2 > height - 30:
            offset2 = 0
            v2 = 0


    
