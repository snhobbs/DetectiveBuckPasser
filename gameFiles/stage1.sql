/**stage1.sql**/
update game set stage = 1 where code = 0;

insert into rooms values(1,0,'Home', '0,1,2,3,4', NULL, "Your apartment. You sit up on your bed with a comforter that used to be blue, and sheets that used to be white. A dim fluorescent light bulb hanging from it's cord oscillates in the middle of the room. A goldfish tank festers in the corner, that's a new smell. Just another damn day.", 100, '3,4');
insert into rooms values(1,1,'Bathroom', '0,1,2,3,4', NULL, "You shuffle to the corner of the room. Technically it's a bathroom, minus the bath... and the room. It's just a flowery plush arm chair with the seat cut out strategically placed over an empty can of Beefarino. There's a stack of Better Homes and Gardens magazines next to the can, what mess.", 101,'1,2');
insert into rooms values(1,2,'Kitchen', '0,1,2,3,4', NULL, "The kitchen, oh boy the kitchen. Stacks of Beefarino and a rusty can opener. It used to be your favorite spot to watch people on the street pass by, but the window was bricked over by the new expansion of the fancy feast cannery. The brick fails to dampen the smell", 102,NULL);
insert into rooms values(1,3,'Window', '0,1,2,3,4', NULL, "As you survey your neighborhood you realize it's the same as always. A sickening red glow from the Hustler sign douses the streets which are littered with emaciated alley cats drawn to the cannery. A hooker is eating a tire.", 103,NULL);


/**
insert into chars values(1, 1, 'Bear', "Smelly corpse", 0,
	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"text" : "Hello Joseph", "nextOpts" : ["opt2"]}, "opt2" : {"text" : "Welcome to...", "nextOpts" : ["opt3"]}, "opt3" : {"text" : "The DDDRREEAAAMMMM WWWOOORRLLDD", "nextOpts" : []}}}',

	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"text" : "Hello Joseph", "nextOpts" : ["opt2"]}, "opt2" : {"text" : "How about you...", "nextOpts" : ["opt3"]}, "opt3" : {"text" : "go fuck yourself", "nextOpts" : []}}}'
	, 0);
**/
