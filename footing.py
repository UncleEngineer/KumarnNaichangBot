#Kumarn Naichang Bot 555
#By Uncle Engineer

import pyautogui as pg
import time
from subprocess import Popen


Popen('C:\\Windows\\System32\\mspaint.exe')
#------Change Page Size-----------
time.sleep(2)
pg.press('altleft')
time.sleep(1)
pg.press('f')
time.sleep(1)
pg.press('e')
pg.typewrite('1000')
pg.press('tab')
pg.typewrite('500')
time.sleep(1)
pg.press('enter')
#------SELECT Tools-----

def selecttools(tools):
	key = ['alt','h','s','h']
	for i in key:
		pg.press(i)
		time.sleep(1)
	toolsnum = tools # 3 for rectangle
	for i in range(toolsnum):
		pg.press('right')
	pg.press('space')



def selectline():
	key = ['alt','h','s','z','space']
	for i in key:
		pg.press(i)
		time.sleep(1)

#------
def drawrec(xp,yp,sz):
	sizex = xp + sz
	sizey = yp + sz
	pg.moveTo(xp,yp)
	pg.dragTo(sizex,sizey, button='left')
	pg.click(sizex+20,sizey+20)




def drawcolumn(xp,yp,sz,columnsize):
	xp2 = (xp + (sz/2)) - (columnsize/2)
	yp2 = (yp + (sz/2)) - (columnsize/2)
	sizex = xp2 + columnsize
	sizey = yp2 + columnsize
	pg.moveTo(xp2,yp2)
	pg.dragTo(sizex,sizey, button='left')
	pg.click(sizex+20,sizey+20)

def drawfooting(xloc,yloc,footingsize,columnsize):
	drawrec(xloc,yloc,footingsize)
	drawcolumn(xloc,yloc,footingsize,columnsize)


# Start Program
selecttools(3)
selectline()
#Begining draw
drawfooting(100,200,200,50)
drawfooting(500,200,200,50)



