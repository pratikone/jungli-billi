from classes import *

class  Message(pygame.sprite.Sprite):
	
	def __init__(self,msg,color=blue,font='freesansbold.ttf',size=32):
		pygame.sprite.Sprite.__init__(self)
		self.font=font
		self.size=size
		self.color=color
		self.fontObj=pygame.font.Font(self.font,self.size)
		self.msg=msg
		self.image=self.fontObj.render(msg,False,color)
	        #self.image.set_colorkey((0,0,0)) # black transparent
	        self.rect = self.image.get_rect()
	        self.radius = 50 # for collide check

	def update(self):
		self.fontObj=pygame.font.Font(self.font,self.size)
		self.image=self.fontObj.render(self.msg,False,self.color)
		self.rect = self.image.get_rect()
