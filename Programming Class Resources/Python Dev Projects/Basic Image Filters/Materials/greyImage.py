# Author: Sherri Goings
# Simple example using cImage to filter a .gif to be in greyscale

from cImage import *

def scale(val):
    """ scales a value to be in the allowable color range for a pixel 0-255 """
    if val < 0:
        val = 0
    elif val > 255:
        val = 255
    return val

def saturatedRGB(r,g,b,k):
    """ takes the red, green, and blue values for the color of a pixel as well
    as a k value that represents how much to saturate the color, then returns
    a list containing the saturated red, green, and blue values of the color"""
    vals = [.3*(1-k), .6*(1-k), .1+.9*k]
    newr =  scale((.3+.7*k)*r + .6*(1-k)*g + .1*(1-k)*b)
    newg = scale(.3*(1-k)*r + (.6+.4*k)*g + .1*(1-k)*b)
    newb = scale(.3*(1-k)*r + .6*(1-k)*g + (.1+.9*k)*b)
    return [int(newr),int(newg),int(newb)]


def greyscale(imag):
    """ takes the original image as an argument, returns a greyscale version
    without modifying the original image at all """
    greyIm = imag.copy()

    # loop through each pixel in the orig image, find the average of the
    # r,g,b values and set the same pixel in the copied image to have
    # r,g,b all equal that average
    numPix = imag.getNumPixels()
    for i in range(numPix):
        p = imag.getPixel1D(i)
        ave = (p.red + p.green + p.blue) // 3
        p.red, p.green, p.blue = ave, ave, ave
        greyIm.setPixel1D(i, p)
    return greyIm


def main():
    # open AA.gif and use its dimensions to make a suitably sized window
    origImage = FileImage("AA.gif")
    win = ImageWin("dogs! are great!",origImage.getWidth()*2,origImage.getHeight())
    origImage.draw(win)

    # draw the greyscale version of origImage to the right of origImage
    greyscaleImage = greyscale(origImage)
    greyscaleImage.setPosition(origImage.getWidth()+1,0)
    greyscaleImage.draw(win)

    # ask for input so window stays open until user hits enter on terminal
    input("enter to quit")

main()
