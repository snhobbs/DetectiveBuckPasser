/**stage0.sql**/

/**characters**/

insert into chars values(0, 0, 'standard', 'Six Dollar Man', 6, "Randy Savage except with a viciously failed wrestling career following a failed marriage. Weakness are his ex wife Sharron, alimony, and the IRS.", 0,
	'{"startOpts" : ["opt1","opt2"], "options" : {"opt1" : {"text" : "Option 1 Default", "nextOpts" : ["opt2","opt3"]}, "opt2" : {"text" : "Option 2 Default", "nextOpts" : ["opt1","opt3"]}, "opt3" : {"text" : "Option 3 Default", "nextOpts" : []}}}',

	'{"startOpts" : ["opt1","opt2"], "options" : {"opt1" : {"text" : "Option 1", "nextOpts" : ["opt2","opt3"]}, "opt2" : {"text" : "Option 2", "nextOpts" : ["opt1","opt3"]}, "opt3" : {"text" : "Option 3", "nextOpts" : []}}}'
	, 0);

insert into chars values(0, 1, 'standard', 'Bear', 1e6, "Trust fund animal. Yeah he sucks but his net worth is absurd. Problem is he wouldn't stop calling at dinner. Really his existance was the issue. If you're thinking one shouldn't speak ill of the dead, you clearly didn't know Bear", 0,
	'{"startOpts" : ["opt1","opt2"], "options" : {"opt1" : {"text" : "Option 1", "nextOpts" : ["opt2","opt3"]}, "opt2" : {"text" : "Option 2", "nextOpts" : ["opt1","opt3"]}, "opt3" : {"text" : "Option 3", "nextOpts" : []}}}',

	'{"startOpts" : ["opt1","opt2"], "options" : {"opt1" : {"text" : "Option 1", "nextOpts" : ["opt2","opt3"]}, "opt2" : {"text" : "Option 2", "nextOpts" : ["opt1","opt3"]}, "opt3" : {"text" : "Option 3", "nextOpts" : []}}}'
	, 0);


/**objects**/
insert into objects values(0,0, 'couch', 'Your shitty beige couch', 'It looks like it used to be suade before the layers of hair grease and cheap whiskey have left it in a state reminiscent of your soul.',0);

insert into objects values(0,1, 'computer', 'Computer', "A beige Dell covered in Cheeto dust. Some Dope website's on the screen", 1);

/**Rooms**/
insert into rooms values(0,0,'home', 'Home', '0,1,2,3', NULL, "You're in your garbage apartment. Your goldfish tank festers in the corner. Just another damn day.", 0,NULL);
insert into rooms values(0,1, 'shop', 'Tchotch-Naughts','0,1,2,3', NULL, "A bodega that appears to be run by a reincarnated JFK", 0,NULL);
insert into rooms values(0,2, 'floor', 'Apartments','0,1,2,3', NULL, "Apartment building foyer", 0,NULL);
insert into rooms values(0,3, 'general', 'Home Depot','0,1,2,3,4', NULL, "Home depot parking lot", 0,NULL);
insert into rooms values(0,4, 'car', 'Pontiac Fiero','0,1,2,3,4', NULL, "Hammer guy's burnt out black pontiac fiero. The tires have sunk into the pavement. Probably runs fine.", 0,NULL);
insert into rooms values(0,5, 'apartment','Murder Scene', '2,6,5', NULL, "Gruesome murder scene", 0,NULL);
insert into rooms values(0,6, 'floor', 'First Floor','2,5,6,7,8', NULL, "First Floor", 0,NULL);
insert into rooms values(0,7, 'floor', 'Second Floor','6,7,8', NULL, "Second Floor", 0,NULL);
insert into rooms values(0,8, 'floor', 'Third Floor','6,7,8', NULL, "Third Floor", 0,NULL);
