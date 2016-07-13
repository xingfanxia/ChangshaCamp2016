#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python rawimage Filter 2 Blur
# @Date    : 2016-07-02 00:00:04
# @Author  : Xingfan Xia
# @Link    : http://xiax.tech
# @Version : v2.0

from cImage import *
import sys
from math import *

def scale(image,scaleFactor):
    width = image.getWidth()
    height = image.getHeight()
    
    #create a new scaled empty image 
    newwidth = round(width*scaleFactor)
    newheight = round(height*scaleFactor)
    nimage = EmptyImage(newwidth,newheight)
    
    #create two lists to store the coordinate of pixels we want to take from the original image
    newx = []
    newy = []
    tx = 0
    x = 0
    ty = 0
    y = 0
    #because the step in for loop can only be integer, we chose while loop by employing an intermediate variable(tx,ty).
    while x <= width:
        newx.append(x)
        tx += 1/scaleFactor
        x = int(0+tx)
    while y <= height:
        newy.append(y)
        ty += 1/scaleFactor
        y = int(0+ty)
    
    #get pixels from original image according to the lists, and put them into the new image.
    for x in range (newwidth):
        for y in range (newheight):
            pix = image.getPixel(newx[x],newy[y])
            nimage.setPixel(x,y,pix)
    return nimage



def blur(image,r):
    #blur on a copy.
    nimage = image.copy()
    nx = []
    ny = []
    #get the coordinate for the first pixel in the square to be blurred. 
    for x in range (0,image.getWidth()-2*r,2*r):
        nx.append(x)
    for y in range(0,image.getHeight()-2*r,2*r):
        ny.append(y)
    
    avgr = 0
    avgg = 0
    avgb = 0
    
    for x in nx:
        for y in ny:
            
            #get the rest of the pixels in the square one by one. Add the rgb of each pixel to the average rgb.
            for i in range (2*r):
                for j in range(2*r):
                    pix = nimage.getPixel(x+i,y+j)
                    avgr, avgg, avgb = avgr+pix.red, avgg+pix.green, avgb+pix.blue
            
            #calculate the average rgb after blurring. 
            avgr, avgg, avgb = round(avgr/((2*r+1)**2)), round(avgg/((2*r+1)**2)), round(avgb/((2*r+1)**2))
            
            #again take each of the pixel in the square one by one, change the rgb for each to the average rgb, then put each one back. 
            for i in range (2*r):
                for j in range(2*r):
                    pix = nimage.getPixel(x+i,y+j)
                    pix.red,pix.green,pix.blue = avgr, avgg, avgb
                    nimage.setPixel(x+i,y+j,pix)
    
    return nimage
   
    
def main():
    image = FileImage(sys.argv[1])
    k = sys.argv[2]
    k = float(k)
    rad = sys.argv[3]
    rad = int(rad)
    win = ImageWin('mengd',round(2*image.getWidth()+image.getWidth()*k), round(image.getHeight()+image.getHeight()*k))
    image.draw(win)
    nimage1 = scale(image,k)
    nimage1.setPosition(image.getWidth()+2,0)
    nimage1.draw(win)
    nimage2 = blur(image,rad)
    nimage2.setPosition(image.getWidth()+nimage1.getWidth()+2,0)
    nimage2.draw(win)
    
    input("enter to quit: ")

if __name__ == '__main__':
	main()