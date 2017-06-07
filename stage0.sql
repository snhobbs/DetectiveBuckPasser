/**stage0.sql**/

/**characters**/
insert into game values(0,0);

insert into chars values(0, 1, 'Bear', "Trust fund animal. Yeah he sucks but his net worth is absurd. Problem is he wouldn't stop calling at dinner. Really his existance was the issue. If you're thinking one shouldn't speak ill of the dead, you clearly didn't know Bear. Also he's starting to smell.", 1,
	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Om man is that a mess", "nextOpts" : []}}}', 0);

insert into chars values(0, 2, 'Six Dollar Man', "Randy Savage except with a viciously failed wrestling career following a failed marriage. Weakness are his ex wife Sharron, alimony, and the IRS.", 2,

	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "I aint got time for this brother, you seen Sharron", "nextOpts" : []}}}', 0);

insert into chars values(0, 3, 'Old Lady', "There is a significant chance that she will be eaten by her herds of cats.", 3,

	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "You want the old foot in the boot?", "nextOpts" : []}}}', 0);

insert into chars values(0, 4, 'Steve The Canadian', "Canadian AF. Real shithole you got here. Worse mess than when I saw this biker get in a tiffy with a moose. He's the hints.", 4,

	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Oh hey there bud, ya want a Molson?", "nextOpts" : []}}}', 0);

insert into chars values(0, 5, 'JFK', "35th president of the United State of America, you know the guy. The way they reattached the bits of his head they managed to scrape off Jackie were unfortunately put together like a muppet. He now runs Tchotch Naught, a novelty store in north Any Town, USA. He's a moon landing 'truther' just like Charlie Rose... the schmuck.", 5,

	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "The moon landing was STTTAAAGGGEEEDDD", "nextOpts" : ["opt2"]}, "opt2" : {"ques" : "Who staged it?", "resp" : "Armstrong`s a fraaaauuuddd", "nextOpts" : []}}}',

	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "The flag was waving, the flag was WAVING!", "nextOpts" : []}}}', 0);

insert into chars values(0, 6, 'Robot', "Early Yahoo AI experiment. After learning everything it knows from the combined knowledge of Geocities, Myspace, tomagachis, and The Charlie Rose Show... the putz, he has been left unplugged and abandoned. The net of his knowledge has left him with the operating IQ of a mid 2000's Crunk rapper. Due a Nas CD left in his drive when unplugged he claims to understand 'the struggle' and knows 'the Bridge'. Thinks OE in plastic is bullshit, coincidentaly Charlie Roses favorite beverage, the narc.", 6,

	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "404: Robot not found", "nextOpts" : []}}}', 0);

insert into chars values(0, 7, 'Joe', "Bear's AA sponsor, had to constantly deal with bear", 7,

	NULL, '{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Im not gonna say Im glad hes dead, but we havent had to hear anymore Reel Big Fish...", "nextOpts" : []}}}', 0);

insert into chars values(0, 8, 'Veterinarian', "Battle fatigued veterinarian. He enjoys putting down animals a bit too much. 'You ever seen what piano wire will do to a pomeranians neck?", 8,

	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Well, lost another patient", "nextOpts" : []}}}', 0);

insert into chars values(0, 10, 'Derrick The Salesman', "Don't buy a car from this guy", 10,

	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Heeyyy muchacho, wanna buy a Pontiac?", "nextOpts" : []}}}', 0);

insert into chars values(0, 11, 'Guy Fieri', "Oh dear god no", 11,

	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Welcome to Flavortown", "nextOpts" : []}}}', 0);

insert into chars values(0, 12, 'Hammer Guy', "Piece of shit, but hey, there's a lot to this guy. He hangs out in fornt of the Home Depot waiting for people to hire him. He's a real ladies man in his thickly motor oil permeated suede duster and his burnt-out '82 Pontic Fiero. He has a pet coyote, 'Keith'. It eats crows, that thing's on the brink of death sitting next to Charlie Rose... the schlump.", 0,

	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "You seen my keys? My cars", "nextOpts" : []}}}',
	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "You seen my keys? My cars", "nextOpts" : []}}}', 0);

/**objects**/
insert into objects values(0,0, 'couch', 'Your shitty beige couch', 'It looks like it used to be suade before the layers of hair grease and cheap whiskey have left it in a state reminiscent of your soul.',0);

insert into objects values(0,1, 'computer', 'Computer', "A beige Dell covered in Cheeto dust. Some Dope website's on the screen", 1);

/**Rooms**/

/**Home Apartment - Every room is connected, only 'Home' is connected to the outside**/
insert into rooms values(0,0,'Home', '0,1,2,3,4', NULL, "Your apartment. You sit up on your bed with a comforter that used to be blue, and sheets that used to be white. A dim fluorescent light bulb hanging from its cord oscillates in the middle of the room. A goldfish tank festers in the corner, that's a new smell. Just another damn day.", 100, NULL);
insert into rooms values(0,1,'Bathroom', '0,1,2,3,4', NULL, "You shuffle to the corner of the room. Technically its a bathroom, minus the bath... and the room. It's just a flowery plush arm chair with the seat cut out strategically placed over an empty can of Beefarino. There's a stack of Better Homes and Gardens magazines next to the can, what mess.", 101,NULL);
insert into rooms values(0,2,'Kitchen', '0,1,2,3,4', NULL, "The kitchen, oh boy the kitchen. Stacks of Beefarino and a rusty can opener. It used to be your favorite spot to watch people on the street pass by, but the window was bricked over by the new expansion of the fancy feast cannery. The brick fails to dampen the smell", 102,NULL);
insert into rooms values(0,3,'Window', '0,1,2,3,4', NULL, "As you survey your neighborhood you realize it's the same as always. A sickening red glow from the Hustler sign douses the streets which are littered with emaciated alley cats drawn to the cannery. A hooker is eating a tire.", 103,NULL);

/**Other Rooms**/
insert into rooms values(0,4,'Tchotch Naughts','0,5', '5', "A bodega that appears to be run by a reincarnated JFK", 104,NULL);
insert into rooms values(0,5,'Apartments','4,6,7,8,23', NULL, "Apartment building foyer", 105,NULL);

insert into rooms values(0,6,'First Floor','23,5,6,7,8,9,10,11', NULL, "First Floor", 106,NULL);
insert into rooms values(0,7,'Second Floor','6,7,8,12,13,14', NULL, "Second Floor", 107,NULL);
insert into rooms values(0,8,'Third Floor','6,7,8,15,16,17', NULL, "Third Floor", 108,NULL);

--
insert into rooms values(0,9,'1 A','6,7,8,18', '4', "Apartment 1A", 109,NULL);
insert into rooms values(0,10,'1 B','6,7,8,19', '6', "Apartment 1B", 110,NULL);
insert into rooms values(0,11,'1 C','6,7,8,20', '7', "Apartment 1C", 111,NULL);

insert into rooms values(0,12,'2 A','6,7,8', '8', "Apartment 2A", 112,NULL);
insert into rooms values(0,13,'2 B','6,7,8', NULL, "Apartment 2B", 113,NULL);
insert into rooms values(0,14,'2 C','6,7,8', '10', "Apartment 2C", 114,NULL);

insert into rooms values(0,15,'3 A','6,7,8', '1', "Apartment 3A", 115,NULL);
insert into rooms values(0,16,'3 B','6,7,8', '3', "Apartment 3B", 116,NULL);
insert into rooms values(0,17,'3 C','6,7,8', '2', "Apartment 3C", 117,NULL);

insert into rooms values(0,18,'Bathroom','9', NULL, "On suite bathroom for 1A", 118,NULL);
insert into rooms values(0,19,'Bathroom','10', NULL, "On suite bathroom for 1B", 119,NULL);
insert into rooms values(0,20,'Bathroom','11', NULL, "On suite bathroom for 1C", 120,NULL);

insert into rooms values(0,21,'Home Depot','4,21,22', NULL, "Home depot parking lot", 121,NULL);
insert into rooms values(0,22,'Pontiac Fiero','21,22', '12', "Hammer guy's burnt out black pontiac fiero. The tires have sunk into the pavement. Probably runs fine.", 122,NULL);
insert into rooms values(0,23,'Murder Scene', '5,6', '1', "Gruesome murder scene", 123,NULL);
