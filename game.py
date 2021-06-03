from turtle import *
from distance import *
from random import randint

SpdShip = 25
SpdBlt = 30
ScreenWidth = 800
ScreenHeight = 800
DELAY=25
xShip = 0
yShip = -300
SpdEnemy = 30

ListBullet = []
ListEnemy = []
bulletImg = "blt.gif"
shipImg = "sh.gif"
backgroundImg = "bg.gif"
enemyImg = "quaivat.gif"
InstructionImg= "instruction.gif"
gameOverImg = "gameover.gif"

wd = Screen()
wd.setup(ScreenWidth,ScreenHeight)
wd.bgpic(InstructionImg)
wd.addshape(shipImg)
wd.addshape(bulletImg)
wd.addshape(enemyImg)

ship = Turtle()
ship.hideturtle()
ship.penup()
ship.shape(shipImg)
ship.goto(0,-300)

point = 0
pen = Turtle()
pen.hideturtle()
pen.penup()
pen.goto(275,350)
pen.color("white")

screenstatus = 1
def Changingscreen():
    global screenstatus
    if screenstatus == 1:
        screenstatus = 2
        wd.bgpic(backgroundImg)
        ship.showturtle()
        CreateEnemy()
        updatePen()
        updateAll()
        
def updatePen():
    pen.clear()
    pen.write("points: "+str(point),font = ("arial",18))

#Tao quai vat
def CreateEnemy():
    enemy = Turtle()
    enemy.hideturtle()
    ListEnemy.append([enemy,1])
    enemy.penup()
    enemy.shape(enemyImg)
    enemy.goto(randint(-ScreenWidth/2,ScreenWidth/2),300)
    enemy.showturtle()

#Update chiec thuyen
def updateShip():
    ship.goto(xShip,yShip)

#Di sang trai
def goleft():
    global xShip
    xShip -= SpdShip

#Di sang phai
def goright():
    global xShip
    xShip += SpdShip

#Di len tren
def goup():
    global yShip
    yShip += SpdShip

#Di xuong
def godown():
    global yShip
    yShip -= SpdShip

#Xoa vien dan
def deleteBullet(x):
    ListBullet.remove(x)
    x.hideturtle()
    del x

#Xoa vien dan
def deleteEnemy(x):
    ListEnemy.remove(x)
    x[0].hideturtle()
    del x

#BangBangBang
def shoot():
    if(len(ListBullet)<3):
        b = Turtle()
        b.penup()
        b.speed(0)
        ListBullet.append(b)
        b.hideturtle()
        b.shape(bulletImg)
        b.goto(ship.xcor(),ship.ycor())
        b.showturtle()
        
#Udate trang thai tat ca vien dan
def UpdateAllBullet():
    for b in ListBullet:
        if (b.ycor()<ScreenHeight/2):
            b.goto(b.xcor(),b.ycor()+SpdBlt)
        #Neu vien dan bay ra khoi screen 
        else:
            deleteBullet(b)

def gameOver():
    wd.bgpic(gameOverImg)
    for i in ListBullet:
        deleteBullet(i)
    for i in ListEnemy:
        deleteEnemy(i)
    ship.hideturtle()

def check():
    global point

    for i in ListBullet:
        for j in ListEnemy:
            if collision(i,j[0]):
                point += 5
                updatePen()
                deleteBullet(i)
                deleteEnemy(j)
                CreateEnemy()

    for i in ListEnemy:
        if collision(ship,i[0]):
            gameOver()

def updateAllEnemy():
    for i in ListEnemy:
        enemy = i[0]
        status = i[1]
        if status == 1:
            if enemy.xcor()>-400:
                enemy.goto(enemy.xcor()-SpdEnemy,enemy.ycor())
            else:
                i[1] = 0
                enemy.goto(enemy.xcor(),enemy.ycor()-SpdEnemy)    
        else:
            if enemy.xcor()<400:
                enemy.goto(enemy.xcor()+SpdEnemy,enemy.ycor())
            else:
                i[1] = 1
                enemy.goto(enemy.xcor(),enemy.ycor()-SpdEnemy)
        if enemy.ycor() < -400 :
            enemy.goto(enemy.xcor(),300)

#Udate trang thai tat ca
def updateAll():
    UpdateAllBullet() 
    updateAllEnemy()
    updateShip()
    check()
    ontimer(updateAll,DELAY)

wd.onkeypress(shoot,"space")
wd.onkeypress(goleft,"a")
wd.onkeypress(goright,"d")
wd.onkeypress(goup,"w")
wd.onkeypress(godown,"s")
wd.onkeypress(Changingscreen,"Return")
wd.listen()

mainloop()

