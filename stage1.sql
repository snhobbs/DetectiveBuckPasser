/**stage1.sql**/
insert into chars values(1, 1, 'standard', 'Bear', 1e6, "Smelly corpse", 0,
	'{"startOpts" : ["opt1","opt2"], "options" : {"opt1" : {"text" : "Option 1", "nextOpts" : ["opt2","opt3"]}, "opt2" : {"text" : "Option 2", "nextOpts" : ["opt1","opt3"]}, "opt3" : {"text" : "Option 3", "nextOpts" : []}}}',

	'{"startOpts" : ["opt1","opt2"], "options" : {"opt1" : {"text" : "Option 1", "nextOpts" : ["opt2","opt3"]}, "opt2" : {"text" : "Option 2", "nextOpts" : ["opt1","opt3"]}, "opt3" : {"text" : "Option 3", "nextOpts" : []}}}'
	, 0);

insert into objects values(1,0, 'couch', 'Your shitty beige couch, stage 1', 'Stage 1 Couch',0);

insert into rooms values(1,2,'murder', 'murder', '0,1', '0,1', "Gruesome murder scene, its starting to smell", 0,'0,1');
