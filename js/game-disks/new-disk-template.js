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

const cut_scenes = {
  street_intro: {
    text:`
    New York City, The Bowery, 1972. 9pm,
      There you are piss drunk, shuffling down the street on a Tuesday parting the rats, cockroaches, and old newspapers like Moses parting the red sea, that is if you count the people you're leading as the almost finished 18 pack of Schaefer in your hand and a lingering question of if you should chase the last one down with a bullet.
But there's no time to finally finish something, someone stops you in your path flashing a switchblade demanding money. You pause.`
  },
};

// This simple game disk can be used as a starting point to create a new adventure.
// Change anything you want, add new rooms, etc.
const demoDisk = {
  intro_screen: intro_screen,
  roomId: 'start', // Set this to the ID of the room you want the player to start in.
  rooms: [
    {
      id: 'start', // Unique identifier for this room. Entering a room will set the disk's roomId to this.
      name: 'Filthy Street', // Displayed each time the player enters the room.
      desc: cut_scenes.street_intro.text, // Displayed when the player first enters the room.
/*      items: [
        {
          name: 'door',
          desc: 'It leads NORTH.', // Displayed when the player looks at the item.
          onUse: () => println(`Type GO NORTH to try the door.`), // Called when the player uses the item.
        },
        {
          name: ['vines', 'vine'], // The player can refer to this item by either name. The game will use the first name.
          desc: `They grew over the DOOR, blocking it from being opened.`,
        },
        {
          name: 'axe',
          desc: `You could probably USE it to cut the VINES, unblocking the door.`,
          isTakeable: true, // Allows the player to take the item.
          onUse: () => {
            // Remove the block on the room's only exit.
            const room = getRoom('start');
            const exit = getExit('north', room.exits);

            if (exit.block) {
              delete exit.block;
              println(`You cut through the vines, unblocking the door to the NORTH.`);
            } else {
              println(`There is nothing to use the axe on.`);
            }
          },
        }
      ],
      exits: [
        {
          dir: 'north', // "dir" can be anything. If it's north, the player will type "go north" to get to the room called "A Forest Clearing".
          id: 'clearing',
          block: `The DOOR leading NORTH is overgrown with VINES.`, // If an exit has a block, the player will not be able to go that direction until the block is removed.
        },
      ],
    },
    {
      id: 'clearing',
      name: 'A Forest Clearing',
      desc: `It's a forest clearing. To the SOUTH is The First Room.`,
      exits: [
        {
          dir: 'south',
          id: 'start',
        },
      ],*/
    }
  ],
};
