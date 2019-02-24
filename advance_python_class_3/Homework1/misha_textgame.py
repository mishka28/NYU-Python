#!/usr/bin/env python3

from random import randint

class Character:
	def __init__(self):
		# self.name = ""
		# self.type = ""
		# self.health = 1 
		# self.health_max = 1
		# self.mana = 1
		# self.mana_man = 1
		# self.defence = 0.5 #Percentage from 1 to 100
		# self.attack = 1 
		# self.healpower = 1
		return
	def do_damage(self, target):
		damage = self.attack * (1 - target.defence)
		target.health = target.health - damage
		return()
	def heal(self, heal_target):
		heal_target.health = min(heal_target.health + self.healpower, heal_target.health_max)
		return()
class Boss(Character):
	def __init__(self):
		# Character.__init__(self)
		self.name = "boss"
		self.type = "Boss"
		self.health = 500 
		self.health_max = 500
		self.mana = 1
		self.mana_man = 1
		self.defence = 0.60 # Percentage from 1 to 100
		self.attack = 55 
		self.healpower = 0
		# self.target = Tank(self) ### what happens is tank dies

class Tank(Character):
	def __init__(self):
		# Character.__init__(self)
		self.name = "tank"
		self.type = "Tank"
		self.health = 200 
		self.health_max = 200
		self.mana = 1
		self.mana_man = 1
		self.defence = 0.5 #Percentage from 1 to 100
		self.attack = 10 
		self.healpower = 0		
		 # Boss(self)
	# def attack(self, target):
	# 	self.target = target
	# 	self.do_damage(self.target)	
class Healer(Character):
	def __init__(self):
		Character.__init__(self)
		self.name = "healer"
		self.type = "Healer"
		self.health = 70 
		self.health_max = 70
		self.mana = 90
		self.mana_man = 90
		self.defence = 0.1 #Percentage from 1 to 100
		self.attack = 5 
		self.healpower = 20	
		self.healmanacost = 7
		self.manaregen = 3

class Archer(Character):
	def __init__(self):
		Character.__init__(self)
		self.name = "archer"
		self.type = "Archer"
		self.health = 90 
		self.health_max = 90
		self.mana = 30
		self.mana_man = 10
		self.defence = 0.15 #Percentage from 1 to 100
		self.attack = 30 
		self.healpower = 0	
if __name__ == "__main__":
	boss = Boss()
	tank = Tank()
	healer = Healer()
	archer = Archer()

	# tank.target = boss
	
	rounds = 30
	# print(tank.attack(boss).target.name)
	# print(tank.target.health)
	print("Tank`s current health {}".format(tank.health))
	print("Boss`s current health {}".format(boss.health))
	for round in range(rounds):
		if tank.health >= 0:
			boss.do_damage(tank)
			tank.do_damage(boss)
			archer.do_damage(boss)
			if boss.health <= 0:
				boss.health = max(boss.health , 0)
				print("{} is dead in {} rounds".format(boss.name,round))
				break
			print("Boss`s current health {} round {}".format(boss.health,round))
			if healer.mana >= healer.healmanacost:
				healer.heal(tank)
				print("Tank`s current health after heal {}".format(tank.health))
				healer.mana = healer.mana - healer.healmanacost
			else:
				print("healer has no nough mana {}".format(healer.mana))				
			
		else:
			print("Tank is dead, boss is killing the archer")
			if archer.health >= 0:
				boss.do_damage(archer)
				archer.do_damage(boss)
				if boss.health <= 0:
					boss.health = max(boss.health , 0)
					print("{} is dead in {} rounds".format(boss.name,round))
					break
				if healer.mana >= healer.healmanacost:
					healer.heal(archer)
					healer.mana = healer.mana - healer.healmanacost
					# tank.do_damage(boss)
				else:
					print("healer has no nough mana {}".format(healer.mana))							
			else:
				print("you failed the Raid")
				break
		healer.mana = healer.mana + healer.manaregen
					
		# boss.do_damage(tank)
	print("Tank`s current health {}".format(tank.health))
	print("Boss`s current health {}".format(boss.health))
	print("Healer`s current mana {}".format(healer.mana))
	print("Archer`s current health {}".format(archer.health))
	
