#Pratik Anand

import pygame, sys
from pygame.locals import *
from random import *

from classes.Billi import *
from classes.Message import *
from classes.Food import *
from classes.Bomb import *

pygame.init()
fpsClock=pygame.time.Clock()

windowSurfaceObj=pygame.display.set_mode((640,480))
pygame.display.set_caption('First test program')

catSurfaceObj=Billi.Billi((80,80))
msgObj=Message.Message("Duniya ko billi ka namaskar")

mouseX,mouseY=0,0

#sound
path=path_to_resource('bounce.mp3')
soundObj=pygame.mixer.Sound(path)

#key repeat ON
pygame.key.set_repeat(5,50)


ladooz = []
bombs = []

for x in range(100,200,10):
	for y in range(100,200,10):
		food=Food.Food('ladoo.png',(randint(0,600), randint(0,440)), (15,15))	
		ladooz.append(food)			

ladoozgroup = pygame.sprite.Group(ladooz)
khayaLadooz=[]
for x in range(0,9):
	bomb = Bomb('bomb.png', (randint(0,600), randint(0,440)), (30,30))
	#khayaLadooz.append(pygame.sprite.spritecollide(bomb, ladoozgroup, False))
	bombs.append(bomb)


bombsgroup = pygame.sprite.Group(bombs)	

while True:
	windowSurfaceObj.fill(white)

	#pygame.draw.polygon(windowSurfaceObj,green,((146,0),(291,106),(236,277),(56,277),(0,106)))
	#pygame.draw.circle(windowSurfaceObj,blue,(300,50),20,0)
	#pygame.draw.rect(windowSurfaceObj,red,(10,10,50,100))
	#pygame.draw.line(windowSurfaceObj,blue,(60,160),(120,60),4)

	#pixArr=pygame.PixelArray(windowSurfaceObj)
	
	for mithai in ladooz:
		windowSurfaceObj.blit(mithai.image,(mithai.x,mithai.y))		

	for bomb in bombs:
		windowSurfaceObj.blit(bomb.image,(bomb.x,bomb.y))
	
	windowSurfaceObj.blit(catSurfaceObj.image,(mouseX,mouseY))

	windowSurfaceObj.blit(msgObj.image,(10,20))

	
	#list comprehension
	ladooz=[mithai for mithai in ladooz if mithai not in khayaLadooz]
	for mithai in ladooz:
		windowSurfaceObj.blit(mithai.image,(mithai.x,mithai.y))
	
	khayaLadooz=pygame.sprite.spritecollide(catSurfaceObj, ladoozgroup, True)

	collisionList=pygame.sprite.spritecollide(catSurfaceObj, bombsgroup, False)	
	if collisionList:
		collidedBomb=collisionList[0]	
		for index,bomb in enumerate(bombs):
			if collidedBomb is bomb:
				bombs[index]=Bomb('boom.png',(collidedBomb.x,collidedBomb.y),(60,60))
		del collidedBomb
		del collisionList

	
	if pygame.sprite.spritecollide(catSurfaceObj, bombsgroup, False):
		msgBombTouch = Message.Message("I will kill you X-(")
		windowSurfaceObj.blit(msgBombTouch.image,(10,80))	
	#print len(ladooz)	
	
	if not ladooz:
		msgObj.msg="Happy and moti billi"
		successMsg = Message.Message("You will live to feed me")
		successMsg2 = Message.Message("ANOTHER DAY")	
		windowSurfaceObj.blit(successMsg.image,(10,50))	
		windowSurfaceObj.blit(successMsg2.image,(10,80))
	
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		elif event.type==MOUSEMOTION:
			mouseX,mouseY=event.pos
		elif event.type==MOUSEBUTTONUP:
			mouseX,mouseY=event.pos
			soundObj.play()
			if event.button in (1,2,3):
				print 'mouse click'
			elif event.button in (4,5):
				print 'mouse scrolled'
		elif event.type==KEYDOWN:
		#	if event.key in (K_LEFT,K_RIGHT,K_UP,K_DOWN):
		#		print 'Arrow keys pressed'
		#		if event.key==K_LEFT: #left
		#			mouseX-=10*0.5
		#		elif event.key==K_RIGHT: #right
		#			mouseX+=10*0.5
		#		elif event.key==K_UP: #up
		#			mouseY-=10*0.5
		#		else:
		#			 mouseY+=10*0.5
		#
		#	if event.key==K_a:
		#		print '"A" key pressed'
			if event.key==K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))   #Posting a QUIT event
	msgObj.update()
	catSurfaceObj.update()
	pygame.display.update()
	fpsClock.tick(30)

	


