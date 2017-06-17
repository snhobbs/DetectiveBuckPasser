/**stage0.sql**/

/**characters**/
insert into game values(0,0);

insert into cutScene values(0, 'The Bowery, New York, 1972. 12:27PM', 'You wake up in your grimey bed. The neon light from the Hustler sign across the street somehow manages to make its way through the dense smog. Your 1 room apartment is doused in its light, the sun doesnt have a chance.^The Fancy Feast cat food cannery across the street has drawn even more alley cats.~Time to start the day');

insert into chars values(0, 1, 'Bear', "Trust fund animal. Yeah he sucks but his net worth is absurd. Problem is he wouldn't stop calling at dinner. Really his existance was the issue. If you're thinking one shouldn't speak ill of the dead, you clearly didn't know Bear. Also he's starting to smell.", 1,
	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Oh man is that a mess", "nextOpts" : []}}}', 0);

insert into chars values(0, 2, 'Six Dollar Man', "Randy Savage except with a viciously failed wrestling career following a failed marriage. Weakness are his ex wife Sharron, alimony, and the IRS.", 2,

	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "I ain|t got time for this brother, you seen Sharron", "nextOpts" : []}}}', 0);

insert into chars values(0, 3, 'Old Lady', "There is a significant chance that she will be eaten by her herds of cats.", 3,

	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "You want the old foot in the boot?", "nextOpts" : []}}}', 0);

insert into chars values(0, 4, 'Steve The Canadian', "6'6`` caucasian male, claims to be from the praries, wherever the hell that is. Could be anywhere as you've never looked at a map. If you cared you be asking why he was carrying a Bowie knife and asking what we were planning on doing with the victim's `hide`", 4,

	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Real shit hole ya got here bud. Worse mess than when my cousin Tom got in a tiffy with a moose in heat. If you need any help come talk to me in 1A, I`ll have a cold Molson waiting for ya.", "nextOpts" : []}}}', '{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Oh hey there bud, ya want a Molson?", "nextOpts" : []}}}', 0);

insert into chars values(0, 5, 'JFK', "35th president of the United State of America, you know the guy. The way they reattached the bits of his head they managed to scrape off Jackie were unfortunately put together like a muppet. He now runs Tchotch Naught, a novelty store in north Any Town, USA. He's a moon landing 'truther' just like Charlie Rose... the schmuck.", 5,

	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "The moon landing was STTTAAAGGGEEEDDD", "nextOpts" : ["opt2"]}, "opt2" : {"ques" : "Who staged it?", "resp" : "Armstrong`s a fraaaauuuddd", "nextOpts" : []}}}',

	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "The flag was waving, the flag was WAVING!", "nextOpts" : []}}}', 0);

insert into chars values(0, 6, 'Robot', "Early Yahoo AI experiment. After learning everything it knows from the combined knowledge of Geocities, Myspace, tomagachis, and The Charlie Rose Show... the putz, he has been left unplugged and abandoned. The net of his knowledge has left him with the operating IQ of a mid 2000's Crunk rapper. Due a Nas CD left in his drive when unplugged he claims to understand 'the struggle' and knows 'the Bridge'. Thinks OE in plastic is bullshit, coincidentaly Charlie Roses favorite beverage, the narc.", 6,

	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "404: Robot not found", "nextOpts" : []}}}', 0);

insert into chars values(0, 7, 'Joe', "Bear's AA sponsor, had to constantly deal with bear", 7,

	NULL, '{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "I|m not gonna say I|m glad hes dead, but we haven|t had to hear anymore Reel Big Fish...", "nextOpts" : []}}}', 0);

insert into chars values(0, 8, 'Veterinarian', "Battle fatigued veterinarian. He enjoys putting down animals a bit too much. 'You ever seen what piano wire will do to a pomeranians neck?", 8,

	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Well, lost another patient", "nextOpts" : []}}}', 0);

insert into chars values(0, 10, 'Derrick The Salesman', "Don't buy a car from this guy", 10,

	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Heeyyy muchacho, wanna buy a Pontiac?", "nextOpts" : []}}}', 0);

insert into chars values(0, 11, 'Guy Fieri', "Oh dear god no", 11,

	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Welcome to Flavortown", "nextOpts" : []}}}', 0);

insert into chars values(0, 12, 'Hammer Guy', "A complete animal by moral standards, but hey, there's a lot to this guy. He hangs out in fornt of the Home Depot waiting for people to hire him. He's a real ladies man in his thickly motor oil permeated suede duster and his burnt-out '82 Pontic Fiero. Denied access to all local fast food restaurant bathrooms.", 12,

	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "You seen my keys? My cars", "nextOpts" : []}}}',
	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "You seen my keys? My cars", "nextOpts" : []}}}', 0);

/**objects**/
insert into objects values(0,0, "Bear's Corpse", "Trust fund animal. Yeah he sucks but his net worth is absurd. Problem is he wouldn't stop calling at dinner. Really his existance was the issue. If you're thinking one shouldn't speak ill of the dead, you clearly didn't know Bear. Also he's starting to smell.", "A cold stiff corpse of a poorly groomed Kodiak Grizzly","Investigate", "Search for clues", "Better leave that for someone else actually",200, 0);

insert into objects values(0,1, 'Toilet', "It's just a flowery plush arm chair with the seat cut out strategically placed over an empty can of Beefarino", "I guess it's a toilet", "flush", "Flush the toilet","You heave the can of beefarino out the window, no one notices, not even the alley cats or the hooker eating a tire",201, 0);

insert into objects values(0,2, 'Magazine', "Dog eared copy of Better Homes and Gardens, the June, 1964 edition", "Better Homes and Gardens June, 1964", "read", "Flip through the magazine","You read the magazine as you have 700 times before. Maybe one day you'll try and make some of these improvements, but there you are with a can as your toilet.",202, 0);

insert into objects values(0,3, 'Phone', "The cord is hopelessly tangled, the reciever is partially clogged with beefarino. If anyone ever wanted to talk to you you'd have to get a new one. Of course they don't so here it is.", 'Your home phone, you have a message','Messages', "Check your messages, do something for once.", "It's the Chief. 'Passer, there's been a murder down the street from you at the Kodiak Apartments. It sounds grizzly, go check it out. I want a report on my desk tomorrow, and it had better be good you layabout.'",203, 0);

insert into objects values(0,4, 'Couch', 'It looks like it used to be suade before the layers of hair grease and cheap whiskey have left it in a state reminiscent of your soul.', 'Your shitty beige couch','sit', "Plop your lazy self down on this gross sofa", "As you throw yourself gracelessly onto the greasy sofa what looks like a cockroach exodus complete with a cockroach Moses leading his people out of the sofa through the parting of the couch cushions begins. You have a quick nap in your natural habitat.",204, 0);
--insert into objects values(0,1, 'computer', 'Computer', "A beige Dell covered in Cheeto dust. Some Dope website's on the screen", 1);

/**Rooms**/

/**Home Apartment - Every room is connected, only 'Home' is connected to the outside**/
insert into rooms values(0,0,'Home', '0,1,2,3', NULL, "Your apartment. You sit up on your bed with a comforter that used to be blue, and sheets that used to be white. A dim fluorescent light bulb hanging from it's cord oscillates in the middle of the room. A goldfish tank festers in the corner, that's a new smell. Just another damn day.", 100, '4,3');
insert into rooms values(0,1,'Bathroom', '0,1,2,3', NULL, "You shuffle to the corner of the room. Technically it's a bathroom, minus the bath... and the room. It's just a flowery plush arm chair with the seat cut out strategically placed over an empty can of Beefarino. There's a stack of Better Homes and Gardens magazines next to the can, what mess.", 101,'1,2');
insert into rooms values(0,2,'Kitchen', '0,1,2,3', NULL, "The kitchen, oh boy the kitchen. Stacks of Beefarino and a rusty can opener. It used to be your favorite spot to watch people on the street pass by, but the window was bricked over by the new expansion of the fancy feast cannery. The brick fails to dampen the smell", 102,NULL);
insert into rooms values(0,3,'Window', '0,1,2,3', NULL, "As you survey your neighborhood you realize it's the same as always. A sickening red glow from the Hustler sign douses the streets which are littered with emaciated alley cats drawn to the cannery. A hooker is eating a tire.", 103,NULL);

/**Other Rooms**/
insert into rooms values(0,4,'Tchotch Naughts','0,5', '5', "A bodega that appears to be run by a reincarnated JFK", 104,NULL);
insert into rooms values(0,5,'Apartments','4,6,7,8,23', NULL, "Apartment building foyer", 105,NULL);

insert into rooms values(0,6,'First Floor','23,5,6,7,8,9,10,11', NULL, "First Floor", 106,NULL);
insert into rooms values(0,7,'Second Floor','6,7,8,12,13,14', NULL, "Second Floor", 107,NULL);
insert into rooms values(0,8,'Third Floor','6,7,8,15,16,17', NULL, "Third Floor", 108,NULL);

--
insert into rooms values(0,9,'1 A','6,7,8,18', NULL, "Apartment 1A, Steve the Canadian's place.", 109,NULL);--Steve's at the murder scene
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
insert into rooms values(0,23,'Murder Scene', '5,6', '4', "Gruesome murder scene", 123,'0');--Steve is here
