# Photolab Image filters
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-01 22:23:37
# @Author  : Xingfan Xia (xiax@carleton.edu)
# @Link    : http://xiax.tech
# @Version : $1.0

from cImage import *
from sys import *

def oneColor(image,color):
    newimage = image.copy()
    
    for i in range(image.getNumPixels()):
        pix = newimage.getPixel1D(i)
        if color == 'r':
            pix.red, pix.blue, pix.green = pix.red, 0, 0
        elif color == 'b':
            pix.red, pix.blue, pix.green = 0, pix.blue, 0
        elif color == 'g':
            pix.red, pix.blue, pix.green = 0, 0, pix.green
        newimage.setPixel1D(i, pix)
    return newimage

def negate(image):
    newimage = image.copy()
    
    for i in range(image.getNumPixels()):
        pix = newimage.getPixel1D(i)
        pix.red, pix.green, pix.blue = 255-pix.red, 255-pix.green, 255-pix.blue
        newimage.setPixel1D(i,pix)
    return newimage

def scale(val):
#credit to Sherri
    if val < 0:
        val = 0
    elif val > 255:
        val = 255
    return val

def saturatedRGB(r,g,b,k):
#credit to Sherri :P
    vals = [.3*(1-k), .6*(1-k), .1+.9*k]    
    newr = scale((.3+.7*k)*r + .6*(1-k)*g + .1*(1-k)*b)
    newg = scale(.3*(1-k)*r + (.6+.4*k)*g + .1*(1-k)*b)
    newb = scale(.3*(1-k)*r + .6*(1-k)*g + (.1+.9*k)*b)
    return [int(newr),int(newg),int(newb)]

def saturate(image, k):
    newimage = image.copy()
    k = float(k)
    for i in range(image.getNumPixels()):
        pix = newimage.getPixel1D(i)
        sColor = saturatedRGB(pix.red,pix.green,pix.blue,k)
        pix.red,pix.green,pix.blue = sColor[0],sColor[1],sColor[2]
        newimage.setPixel1D(i,pix)
    return newimage

def main():
    
    image = FileImage(argv[1])
    win = ImageWin('mengd',image.getWidth()*2,image.getHeight()*2)
    image.draw(win)
    
    onecolor = oneColor(image,argv[2])
    onecolor.setPosition(image.getWidth()+1, 0)
    onecolor.draw(win)
    
    negateimage = negate(image)
    negateimage.setPosition(0, image.getHeight()+1)
    negateimage.draw(win)
    
    saturatedimage = saturate(image,argv[3])
    saturatedimage.setPosition(image.getWidth()+1,image.getHeight()+1)
    saturatedimage.draw(win)
    
    input("enter to quit: ")

if __name__ == '__main__':
    main()
