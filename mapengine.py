from mapclass import *

class levelmanager:
	def __init__(self, activelevel: 'level', activefloor: int = None, direction: int = 0) -> None:
		self.activelevel = activelevel
		if activefloor == None:
			self.activefloor = activelevel.defaultfloor
		else:
			self.activefloor = activefloor
		if direction == None:
			self.direction = activelevel.defaultdirection
		else:
			self.direction = direction
		self.pxpos = activelevel.defaultxpos
		self.pypos = activelevel.defaultypos

	def move(self, direction: int) -> bool:
		match direction:
			case 0:
				if self.activelevel.floors[self.activefloor].layout[self.pypos][self.pxpos].sides[0].passthru:
					self.pypos -= 1
					return False
				else:
					return True
			case 1:
				if self.activelevel.floors[self.activefloor].layout[self.pypos][self.pxpos].sides[1].passthru:
					self.pxpos += 1
					return False
				else:
					return True
			case 2:
				if self.activelevel.floors[self.activefloor].layout[self.pypos][self.pxpos].sides[2].passthru:
					self.pypos += 1
					return False
				else:
					return True
			case 3:
				if self.activelevel.floors[self.activefloor].layout[self.pypos][self.pxpos].sides[3].passthru:
					self.pxpos -= 1
					return False
				else:
					return True
			
	def get_event(self):
		return self.activelevel.floors[self.activefloor].layout[self.pxpos][self.pypos]

	def change_floor(self, floor:int = 0, xpos:int = 0, ypos:int = 0):
		self.activefloor = 0
		self.pxpos = xpos
		self.pypos = ypos
		
	def change_level(self, newlevel: 'level', activefloor: int = 0, direction: int = 0):
		self.activelevel = newlevel
		self.activefloor = 0
		self.direction = direction

	def get_state(self):
		return self.activelevel
	
	def get_activemap(self):
		return self.activelevel.floors[self.activefloor]

	def turn_right(self):
		if self.direction > 3:
			self.direction = 0
		
	def turn_left(self):
		if self.direction < 0:
			self.direction = 3

	def reverse(self):
		match self.direction:
			case 0:
				self.direction = 2
			case 1:
				self.direction = 3
			case 2:
				self.direction = 0
			case 3:
				self.direction = 1


