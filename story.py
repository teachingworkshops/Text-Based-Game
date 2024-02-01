"""
    Json file will add more code for no reason, content object will store description and dialogue.
"""

content = {
    "Jail": {
        "description": "You are sitting at a desk inside the jail, you see in front of you some papers in front of "
                       "you,"
                       "a revolver and a sheriff's badge.\n"
                       "You may want to review your papers with “info papers”\n"
                       "To start, pickup your badge and revolver using “Pick up badge” and “Pick up revolver”.\n"
    },
    "Bank": {
        "description": "As you swing open the creaky Wild West bank doors, the once charming scene has turned "
                       "chaotic.\nDust particles dance in the sunlight that now reveals an armed delinquent, "
                       "their face hidden beneath a bandana, corralling frightened citizens.\nThe grizzled bank "
                       "teller, beads of sweat forming on his forehead, reluctantly assists the criminals.\nThe worn "
                       "wooden counters, now cluttered with overturned inkwells and scattered papers, bear the scars "
                       "of the sudden upheaval.\nThe vault door, usually a symbol of security, now looms ominously in "
                       "the background, a canvas for wanted posters flapping in the uneasy breeze.",
        "dialogue": "Sheriff: Halt! I see you there, you scoundrel. This is the law speakin\'\n"
                    "Bandit: Well, well, Sheriff McClane, look who stumbled into my little shindig. This wooden foot "
                    "of mine?"
                    "More stories than a campfire at dusk. Your move, Sheriff.\n"
                    "You've got two choices now.\n"
                    "Settle this the old fashioned way, with a gunfight.\n"
                    "Try to resolve this peacefully.\n",
        "dialogue_peaceful": "In a tense standoff, the sheriff, eyes steely and resolve unwavering, \n"
                             "positioned himself between the hostages and the bandit, \n"
                             "creating a makeshift shield of justice in the dimly lit bank. \n"
                             "Faced with an impossible choice, the sheriff, with a reluctant nod, \n"
                             "allowed the bandit a narrow escape route, prioritizing the safety of the hostages \n"
                             "over immediate capture. As the bandit vanished into the shadows, the sheriff, \n"
                             "haunted by the decision, ensured the hostages emerged unscathed, the weight of the \n"
                             "untamed frontier etched into the lines of his weathered face.",
    },
    "Saloon": {
        "description": "In Desert Rose Saloon, a lively Wild West establishment, weathered cowboys with sun-worn hats "
                       "and worn leather boots gather at scarred wooden tables. \nThe air is thick with laughter, the "
                       "clinking of glasses, and the occasional outburst of a poker game gone south. \nA motley "
                       "crew of patrons, each with a story etched into lines on their faces, find solace in the "
                       "shared tales of adventure, heartbreak, and the promise of a fresh start in the rugged "
                       "frontier.\n"
                       "1. A character in mismatched patterns and a hat made of tied bandanas nurses a mug of "
                       "sarsaparilla, spinning tales of chasing elusive tumbleweeds in the desert.\n"
                       "2. A sharpshooting cowgirl, wearing a sombrero adorned with rattlesnake tails and fringes, "
                       "flips a silver dollar before joining a poker game filled with inflatable cacti.\n"
                       "3. The brooding stranger at the corner table sports a top hat adorned with two monocles, a "
                       "duster coat covered in peculiar patches, and boasts a wooden foot that taps an unconventional "
                       "rhythm.\n"
                       "4. A wiry musician with a guitar shaped like a horseshoe, playing a tune on a harmonica around "
                       "his neck, fills the saloon with the eclectic sounds of a tumbleweed serenade.\n"
                       "5. The local sawbones, dressed in a lab coat with a sheriff's badge, leans against the bar, "
                       "sipping sarsaparilla from a mason jar while sharing tales of patching up cowboy mishaps in the"
                       " Old West.\n"
                       "6. A towering rancher, wearing a cowboy hat fashioned from a large pair of spurs, regales the "
                       "crowd with tales of herding mechanical cattle and breaking in robotic mustangs.\n"
                       "7. Shrouded in mystery, a figure with a veil and dark eyes, dons a wig made of twine and "
                       "feathers, wearing a cloak that billows in the wind like a desert dust storm.\n"
                       "8. The bartender, rocking a top hat made of leather patches, juggles bottles while wearing a "
                       "serape, transforming the bar into a whimsical saloon for spirits and laughter.\n"
                       "You have one chance to approach the criminal without him escaping out one of the exits.\n"
                       "Which patron do you approach?\n"
                       "1,2,3,4,5,6,7,8?\n",
        "correct_guess": "He is caught off guard as Sheriff McClane confronts him. He stumbles backward, wide-eyed and"
                         "startled, managing to escape in a flurry, leaving the sheriff with only the \nlingering echo "
                         "of hurried footsteps and a disappearing silhouette scampering toward the General Store.\n"
                         "Patron: Sheriff, I saw that Bandit feller high-tailin' it outta here like a scared rabbit. "
                         "Take my shotgun; reckon you'll need it more than I do to bring that varmint to justice.\n"
                         "Sheriff McClane: Much obliged, friend. You keep an eye on the saloon. I'll make sure Bandit's"
                         " days of dodging the law are over.\n",
        "incorrect_guess1": "’Sheriff, you got the wrong tune; I'm just here for a melody, not mischief,’\n "
                            "stammers the wiry musician with the horseshoe-shaped guitar.",
        "incorrect_guess2": "Sheriff, I've been stitching up folks, not robbing banks! You got the wrong patient.",
        "incorrect_guess3": "Sheriff, I've been winning cards, not pulling heists! I swear it on my sombrero.",
        "incorrect_guess4": "Sheriff McClane, no need for handcuffs; I've been wrestling mechanical cattle, \n"
                            "not robbing banks.",
        "incorrect_guess5": "Sheriff, I'm just here for the shadows, not the outlaws.",
        "incorrect_guess6": "Sheriff, I've been chasing tumbleweeds, not running from the law. \n"
                            "You're barking up the wrong desert.",
        "incorrect_guess7": "Sheriff, my circus is all about laughs, not larceny. You've got the wrong ringmaster.",
        "incorrect_guess8": "Sheriff, my fashion crimes are in bad taste, not bank theft! \n"
                            "You're looking for someone else.",
        "incorrect_guess9": "Sheriff, my only crime is questionable fashion, not robbing banks. \n"
                            "I'm just a patchwork cowboy.",
        "incorrect_guess10": "Sheriff, I'm just sipping rainbow brews, not stirring up trouble. \n"
                             "You've got the wrong drinker.",
        "incorrect_guess11": "Sheriff, my presence is mysterious, not criminal. I'm just here for an enigmatic breeze.",
        "incorrect_guess12": "Sheriff, I'm just a card-playing cowboy, not a bank-robbing bandit. \n"
                             "You're wrangling the wrong snake.",
        "bartender-tip": ""
        ,
    },
    "General Store": {
        "description": "Welcome to the Wagon Wheel Emporium, the beating heart of this dusty frontier town. The wooden"
                       " floor creaks beneath your boots as you step inside. \nSunlight filters through the worn "
                       "shutters, revealing shelves stocked with provisions – barrels of beans, sacks of flour, and "
                       "jars of preserves. \nThe grizzled store keeper is hidden behind the counter, avoiding the "
                       "brewing fight. You see the criminal around the corner, if you enter \'Y\', "
                       "the fight will begin."

    },
    "Items": {
        "badge": "A gleaming silver sheriff's badge, adorned with intricate engravings,\n "
                 "its star-shaped design symbolizing authority and justice. It fills you with encouragement. +1 xp",
        "revolver": "A weathered, nickel-plated six-shooter with ivory grips, its barrel marked by the scars of \n"
                    "countless showdowns, epitomizing the gritty resilience of the Wild West. +1 xp",

        "papers": "Move [LOCATION]: move to that place\n"
                  "Info [PERSON/ITEM]: start a dialogue or get a description of an item\n"
                  "Inventory: Look at what items you have on you\n"
                  "List items in Room: Look at what items are available in the room have\n"
                  "List connections: Look at what places you can \"Move\" to\n"
                  "Pick up [ITEM]: Add that item to your inventory\n"
                  "Where am I?: Displays what room the sheriff is currently in\n"
                  "Help: Display a list of the commands available\n",

        "hostages": "Citizen 1: (voice trembling) I never thought I'd see the day we'd be staring down the barrel"
                    "of a bandit's gun, Pa.\n"
                    "Citizen 2: (nodding, eyes wide) Ain't nothin' scarier than the Wild West, son. Just thankful"
                    "the sheriff showed up when he did.\n"
                    "Citizen 3: (gazing at the sheriff's badge) That badge ain't just silver; it's a beacon of"
                    "salvation. We owe our lives to that lawman.\n",
        "banker": "Bank Teller: (breathing heavily) Look at him go, straight to the saloon! Guess he figures"
                  "he can blend into the chaos there. \nIf he thinks he can hide in the saloon, he's in for a "
                  "surprise – the sheriff don't let trouble brew in his town for long.",
        "wanted-poster": "The wanted poster prominently displays the elusive Bandit Joe Whisper, featuring a "
                         "distinctive touch with a wooden foot and the unusual flair of two monocles.\nBeneath the"
                         "stern proclamation of 'Dead or Alive' lies a laundry list of crimes, including bank "
                         "robbery and cattle rustling, enticing any \nbounty hunter with the promise of a $5,000 "
                         "reward. The artistic rendering captures the essence of an enigmatic outlaw, \ninviting "
                         "the vigilant to keep an eye out for this uniquely adorned ne'er-do-well in the vast "
                         "expanse of the Wild West.",
        "correct-patron1": "Well, I'll be hornswoggled, Sheriff! \n"
                           "You nailed that Bandit right on the money — reckon you've got a nose for justice.",
        "correct-patron2": "Sheriff McClane, you're a true sharpshooter of the law; \n"
                           "Whisper won't be whisperin' his way outta this one.",
        "correct-patron3": "Shoot, Sheriff, you had us worried there, \n"
                           "but you tracked that Bandit like a bloodhound on a fresh trail.",
        "correct-patron4": "Looks like the sheriff roped in the right outlaw; \n"
                           "that Bandit won't be causin' any more ruckus 'round these parts.",
        "correct-patron5": "Sheriff, you sure roped in the right steer with that Bandit; \n"
                           "reckon the jailhouse is awaitin' his tall tales now.",
        "correct-patron6": "Well, slap me with a cactus! \n"
                           "You corralled that Bandit faster than a tumbleweed in a dust storm, Sheriff.",
        "correct-patron7": "Sheriff McClane, you're quicker on the draw than a sidewinder, \n"
                           "and that Bandit learned it the hard way.",
        "correct-patron8": "I was wonderin' when you'd show that Bandit the long arm of the law, \n"
                           "Sheriff — reckon you had it all figured out.",
        "correct-patron9": "Sheriff, you called that Bandit's bluff like a seasoned poker player; \n"
                           "he ain't gamblin' with the law anymore.",
        "correct-patron10": "Well, I'll be a lonesome cowboy; you snared that Bandit like a wild stallion, \n"
                            "Sheriff, and no one's sheddin' tears for his escape.",
        "correct-patron11": "Sheriff, you tracked down that Bandit quicker than a prairie fire, \n"
                            "and now justice is burnin' hot on his trail.",
        "correct-patron12": "Looks like the Sheriff's intuition is sharper than a branding iron; \n"
                            "that Bandit won't be rustlin' trouble no more.",

        "incorrect-patron1": "Dagnabbit, Sheriff, you might need a new pair of spectacles; \n"
                             "that Bandit just slipped through your fingers like sand through a sieve.",
        "incorrect-patron2": "Sheriff McClane, seems like you were chasin' shadows instead of the real Bandit — \n"
                             "he's probably halfway to the next county by now.",
        "incorrect-patron3": "Well, I reckon the Sheriff's guessin' skills are rustier than an abandoned wagon;\n"
                             " that Bandit just gave us the slip.",
        "incorrect-patron4": "Sheriff, you might need a tracker instead of a lawman; \n"
                             "that Bandit's ghostin' through the prairie while you're guessin' in the dark.",
        "incorrect-patron5": "Looks like the Sheriff's instincts were as dry as a creek bed; \n"
                             "that Bandit's probably enjoyin' a drink in the next town by now.",
        "incorrect-patron6": "Sheriff McClane, you might need a map to go with that badge; \n"
                             "that Bandit just rode off into the sunset, and you're left in the dust.",
        "incorrect-patron7": "Sheriff, your hunches might need a tune-up; \n"
                             "that Bandit's probably laughin' in some hideout while you're guessin' at shadows.",
        "incorrect-patron8": "Well, slap me with a saguaro cactus! \n"
                             "Sheriff, your guessin' game was off, and that Bandit's skippin' town faster than a \n"
                             "jackrabbit.",
        "incorrect-patron9": "Sheriff, seems like your aim was as shaky as a tumbleweed; \n"
                             "that Bandit vanished like smoke in the wind.",
        "incorrect-patron10": "I reckon the Sheriff's instincts were as lost as a tumbleweed rollin' in the breeze; \n"
                              "that Bandit's probably halfway to the border by now.",
        "incorrect-patron11": "Sheriff McClane, your guess might've been as wild as a mustang; \n"
                              "that Bandit's probably rustlin' trouble somewhere far from here.",
        "incorrect-patron12": "Looks like the Sheriff's badge ain't a compass; \n"
                              "that Bandit made a clean getaway while you were guessin' his trail.",
        "shotgun": "The old western shotgun, worn and weathered, boasts a double-barreled menace, \n"
                   "its stock bearing the scars of countless showdowns, \n"
                   "embodying the rugged reliability of the Wild West frontier.",
        "bartender": "Sheriff, that Bandit fella slipped through quicker than a snake in the grass. \n"
                     "I'd bet he's takin shelter in the Wagon Wheel Emporium, the Store. Check there"

    },
    "Help": {
        "commands": "Move [LOCATION]: move to that place\n"
                    "Info [PERSON/ITEM]: start a dialogue or get a description of an item\n"
                    "Inventory: Look at what items you have on you\n"
                    "List items in Room: Look at what items are available in the room have\n"
                    "List connections: Look at what places you can \"Move\" to\n"
                    "Pick up[ITEM]: Add that item to your inventory\n"
                    "Where am I?: Displays what room the sheriff is currently in\n"
                    "Help: Display a list of the commands available\n",
    },
    "Battle": {
        "ouchie!": "Grimacing through pain, you hastily bandage the gunshot wound in your leg, \n"
                   "crafting a crude splint from nearby branches. With steely determination, you hobble forward, \n"
                   "catching a fleeting glimpse of the bandit slipping into the saloon, the pursuit persisting on the\n"
                   "unforgiving trail of the Wild West. The people of the bank will remember this (-50 honor).",
        "standoff": "Both the bandit and you are locked in an unspoken standoff, fingers hovering over their holsters.\n"
                    "The quiet before the storm, where the weight of justice and the allure of escape held the air, \n"
                    "the piercing gaze between them echoing the imminent clash in the Wild West.",
        "bandit-die": "Amidst the noonday silence, gunfire erupted, the sheriff's bullet finding its mark \n"
                      "and ending the bandit's desperate escape in a cloud of swirling dust. \n"
                      "The fallen outlaw, framed by the unforgiving frontier, became a testament to justice served \n"
                      "in the piercing echo of the Wild West's relentless dance.",
    },
    "End_Text": {
        "win": "PLACEHOLDER: WIN",
        "lose": "PLACEHOLDER: LOSE",
    }

}
