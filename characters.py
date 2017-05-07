#characters.py
from Character import Character

def characterFactory(db, code):
	charObj = Character(db = db, code = code)
	charObj.readFromDB()
	subType = charObj.subType.value

	charDict = {
		'sixdollarman':SixDollarMan,
		'bear':Bear,
		'jfk':JFK,
		'hammerguy':HammerGuy,
		'guyfieri':GuyFieri,
		'robot':Robot
	}
	try:
		character = charDict[subType](db)
		character.readFromDB()
		return character
	except KeyError:
		raise UserWarning('Unknown character type {}'.format(subType))

class SixDollarMan(Character):
	def __init__(self,db):
		self.code = 0
		subType = 'SixDollarMan'
		charName = 'Six Dollar Man'
		money = 6
		bac = .6
		descrip = "Randy Savage except with a viciously failed wrestling career following a failed marriage. Weakness are his ex wife Sharron, alimony, and the IRS."
		Character.__init__(self,db, self.code, subType,charName,money, bac, descrip)
	def talk(self):
		print("Six Dollar Man: Brother, I got no time for this, you seen Sharron?")

	def kill(self):
		print("As you unholster the greasy tarnished M1911 you see the look of exceptance in Six Dollar's eyes. He embraces the sweet release of death, you reholster your gun, who are you to give such satisfaction?")

class Bear(Character):
	def __init__(self,db):
		self.code = 1
		subType = 'Bear'
		charName = 'Bear'
		money = float('inf')
		bac = 0
		descrip = "Trust fund animal. Yeah he sucks but his net worth is absurd. Problem is he wouldn't stop calling at dinner. Really his existance was the issue. If you're thinking one shouldn't speak ill of the dead, you clearly didn't know Bear"
		Character.__init__(self,db, self.code, subType,charName,money, bac, descrip)
	def talk(self):
		print("Six Dollar Man: He Dead Brotherrr")


class Robot(Character):
	def __init__(self,db):
		self.code = 2
		subType = 'Robot'
		charName = 'Robot'
		money = 0
		bac = 0
		descrip = "Early Yahoo AI experiment. After learning everything it knows from the combined knowledge of Geocities, Myspace, tomagachis, and The Charlie Rose Show... the putz, he has been left unplugged and abandoned. The net of his knowledge has left him with the operating IQ of a mid 2000's Crunk rapper. Due a Nas CD left in his drive when unplugged he claims to understand 'the struggle' and knows 'the Bridge'. Thinks OE in plastic is bullshit, coincidentaly Charlie Roses favorite beverage, the narc."
		Character.__init__(self,db, self.code, subType,charName,money, bac, descrip)

class JFK(Character):
	def __init__(self,db):
		self.code = 3
		Character.__init__(self,db, self.code)
		self.subType = 'JFK'
		self.charName = 'John F. Kennedy'
		self.money = 4e7
		bac = 0
		descrip = "35th president of the United State of America, you know the guy. The way they reattached the bits of his head they managed to scrape off Jackie were unfortunately put together like a muppet. He now runs Chach Naught, a novelty store in north Any Town, USA. He's a moon landing 'truther' just like Charlie Rose... the schmuck."
		Character.__init__(self,db, self.code, subType,charName,money, bac, descrip)

class HammerGuy(Character):
	def __init__(self,db):
		self.code = 4
		subType = 'HammerGuy'
		charName = 'Hammer'
		money = 0
		bac = 0
		descrip = "Piece of shit, but hey, there's a lot to this guy. He hangs out in fornt of the Home Depot waiting for people to hire him. He's a real ladies man in his thickly motor oil permeated suede duster and his burnt-out '82 Pontic Fiero. He has a pet coyote, 'Keith'. It eats crows, that thing's on the brink of death sitting next to Charlie Rose... the schlump."
		Character.__init__(self,db, self.code, subType,charName,money, bac, descrip)

class GuyFieri(Character):
	'''
	you just shoot him when you open the door and his aprtment is no longer accessible
	'''
	def __init__(self,db):
		self.code = 5
		subType = 'GuyFieri'
		charName = 'Guy Fieri'
		money = 1e5
		bac = 0
		descrip = "2 options shoot or there must be a better way, then instinct takes over and you shoot him anyway"
		Character.__init__(self,db, self.code, subType,charName,money, bac, descrip)

class OldLady(Character):
	def __init__(self,db):
		self.code = 6
		subType = 'OldLady'
		charName = 'Susan'
		money = 1e5
		bac = 0
		descrip = "He hs got a boot with a foot in it. SHE'S ALL ABOUT THE BUM"
		Character.__init__(self,db, self.code, subType,charName,money, bac, descrip)

class Canadian(Character):
	def __init__(self,db):
		self.code = 7
		subType = 'Canadian'
		charName = 'Steve'
		money = 1e5
		bac = 2
		descrip = "Canadian AF. Real shithole you got here. Worse mess than when I saw this biker get in a tiffy with a moose. He's the hints."
		Character.__init__(self,db, self.code, subType,charName,money, bac, descrip)

class Veterinarian(Character):
	def __init__(self,db):
		self.code = 8
		subType = 'Veterinarian'
		charName = 'Dr. '
		money = 1e5
		bac = 0
		descrip = "Battle fatigued veterinarian. He enjoys putting down animals a bit too much. 'You ever seen what piano wire will do to a pomeranians neck?'"
		Character.__init__(self,db, self.code, subType,charName,money, bac, descrip)

class AASponser(Character):
	def __init__(self,db):
		self.code = 9
		subType = 'AASponser'
		charName = 'Joe'
		money = 1e5
		bac = 0
		descrip = "Bear's AA sponsor, roommates with Simon. Has to constantly deal with bear"
		Character.__init__(self,db, self.code, subType,charName,money, bac, descrip)

class AASponserRoommate(Character):
	def __init__(self,db):
		self.code = 10
		subType = 'AASponserRoommate'
		charName = 'Simon'
		money = 1e5
		bac = 0
		descrip = "Pep talks Joe as to how to standup to bear, always resorts to camping guides for dealing with bear encounters"
		Character.__init__(self,db, self.code, subType,charName,money, bac, descrip)

class Salesman(Character):
	def __init__(self,db):

