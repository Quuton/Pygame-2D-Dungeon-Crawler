import pygame
import pickle
import os
from mapengine import *
from mapclass import *
from Levelrenderer import * 
#Initialize pygame
pygame.init()

SWIDTH = 960
SHEIGHT = 720
running = True
class imgobj:
	def __init__(self,imgpath: 'str' = None,  flip:bool = False, xpos: int = 0, ypos: int = 0):
		if flip:
			self.img:'pygame.surface' = pygame.transform.flip(pygame.image.load(imgpath), True, False)
		else:
			self.img:'pygame.surface' = pygame.image.load(imgpath)
		self.xpos = xpos
		self.ypos = ypos

def load(levelname: str) -> 'level':
    x = "levels/" + levelname + '.pkl'
    if os.path.isfile(x):
        with open(x, 'rb') as inp:
            print("File found, loading")
            return pickle.load(inp)
    else:
        print("File does not exist bruh")
        return None

def drawtexture(screen:'pygame.Surface', imgobject:'imgobj'):
	screen.blit(imgobject.img, (imgobject.xpos, imgobject.ypos))

def create_screen(height:int, width:int):
	return pygame.display.set_mode((SWIDTH, SHEIGHT))

def quit_check():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return False
		else:
			return True

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
dest=(448,650)
font = pygame.font.Font(None, 64) 
North= font.render('N', True, green)
East= font.render('E', True, green)
South= font.render('S', True, green)
West= font.render('W', True, green)

#Load level
currentlevel = load("level1")
mplevel = levelmanager(load("level1"), 0, 0)
initialize(currentlevel)
screen1 = create_screen(SWIDTH, SHEIGHT)
while running:
	# running = quit_check()
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				mplevel.direction -= 1
				if mplevel.direction < 0:
					mplevel.direction = 3
			if event.key == pygame.K_RIGHT:
				mplevel.direction += 1
				if mplevel.direction > 3:
					mplevel.direction = 0
			if event.key == pygame.K_DOWN:
				match mplevel.direction:
					case 0:
						mplevel.direction = 2
					case 1:
						mplevel.direction = 3
					case 2:
						mplevel.direction = 0
					case 3:
						mplevel.direction = 1
			if event.key == pygame.K_UP:
				mplevel.move(mplevel.direction)
	imgtorender = render(mplevel.activelevel.floors[mplevel.activefloor], mplevel.pxpos, mplevel.pypos, mplevel.direction)
	for i in imgtorender:
		screen1.blit(i.img, (i.xpos, i.ypos))
	match mplevel.direction:
		case 0:
			screen1.blit(North,dest)
		case 1:
			screen1.blit(East,dest)
		case 2:
			screen1.blit(South,dest)
		case 3:
			screen1.blit(West,dest)
	pygame.display.update()
