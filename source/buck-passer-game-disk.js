const intro_screen =
`
  ____       _            _                 ____             _
 |  _ \\  ___| |_ ___  ___| |_(_)_   _____  | __ ) _   _  ___| | __
 | | | |/ _ \\ __/ _ \\/ __| __| \\ \\ / / _ \\ |  _ \\| | | |/ __| |/ /
 | |_| |  __/ ||  __/ (__| |_| |\\ V /  __/ | |_) | |_| | (__|   <
 |____/ \\___|\\__\\___|\\___|\\__|_| \\_/ \\___| |____/ \\__,_|\\___|_|\\_\\

                     ____
                    |  _ \\ __ _ ___ ___  ___ _ __
                    | |_) / _\` / __/ __|/ _ \\ '__|
                    |  __/ (_| \\__ \\__ \\  __/ |
                    |_|   \\__,_|___/___/\\___|_|


          ,   /\\   ,             |=|                     .-.
         / '-'  '-' \\           /   \\                   /  /
        |    NYPD    |         /     \\                 /. /
        \\    .--.    /        /       \\       )       /c\\/
         |  (9th )  |        |         |       (     /'\\/
         \\   '--'   /        | _______ |      )     /  /
          '--.  .--'         | Colt 45 |     (     /  /
              \\/             | ------- |      )   /  /
                             |  40 Oz  |       ( /. /
                             |         |       .\`.'.
                             |         |        \`'\`\`
                             |         |
                             |;;;;;;;;;|
`;

/*
 * Characters
 * */
const characters = [
  {
    name: "switchblade man",
    roomId: 'street',
    desc: 'Shlub with a shaky hand and a shakier grasp of whats healthy',
  },
  {
    name:'Bear',
    roomId:"hotel lobby",
    desc:`Trust fund animal. Yeah he sucks but his net worth is absurd. Problem is he wouldn't stop calling at dinner. Really his existance was the issue. If you're thinking one shouldn't speak ill of the dead, you clearly didn't know Bear. Also he's starting to smell.`
  },
  {
    name:'The Tire Hooker',
    roomId:"apartment window",
    desc:`Hooker eating a tire, looks like a Perelli.`
  },
  {
    name: 'Six Dollar Man',
    roomId: 'hotel 2A',
    desc:`Randy Savage except with a viciously failed wrestling career following a failed marriage. Weakness are his ex wife Sharron, alimony, and the IRS.`
    /*
     *
	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "I ain|t got time for this brother, you seen Sharron", "nextOpts" : []}}}', 0);
     * */
  },
  {
    name:'Old Lady',
    roomId:'hotel 2B',
    desc:`There is a significant chance that she will be eaten by her herds of cats.`
    /*
     *
	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "You want the old foot in the boot?", "nextOpts" : []}}}', 0);
     * */
  },
  {
    name:'Steve The Canadian',
    roomId:'hotel 2C',
    desc:`6'6\`\` caucasian male, claims to be from the praries, wherever the hell that is. Could be anywhere as you've never looked at a map. If you cared you be asking why he was carrying a Bowie knife and asking what we were planning on doing with the victim's \`hide\``
    /*'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Real shit hole ya got here bud. Worse mess than when my cousin Tom got in a tiffy with a moose in heat. If you need any help come talk to me in 1A, I`ll have a cold Molson waiting for ya.", "nextOpts" : []}}}', '{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Oh hey there bud, ya want a Molson?", "nextOpts" : []}}}', 0);
     *
     * */
  },
  {
    name:'JFK',
    roomId:'bodega',
    desc:`35th president of the United State of America, you know the guy. The way they reattached the bits of his head they managed to scrape off Jackie were unfortunately put together like a muppet. He now runs Tchotch Naught, a novelty store in north Any Town, USA. He's a moon landing 'truther' just like Charlie Rose... the schmuck.`
/*
	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "The moon landing was STTTAAAGGGEEEDDD", "nextOpts" : ["opt2"]}, "opt2" : {"ques" : "Who staged it?", "resp" : "Armstrong`s a fraaaauuuddd", "nextOpts" : []}}}',

	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "The flag was waving, the flag was WAVING!", "nextOpts" : []}}}', 0);
  */
  },
  {
    name:'Robot',
    roomId:'hotle lobby',
    desc:`Early Yahoo AI experiment. After learning everything it knows from the combined knowledge of Geocities, Myspace, tomagachis, and The Charlie Rose Show... the putz, he has been left unplugged and abandoned. The net of his knowledge has left him with the operating IQ of a mid 2000's Crunk rapper. Due a Nas CD left in his drive when unplugged he claims to understand 'the struggle' and knows 'the Bridge'. Thinks OE in plastic is bullshit, coincidentaly Charlie Roses favorite beverage, the narc.`
/*
	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "404: Robot not found", "nextOpts" : []}}}', 0);
  */
  },
  {
    name:'Joe',
    roomId:'hotel 7A',
    desc:`Bear's AA sponsor, had to constantly deal with bear`,
/*
	NULL, '{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "I|m not gonna say I|m glad hes dead, but we haven|t had to hear anymore Reel Big Fish...", "nextOpts" : []}}}', 0);
  */
  },
  {
    name:'Veterinarian',
    roomId:'hotel lobby',
    desc:`Battle fatigued veterinarian. He enjoys putting down animals a bit too much. 'You ever seen what piano wire will do to a pomeranians neck?`,
/*
	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Well, lost another patient", "nextOpts" : []}}}', 0);
  */
  },
  {
    name:'Derrick The Salesman',
    roomId:'hotel 4A',
    desc:`Don't buy a car from this guy`,
      /*
       *
	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Heeyyy muchacho, wanna buy a Pontiac?", "nextOpts" : []}}}', 0);
       * */
  },

  {
    name:'Guy Fieri',
    roomId:'hotel 3A',
    desc:`Oh dear god no`
    /*
     *
	NULL,'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "Welcome to Flavortown", "nextOpts" : []}}}', 0);
     * */
  },
  {
    name:'Hammer Guy',
    roomId:'Parking Lot',
    desc:`A complete animal by moral standards, but hey, there's a lot to this guy. He hangs out in fornt of the Home Depot waiting for people to hire him. He's a real ladies man in his thickly motor oil permeated suede duster and his burnt-out '82 Pontic Fiero. Denied access to all local fast food restaurant bathrooms.`
    /*
	'{"startOpts" : ["opt1"], "options" : {"opt1" : {"ques" : null, "resp" : "You seen my keys? My cars", "nextOpts" : []}}}', 0);
     * */
  },
];


/**
 * objects, list of none critical objects
 * **/
const objects = {
  "Beer Bottle": {
    name: ["beer", "bottle", "beer bottle"],
    desc: 'A full case of Schaefer bottles, three left.',
    isTakeable: true
    //onUse: () => {}
  },
  "Bears Corpse": {
    name: ["Bear's Corpse", "body", "bear", "corpse"],
    desc: `Trust fund animal. Yeah he sucks but his net worth is absurd. Problem is he wouldn't stop calling at dinner. Really his existance was the issue. If you're thinking one shouldn't speak ill of the dead, you clearly didn't know Bear. Also he's starting to smell.`,
    onUse: () => {
      println("Better leave that for someone else actually");
    },
    onInspect: () => {
      println("A cold stiff corpse of a poorly groomed Kodiak Grizzly");
    }
  },
  "Toilet":{
    name:["toilet", "throne", "john"],
    desc:`It's just a flowery plush arm chair with the seat cut out strategically placed over an empty can of Beefarino`,
    onUse: () => {
      println("You heave the can of beefarino out the window, no one notices, not even the alley cats or the hooker eating a tire");
    },
    inspect: "I guess it's a toilet"
  },
  "Magazine":{
    name:"Magazine",
    desc:`Dog eared copy of Better Homes and Gardens, the June, 1964 edition`,
    inspect:`You read the magazine as you have 700 times before. Maybe one day you'll try and make some of these improvements, but there you are with a can as your toilet.`
  },
  "Phone":{
    name: "Phone",
    desc:`The cord is hopelessly tangled, the reciever is partially clogged with beefarino. If anyone ever wanted to talk to you you'd have to get a new one. Of course they don't so here it is.`,
    inspect:`Your shitty beige couch`,
    use:`As you throw yourself gracelessly onto the greasy sofa what looks like a cockroach exodus complete with a cockroach Moses leading his people out of the sofa through the parting of the couch cushions begins. You have a quick nap in your natural habitat.`
/*
insert into objects values(0,3, 'Phone', "", 'Your home phone, you have a message','Messages', "Check your messages, do something for once.", "It's the Chief. 'Passer, there's been a murder down the street from you at the Kodiak Apartments. It sounds grizzly, go check it out. I want a report on my desk tomorrow, and it had better be good you layabout.'",203, 0);
*/
  },
  "Couch":{
    name:"Couch",
    desc:`It looks like it used to be suade before the layers of hair grease and cheap whiskey have left it in a state reminiscent of your soul.`,
    inspect:"Your shitty beige couch"
  }
};

const rooms = [
  {
    id:'start',
    name:'Filthy Street',
    desc: cut_scenes.street_intro_full.text + "\n type go **HOME** to head into your dump",
    exits: [
      {
        dir:'home',
        id:'home'
      }
    ]
  },
  {
    id:'home',
    name:'Home',
    desc:`Your apartment. You sit up on your bed with a comforter that used to be blue, and sheets that used to be white. A dim fluorescent light bulb hanging from it's cord oscillates in the middle of the room. A goldfish tank festers in the corner, that's a new smell. Just another damn day.`,
    items: [objects["Couch"], objects["Phone"]],
    exits: [
      {
        dir:'bathroom',
        id:'bathroom'
      },
      {
        dir:'kitchen',
        id:'kitchen'
      },
      {
        dir:'bed',
        id:'bed'
      },
      {
        dir:["apartment window", "window"],
        id:"apartment window"
      }
    ],
  },
  {
    id:'bathroom',
    name:'\"Bathroom\"',
    desc:`You shuffle to the corner of the room. Technically it's a bathroom, minus the bath... and the room. It's just a flowery plush arm chair with the seat cut out strategically placed over an empty can of Beefarino. There's a stack of Better Homes and Gardens magazines next to the can, what mess.`,
    items:[objects["toilet"], objects["magazine"]]
  },
  {
    id:'kitchen',
    name:'Kitchen',
    desc:`The kitchen, oh boy the kitchen. Stacks of Beefarino and a rusty can opener. It used to be your favorite spot to watch people on the street pass by, but the window was bricked over by the new expansion of the fancy feast cannery. The brick fails to dampen the smell`,
    exits: [
      {
        dir:'bathroom',
        id:'bathroom'
      },
      {
        dir:'kitchen',
        id:'kitchen'
      },
      {
        dir:'bed',
        id:'bed'
      },
      {
        dir:["apartment window", "window"],
        id:"apartment window"
      }
    ],
  },
  {
    id:'apartment window',
    name:['Apartment Window','window'],
    desc:`As you survey your neighborhood you realize it's the same as always. A sickening red glow from the Hustler sign douses the streets which are littered with emaciated alley cats drawn to the cannery. A hooker is eating a tire.`,
    exits: [
      {
        dir:'bathroom',
        id:'bathroom'
      },
      {
        dir:'kitchen',
        id:'kitchen'
      },
      {
        dir:'bed',
        id:'bed'
      },
      {
        dir:["apartment window", "window"],
        id:"apartment window"
      }
    ],
  },
  {
    id: 'rays',
    name: 'Ray\'s Pizza',
    desc: `The rats are the best patrons, it\'s probably a front. At least its open.`,
    exits: [
      {
        dir: 'south',
        id: 'start'
      },
    ],
  },
  {
    id: 'street',
    name: 'Filthy Street', // Displayed each time the player enters the room.
    desc: cut_scenes.street_intro.text, // Displayed when the player first enters the room.
    items: [
      {
        name: ["beer", "bottle", "beer bottle"],
        desc: 'A full case of Schaefer bottles, three left.',
        isTakeable: true,
        onUse: () => {
          // Remove the block on the room's only exit.
          const room = getRoom('start');
          const character = getCharacter("switchblade man");
          character.room = "";
          room.desc = "Same filthy street, last weeks \"Looking For Love\" section blows over the body to your left. Broken glass and the smell of cheap beer surround you. Your hands are sticky. You're out of beer.";
          const exit = getExit('rays', room.exits);

          if (exit.block) {
            delete exit.block;
            println(`As you finish smashing the bottle over the man's head everything comes back into focus, Ray's is open for another hour.`);
          } else {
            println(`Has that Milwaukee rust flavor you know so well`);
          }
        },
      },
      {
        name: ['Ray\'s Pizza Entrance', 'pizza', 'rays', 'restaurant'],
        desc: `Ray's Pizza, they're open for another hour`,
      },
    ],
    exits: [
      {
        dir: 'rays', // "dir" can be anything. If it's north, the player will type "go north" to get to the room called "A Forest Clearing".
        id: 'rays',
        block: `This guys interfering`,
      },
    ],
  },
];

const game_disk = {
  intro_screen: intro_screen,
  roomId: 'start', // Set this to the ID of the room you want the player to start in.
  characters: characters,
  rooms: rooms,
};
