while(True):
	print('''
================================
Please select a drink you want!=
1 for Apple Juice              =
2 for Coke                     =
3 for Orange Juice             =
================================
	''')
	a =int(input("please enter your choice:\n"))
	if(a == 1):
		print("Here is your apple juice")
	elif(a == 2):
		print("Here is your Coke")
	elif(a == 3):
		print("Here is your orange juice")
	else:
		print("You can't always get what you want")