#!/usr/bin/env python3

from random import randint



class Character:
	def __init__(self):
		return

	def scale(self, multiplier):
		self.multiplier = multiplier
		self.name = "boss"
		self.type = "Boss"
		self.health = self.health * self.multiplier
		self.health_max = self.health_max * self.multiplier
		self.mana = self.mana * self.multiplier
		self.mana_max = self.mana_max * self.multiplier
		self.defence = self.defence # Percentage from 1 to 100
		for x in range(self.multiplier):
			if x == 0:
				self.defence = self.defence
			else:
				self.defence = self.defence + (1 - self.defence) * (1 / 2)
		self.attack = self.attack * self.multiplier
		self.healpower = self.healpower * self.multiplier
		return()

	def do_damage(self, target):
		damage = self.attack * (1 - target.defence)
		target.health = target.health - damage
		return()

	def heal(self, heal_target):
		heal_target.health = min(heal_target.health + self.healpower, heal_target.health_max)
		return()
	

class Boss(Character):
	def __init__(self):
		Character.__init__(self)
		self.name = "valakas"
		self.type = "Boss"
		self.health = 400 
		self.health_max = 1000 
		self.defence = 0.60 # Percentage from 1 to 100
		self.mana = 0
		self.mana_max = 0
		self.attack = 55 
		self.healpower = 0

class Tank(Character):
	def __init__(self):
		Character.__init__(self)
		self.name = "dark avenger"
		self.type = "Tank"
		self.health = 200 
		self.health_max = 200
		self.mana = 0
		self.mana_max = 0
		self.defence = 0.5 #Percentage from 1 to 100
		self.attack = 10 
		self.healpower = 0


class Healer(Character):
	def __init__(self):
		self.name = "cardinal"
		self.type = "Healer"
		self.health = 70 
		self.health_max = 70
		self.defence = 0
		self.attack = 0
		self.mana = 90
		self.mana_max = 90
		self.healpower = 20	
		self.healmanacost = 7
		self.manaregen = 3

class Archer(Character):
	def __init__(self):
		self.name = "arbalester"
		self.type = "Archer"
		self.health = 90 
		self.health_max = 90
		self.mana = 0
		self.mana_max = 0
		self.defence = 0.15 #Percentage from 1 to 100
		self.attack = 30 
		self.healpower = 0

if __name__ == "__main__":
	boss = Boss()
	tank = Tank()
	healer = Healer()
	archer = Archer()
	
	max_characters = 5
	print("The game is about going for a raid to kill the Boss")
	print("Your group consists of maximum {}".format(max_characters))
	print("You can choose your character from below list \ntank \nhealer \narcher")
	
	n_o_tank = 1
	n_o_archer = 1
	n_o_healer = 1

	print("How many tanks would you like?")
	n_o_tank = int(input())
	print("How many archers would you like?")
	n_o_archer = int(input())
	print("How many healers would you like?")
	n_o_healer = int(input())
	healer.scale(n_o_healer)
	archer.scale(n_o_archer)
	tank.scale(n_o_tank)
	
	rounds = 15
	print("How many rounds would you like to go, the default is {}".format(rounds))
	rounds = int(input())

	print("Tank`s initial health {}".format(tank.health))
	print("Boss`s initial health {}".format(boss.health))
	for round in range(rounds):
		if round >= 1:
			for retry in range(3):
				print("Would you like to another round? Yes or No")
				y_n = input()
				if y_n == "Yes":
					break
				elif y_n == "No":
					print("You finished after round {}".format(rounds + 1))
					exit(1)
				else:
					print("You have to choose capital Yes or No")
			else:
				print("You failed 3 times you Suck!")
				exit(1)

			if tank.health >= 0:
				boss.do_damage(tank)
				tank.do_damage(boss)
				archer.do_damage(boss)
				if boss.health <= 0:
					boss.health = max(boss.health , 0)
					print("{} is dead in {} rounds".format(boss.type,round))
					break
				print("Boss`s current health {} round {}".format(boss.health,round))
				if healer.mana >= healer.healmanacost:
					print("Tank`s current health before heal {}".format(tank.health))
					healer.heal(tank)
					print("Tank`s current health after heal {}".format(tank.health))
					healer.mana = healer.mana - healer.healmanacost
					print("health current mana {}".format(healer.mana))

				else:
					print("healer has not nough mana {}".format(healer.mana))				
				
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
	else:
		print("you failed the Raid, could not finish in {} rounds, try harder".format(rounds))
		break				
		# boss.do_damage(tank)
	# print("Tank`s current health {}".format(tank.health))
	# print("Boss`s current health {}".format(boss.health))
	# print("Healer`s current mana {}".format(healer.mana))
	# print("Archer`s current health {}".format(archer.health))
	
