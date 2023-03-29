import armordata as armor
import consumabledata as items
import enemydata as enemy
import eventdata as event
import skilldata as skill
import weapondata as weapon
import os
import pickle
def save(level: dict, name:str):
	x = "data/" + name + '.pkl'
	if not os.path.isfile(x):
		open(x, "x")
		print(x + " level file does not exist, creating a new file")
	with open(x, 'wb') as outp:
		pickle.dump(level, outp, pickle.HIGHEST_PROTOCOL)
	print(x + " level file has been saved")
