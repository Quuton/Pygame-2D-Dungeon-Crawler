from characterclass import *
import enemydata
partylist = []
enemylist = []
def initialize(party:list['partycharacter'], enemyids:list['str']):
    global partylist
    global enemylist
    partylist =  party[:4]
    for i in enemyids:
        enemy = enemydata.enemies[i]
        enemylist = enemycharacter(enemy["hp"],enemy["hp"],enemy["strength"],enemy["vitality"],enemy["intelligence"],enemy["agility"],enemy["luck"],enemy["physrs"], enemy["firers"],enemy["elecrs"],enemy["skills"],enemy["aicode"])
