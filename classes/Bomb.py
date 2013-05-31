from classes import *

class  Bomb(pygame.sprite.Sprite):
	
	def __init__(self,image,(x,y),(width,height)=(20,30)):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(path_to_resource(image))
		self.size=(width,height)
		self.scale(width,height)			        
		#self.image.set_colorkey((0,0,0)) # black transparent
	        self.image = self.image.convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
	        self.radius = 50 # for collide check
		self.x,self.y=x,y
		
	def scale(self,width=20, height=30):
		self.image=pygame.transform.scale(self.image,(width,height))

	def update(self):
		self.rect = self.image.get_rect()
