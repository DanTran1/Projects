#  File: RPG.py
#  Description: RPG Game
#  Student's Name: Tam Dan Tran
#  Student's UT EID: tvt287
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: 09/18/17
#  Date Last Modified: 09/22/17



class RPGCharacter:

	# initialize object
	def __init__(self):

		self.armor = Armor("none")
		self.weapon_wield = Weapon("none")
		self.armor_class = self.armor.armor_protection()
	# returns a string of character's attributes
	def __str__(self):

		string = "\n" + str(self.name) + "\n\t" \
			"Current Health: " + str(self.health) + "\n\t" \
			"Current Spell Points: " + str(self.spell_points) + "\n\t" \
			"Weilding: " + str(self.weapon_wield) + "\n\t" \
			"Wearing: " + str(self.armor) + "\n\t" \
			"Armor class: " + str(self.armor_class) + "\n"

		return string
	# wield weapons and check if option is allowed
	def wield(self,weapon):

		# if character is a wizard, not allowed to use axe or sword
		if isinstance(self, Wizard):

			axe = False
			sword = False
		# else character is fighter, allowed to use all weapons
		else:

			pass

		# if weapon is allowed, wield weapon
		if weapon != False:

			print (self.name, "is now wielding a(n)", weapon)
			self.weapon_wield = weapon

		# if weapons is not allow, print statement
		else:

			print ("Weapon is not allowed for this character class.")

	# unwield weapons
	def unwield(self,weapon):

		self.weapon_wield = Weapon("none")
	
	# put on armor, checks if armor is allowed for character class
	def put_on_armor(self,armor):

		if isinstance(self, Wizard):

			print("Armor is not allowed for this character class.")

		else:

			self.armor_class = armor.armor_protection()
			self.armor = armor
			print(self.name, "is now wearing", armor)

	# take off armor and prints message
	def take_off_armor(self,armor):

		self.armor = Armor("none")
		self.armor_class = armor.armor_protection()
		print(self.name,"is no longer wearing anything.")

	# records attacks, damage, and new health of characters
	def fight(self,character):

		print(self.name,"attacks",character.name,"with a(n)",self.weapon_wield)

		character.health -= self.weapon_wield.weapon_damage()
		print(self.name,"does",self.weapon_wield.weapon_damage(),"damage to",character.name)

		print(character.name,"is now down to",character.health,"health")

		self.check_for_defeat(character)

	# checks if character's health is less than 0
	def check_for_defeat(self, character):

		if character.health <= 0:

			print(character.name,"has been defeated!")
# creates a subclass of RPGCharacter name Fighter
class Fighter(RPGCharacter):

	def __init__(self, name):

		super().__init__()
		self.health = 40
		self.spell_points = 0
		self.name = name

class Wizard(RPGCharacter):

	def __init__(self, name):

		super().__init__()
		self.health = 16
		self.spell_points = 20
		self.name = name 

	# method allowing Wizards to cast spells
	def cast_spell(self,spell_name,character):

		# spells dictionary
		# key is spell name, values are cost and effect (in that order)
		spells = {"Fireball":[3,5],"Lightning Bolt":[10,10],"Heal":[6,-6]}

		# puts spell cost into a variable
		spell_cost = spells[spell_name][0]
		# puts spell effect into a variable
		spell_effect = spells[spell_name][1]

		print(self.name,"casts",spell_name,"at",character.name)

		# checks if spell is available
		if spell_name not in spells:

			print("Unknown spell name. Spell failed.")
			return

		# checks if character has sufficient spell points
		if spell_cost > self.spell_points:

			print("Insufficienct spell points")
			return

		# changes health based on effect of spell
		character.health -= spell_effect

		# changes spell points based on cost of spell
		self.spell_points -= spell_cost

		if spell_name == "Heal":

			# if spell "Heal" increase character's health over maximum for class
			if isinstance(character,Wizard) and character.health > 16:

				spell_effect = 16 - character_health
				character.health = 16

			# logs actions
			print(self.name,"heals",character.name,"for",abs(spell_effect),"health points")
			print(self.name,"is now at",self.health,"health")

		else:

			# records spell cast and damage effect 
			print(self.name,"does",spell_effect,"damage to",character.name)
			print(character.name,"is now down to",character.health,"health")

		super().check_for_defeat(character)

# creates class Weapon
class Weapon:

	def __init__(self,weapon_type):

		self.weapon_type = weapon_type

	# get weapons damage points
	def weapon_damage(self):

		weapon = {"dagger":4,"axe":6,"staff":6,"sword":10,"none":1}

		damage_points = weapon[self.weapon_type]

		return damage_points

	# returns a string of the weapon_type
	def __str__(self):

		return self.weapon_type

# creates class Armor
class Armor:

	def __init__(self,armor_type):

		self.armor_type = armor_type

	# returns armor class points for types of armor
	def armor_protection(self):

		armor = {"plate":2,"chain":5,"leather":8,"none":10}

		armor_points = armor[self.armor_type]

		return armor_points

	# returns a string of armor type
	def __str__(self):

		return self.armor_type



def main():

	# create objects for each armor/weapon
	plateMail = Armor("plate")
	chainMail = Armor("chain")
	sword = Weapon("sword")
	staff = Weapon("staff")
	axe = Weapon("axe")

	# create character Gandalf the Grey as a wizard
	gandalf = Wizard("Gandalf the Grey")
	# wields a staff for gandalf
	gandalf.wield(staff)
	# create character Aragorn
	aragorn = Fighter("Aragorn")
	# give aragon platemail 
	aragorn.put_on_armor(plateMail)
	# wield an axe for aragon
	aragorn.wield(axe)

	print(gandalf)
	print(aragorn)

	# gandalf and aragon attacks each other
	gandalf.cast_spell("Fireball",aragorn)
	aragorn.fight(gandalf)

	print(gandalf)
	print(aragorn)

	# they attack each other again
	gandalf.cast_spell("Lightning Bolt",aragorn)
	aragorn.wield(sword)

	print(gandalf)
	print(aragorn)

	# gandalf heals himself, while aragon attacks gandalf
	gandalf.cast_spell("Heal",gandalf)
	aragorn.fight(gandalf)

	# they go at it again.. 
	gandalf.fight(aragorn)
	aragorn.fight(gandalf)

	print(gandalf)
	print(aragorn)


main()

