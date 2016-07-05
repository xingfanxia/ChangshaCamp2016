# Python CLI Cipher
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-01 22:23:37
# @Author  : Xingfan Xia (xiax@carleton.edu)
# @Link    : http://xiax.tech
# @Version : $1.0

import random
message = input("please enter the code you want to encrypt: ")


#quit when the message is 'q'
while message != 'q':
    shift =input("enter the shift you want to use: ") 
    newm = ""

    #for the bonus part where we pick a number randomly between(included) 1 to 25. 
    if shift == 'random':
        shift = random.randint(1,25)
    else:
        shift = int(shift)
     
    
    #we use this loop to encrypt each letter in the message.
    for c in message: 
        
        c = ord(c)
        #we seperated lower and upper cases in case the user uses a large shift 
        #for the lower case:
        if  97<=c<=122:
            if c+shift > 122:
                c = 96 + (((c+shift)-122)%26) 
                #we used modulo here in case the user inputs a shift bigger than 26.
                newm = newm + chr(c)
            else:
                c = chr(c+shift)
                newm = newm + c
        #for the upper case
        elif 65<=c<=90:
            if c+shift > 90:
                c = 64 + (((c+shift)-90)%26)
                newm = newm + chr(c)
            else:
                c = chr(c+shift)
                newm = newm + c
        #for things other than letters
        else:
            newm = newm + chr(c)
    
    
    print (newm)
    print ('a shift of', shift, 'was used')
    #begin a new encryption. 
    message = input("enter the text to encrypt: ")
   

print("done")