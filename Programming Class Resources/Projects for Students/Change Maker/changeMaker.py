#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-01 22:23:37
# @Author  : Xingfan Xia (xiax@carleton.edu)
# @Link    : http://xiax.tech
# @Version : $1.0
from __future__ import division
import math

def main():
	itemAmt = float(input("Please enter the item price:"))
	cashAmt = float(input("Please enter the cash payed:"))
	changeAmt = cashAmt - itemAmt
	change(changeAmt)

def change(amount):
	# Assume there are notes of 100, 50, 20, 10 and 5 
	# coins of 50cents and 10cents
	notes_coins = [100, 50, 20, 10, 5, 1, 0.5, 0.1, 0.05, 0.01]
	change_list = []
	# while(amount>0):
	for c in range(len(notes_coins)):
		temp = int(amount//notes_coins[c])
		change_list.append(temp)
		amount = round(amount - temp*notes_coins[c], 2)
	for n in range(len(change_list)):
		print("You need {} of notes of {}".format(change_list[n], notes_coins[n]))

if __name__ == '__main__':
	main()