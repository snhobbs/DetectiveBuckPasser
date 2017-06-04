/**stage0.sql**/

/**characters**/

insert into chars values(0, 0, 'standard', 'Six Dollar Man', 6, "Randy Savage except with a viciously failed wrestling career following a failed marriage. Weakness are his ex wife Sharron, alimony, and the IRS.", 0,
	'{"startOpts" : ["opt1","opt2"], "options" : {"opt1" : {"text" : "Option 1 Default", "nextOpts" : ["opt2","opt3"]}, "opt2" : {"text" : "Option 2 Default", "nextOpts" : ["opt1","opt3"]}, "opt3" : {"text" : "Option 3 Default", "nextOpts" : []}}}',

	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"text" : "Option 1", "nextOpts" : []}}}'
	, 0);

insert into chars values(0, 1, 'standard', 'Bear', 1e6, "Trust fund animal. Yeah he sucks but his net worth is absurd. Problem is he wouldn't stop calling at dinner. Really his existance was the issue. If you're thinking one shouldn't speak ill of the dead, you clearly didn't know Bear", 0,
	'{"startOpts" : ["opt1","opt2"], "options" : {"opt1" : {"text" : "Option 1", "nextOpts" : ["opt2","opt3"]}, "opt2" : {"text" : "Option 2", "nextOpts" : ["opt1","opt3"]}, "opt3" : {"text" : "Option 3", "nextOpts" : []}}}',

	'{"startOpts" : ["opt1","opt2"], "options" : {"opt1" : {"text" : "Option 1", "nextOpts" : ["opt2","opt3"]}, "opt2" : {"text" : "Option 2", "nextOpts" : ["opt1","opt3"]}, "opt3" : {"text" : "Option 3", "nextOpts" : []}}}'
	, 0);


insert into chars values(0, 5, 'standard', 'JFK', 1e6, "35th president of the United State of America, you know the guy. The way they reattached the bits of his head they managed to scrape off Jackie were unfortunately put together like a muppet. He now runs Tchotch Naught, a novelty store in north Any Town, USA. He's a moon landing 'truther' just like Charlie Rose... the schmuck.", 0,

	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "The flag was waving, the flag was WAVING!", "nextOpts" : []}}}',

	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "The moon landing was STTTAAAGGGEEEDDD", "nextOpts" : ["opt2"]}, "opt2" : {"ques" : "Who staged it?", "resp" : "Armstrong`s a fraaaauuuddd", "nextOpts" : []}}}'
	, 0);


/**objects**/
insert into objects values(0,0, 'couch', 'Your shitty beige couch', 'It looks like it used to be suade before the layers of hair grease and cheap whiskey have left it in a state reminiscent of your soul.',0);

insert into objects values(0,1, 'computer', 'Computer', "A beige Dell covered in Cheeto dust. Some Dope website's on the screen", 1);

/**Rooms**/
/**


**/

/**Home Apartment**/
insert into rooms values(0,0,'Home', '0,1,2,3,4', NULL, "Your apartment. You sit up on your bed with a comforter that used to be blue, and sheets that used to be white. A dim fluorescent light bulb hanging from its cord oscillates in the middle of the room. A goldfish tank festers in the corner, that's a new smell. Just another damn day.", 0,NULL);
insert into rooms values(0,1,'Bathroom', '0,1,2,3,4', NULL, "You shuffle to the corner of the room. Technically its a bathroom, minus the bath... and the room. It's just a flowery plush arm chair with the seat cut out strategically placed over an empty can of Beefarino. There's a stack of Better Homes and Gardens magazines next to the can, what mess.", 0,NULL);
insert into rooms values(0,2,'Kitchen', '0,1,2,3,4', NULL, "The kitchen, oh boy the kitchen. Stacks of Beefarino and a rusty can opener. It used to be your favorite spot to watch people on the street pass by, but the window was bricked over by the new expansion of the fancy feast cannery. The brick fails to dampen the smell", 0,NULL);
insert into rooms values(0,3,'Window', '0,1,2,3,4', NULL, "As you survey your neighborhood you realize it's the same as always. A sickening red glow from the Hustler sign douses the streets which are littered with emaciated alley cats drawn to the cannery. A hooker is eating a tire.", 0,NULL);

insert into rooms values(0,4,'Tchotch Naughts','0,5', '5', "A bodega that appears to be run by a reincarnated JFK", 0,NULL);
insert into rooms values(0,5,'Apartments','4,6,7,8,23', NULL, "Apartment building foyer", 0,NULL);

insert into rooms values(0,6,'First Floor','23,5,6,7,8,9,10,11', NULL, "First Floor", 0,NULL);
insert into rooms values(0,7,'Second Floor','6,7,8,12,13,14', NULL, "Second Floor", 0,NULL);
insert into rooms values(0,8,'Third Floor','6,7,8,15,16,17', NULL, "Third Floor", 0,NULL);

--
insert into rooms values(0,9,'1 A','6,7,8,20', NULL, "Apartment 1A", 0,NULL);
insert into rooms values(0,10,'1 B','6,7,8,19', NULL, "Apartment 1B", 0,NULL);
insert into rooms values(0,11,'1 C','6,7,8,20', NULL, "Apartment 1C", 0,NULL);

insert into rooms values(0,12,'2 A','6,7,8', NULL, "Third Floor", 0,NULL);
insert into rooms values(0,13,'2 B','6,7,8', NULL, "Third Floor", 0,NULL);
insert into rooms values(0,14,'2 C','6,7,8', NULL, "Third Floor", 0,NULL);

insert into rooms values(0,15,'3 A','6,7,8', NULL, "Third Floor", 0,NULL);
insert into rooms values(0,16,'3 B','6,7,8', NULL, "Third Floor", 0,NULL);
insert into rooms values(0,17,'3 C','6,7,8', NULL, "Third Floor", 0,NULL);

insert into rooms values(0,18,'Bathroom','9', NULL, "On suite bathroom for 1A", 0,NULL);
insert into rooms values(0,19,'Bathroom','10', NULL, "On suite bathroom for 1B", 0,NULL);
insert into rooms values(0,20,'Bathroom','11', NULL, "On suite bathroom for 1C", 0,NULL);

insert into rooms values(0,21,'Home Depot','4,21,22', NULL, "Home depot parking lot", 0,NULL);
insert into rooms values(0,22,'Pontiac Fiero','21,22', NULL, "Hammer guy's burnt out black pontiac fiero. The tires have sunk into the pavement. Probably runs fine.", 0,NULL);
insert into rooms values(0,23,'Murder Scene', '5,6', NULL, "Gruesome murder scene", 0,NULL);
