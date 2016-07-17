# Published on https://www.pythonanywhere.com/user/xiax/files/home/xiax/game1.py?edit
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding=utf-8 
# @Date    : 2016-07-17 22:23:37
# @Author  : Xingfan Xia (xiax@carleton.edu)
# @Link    : http://xiax.tech
# @Version : $1.3

# 导入系统模块
import sys
HP = 10	#血
ATK = 5	#攻
DEF = 5	#防
MON = 0 #钱
LV = 0 #等级
Exp = 0 #经验值
Luck = 2 #运气
roles = 0 #角色

def upgrade():
	global Exp, LV, roles
	if(Exp >= 10):
		if (roles == 1):
			LV = LV +1
			ATK = ATK + 3
			DEF = DEF + 7
			HP = HP + 10
			Exp = 0
		elif (roles == 2):
			LV = LV +1
			ATK = ATK + 12
			DEF = DEF + 3
			HP = HP + 5
			Exp = 0
		elif (roles == 3):
			LV = LV +1
			ATK = ATK + 18
			DEF = DEF + 1
			HP = HP + 1
			Exp = 0

def role():
	global HP, ATK, DEF, roles
	print('''
1. 成为战士，变得很强壮
2. 成为刺客，很擅长阴人
3. 成为装逼者
		''')
	a = input("选择你的角色\n")
	if(a == '1'):
		roles = 1
		HP = 10
		ATK = 5
		DEF = 15
		print("你变得很耐揍")
	elif(a == '2'):
		roles = 2
		HP = 10
		ATK = 15
		DEF = 5
		print("你不耐揍，但是别人对你来说其实也不是很耐揍")
	elif(a == '3'):
		roles = 3
		HP = 1
		ATK = 28
		DEF = 1
		print("装逼不需要任何__")

def begin():
	if(HP<=0):
		print("你永久死亡了")
		input("按回车退出")
		sys.exit("还想重来吗")
	print("从前有座山")
	print("这时候你来来到了山路口，遇到两个强盗；你决定干什么\n")
	role()
	main1()

def main1():
	print('''
1. 打劫强盗
2. 付过路费
3. 杀了强盗
		''')
	a = input("输入你要的选项\n")
	if(a == '1'):
		branch1()
	elif(a == '2'):
		branch2()
	elif(a == '3'):
		branch3()
 
def branch1():
	global ATK, Exp, MON
	if (ATK > 10):
		print("你打劫了强盗，你获得了5元")
		MON = MON + 5
		Exp = Exp + 10
		## 更多后续剧情
	else:
		print("你的攻击力只有{}".format(ATK),"打不过")
		print("你被强行交\u2642易...")
		endgame()

def branch2():
	global DEF, ATK
	print("你并没有钱，强盗把你身上可能能值点钱的衣物都扒光了\n 你的属性下降，但是他们没有杀你")
	DEF = DEF - 2
	ATK = ATK - 2
	## 更多后续剧情

def branch3():
	global ATK, DEF, MON
	if (ATK > 10 and DEF>10):
		print("你杀了强盗，你获得了5元")
		MON = MON + 5
		Exp = Exp + 10
		upgrade()
		## 更多后续剧情
	else:
		print("你的攻击力只有{}，防御力只有{}".format(ATK, DEF),"打不过")
		print("虽然你很勇敢地上了；但是实力低微；你被强行交\u2642易... \n")
		endgame()

def endgame():
	global HP
	print("你死了")
	print("你的HP属性下降。。。")
	print("命运给了你重来的机会，好好珍惜")
	HP = HP -2
	begin()


if __name__ == '__main__':
	begin()