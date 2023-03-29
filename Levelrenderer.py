import pygame
from mapengine import *
from mapclass import *
SWIDTH = 960
SHEIGHT = 720
texturegroups = []
background:'pygame.surface' = None
class imgobj:
	def __init__(self,imgpath: 'str' = None,  flip:bool = False, xpos: int = 0, ypos: int = 0):
		if flip:
			self.img:'pygame.surface' = pygame.transform.flip(pygame.image.load(imgpath), True, False)
		else:
			self.img:'pygame.surface' = pygame.image.load(imgpath)
		self.xpos = xpos
		self.ypos = ypos

class texturegroup:
	def __init__(self, texturegroupname:str):
		path = "Textures/"+ texturegroupname
		self.lside = [imgobj(path +"/L1L.png", False, 0, 0), imgobj(path +"/L2L.png", False, 118, 101), imgobj(path +"/L3L.png", False, 224, 192), imgobj(path +"/L4L.png", False, 280, 242)]
		self.rside = [imgobj(path +"/L1L.png", True, 842, 0),imgobj(path +"/L2L.png", True, 736, 101),imgobj(path +"/L3L.png", True, 679, 192), imgobj(path +"/L4L.png", True, 640, 242)]
		self.m1side = [imgobj(path +"/L4M2.png", False, 0, 276),imgobj(path +"/L3M1.png", False, 0, 242),imgobj(path +"/L2M1.png", False, 0, 193),imgobj(path +"/L1M1.png", False, 0, 101)]
		self.m2side = [imgobj(path +"/L1M2.png", False, 118, 101), imgobj(path +"/L2M2.png", False, 224, 193),imgobj(path +"/L3M2.png", False, 281, 242),imgobj(path +"/L4M2.png", False, 320, 276)]
		self.m3side = [imgobj(path +"/L4M2.png", False, 640, 276),imgobj(path +"/L3M3.png", False, 679, 242),imgobj(path +"/L2M3.png", False, 736, 193),imgobj(path +"/L1M3.png", False, 842, 101)]

def initialize(lvlmap:'level'):
	global background
	path = "Textures/default/background.png"
	background = imgobj(path,False, 0,0)
	for i in lvlmap.texturenames:
		texturegroups.append(texturegroup(i))

def render(lvlmap: 'level.map', pxpos: int, pypos: int, direction: int):
	mplyt = lvlmap.layout
	torender = []
	torender.append(background)
	match direction:
		case 0:
			#Column 1
			if pxpos >= 1:
				counter = 0
				for i in range(pypos - 3, pypos + 1):
					if i >= 0 and i < lvlmap.ysize:
						if not mplyt[i][pxpos - 1].sides[0].transparent:
							x = mplyt[i][pxpos - 1].sides[0].texturegroup
							torender.append(texturegroups[x].m1side[counter])
					counter += 1
			#Column 3
			if pxpos < (lvlmap.xsize - 1):
				counter = 0
				for i in range(pypos - 3, pypos + 1):
					if i >= 0 and i < lvlmap.ysize:
						if not mplyt[i][pxpos + 1].sides[0].transparent:
							x = mplyt[i][pxpos + 1].sides[0].texturegroup
							torender.append(texturegroups[x].m3side[counter])
					counter += 1
			#Column 2 and sides
			counter = 0
			for i in range(pypos, pypos-4, -1):
				if i >= 0 and i < lvlmap.ysize:
					if not mplyt[i][pxpos].sides[3].transparent:
						x = mplyt[i][pxpos].sides[3].texturegroup
						torender.append(texturegroups[x].lside[counter])
					if not mplyt[i][pxpos].sides[1].transparent:
						x = mplyt[i][pxpos].sides[1].texturegroup
						torender.append(texturegroups[x].rside[counter])
					if not mplyt[i][pxpos].sides[0].transparent:
						x = mplyt[i][pxpos].sides[0].texturegroup
						torender.append(texturegroups[x].m2side[counter])
						break
					else:
						counter += 1
						continue
		case 1:
			# Render left column
			counter = 0
			if pypos >= 1:
				for i in range(pxpos + 3, pxpos - 1, -1):
					if i >= 0 and i < lvlmap.xsize:
						if not mplyt[pypos - 1][i].sides[1].transparent:
							x = mplyt[pypos - 1][i].sides[1].texturegroup
							torender.append(texturegroups[x].m1side[counter])
					counter += 1

			# Render right column
			counter = 0
			if pypos < (lvlmap.ysize - 1):
				for i in range(pxpos + 3, pxpos - 1, -1):
					if i >= 0 and i < lvlmap.xsize:
						if not mplyt[pypos + 1][i].sides[1].transparent:
							x = mplyt[pypos + 1][i].sides[1].texturegroup
							torender.append(texturegroups[x].m3side[counter])
					counter += 1
			# Render column 0
			counter = 0
			for i in range(pxpos, pxpos + 4):
				if i >= 0 and i < lvlmap.xsize:
					if not mplyt[pypos][i].sides[0].transparent:
						x = mplyt[pypos][i].sides[0].texturegroup
						torender.append(texturegroups[x].lside[counter])
					if not mplyt[pypos][i].sides[2].transparent:
						x = mplyt[pypos][i].sides[2].texturegroup
						torender.append(texturegroups[x].rside[counter])
					if not mplyt[pypos][i].sides[1].transparent:
						x = mplyt[pypos][i].sides[1].texturegroup
						torender.append(texturegroups[x].m2side[counter])
						break
					else:
						counter += 1
						continue
		case 2:
			#Column 1
			if pxpos < (lvlmap.xsize - 1):
				counter = 0
				for i in range(pypos + 3, pypos - 1, -1):
					if i >= 0 and i < lvlmap.ysize:
						if not mplyt[i][pxpos + 1].sides[2].transparent:
							x =mplyt[i][pxpos + 1].sides[2].texturegroup
							torender.append(texturegroups[x].m1side[counter])
					counter += 1
			#Column 3
			if pxpos >= 1:
				counter = 0
				for i in range(pypos + 3, pypos - 1, -1):
					if i >= 0 and i < lvlmap.ysize:
						if not mplyt[i][pxpos - 1].sides[2].transparent:
							x =  mplyt[i][pxpos - 1].sides[2].texturegroup
							torender.append(texturegroups[x].m3side[counter])
					counter += 1
			#Column 2 and sides
			counter = 0
			for i in range(pypos, pypos + 4):
				if i >= 0 and i < lvlmap.ysize:
					if not mplyt[i][pxpos].sides[1].transparent:
						x = mplyt[i][pxpos].sides[1].texturegroup
						torender.append(texturegroups[x].lside[counter])
					if not mplyt[i][pxpos].sides[3].transparent:
						x = mplyt[i][pxpos].sides[3].texturegroup
						torender.append(texturegroups[x].rside[counter])
					if not mplyt[i][pxpos].sides[2].transparent:
						x = mplyt[i][pxpos].sides[2].texturegroup
						torender.append(texturegroups[x].m2side[counter])
						break
					else:
						counter += 1
						continue
		case 3:
			# Render left column
			counter = 0
			if pypos < (lvlmap.ysize - 1):
				for i in range(pxpos - 3, pxpos + 1):
					if i >= 0 and i < lvlmap.xsize:
						if not mplyt[pypos + 1][i].sides[3].transparent:
							x = mplyt[pypos + 1][i].sides[3].texturegroup
							torender.append(texturegroups[x].m1side[counter])
					counter += 1

			# Render column 1
			counter = 0
			if pypos >= 1:
				for i in range(pxpos - 3, pxpos + 1):
					if i >= 0 and i < lvlmap.xsize:
						if not mplyt[pypos - 1][i].sides[3].transparent:
							x = mplyt[pypos - 1][i].sides[3].texturegroup
							torender.append(texturegroups[x].m3side[counter])
					counter += 1
			# Render column 0
			counter = 0
			for i in range(pxpos, pxpos - 4, -1):
				if i >= 0 and i < lvlmap.xsize:
					if not mplyt[pypos][i].sides[2].transparent:
						x = mplyt[pypos][i].sides[2].texturegroup
						torender.append(texturegroups[x].lside[counter])
					if not mplyt[pypos][i].sides[0].transparent:
						x = mplyt[pypos][i].sides[0].texturegroup
						torender.append(texturegroups[x].rside[counter])
					if not mplyt[pypos][i].sides[3].transparent:
						x = mplyt[pypos][i].sides[3].texturegroup
						torender.append(texturegroups[x].m2side[counter])
						break
					else:
						counter += 1
						continue
	return torender