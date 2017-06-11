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
insert into items values(3, 'Cocaine', 'Just enough blow to make this a drug squad issue', 0.1, 1);
insert into items values(4, 'Rent Money', "Roughly $17 in a crumped up ball", 1, 1);

--Tchotch-Naughts Store Items

insert into items values(5, 'Dancing Pickle', "PJ The Party Pickle, you know what it is", 15, 1);
insert into items values(6, 'Post Card', "It reads: Wish you were here. The Grassy Knoll, Dallas TX", 1, 1);
insert into items values(7, 'Portable Glory Hole', "A pocket size apparatus that make anonymous oral sex a breeze! *Limit 1 per customer.", 1, 1);
insert into items values(8, 'Hand in a jar', "Captain Hook's missing hand suspended in fromaldahyde.", 2, 1);
insert into items values(9, 'Cedar Box', "Bud Abbott's mustache on a velvet pillow.", .2, 1);
insert into items values(10, "Vinyl Record", "Phil Harmonix's Dog Whistle Orchestra", .05, 1);
insert into items values(11, "Pez Dispenser", "Limited edition Larry David, Curb Your Insulin Pez dispenser", .01, 1);
insert into items values(12, "Lighter", "Ford Pinto shaped Zippo lighter, how fitting", .025, 1);
insert into items values(13, "Book", "Pen Pals by Ted Kaczynski", 1.2, 1);
insert into items values(14, "Cookbook", "Eating Right by Jeffery Dahmer", .01, 1);
insert into items values(15, "Gin", "Your only solace", .05, 1);
insert into items values(16, 'Roller Skates', "Saturn V Rocket powered roller skates", 1, 0);
insert into items values(17, 'Textbook', "Introduction to the Moon Landing Truth by John Fitzgerald Kennedy. All signed by the author!", 1, 0);
insert into items values(18, 'Body Part', "Gorbachev's birthmark delicately stapled to a Mickey Mantle rookie card", 1, 0);

/**inventory**/
insert into inventory values(0, 0, 100);
insert into inventory values(0, 1, 2);
insert into inventory values(0, 5, 20);

insert into inventory values(100, 5, 20);

insert into inventory values(104, 5, 20);
insert into inventory values(104, 6, 20);
insert into inventory values(104, 7, 1);
insert into inventory values(104, 8, 20);
insert into inventory values(104, 9, 20);
insert into inventory values(104, 10, 20);
insert into inventory values(104, 11, 1);
