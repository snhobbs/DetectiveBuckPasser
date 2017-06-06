/**stage1.sql**/
update game set stage = 1 where code = 0;

insert into chars values(1, 1, 'Bear', "Smelly corpse", 0,
	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"text" : "Hello Joseph", "nextOpts" : ["opt2"]}, "opt2" : {"text" : "Welcome to...", "nextOpts" : ["opt3"]}, "opt3" : {"text" : "The DDDRREEAAAMMMM WWWOOORRLLDD", "nextOpts" : []}}}',

	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"text" : "Hello Joseph", "nextOpts" : ["opt2"]}, "opt2" : {"text" : "How about you...", "nextOpts" : ["opt3"]}, "opt3" : {"text" : "go fuck yourself", "nextOpts" : []}}}'
	, 0);
