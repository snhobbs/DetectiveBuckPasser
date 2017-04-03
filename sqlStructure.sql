--sqlStructure
DROP TABLE IF EXISTS inventory, rooms, people, hero, objects, items;

create table items(
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
	itemCount int NOT NULL,
);

create table people(
	charCode int NOT NULL,
	charName text NOT NULL,
	money float NOT NULL,
	bac float NOT NULL,--blood alcohol level
	roomCode int,
	descrip text NOT NULL,
	inventoryCode int,
	primary key(charCode)
);

create table rooms(
	roomType string NOT NULL,
	roomCode int NOT NULL,
	neighbors int NOT NULL,--accessible rooms
	people text,--people in the room, csv string of charCodes
	descrip text NOT NULL,
	inventoryCode int,
	objects text,
	primary key(roomCode)
);

create table objects(--interactable objects
	objCode int NOT NULL,
	description text NOT NULL,
	inventoryCode int,
	primary key(objCode)
);
