import pygame, sys,os
from pygame.locals import *


#Colors
red=pygame.Color(255,0,0)
green=pygame.Color(0,255,0)
blue=pygame.Color(0,0,255)
white=pygame.Color(255,255,255)

def path_to_resource(image):
	cwd=os.getcwd()
	upFolder=os.path.dirname(cwd)
	path=os.path.join(cwd+'/resources',image)
	return path	
