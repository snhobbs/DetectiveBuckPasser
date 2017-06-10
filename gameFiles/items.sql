/**items.sql**/

insert into items values(0, 'Bottle', 'An empty bottle, like the one that biker beat you with last week at the End Zone', 0.1, 1);
insert into items values(1, 'Whiskey', 'Old Crow, best bourbon in the $5 price range', 0.5, 1);
insert into items values(2, 'Foot in the boot', 'An old foot in a boot', 7, 1);
insert into items values(3, 'Cocaine', 'Just enough blow to mess make this a drug squad issue', 0.1, 1);
insert into items values(4, 'Rent Money', "Wad of greasy $1's", 1, 1);

insert into items values(5, 'Book', "Pen Pal's by Ted Kaczynski", 1, 0);
insert into items values(6, 'Cookbook', "Eating Well by Jeffery Dahmer", 1, 0);
insert into items values(7, 'Cedar Box', "Has Bud Abbott's mustache on a velvet pillow inside", 1, 0);
insert into items values(8, 'Portable Glory Hole', "Makes anonymous oral sex portable!", 1, 0);
insert into items values(9, 'Roller Skates', "Saturn V Rocket powered roller skates", 1, 0);
insert into items values(10, 'Textbook', "Introduction to the Moon Landing Truth by John Fitzgerald Kennedy. All signed by the author!", 1, 0);
insert into items values(11, 'Body Part', "Gorbachev's mole delicately stapled to a Mickey Mantle rookie card", 1, 0);

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
