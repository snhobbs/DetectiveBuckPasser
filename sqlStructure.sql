--sqlStructure
/**DROP TABLE IF EXISTS inventory, rooms, people, hero, objects, items;**/

create table items(
	subType string NOT NULL,
	itemCode int NOT NULL,
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
	subType string NOT NULL,
	charCode int NOT NULL,
	charName text NOT NULL,
	money float NOT NULL,
	bac float NOT NULL,--blood alcohol level
	descrip text NOT NULL,
	inventoryCode int,
	primary key(charCode)
);

create table rooms(
	subType string NOT NULL,
	roomCode int NOT NULL,
	neighbors int NOT NULL,--accessible rooms
	chars text,--people in the room, csv string of charCodes
	descrip text NOT NULL,
	inventoryCode int,
	objects text,
	primary key(roomCode)
);

/**interactable objects**/
create table objects(
	subType string NOT NULL,
	objCode int NOT NULL,
	objName string NOT NULL,
	descrip text NOT NULL,
	inventoryCode int,
	objects text,
	primary key(objCode)
);
