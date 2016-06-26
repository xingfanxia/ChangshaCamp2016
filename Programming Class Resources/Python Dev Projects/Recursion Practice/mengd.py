#Author: Daihui Meng
def drawFractal(win,length,detail,x=100,y=100):
    
    if detail == 0:
        tri = Polygon(Point(x,y),Point(x+length,y),Point(x+1/2*length,y+length))
        tri.draw(win)
        return
    
    triPoints = [[Point(x,y),Point(x+1/2*length,y),Point(x+1/4*length,y+1/2*length)],[Point(x+1/2*length,y),Point(x+length,y),Point(x+3/4*length,y+1/2*length)],[Point(x+1/4*length,y+1/2*length),Point(x+3/4*length,y+1/2*length),Point(x+1/2*length,y+length)]]
    
    for points in triPoints:
        tri = Polygon(points)
        tri.draw(win)
        drawFractal(win,length//2,detail-1,points[0].getX(),points[0].getY())
    return
  
    
        
from graphics import *
from sys import *
win = GraphWin('hw',800,800)
length = int(argv[1])
detail = int(argv[2])
drawFractal(win,length,detail)
input("enter to quit")
