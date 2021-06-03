
from turtle import *
import math 


def getdistance(a,b):
    dx=a.xcor()-b.xcor()
    dy=a.ycor()-b.ycor()
    d=math.sqrt(dx**2+dy**2)
    return d
    
def collision(a,b):
    if getdistance(a,b)<=50:
        return True
    if getdistance(a,b)>50:
        return False 