from mapclass import *
import keyboard
import pickle
import os
import time

# Quick presets


class preset:
	@staticmethod
	def wall(type: str = "wall"):
		match type:
			case "wall":
				return level.map.cell.wall(0, False, False)
			case "door":
				return level.map.cell.wall(1, True, False)
			case "none":
				return level.map.cell.wall(0, True, True)

	@staticmethod
	def floor():
		return level.map.cell.floor()

	@staticmethod
	def cell(type: str = "none"):
		match type:
			case "all":
				return level.map.cell([preset.wall("wall"), preset.wall("wall"),
									   preset.wall("wall"), preset.wall("wall")], level.map.cell.floor())
			case "none":
				return level.map.cell([preset.wall("none"), preset.wall("none"),
									   preset.wall("none"), preset.wall("none")], level.map.cell.floor())
			case "north":
				return level.map.cell([preset.wall("wall"), preset.wall("none"),
									   preset.wall("none"), preset.wall("none")], level.map.cell.floor())
			case "northeast":
				return level.map.cell([preset.wall("wall"), preset.wall("wall"),
									   preset.wall("none"), preset.wall("none")], level.map.cell.floor())
			case "east":
				return level.map.cell([preset.wall("none"), preset.wall("wall"),
									   preset.wall("none"), preset.wall("none")], level.map.cell.floor())
			case "southeast":
				return level.map.cell([preset.wall("none"), preset.wall("wall"),
									   preset.wall("wall"), preset.wall("none")], level.map.cell.floor())
			case "south":
				return level.map.cell([preset.wall("none"), preset.wall("none"),
									   preset.wall("wall"), preset.wall("none")], level.map.cell.floor())
			case "southwest":
				return level.map.cell([preset.wall("none"), preset.wall("none"),
									   preset.wall("wall"), preset.wall("wall")], level.map.cell.floor())
			case "west":
				return level.map.cell([preset.wall("none"), preset.wall("none"),
									   preset.wall("none"), preset.wall("wall")], level.map.cell.floor())
			case "northwest":
				return level.map.cell([preset.wall("wall"), preset.wall("none"),
									   preset.wall("none"), preset.wall("wall")], level.map.cell.floor())

def save(level: 'level'):
	x = "levels/" + level.name + '.pkl'
	if not os.path.isfile(x):
		open(x, "x")
		print(x + " level file does not exist, creating a new file")
	with open(x, 'wb') as outp:
		pickle.dump(level, outp, pickle.HIGHEST_PROTOCOL)
	print(x + " level file has been saved")


def load(levelname: str) -> 'level':
	x = "levels/" + levelname + '.pkl'
	if os.path.isfile(x):
		with open(x, 'rb') as inp:
			print("File found, loading")
			return pickle.load(inp)
	else:
		print("File does not exist bruh")
		return None

def create_level(maps: list['level.map'], name: str, defaultxpos: int = 0, defaultypos: int = 0, defaultfloor = 0, defaultdirection = 0, texturenames:list[str] = None):
	return level(maps, name, defaultxpos, defaultypos, defaultfloor, defaultdirection, texturenames)


def create_new_map(xsize: int = 3, ysize: int = 3):
	newmap = []
	for y in range(ysize):
		newmap.append([])
		for x in range(xsize):
			if (y == 0 and x == 0):
				newmap[y].append(preset.cell("northwest"))
			elif (y == 0) and (x == (xsize - 1)):
				newmap[y].append(preset.cell("northeast"))
			elif (y == (ysize - 1)) and (x == 0):
				newmap[y].append(preset.cell("southwest"))
			elif (y == (ysize - 1)) and (x == (xsize-1)):
				newmap[y].append(preset.cell("southeast"))
			elif (y == 0):
				newmap[y].append(preset.cell("north"))
			elif (x == 0):
				newmap[y].append(preset.cell("west"))
			elif (x == (xsize - 1)):
				newmap[y].append(preset.cell("east"))
			elif (y == (ysize - 1)):
				newmap[y].append(preset.cell("south"))
			else:
				newmap[y].append(preset.cell("none"))

	return level.map(xsize, ysize, newmap)


def display_level(level: 'level', pxpos: int = 0, pypos: int = 0):
	for i, floor in enumerate(level.floors):
		print("Map layout L" + str(i))
		print("level textures are:" + str(level.texturenames))
		display_layout(floor, pxpos, pypos)


def display_layout(mplayout: 'level.map', pxpos, pypos):
	a1 = "+     +"
	a2 = "+-----+"
	a3 = "+-_-_-"
	a4 = "+-   -+"
	b1 = "   "
	b2 = "  |"
	b3 = "  :"
	for idx1 in range(mplayout.ysize):
		top = ""
		mid = ""
		bottom = ""
		for idx2, cell in enumerate(mplayout.layout[idx1]):
			if cell.sides[0].transparent:
				if cell.sides[0].passthru:
					top += a1
				else:
					top += a3
			else:
				if cell.sides[0].passthru:
					top += a4
				else:
					top += a2
		print(top)
		for idx2, cell in enumerate(mplayout.layout[idx1]):
			x = " "
			if idx1 == pypos and idx2 == pxpos:
				x = "*"
			if cell.sides[3].transparent:
				mid += " "
			else:
				if cell.sides[3].passthru:
					mid += ":"
				else:
					mid += "|"
			if cell.sides[1].transparent:
				mid += "  " + x + b1
			else:
				if cell.sides[1].passthru:
					mid += "  " + x + b3
				else:
					mid += "  " + x + b2
		print(mid)
		for idx2, cell in enumerate(mplayout.layout[idx1]):
			if cell.sides[2].transparent:
				if cell.sides[2].passthru:
					bottom += a1
				else:
					bottom += a3
			else:
				if cell.sides[2].passthru:
					bottom += a4
				else:
					bottom += a2
		print(bottom)

def configure_level():
	#Level name
	print("Give this level a name")
	name = input()
	#Number of floors
	print("How many floors do you want for this level?")
	floors = int(input())
	#Configuring mastrix dimension
	temp_floors = []
	for i in range(floors):
		print("Now setting up level " + str(i))
		print("Determine the width")
		a = int(input())
		if a < 3:
			a = 3
		print("Determine the height")
		b = int(input())
		if b < 3:
			b = 3
		temp_floors.append(create_new_map(a, b))
		os.system('cls')
	usedtextures = []
	while True:
		print("give texturegroup names")
		x = str(input())
		usedtextures.append(x)
		print("continue?")
		z = input()
		if z == 'N' or z == 'n':
			break
		else:
			continue
	lvl = create_level(temp_floors, name, 0, 0, 0, 0, usedtextures)
	save(lvl)
	display_level(lvl)

def edit_level(level):
	pointerxpos = 0
	pointerypos = 0
	current_floor = 0
	wallmode = "wall"

	print("current level is " + level.name +
		  ", you are viewing floor " + str(current_floor))
	display_layout(level.floors[current_floor], pointerxpos, pointerypos)
	while True:
		try:
			def refresh():
				os.system('cls')
				print("current level is " + level.name +
					  ", you are viewing floor " + str(current_floor))
				display_layout(
					level.floors[current_floor], pointerxpos, pointerypos)

			if keyboard.is_pressed('left'):
				if pointerxpos > 0:
					pointerxpos -= 1
					refresh()
			if keyboard.is_pressed('right'):
				if pointerxpos < (level.floors[current_floor].xsize - 1):
					pointerxpos += 1
					refresh()
			if keyboard.is_pressed('up'):
				if pointerypos > 0:
					pointerypos -= 1
					refresh()
			if keyboard.is_pressed('down'):
				if pointerypos < (level.floors[current_floor].ysize - 1):
					pointerypos += 1
					refresh()

			if keyboard.is_pressed('z'):
				wallmode = "door"
				refresh()
				print("Door mode enabled")

			if keyboard.is_pressed('x'):
				wallmode = "none"
				refresh()
				print("Destroy mode enabled")

			if keyboard.is_pressed('c'):
				wallmode = "wall"
				refresh()
				print("Normal mode enabled")

			if keyboard.is_pressed('w'):
				level.floors[current_floor].layout[pointerypos][pointerxpos].sides[0] = preset.wall(
					wallmode)
				refresh()
				if pointerypos > 0:
					level.floors[current_floor].layout[pointerypos -
													   1][pointerxpos].sides[2] = preset.wall(wallmode)
					refresh()
				refresh()
			if keyboard.is_pressed('a'):
				level.floors[current_floor].layout[pointerypos][pointerxpos].sides[3] = preset.wall(
					wallmode)
				if pointerxpos > 0:
					level.floors[current_floor].layout[pointerypos][pointerxpos -
																	1].sides[1] = preset.wall(wallmode)
				refresh()
			if keyboard.is_pressed('s'):
				level.floors[current_floor].layout[pointerypos][pointerxpos].sides[2] = preset.wall(
					wallmode)
				if pointerypos < (level.floors[current_floor].ysize - 1):
					level.floors[current_floor].layout[pointerypos +
													   1][pointerxpos].sides[0] = preset.wall(wallmode)
				refresh()
			if keyboard.is_pressed('d'):
				level.floors[current_floor].layout[pointerypos][pointerxpos].sides[1] = preset.wall(
					wallmode)
				if pointerxpos < (level.floors[current_floor].xsize - 1):
					level.floors[current_floor].layout[pointerypos][pointerxpos +
																	1].sides[3] = preset.wall(wallmode)
				refresh()
			if keyboard.is_pressed('e'):
				print("Accessing cell at (" + str(pointerxpos) +
					  ", " + str(pointerypos) + ")")
				print("This cell has eventid of " + (level.floors[current_floor].layout[pointerypos]
					  [pointerxpos].eventid if level.floors[current_floor].layout[pointerypos]
					  [pointerxpos].eventid != None else "None"))
				print("Please enter a string for the eventid")
				x = str(input())
				c = None
				if x == "":
					x = None
					c = False
				else:
					c = True
				level.floors[current_floor].layout[pointerypos][pointerxpos].eventid = x
				print("Eventid has been saved")
				level.floors[current_floor].layout[pointerypos][pointerxpos].eactive = c
				print("The event status here is " + str(level.floors[current_floor].layout[pointerypos][pointerxpos].eactive))
				print("do you want to toggle it?")
				print("Enter Y to toggle, enter anything else to cancel")
				z = input()
				if z == "Y" or z == "y":
					level.floors[current_floor].layout[pointerypos][pointerxpos].eactive = not level.floors[current_floor].layout[pointerypos][pointerxpos].eactive
					print("Event toggled!")
				refresh()
				print("Cell at (" + str(pointerxpos) + ", " +
					  str(pointerypos) + ") has Eventid of " + (x if x!= None else "None"))

			if keyboard.is_pressed('r'):
				if current_floor < (len(level.floors)-1):
					current_floor += 1
				else:
					current_floor = 0
				pointerxpos = 0
				pointerypos = 0
				refresh()
			if keyboard.is_pressed('t'):
				refresh()
				save(level)
			if keyboard.is_pressed('h'):
				refresh()
				print("Control hints:")
				print("Use arrow keys to move the pointer in the grid")
				print("Use wasd keys to place an object")
				print("Use [Z] to enter door mode to place doors")
				print("Use [X] to enter destory mode to rmeove walls or doors")
				print("Use [C] to enter normal mode to place walls")
				print("Use [E] to edit the cell's event")
				print("Use [R] to cycle the level floor")
				print("Use [T] to save the floor")
		except:
			continue
		time.sleep(0.08)
def menu():
	while(True):
		print("[1] Create new level")
		print("[2] Load and edit level")
		print("[3] Exit the editor")
		y = int(input())
		if y > 3 or y < 1:
			os.system('cls')
			print("Please input a valid choice!")
			continue
		else:
			break
	match y:
		case 1:
			configure_level()
		case 2:
			while (True):
				print("Give the name of the level")
				x = str(input())
				try:
					lvl = load(x)
				except:
					os.system('cls')
					print("level is not found try again")
					continue
				if lvl != None:
					break
			os.system('cls')
			edit_level(lvl)

def main():
    menu()


main()	
	