insert into rooms values(3,23,'Murder Scene', '5,6', NULL, "Gruesome murder scene", 123,'0');--Steve has left the murder and gone to his own apartment
insert into rooms values(3,9,'1 A','6,7,8,18', '4', "Apartment 1A, Steve the Canadian's place.", 109,NULL);--Steve's home

insert into chars values(3, 4, 'Steve The Canadian', "Canadian AF. Real shithole you got here. Worse mess than when I saw this biker get in a tiffy with a moose. He's the hints.", 4, NULL, 
	'{"startOpts" : ["opt1"], "options" : 
		{"opt1": {"ques": null, "resp" : "Oh hey there bud, whats on your mind? ya want a Molson?", "nextOpts" : ["opt2", "opt3", "opt4"]}, 
		 "opt2": {"ques": "Just give me the beer", "resp": "Sure thing there, let me know if ya need a hand looking around", "nextOpts": []}, 
		 "opt3": {"ques": "I hear you know things. Tell me whats going on", "resp": "Oh I keep my ear to the tundra, what do ya want ta know bud?", "nextOpts": ["opt5", "opt6"]}, 
		 "opt4": {"ques": "Tell me everything you know", "resp": "Hey bud, Im happy to help but youll need to be more polite than that. How about that Molson?", "nextOpts": []},
		 "opt5": {"ques": "Who should I talk to?", "resp": "Oh I would suggest talking to everyone, arent you supposed to be the mountie?", "nextOpts": []}, 
		 "opt6": {"ques": "What do I need to get?", "resp": "I havent heard of anything", "nextOpts": []} }}', 0);
