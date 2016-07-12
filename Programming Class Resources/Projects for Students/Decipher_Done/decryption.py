# Python Decipher with File Handling
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-01 22:23:37
# @Author  : Xingfan Xia (xiax@carleton.edu)
# @Link    : http://xiax.tech
# @Version : $1.0

import sys
#a function that lists out the frequency of each alphabetical character
def frequencyList(content):
    
    content.lower()
    frequencyList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    for i in range (97, 123):
        for letter in content:
            if ord(letter) == i:
                frequencyList[i-97]+=1
    
    return frequencyList

# a function that finds the nth most common character in a list
def frequencyRanking(list,ranking):
    #find out the nth biggest frequency   
    templist = list[::]
    templist.sort()
    
    n=templist[-ranking]

    return n

# a function that finds out the corresponding character that has the frequency.
def frequencyMatching(list,frequency):
    character = ''
    for j in range(len(list)):
        if list[j]==frequency:
            character = chr(j+97)
            break
    
    return character

#a function that decyphers the texts.
def decypher(mostCommon,secondMost,content):
        
    #find out the shift
    shift = ord(mostCommon)-ord('e')
    
    #findout the corresponding second commonest before shift:
    secondMost = ord(secondMost)
    if secondMost-shift < 97:
        secondMost = chr(123-(97-(secondMost-shift)))
        
    else:
        secondMost = chr(secondMost-shift)
    

    #decypher
    decodedContent = ''
    if secondMost == 'a' or secondMost == 't':
        for c in content: 
            c = ord(c) 
            if  97<=c<=122:
                if c-shift < 97:
                    c = 123-(97-(c-shift))
                    decodedContent+=chr(c)
                else:
                    c = chr(c-shift)
                    decodedContent+=c

            elif 65<=c<=90:
                if c-shift <65:
                    c = 91 - (65-(c-shift))
                    decodedContent+=chr(c)
                else:
                    c = chr(c-shift)
                    decodedContent+=c

            else:
                decodedContent+=chr(c)
        print(decodedContent, file=decoded)
    else:
        print("unable to decrypt this text", file=decoded)

def main():       
    
    content = coded.read()
    list = frequencyList(content)
    n1 = frequencyRanking(list,1)
    n2 = frequencyRanking(list,2)
    c1 = frequencyMatching(list,n1)
    c2 = frequencyMatching(list,n2)
    decypher(c1,c2,content)

#Pass in the name of the file to be decrypted
codedfileName = str(sys.argv[1])
coded = open(codedfileName)
decoded = open('decoded.txt', 'w')     
main()
coded.close()
decoded.close()
    