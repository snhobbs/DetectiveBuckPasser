--sqlStructure
--DROP TABLE IF EXISTS inventory, rooms, people, hero, objects, items;

create table items(
	itemCode int NOT NULL,
	subType string NOT NULL,
	itemName text NOT NULL,
	descrip text NOT NULL,
	weight int NOT NULL,
	itemSize int NOT NULL,
	critical bool NOT NULL,
	primary key(itemCode)
);

create table inventory(
	inventoryCode int NOT NULL,
	itemCode int NOT NULL,
	amount float NOT NULL
);

create table chars(
	charCode int NOT NULL,
	subType string NOT NULL,
	charName text NOT NULL,
	money float NOT NULL,
	bac float NOT NULL,--blood alcohol level
	descrip text NOT NULL,
	inventoryCode int,
	primary key(charCode)
);

create table rooms(
	roomCode int NOT NULL,
	subType string NOT NULL,
	roomName string NOT NULL,
	neighbors string NOT NULL,--accessible rooms
	chars text,--people in the room, csv string of charCodes
	descrip text NOT NULL,
	inventoryCode int,
	objects text,
	primary key(roomCode)
);

/**interactable objects**/
create table objects(
	objCode int NOT NULL,
	subType string NOT NULL,
	objName string NOT NULL,
	descrip text NOT NULL,
	inventoryCode int,
	primary key(objCode)
);
--inventory
insert into inventory values(0, 0, 3)
insert into inventory values(0, 1, 3.2)

--items
insert into items values(0, 'General', 'bottle', 'An empty bottle, like the one that biker beat you with last week at the End Zone', 0.1, 1, 0);
insert into items values(0, "Booze", 'Old Crow Burboun', 'Best burboun in the $5 price range', 0.5, 1, 1);

--characters
insert into chars values(0, 'sixdollarman', 'Six Dollar Man', 6, .6, "Randy Savage except with a viciously failed wrestling career following a failed marriage. Weakness are his ex wife Sharron, alimony, and the IRS.", 0);
insert into chars values(1, 'bear', 'Bear', 1e6, 0, "Trust fund animal. Yeah he sucks but his net worth is absurd. Problem is he wouldn't stop calling at dinner. Really his existance was the issue. If you're thinking one shouldn't speak ill of the dead, you clearly didn't know Bear", 0);

--objects
insert into objects values(0, 'couch', 'Your shitty beige couch', 'It looks like it used to be suade before the layers of hair grease and cheap whiskey have left it in a state reminiscent of your soul.',0);
insert into objects values(1, 'computer', 'Computer', "A beige Dell covered in Cheeto dust. Some Dope website's on the screen", 1);

--Rooms
insert into rooms values(0,'home', 'home', '1,2', NULL, "You're in your garbage apartment. Your goldfish tank festers in the corner. Just another damn day.", 0,'0,1');
insert into rooms values(1,'apartment', 'b3', '0,2', '0', "Apartment B3.", 0,'0,1');
insert into rooms values(2,'murder', 'murder', '0,1', '0,1', "Gruesome murder scene", 0,'0,1');
