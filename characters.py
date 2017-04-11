#characters.py
from Character import Character

def characterFactory(db, code):
	charObj = Character(db = db, code = code)
	charObj.readFromDB()
	subType = charObj.subType.value

	if subType in ['SixDollarMan']:
		character = SixDollarMan(db)

	elif subType in ['Bear']:
		character = Bear(db)

	elif subType in ['JFK']:
		character = JFK(db)

	elif subType in ['HammerGuy']:
		character = HammerGuy(db)

	elif subType in ['GuyFieri']:
		character = GuyFieri(db)

	elif subType in ['Robot']:
		character = Robot(db)

	else:
		raise UserWarning('Unknown Character subType {}'.format(subType))

	character.readFromDB()
	return character


class SixDollarMan(Character):
	def __init__(self,db):
		self.code = 0
		Character.__init__(self,db, self.code)
		self.subType.value = 'SixDollarMan'
		self.charName.value = 'Six Dollar Man'
		self.money.value = 6
		self.bac.value = .6
		self.descrip.value = "Randy Savage except with a viciously failed wrestling career following a failed marriage. Weakness are his ex wife Sharron, alimony, and the IRS."

	def talk(self):
		print("Six Dollar Man: Brother, I got no time for this, you seen Sharron?")

	def kill(self):
		print("As you unholster the greasy tarnished M1911 you see the look of exceptance in Six Dollar's eyes. He embraces the sweet release of death, you reholster your gun, who are you to give such satisfaction?")

class Bear(Character):
	def __init__(self,db):
		self.code = 1
		Character.__init__(self,db, self.code)
		self.subType.value = 'Bear'
		self.charName.value = 'Bear'
		self.money.value = float('inf')
		self.bac.value = 0
		self.descrip.value = "Trust fund animal. Yeah he sucks but his net worth is absurd. Problem is he wouldn't stop calling at dinner. Really his existance was the issue. If you're thinking one shouldn't speak ill of the dead, you clearly didn't know Bear"

	def talk(self):
		print("Six Dollar Man: He Dead Brotherrr")


class Robot(Character):
	def __init__(self,db):
		self.code = 2
		Character.__init__(self,db, self.code)
		self.subType.value = 'Robot'
		self.charName.value = 'Robot'
		self.money.value = 0
		self.bac.value = 0
		self.descrip.value = "Early Yahoo AI experiment. After learning everything it knows from the combined knowledge of Geocities, Myspace, tomagachis, and The Charlie Rose Show... the putz, he has been left unplugged and abandoned. The net of his knowledge has left him with the operating IQ of a mid 2000's Crunk rapper. Due a Nas CD left in his drive when unplugged he claims to understand 'the struggle' and knows 'the Bridge'. Thinks OE in plastic is bullshit, coincidentaly Charlie Roses favorite beverage, the narc."

class JFK(Character):
	def __init__(self,db):
		self.code = 3
		Character.__init__(self,db, self.code)
		self.subType.value = 'JFK'
		self.charName.value = 'John F. Kennedy'
		self.money.value = 4e7
		self.bac.value = 0
		self.descrip.value = "35th president of the United State of America, you know the guy. The way they reattached the bits of his head they managed to scrape off Jackie were unfortunately put together like a muppet. He now runs Chach Naught, a novelty store in north Any Town, USA. He's a moon landing 'truther' just like Charlie Rose... the schmuck."

class HammerGuy(Character):
	def __init__(self,db):
		self.code = 4
		Character.__init__(self,db, self.code)
		self.subType.value = 'HammerGuy'
		self.charName.value = 'Hammer'
		self.money.value = 0
		self.bac.value = 0
		self.descrip.value = "Piece of shit, but hey, there's a lot to this guy. He hangs out in fornt of the Home Depot waiting for people to hire him. He's a real ladies man in his thickly motor oil permeated suede duster and his burnt-out '82 Pontic Fiero. He has a pet coyote, 'Keith'. It eats crows, that thing's on the brink of death sitting next to Charlie Rose... the schlump."

class GuyFieri(Character):
	def __init__(self,db):
		self.code = 5
		Character.__init__(self,db, self.code)
		self.subType.value = 'GuyFieri'
		self.charName.value = 'Guy Fieri'
		self.money.value = 1e5
		self.bac.value = 0
		self.descrip.value = "2 options shoot or there must be a better way, then instinct takes over and you shoot him anyway"
