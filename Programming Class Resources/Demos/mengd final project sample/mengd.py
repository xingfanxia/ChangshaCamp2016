#Author: Daihui Meng
#Special thanks to Xingfan Xia!Who after testing my game, contributed a lot of interesting ideas to improve it and makes it much more fun! Also thanks Alex my roommate who checked the grammar mistakes in instructions for me lol.


#Because pygame doesnt have a good built-in function for these graphics to track some important points or data, so I created my own. 
from __future__ import division
from random import *   
import pygame
from pygame.locals import *

class Rectangle:
    def __init__(self,win,color,origin,width,height):
        self.color = color
        self.win = win
        self.origin = origin
        self.width = width
        self.height = height
        self.center = [origin[0]+width//2,origin[1]+height//2]
        
    def draw(self):
        pygame.draw.rect(self.win,self.color,self.origin+[self.width,self.height])
        

    
class Line:
    def __init__(self,win,p1,p2,color,btype=1):
        self.p1 = p1
        self.p2 = p2
        self.color = color
        self.win = win
        self.btype = btype
    def draw(self):
        pygame.draw.line(self.win,self.color,(self.p1[0],self.p1[1]),(self.p2[0],self.p2[1]))
        
class Circle:
    def __init__(self,win,center,r,color):
        self.center = center
        self.win = win
        self.radius = r
        self.color = color
        
    def draw(self):
        pygame.draw.circle(self.win,self.color,self.center,self.radius)
    
 
    

    

#This class is for the buttons in the interface. 
class Towerbutton:
    def __init__(self,win,center,width,height,label):
        w,h = width/2.0, height/2.0
        x,y = center[0], center[1]
        self.xmax,self.xmin = x+w, x-w
        self.ymax,self.ymin = y+h, y-h
        self.width,self.height=width,height
        self.center = center
        self.label = label
        self.color = (100,100,100)
        #This availability is used to control towers' cooldown, calculated by updating tupdate.
        self.available = True
        self.tupdate = 0

    def draw(self,win):
        pygame.draw.rect(win,self.color,[self.xmin,self.ymin,self.width,self.height])
        self.font = pygame.font.SysFont("Cambria", 22)  
        label = self.font.render(self.label,1,((150, 25, 25)))
        win.blit(label,(self.xmin+10,self.ymin+5))
        
    def clicked(self,p,money):
    #Check if the button is clikced, return true if it is clicked and the user has enough money and the tower is available.
        if self.label == 'Tower I':
            if self.xmin <= p[0] <= self.xmax and self.ymin <= p[1] <= self.ymax and money>=150 and self.available:
                return True
        if self.label == 'Tower II':
            if self.xmin <= p[0] <= self.xmax and self.ymin <= p[1] <= self.ymax and money>=300 and self.available:
                return True
        
        if self.label == 'Remove':
            if self.xmin <= p[0] <= self.xmax and self.ymin <= p[1] <= self.ymax and money>=150 and self.available:
                return True
            
        if self.label == '  Block':
            if self.xmin <= p[0] <= self.xmax and self.ymin <= p[1] <= self.ymax and money>=100 and self.available:
                return True

    def cooldown(self):
        self.color = (50,50,50)
        self.available = False
    
    def ready(self):
        self.color = (100,100,100)
        self.available = True

        

        
        
#This class is for all the towers.        
class Tower:
    def __init__(self,win,origin,width,height,Ttype=1):
        
        self.Ttype = Ttype
        self.win = win
        self.origin = origin
        self.width = width
        self.height = height
        self.shape = []
        self.tupdate = 0 
        self.level = 1
        self.font = pygame.font.SysFont("Cambria", 50) 
        
        #Different types have different features. 
        if Ttype == 1:
            self.dmg = 30
            self.hp = 150
            self.firerate = 5
            self.color = (125,125,200)
            self.cost = 150
            self.shape = Rectangle(self.win,self.color,self.origin,self.width,self.height)

        if Ttype == 2:
            self.dmg = 100
            self.hp = 150
            self.firerate = 15
            self.color = (200,125,125)
            self.cost = 300
            self.shape = Rectangle(self.win,self.color,self.origin,self.width,self.height)

        if Ttype == 3:
            self.hp = 600
            self.color = (75,20,75)
            self.cost = 100
            self.shape = Rectangle(self.win,self.color,self.origin,self.width,self.height)
            
    def draw(self):
        body = Rectangle(self.win,self.color,self.origin,self.width,self.height)
        body.draw()
        level = self.font.render(str(self.level),1,(255,255,255))
        self.win.blit(level,(self.shape.origin[0]+65,self.shape.origin[1]+50))
    
    def shoot(self,win):

        p1 = self.shape.center
        p2 = [self.shape.center[0]+40,self.shape.center[1]]
        beam = Line(win,p1,p2,self.color)
        return beam

    

    
    
#This class if for all the minions in the game. 
class Minion:
    def __init__(self, mtype=1,level=0):
        Black = (25,25,70)
        Red = (70,25,25)
        y = [185,350,510]
        self.pos = [1300,y[randint(0,2)]]
        self.mtype = mtype
        
        #Different minions have different data. 
        if mtype == 1:
            self.radius = 20
            self.color = Black
            self.ms = 3
            self.hp = 90 + level*4    #I added level for minions, the higher the level is, the more damage and hp they have.
            self.dmg = 70 + level*2
        if mtype == 2:
            self.radius = 20
            self.color = Red
            self.ms = 5
            self.hp = 50 + level*4
            self.dmg = 30 + level*2
            
    def draw(self,win):
        minion = pygame.draw.circle(win,self.color,(self.pos[0],self.pos[1]),self.radius)
        
        
        

        
#MAIN class.
class Game:
    def __init__(self,win):
       
        self.interface = Interface(win)
        self.hp = 100
        self.money = 400
        self.score = 0
        self.tower1 = []
        self.tower2 = []
        self.block = []
        self.beam1 = []
        self.beam2 = []
        self.tupdate = 0
        self.minions = []
        self.balance = 0
        self.highestscore = 0
        self.miniondeath = 0 #Minions level up by dying...The more they die, the stronger they will be...
        self.odd = 3 #This refers to the odd which determines whether a minion will be generated in each round. 
    

    def addTower(self,event):
    #When the user clicks a button, it will check which button the user clicked and pause the game. Then if the user clicks again, the function will check if the user clicks in any of the spots. Then it will check whether on that spot there is already any tower(block). If not, it will build the tower on the spot.
    
        time = pygame.time.get_ticks()
        ttype = 0
        if event.type == MOUSEBUTTONDOWN:
    
            pt = pygame.mouse.get_pos()
            if self.interface.tower1.clicked(pt,self.money):  
                ttype = 1
            if self.interface.tower2.clicked(pt,self.money):
                ttype = 2
            if self.interface.block.clicked(pt,self.money):
                ttype = 3
            if ttype:
                newevent = pygame.event.poll()
                while newevent.type != MOUSEBUTTONDOWN:
                    newevent = pygame.event.poll()
                if newevent.type == MOUSEBUTTONDOWN:
                    pt2 = pygame.mouse.get_pos()
                    for spot in self.interface.spots:
                        if spot.origin[0] <= pt2[0] <= spot.origin[0]+spot.width and spot.origin[1] <= pt2[1] <= spot.origin[1]+spot.height:
                            tower = Tower(self.interface.win,spot.origin,spot.width,spot.height,ttype)
                            tower.draw()
                            condition = True
                            for t in self.tower1:
                                if tower.origin == t.origin:
                                    condition = False
                            for t in self.tower2:
                                if tower.origin == t.origin:
                                    condition = False
                            for t in self.block:
                                if tower.origin == t.origin:
                                    condition = False
                            if condition:
                                if ttype == 1:
                                    self.tower1.append(tower)
                                    self.money = self.money - tower.cost
                                    self.interface.tower1.cooldown()
                                    self.interface.tower1.tupdate = time
                                if ttype == 2:
                                    self.tower2.append(tower)
                                    self.money = self.money - tower.cost
                                    self.interface.tower2.cooldown()
                                    self.interface.tower2.tupdate = time
                                if ttype == 3:
                                    self.block.append(tower)
                                    self.money = self.money - tower.cost
                                    self.interface.block.cooldown()
                                    self.interface.block.tupdate = time
          
    def towerpreparing(self):
    #This is calculating tower's cooldown time. After a certain time interval, the tower will be ready to build again.
    
        t = pygame.time.get_ticks()
        if t-self.interface.tower1.tupdate > 5000:
            self.interface.tower1.ready()
            self.interface.tower1.tupdate = t
        if t-self.interface.tower2.tupdate > 5000:
            self.interface.tower2.ready()
            self.interface.tower2.tupdate = t
        if t-self.interface.block.tupdate > 50000:
            self.interface.block.ready()
            self.interface.block.tupdate = t
            
                                
    def removetower(self,event):
    #If the user click the remove button, it will pause the game then wait for the user to click again. If the place where the user clicks is a tower or block, it will remove it.    
    
        if event.type == MOUSEBUTTONDOWN:
            pt = pygame.mouse.get_pos()
            if self.interface.tower3.clicked(pt,self.money):  
                
                newevent = pygame.event.poll()
                while newevent.type != MOUSEBUTTONDOWN:
                  
                    newevent = pygame.event.poll()
                if newevent.type == MOUSEBUTTONDOWN:
           
                    pt2 = pygame.mouse.get_pos()
                    for t in self.tower1:
                        if t.origin[0] <= pt2[0] <= t.origin[0]+t.width and t.origin[1] <= pt2[1] <= t.origin[1]+t.height:
                            self.tower1.remove(t)
                            self.money = self.money-150
                    for t in self.tower2:
                        if t.origin[0] <= pt2[0] <= t.origin[0]+t.width and t.origin[1] <= pt2[1] <= t.origin[1]+t.height:
                            self.tower2.remove(t)
                            self.money = self.money-150
                    for block in self.block:
                        if block.origin[0] <= pt2[0] <= block.origin[0]+block.width and block.origin[1] <= pt2[1] <= block.origin[1]+block.height:
                            self.block.remove(block)
                            self.money = self.money-150
                    
    
    def addMinion(self):
    #This is the most crucial part.     
        
        time = pygame.time.get_ticks()-self.balance
        #After certain amount of time, the odd for generating the minions will decrease a bit to give users some time to adjust themselves. 
        if time >= 10000 and (time//10000)%8==0:
            self.balance = self.balance + 80000
            self.odd = self.odd - 5
            time = time - self.balance
            self.tupdate = self.tupdate-self.balance
        
        #The odd for generating minions will increase after a certain interval of time. The maximum is set to be 90.
        if time - self.tupdate > 13000:
            self.odd = self.odd + 3
            self.tupdate = time
        if self.odd >= 90:
            self.odd = self.odd - 5
            
        #Randomly generate one of the types of minions.    
        chance = randint(1,1000)
        mtype = randint(1,2)
        if chance <= self.odd and len(self.minions)<=30:
            if mtype == 1: 
                minion = Minion(mtype,int(self.miniondeath/20))
                self.minions.append(minion) 
            if mtype == 2:
                minion = Minion(mtype,int(self.miniondeath/20))
                self.minions.append(minion)


    def towershoot(self):
    #Tower shoot out a beam to attack. Time interval depends on firerate. 
    
        time = pygame.time.get_ticks()
        if self.tower1:
            if time - self.tower1[0].tupdate > self.tower1[0].firerate*200:
                for tower in self.tower1:
                    beam = tower.shoot(self.interface.win)
                    self.beam1.append(beam)
                    self.tower1[0].tupdate = time
        if self.tower2:
            if time - self.tower2[0].tupdate > self.tower2[0].firerate*200 :
                for tower in self.tower2:
                    beam = tower.shoot(self.interface.win)
                    self.beam2.append(beam)
                    self.tower2[0].tupdate = time

            
    def minionwalk(self):
        for minion in self.minions:
            minion.pos = [minion.pos[0]-minion.ms,minion.pos[1]]
            minion.draw(self.interface.win)
      
            
            
    def beamfly(self):
    #Beams fly for a small distance. It will be removed from the list if it flies out of the interface. 
    
        for beam in self.beam1:
            nbeam = beam
            nbeam.p1 = [beam.p1[0]+5,beam.p1[1]]
            nbeam.p2 = [beam.p2[0]+5,beam.p2[1]]
            nbeam = Line(beam.win,beam.p1,beam.p2,beam.color)
            if nbeam.p2[0] >= 1300:
                self.beam1.remove(beam)
            beam.draw()
        for beam in self.beam2:
            nbeam = beam
            nbeam.p1 = [beam.p1[0]+5,beam.p1[1]]
            nbeam.p2 = [beam.p2[0]+5,beam.p2[1]]
            nbeam = Line(beam.win,beam.p1,beam.p2,beam.color)
            if nbeam.p2[0] >= 1300:
                self.beam2.remove(beam)
            beam.draw()

            
    def beamdmg(self):
    #beams do damage. After each damage the beam will disappear. 
    
        for beam in self.beam1:
            condition = False
            for minion in self.minions:
                if minion.pos[0]-beam.p2[0] <= 1 and minion.pos[1] == beam.p2[1]:
                    minion.hp = minion.hp-self.tower1[0].dmg
                    condition = True
            if condition:
                self.beam1.remove(beam)
        for beam in self.beam2:   
            condition = False
            for minion in self.minions:
                 if minion.pos[0]-beam.p2[0] <= 1 and minion.pos[1] == beam.p2[1]:
                    minion.hp = minion.hp-self.tower2[0].dmg
                    condition = True
            if condition:
                self.beam2.remove(beam)
                
                   
    def miniontakedmg(self):
        
        for minion in self.minions:
            if minion.hp <= 0:
                self.minions.remove(minion)
                self.money+= 20
                self.score+=100
                self.miniondeath+=1
                
                
    def miniondmg(self):
    #If the minion touches the tower(or base) it causes damage to the tower and disappear. Then the tower/base will change width, which represents its hp. 
    
        for minion in self.minions:
            for tower in self.tower1:
                if minion.pos[0]-(tower.shape.origin[0]+tower.shape.width)<=5 and minion.pos[1] == tower.shape.center[1]:
                    chp = tower.hp
                    tower.hp = tower.hp-minion.dmg
                    tower.width = int(tower.width*(tower.hp/chp))
                    self.minions.remove(minion)
            for tower in self.tower2:
                if minion.pos[0]-(tower.shape.origin[0]+tower.shape.width)<=5 and minion.pos[1] == tower.shape.center[1]:
                    chp = tower.hp
                    tower.hp = tower.hp-minion.dmg
                    tower.width = int(tower.width*(tower.hp/chp))
                    self.minions.remove(minion)
            for block in self.block:
                if minion.pos[0]-(block.shape.origin[0]+block.shape.width)<=5 and minion.pos[1] == block.shape.center[1]:
                    chp = block.hp
                    block.hp = block.hp-minion.dmg
                    block.width = int(block.width*(block.hp/chp))
                    self.minions.remove(minion)
            if minion.pos[0]-180<=5:
                chp = self.hp
                self.hp = self.hp-minion.dmg//3
                self.interface.base.height = int(self.interface.base.height*(self.hp/100))
                self.minions.remove(minion)
                   
    def towertakedmg(self):
        for tower in self.tower1:
            if tower.hp<=0:
                self.tower1.remove(tower)
        for tower in self.tower2:
            if tower.hp<=0:
                self.tower2.remove(tower)
        for block in self.block:
            if block.hp<=0:
                self.block.remove(block)
    
                
    def updateinter(self):
    #Update data from the game to the interface for display.    
        
        self.interface.hp = self.hp
        self.interface.money = self.money
        self.interface.score = self.score
        self.interface.minionkill = self.miniondeath
        if self.score > self.highestscore:
            self.highestscore = self.score
        
        
    def updatetower(self):
    #Draw all the towers each round.
        for tower in self.tower1:
            tower.draw()
        for tower in self.tower2:
            tower.draw()
        for block in self.block:
            block.draw()
            
            
    def upgrade(self,event):
    #Another important feature. If the user has enough money and clicks one of the tower/block, it will beleveled up. The maximum level is 3. The cost is 1000*level.  
        
        if event.type == MOUSEBUTTONDOWN:
            pt = pygame.mouse.get_pos()
            
            for t in self.tower1:
                if t.origin[0] <= pt[0] <= t.origin[0]+t.width and t.origin[1] <= pt[1] <= t.origin[1]+t.height and self.money >= 1000*t.level and t.level<=2:
                    self.money = self.money-1000*t.level
                    t.hp = t.hp * 3
                    t.firerate = t.firerate - 1
                    t.dmg = t.dmg + 60
                    t.level+=1
            for t in self.tower2:
                if t.origin[0] <= pt[0] <= t.origin[0]+t.width and t.origin[1] <= pt[1] <= t.origin[1]+t.height and self.money >= 1000*t.level and t.level<=2:
                    self.money = self.money-1000*t.level
                    t.hp = t.hp * 3
                    t.firerate = t.firerate - 5
                    t.dmg = t.dmg + 100
                    t.level+=1

            for block in self.block:
                if block.origin[0] <= pt[0] <= block.origin[0]+block.width and block.origin[1] <= pt[1] <= block.origin[1]+block.height and self.money >=1000*block.level and block.level<=2:
                    block.hp = block.hp*2
                    self.money = self.money-1000*block.level
                    block.level+=1
                    


    def run(self,event):
        self.upgrade(event)
        self.addTower(event)
        self.towerpreparing()
        self.removetower(event)
        self.towershoot()
        self.beamfly()
        self.addMinion()
        self.minionwalk()
        self.beamdmg()
        self.miniontakedmg()
        self.miniondmg()
        self.towertakedmg()
        self.updateinter()
        self.updatetower()

        
    def reset(self):    

        self.hp = 100
        self.money = 400
        self.score = 0
        self.tower1 = []
        self.tower2 = []
        self.beam1 = []
        self.beam2 = []
        self.tupdate = 0
        self.minions = []
        self.block = []
        self.odd = 3
        self.interface.base.width = 170
        self.interface.tower1.ready()
        self.interface.tower2.ready()
        self.interface.block.ready()
        self.miniondeath = 0

        

class Interface():
    
    def __init__(self,win):
    
        self.font = pygame.font.SysFont("Cambria", 22)  
        
        self.win = win
        GREY = (200,200,200)
        GREEN = (125, 200, 125)
        self.base = Rectangle(self.win,GREEN,[10,95],170,500)
        
        r1 = Rectangle(win,GREY,[185,105],155,160)
        r2 = Rectangle(win,GREY,[185,275],155,150)
        r3 = Rectangle(win,GREY,[185,435],155,150)
        r4 = Rectangle(win,GREY,[345,105],155,160)
        r5 = Rectangle(win,GREY,[345,275],155,150)
        r6 = Rectangle(win,GREY,[345,435],155,150)
        r7 = Rectangle(win,GREY,[505,105],155,160)
        r8 = Rectangle(win,GREY,[505,275],155,150)
        r9 = Rectangle(win,GREY,[505,435],155,150)
        r10 = Rectangle(win,GREY,[665,105],155,160)
        r11 = Rectangle(win,GREY,[665,275],155,150)
        r12 = Rectangle(win,GREY,[665,435],155,150)
        self.spots = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12]
        
        self.tower1 = Towerbutton(self.win,[300,50],100,40,'Tower I')
        self.tower2 = Towerbutton(self.win,[450,50],100,40,'Tower II')
        self.tower3 = Towerbutton(self.win,[750,50],100,40,'Remove')
        self.block = Towerbutton(self.win,[600,50],100,40,'  Block')
        
        self.hp = 100
        self.money = 1000
        self.score = 0
        self.minionkill = 0
        
    def draw(self):
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        GREY = (125,125,125)
        
        hp = self.font.render('HP = '+str(self.hp),1,((20, 75, 75)))
        self.win.blit(hp,(300,600))
        money = self.font.render('Money = '+str(self.money),1,((20, 75, 75)))
        self.win.blit(money,(500,600))
        score = self.font.render('Score = '+str(self.score),1,((20, 75, 75)))
        self.win.blit(score,(700,600))
        minionkill = self.font.render('You have executed '+str(self.minionkill)+'    minions',1,((70,25,25,)))
        self.win.blit(minionkill,(950,40))
        
        pygame.draw.line(self.win,BLACK,[180,95],[900,95])
        pygame.draw.line(self.win,BLACK,[180,595],[900,595])
        self.base.draw()
        
        pygame.draw.line(self.win,BLACK,[180,104],[900,104])
        pygame.draw.line(self.win,BLACK,[180,265],[900,265])
        pygame.draw.line(self.win,BLACK,[180,274],[900,274])
        pygame.draw.line(self.win,BLACK,[180,425],[900,425])
        pygame.draw.line(self.win,BLACK,[180,434],[900,434])
        pygame.draw.line(self.win,BLACK,[180,585],[900,585])
        
        for rect in self.spots:
            rect.draw()
        
        self.tower1.draw(self.win)
        self.tower2.draw(self.win)
        self.tower3.draw(self.win)
        self.block.draw(self.win)
        fontc = pygame.font.SysFont('Cambria',10)
        cost1 = self.font.render('cost=150',1,(200,125,125))
        cost2 = self.font.render('cost=300',1,(200,125,125))
        cost3 = self.font.render('cost=150',1,(200,125,125))
        cost4 = self.font.render('cost=100',1,(200,125,125))
        self.win.blit(cost1,(self.tower1.xmin,self.tower1.ymax))
        self.win.blit(cost2,(self.tower2.xmin,self.tower2.ymax))
        self.win.blit(cost3,(self.tower3.xmin,self.tower3.ymax))
        self.win.blit(cost4,(self.block.xmin,self.block.ymax))
        
        
    def startscreen(self):
  
        instruction1 = self.font.render("Instructions: This is a tower defense game", 1, (75, 0, 75))
        instruction2 = self.font.render("                         Survive longer to get a higher score!", 1, (75, 0, 75))
        instruction3 = self.font.render('                         When you click the tower type you want to build, the game will pause until you build a tower, ', 1, (75,0,75))
        instruction4 = self.font.render('                         then click the grey spot where you want to build the tower.', 1, (75,0,75))
        instruction5 = self.font.render('                         Each tower has a different firerate, damage and cooldown, try them out!',1,(75,0,75))
        instruction6 = self.font.render('                         IMPORTANT TIP: Minions will grow stronger every 20 deaths.',1,(75,0,75))
        instruction7 = self.font.render('                         IMPORTANT TIP: You can UPGRADE your tower!!! It costs 1000*level.Maximum level is 3 ',1,(75,0,75))
        instruction8 = self.font.render('                                                          Simply click the tower(or block) you want to upgrade when you have enough money.',1,(75,0,75))
        instruction9 = self.font.render('                         Press RETURN to start and GOOD LUCK!',1,(75,0,75))
        instruction10 = self.font.render('                        P.S. This game is HARD! Try several times to get used to its pace! You could get more than 100000 !',1,(75,0,75))
        instruction11 = self.font.render('                        P.P.S Actually I think I got the highest scores, its around 260000. Try to win me lol!',1, (75,0,75))
        self.win.blit(instruction1,(50, 100))
        self.win.blit(instruction2,(50, 125))
        self.win.blit(instruction3,(50,150))
        self.win.blit(instruction4,(50,175))
        self.win.blit(instruction5,(50,200))
        self.win.blit(instruction6,(50,250))
        self.win.blit(instruction7,(50,275))
        self.win.blit(instruction8,(50,300))
        self.win.blit(instruction9,(50,350))
        self.win.blit(instruction10,(50,400))
        self.win.blit(instruction11,(50,425))
        pygame.display.flip()
    
    def endscreen(self,score,hscore):
        s1 = self.font.render('GAME OVER',1,(100,0,75))
        s2 = self.font.render('Your score is: '+str(score),1,(75,0,75))
        s3 = self.font.render('Highest score is: '+str(hscore),1,(75,0,75))
        s4 = self.font.render('Press RETURN to start a new game',1,(75,0,75))
        self.win.blit(s1,(100,150))
        self.win.blit(s2,(100,170))
        self.win.blit(s3,(100,190))
        self.win.blit(s4,(100,210))
        pygame.display.flip()
        

    
def main():
    size = (1300,700)
    bgcolor = (255,255,255)
    win = pygame.display.set_mode(size)
    pygame.init()
    win.fill(bgcolor)
    game = Game(win)
    clock = pygame.time.Clock()
    event = pygame.event.poll()
    
    while not (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
      
        if event.type == pygame.QUIT:
            quit()
        game.interface.startscreen()
        clock.tick(50)
        event = pygame.event.poll()
    
    while event.type != pygame.QUIT:
        while  game.hp >= 0:
            if event.type == pygame.QUIT:
                quit()
            win.fill(bgcolor)
            game.interface.draw()
            game.run(event)
            pygame.display.flip()
            clock.tick(50)
            event = pygame.event.poll()
        while not (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
            win.fill(bgcolor)
            game.interface.endscreen(game.score,game.highestscore)
            clock.tick(50)
            if event.type == pygame.QUIT:
                quit()
            event = pygame.event.poll()
        game.reset()
        

    quit()
  
    
    


main()