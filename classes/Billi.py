from classes import *

class  Billi(pygame.sprite.Sprite):
	
	def __init__(self,(width,height)=(20,30)):
	        pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.image.load(path_to_resource('cat.png'))
		self.size=(width,height)
	        #self.image.set_colorkey((0,0,0)) # black transparent
		self.scale(width,height)			        	        
		self.image = self.image.convert_alpha()
	        self.rect = self.image.get_rect()
	        self.radius = 50 # for collide check
		
	def scale(self,width=20, height=30):
		self.image=pygame.transform.scale(self.image,(width,height))
	
	def update(self):
		self.rect = self.image.get_rect()
		self.rect.center=pygame.mouse.get_pos()
