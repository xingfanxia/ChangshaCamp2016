#author: Daihui Meng, Alex Lee

from graphics import *

t = int(input("please enter the current time: "))
p = input("am or pm: ")

win = GraphWin("scene", 800, 500)

#draw the sky according to the user's input.
sky = Rectangle(Point(0,0), Point(800, 450))
sky.draw(win)

if p == "pm":
    sky.setFill(color_rgb(225-18.75*(t%12), 225-18.75*(t%12), 250-18.75*(t%12)))
    t = t+0.25
elif p == "am":
    sky.setFill(color_rgb(18.75*(t%12), 18.75*(t%12), 18.75*(t%12)+25))
    t = t+0.25

#draw the house
rooftop = Polygon(Point(700, 300), Point(600, 350), Point(800, 350))
rooftop.draw(win)
rooftop.setFill("red")
house = Rectangle(Point(625, 350), Point(775, 450))
house.draw(win)
house.setFill("brown")
road = Line(Point(0, 450), Point(800, 450))
road.draw(win)

#draw the car
carBody = Rectangle(Point(0,435),Point(80,400))
carBody.draw(win)
carBody.setFill('yellow')
wheel1 = Circle(Point(15,435),15)
wheel1.draw(win)
wheel1.setFill('black')
wheel2 = Circle(Point(65,435),15)
wheel2.draw(win)
wheel2.setFill('black')


#change the color of the sky automatically as time lapses. 
for i in range (105):

    if p == "pm":
        if (t%12) != 0 and (t%12) < 12:
            sky.setFill(color_rgb(225-18.75*(t%12), 225-18.75*(t%12), 250-18.75*(t%12)))  
        if t%12 == 0:
            sky.setFill(color_rgb(0, 0, 25))
            p = "am"
        t = t+0.25
            
            
    if p == "am":
        if  (t%12) != 0 and (t%12) < 12:
            sky.setFill(color_rgb(18.75*(t%12), 18.75*(t%12), 18.75*(t%12)+25))
        if t%12==0:
            sky.setFill(color_rgb(225, 225, 255))
            p = "pm"
        t = t+0.25

#animating the car
    carBody.move(5,0)
    wheel1.move(5,0)
    wheel2.move(5,0)



input("hit enter to quit")
