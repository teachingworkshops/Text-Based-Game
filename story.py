"""
    Json file will add more code for no reason, content object will store description and dialogue.
"""

content = {
    "Jail": {
        "description": "You are sitting at a desk inside the jail, you see in front of you some papers in front of "
                       "you,"
                       "a revolver and a sheriff's badge.\n"
                       "You may want to review your papers with “info papers”\n" 
                       "To start, pickup your badge and gun using “pickup badge” and “pickup gun”.\n"
    },
    "Bank": {
        "description": "As you swing open the creaky Wild West bank doors, the once charming scene has turned "
                       "chaotic.\nDust particles dance in the sunlight that now reveals an armed delinquent, "
                       "their face hidden beneath a bandana, corralling frightened citizens.\nThe grizzled bank "
                       "teller, beads of sweat forming on his forehead, reluctantly assists the criminals.\nThe worn "
                       "wooden counters, now cluttered with overturned inkwells and scattered papers, bear the scars "
                       "of the sudden upheaval.\nThe vault door, usually a symbol of security, now looms ominously in "
                       "the background, a canvas for wanted posters flapping in the uneasy breeze.",
        "dialogue": "Sheriff: Halt! I see you there, you scoundrel. This is the law speakin\'"
                    "Bandit: Well, well, Sheriff McClane, look who stumbled into my little shindig. This wooden foot "
                    "of mine?\n"
                    "More stories than a campfire at dusk. Your move, Sheriff.\n"
                    "You've got two choices now.\n"
                    "Settle this the old fashioned way, with a gunfight.\n"
                    "Try to resolve this peacefully.\n",
        "info-citizens": "Citizen 1: (voice trembling) I never thought I'd see the day we'd be staring down the barrel" 
                         "of a bandit's gun, Pa.\n"
                         "Citizen 2: (nodding, eyes wide) Ain't nothin' scarier than the Wild West, son. Just thankful" 
                         "the sheriff showed up when he did.\n"
                         "Citizen 3: (gazing at the sheriff's badge) That badge ain't just silver; it's a beacon of" 
                         "salvation. We owe our lives to that lawman.\n",
        "info-banker": "Bank Teller: (breathing heavily) Look at him go, straight to the saloon! Guess he figures" 
                       "he can blend into the chaos there. \nIf he thinks he can hide in the saloon, he's in for a "
                       "surprise – the sheriff don't let trouble brew in his town for long.",
        "info-wanted poster": "The wanted poster prominently displays the elusive Bandit Joe Whisper, featuring a "
                              "distinctive touch with a wooden foot and the unusual flair of two monocles.\nBeneath the"
                              "stern proclamation of 'Dead or Alive' lies a laundry list of crimes, including bank "
                              "robbery and cattle rustling, enticing any \nbounty hunter with the promise of a $5,000 "
                              "reward. The artistic rendering captures the essence of an enigmatic outlaw, \ninviting "
                              "the vigilant to keep an eye out for this uniquely adorned ne'er-do-well in the vast "
                              "expanse of the Wild West."
    },

    "Desert Rose Saloon": {
        "description": "In Desert Rose Saloon, a lively Wild West establishment, weathered cowboys with sun-worn hats "
                       "and worn leather boots gather at scarred wooden tables. \nThe air is thick with laughter, the "
                       "clinking of glasses, and the occasional outburst of a poker game gone south. \nA motley "
                       "crew of patrons, each with a story etched into lines on their faces,\n find solace in the "
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
        "1": "Sheriff, my fashion crimes are in bad taste, not bank theft! You're looking for someone else.\n",
        "2": "Sheriff, I've been winning cards, not pulling heists! I swear it on my sombrero.\n",
        "4": "Sheriff, you got the wrong tune; I'm just here for a melody, not mischief, stammers the wiry" 
             "musician with the horseshoe-shaped guitar.\n",
        "5": "Sheriff, I've been stitching up folks, not robbing banks! You got the wrong patient.\n",
        "6": "Sheriff McClane, no need for handcuffs; I've been wrestling mechanical cattle, not robbing banks.\n",
        "7": "Sheriff, my presence is mysterious, not criminal. I'm just here for an enigmatic breeze.\n",
        "8": "Sheriff, I'm just sipping rainbow brews, not stirring up trouble. You've got the wrong drinker.\n",
        "3": "He is caught off guard as Sheriff McClane confronts him. He stumbles backward, wide-eyed and startled, "
             "managing to escape in a flurry, leaving the sheriff with only the lingering echo of hurried footsteps \n"
             "and a disappearing silhouette scampering toward the General Store.\n"
	         "Patron: Sheriff, I saw that Bandit feller high-tailin' it outta here like a scared rabbit. Take my "
             "shotgun, reckon you'll need it more than I do to bring that varmint to justice.\n"
             "Sheriff McClane: Much obliged, friend. You keep an eye on the saloon. I'll make sure Bandit's days of" 
             "dodging the law are over.\n"
    },
    "General Store": {
        "description": "Welcome to the Wagon Wheel Emporium, the beating heart of this dusty frontier town. The wooden"
                       " floor creaks beneath your boots as you step inside. \nSunlight filters through the worn "
                       "shutters, revealing shelves stocked with provisions – barrels of beans, sacks of flour, and "
                       "jars of preserves. \nThe grizzled store keeper is hidden behind the counter, avoiding the "
                       "brewing fight. You see the criminal around the corner, if you move forward, "
                       "the fight will begin."

    }

}