"""
    Json file will add more code for no reason, content object will store description and dialogue.
"""

content = {
    "Jail": {
        "description": "You are sitting at a desk inside the jail, "
                       "in front of you sits a 'Gun', and a sheriff's 'Badge' \n"
        # "You may want to review your papers with “info papers”\n" 
                       "You won't be able to get to the Bank until you finish up here.\n"
                       "To start, pick up your badge and gun using “Pick up Badge” and “Pick up Gun”. Type \"Help\""
                       " for a list of commands\n"
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
                    "of mine?\n"
                    "More stories than a campfire at dusk. Your move, Sheriff.\n \n"
                    "You've got two choices now:\n"
                    "Settle this the old fashioned way, with a gunfight.\n"
                    "Try to resolve this peacefully, you may not have the experience to beat him yet.\n",
        "dialogue_violent": "PLACEHOLDER_VIOLENT",
        "dialogue_peaceful": "PLACEHOLDER_PEACEFUL",

    },
    "Saloon": {
        "description": "In Desert Rose Saloon, a lively Wild West establishment, weathered cowboys with sun-worn hats "
                       "and worn leather boots gather at scarred wooden tables. \nThe air is thick with laughter, the "
                       "clinking of glasses, and the occasional outburst of a poker game gone south. \nA motley "
                       "crew of patrons, each with a story etched into lines on their faces, find solace in the "
                       "shared tales of adventure, heartbreak, and the promise of a fresh start in the rugged "
                       "frontier.\nIn this fine establishment you spot a nice bottle of whiskey. You probably "
                       "shouldn't take it.\n \n"
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
                       "serape, transforming the bar into a whimsical saloon for spirits and laughter.\n \n"
                       "You have one chance to approach the criminal without him escaping out one of the exits.\n"
                       "Which patron do you approach?\n"
                       "1,2,3,4,5,6,7,8?\n",
        "correct_guess": "PLACEHOLDER_CORRECT",
        "incorrect_guess": "PLACEHOLDER_INCORRECT",
    },
    "General Store": {
        "description": "PLACEHOLDER: GENERAL STORE DESCRIPTION",
    },

    "Help": {
        "commands": "PLACEHOLDER: LIST OF COMMANDS + DESCRIPTION",
    }

}
