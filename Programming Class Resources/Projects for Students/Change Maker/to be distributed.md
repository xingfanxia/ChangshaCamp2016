```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-01 22:23:37
# @Author  : Xingfan Xia (xiax@carleton.edu)
# @Link    : http://xiax.tech
# @Version : $1.6

from __future__ import division
import math

# price
appleJuice = 19.5
coke = 3.7
orangeJuice = 12.4
instantnoodles = 2.7


def main():
	itemAmt = goods()
	print("The total amount to be piad is {}".format(itemAmt))
	cashAmt = float(input("Please enter the cash payed: \n"))
	changeAmt = round(cashAmt - itemAmt, 2)
	print("The total amount you paied is {}; The total price is {}; The change is {}".format(cashAmt, itemAmt, changeAmt))
	change(changeAmt)

def change(amount):
	# Assume there are notes of 100, 50, 20, 10 and 5 
	# coins of 50cents and 10cents
	notes_coins = [100, 50, 20, 10, 5, 1, 0.5, 0.1, 0.05, 0.01]
	change_list = []
	for c in range(len(notes_coins)):
		temp = int(amount//notes_coins[c])
		change_list.append(temp)
		amount = round(amount - temp*notes_coins[c], 2)
	for n in range(len(change_list)):
		print("You need {} of notes of {}".format(change_list[n], notes_coins[n]))

def goods():
	totalValue = 0.00
	while(True):
		print('''
	================================
	Please select a drink you want!=
	1 for Apple Juice              =
	2 for Coke                     =
	3 for Orange Juice             =
	4 for Instant Noddles          =
	q for leave the supermarket    =
	================================
		''')
		a =input("please enter your choice:\n")
		if(a == '1'):
			print("You have put apple juice in the basket")
			totalValue = totalValue + appleJuice
		elif(a == '2'):
			print("You have put Coke in the basket")
			totalValue = totalValue + coke
		elif(a == '3'):
			print("You have put orange juice in the basket")
			totalValue = totalValue + orangeJuice
		elif(a == '4'):
			print("You have put instant noodles in the basket")
		elif(a == 'q'):
			print("Leaving the supermarket")
			break
		else:
			print("You can't always get what you want")
	return round(totalValue, 2)

if __name__ == '__main__':
	main()
```

