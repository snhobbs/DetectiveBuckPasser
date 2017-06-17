/**items.sql**/

/**
	itemName text NOT NULL,
	descrip text NOT NULL,
	weight int NOT NULL,
	smallestUnit float NOT NULL,
**/

insert into items values(0, 'Bottle', 'An empty bottle, like the one that biker beat you with last week at the End Zone', 0.1, 1);
insert into items values(1, 'Whiskey', 'Old Crow, best bourbon in the $5 price range', 0.5, 1);

insert into items values(2, 'Foot in the Boot', 'An old foot in a boot', 7, 1);
insert into items values(3, 'Cocaine', 'Just enough bugger sugar to make this a drug squad issue', 0.1, 1);
insert into items values(4, 'Rent Money', "Roughly $17 in a crumped up ball", 1, 1);
insert into items values(5, 'Car Keys', 'Someones keys, there are 12 lock box keys in various stages of rust and a heavily worn car key that is kept on the chain with piano wire.', .2, 1);
insert into items values(6, 'Marriage Certificate', "Apparently Six Dollar Man's real is Oswald. I guess this is Sharron. He probably doesn't want anyone to know where to send the alimony late notices.", .2, 1);
insert into items values(7, "Wire Cutters", "", 2.7, 1);
insert into items values(8, "Hammer", "The murder weapon. Better hide this.", 2.7, 1);
insert into items values(9, "Beer", "Most of a 12 pack of Schafer, the cans are rusting.", 4, .1);
insert into items values(10, "Search Warrent", "You have a stack of these in your drawer, you dont even try and make them look official anymore.", .01, 1);
--Tchotch-Naughts Store Items

insert into items values(105, 'Dancing Pickle', "PJ The Party Pickle, you know what it is", 15, 1);
insert into items values(106, 'Post Card', "It reads: Wish you were here. The Grassy Knoll, Dallas TX", 1, 1);
insert into items values(107, 'Portable Glory Hole', "A pocket size apparatus that make anonymous oral sex a breeze! *Limit 1 per customer.", 1, 1);
insert into items values(108, 'Hand in a jar', "Captain Hook's missing hand suspended in fromaldahyde.", 2, 1);
insert into items values(109, 'Cedar Box', "Bud Abbott's mustache on a velvet pillow.", .2, 1);
insert into items values(110, "Vinyl Record", "Phil Harmonix's Dog Whistle Orchestra", .05, 1);
insert into items values(111, "Pez Dispenser", "Limited edition Larry David, Curb Your Insulin Pez dispenser", .01, 1);
insert into items values(112, "Lighter", "Ford Pinto shaped Zippo lighter, how fitting", .025, 1);
insert into items values(113, "Book", "Pen Pals by Ted Kaczynski", 1.2, 1);
insert into items values(114, "Cookbook", "Eating Right by Jeffery Dahmer", .01, 1);
insert into items values(115, "Gin", "Your only solace", .05, 1);
insert into items values(116, 'Roller Skates', "Saturn V Rocket powered roller skates", 1, 0);
insert into items values(117, 'Textbook', "Introduction to the Moon Landing Truth by John Fitzgerald Kennedy. All signed by the author!", 1, 0);
insert into items values(118, 'Body Part', "Gorbachev's birthmark delicately stapled to a Mickey Mantle rookie card", 1, 0);

/**Player Inventory**/
insert into inventory values(0, 0, 100);
insert into inventory values(0, 1, 2);
insert into inventory values(0, 5, 20);

/**Tchotch-Naughts**/
insert into inventory values(104, 105, 20);
insert into inventory values(104, 106, 20);
insert into inventory values(104, 107, 1);
insert into inventory values(104, 108, 20);
insert into inventory values(104, 109, 20);
insert into inventory values(104, 110, 20);
insert into inventory values(104, 111, 1);
insert into inventory values(104, 112, 1);
insert into inventory values(104, 113, 1);
insert into inventory values(104, 114, 1);
insert into inventory values(104, 115, 1);
insert into inventory values(104, 116, 1);
insert into inventory values(104, 117, 1);
insert into inventory values(104, 118, 1);
