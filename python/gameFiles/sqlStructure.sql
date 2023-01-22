/**sqlStructure**/
/**DROP TABLE IF EXISTS inventory, rooms, people, hero, objects, items;**/

create table game(
	code int NOT NULL,
	stage int NOT NULL
);

create table events(
	stage int NOT NULL,
	itemCode int,
	amount float,
	charCode int,
	objCode int,
	roomCode int,
	eventDescrip string,
	primary key(stage)
);

create table cutScene(
	stage int NOT NULL,
	title text NOT NULL,
	text text NOT NULL,
	primary key(stage)
);

create table items(
	itemCode int NOT NULL,
	itemName text NOT NULL,
	descrip text NOT NULL,
	weight int NOT NULL,
	smallestUnit float NOT NULL,
	primary key(itemCode)
);

create table inventory(
	inventoryCode int NOT NULL,
	itemCode int NOT NULL,
	amount float NOT NULL
);

create table chars(
	stage int NOT NULL,
	charCode int NOT NULL,
	charName text NOT NULL,
	descrip text NOT NULL,
	inventoryCode int,
	conv text,
	defaultConv text NOT NULL,
	interactedFlag bool NOT NULL,
	primary key(stage, charCode)
);

create table rooms(
	stage int NOT NULL,
	roomCode int NOT NULL,
	roomName string NOT NULL,
	neighbors string NOT NULL,--accessible rooms
	chars text,--people in the room, csv string of charCodes
	descrip text NOT NULL,
	inventoryCode int,
	objects text,
	primary key(roomCode, stage)
);

/**interactable objects**/
create table objects(
	stage int NOT NULL,
	objCode int NOT NULL,
	objName string NOT NULL,
	descrip text NOT NULL,
	shortDescrip text NOT NULL,
	useAlias text,
	useDescrip text,
	usePrint text,
	inventoryCode int,
	interactedFlag bool NOT NULL,
	primary key(objCode, stage)
);
