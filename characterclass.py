class character():
	#1 Burn
	#2 Poison
	#3 Shock
	#4 Fatigue
	#5 Sleep
	guarding = False
	statuses = [0,0,0,0,0]
	crit = 0
	evade = 0
	accuracy = 0
	def __init__(self, hp, maxhp, strength, vitality, intelligence, agility, luck, physrs, firers, elecrs, skills:list) -> None:
			self.hp = hp
			self.maxhp = maxhp
			self.strength = strength
			self.vitality = vitality
			self.intelligence = intelligence
			self.agility = agility
			self.luck = luck
			self.physrs = physrs
			self.firers = firers
			self.elecrs = elecrs
			if skills[0] != "0000":
				self.skills = ["0000"] + skills
			else:
				self.skills = skills

	def change_hp(self, hp:int):
		self.hp += hp

	def guard(self):
		self.guard = True

	def removeguard(self):
		self.guard = False

	def set_status(self,statnum:int, turns:int = 1) -> bool:
		if self.statuses[statnum] == 0:
			self.statuses[statnum] = turns
			return True
		else:
			#return False to tell the engine your skill did jack shit
			return False

	def countdown_status(self):
		for i in self.statuses:
			if i > 0:
				i -= 1
class enemycharacter(character):
	def __init__(self, hp, maxhp, strength, vitality, intelligence, agility, luck, physrs, firers, elecrs, skills: list, aicode) -> None:
		super().__init__(hp, maxhp, strength, vitality, intelligence, agility, luck, physrs, firers, elecrs, skills)
		self.aicode = aicode
class partycharacter(character):
	down = False
	def __init__(self, hp, maxhp, mp, maxmp, strength, vitality, intelligence, agility, luck, physrs, firers, elecrs, skills: list, crit, accuracy, evade) -> None:
		super().__init__(hp, maxhp, strength, vitality, intelligence, agility, luck, physrs, firers, elecrs, skills)
		self.mp = mp
		self.maxmp = maxmp
		self.crit = crit
		self.evade = evade
		self.accuracy = accuracy

	def change_mp(self,mp:int):
		self.mp += mp
	
	def set_down(self):
		self.down = not self.down