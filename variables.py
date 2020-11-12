from kivy.core.window import Window

# App window
Window.clearcolor = (0.9, 0.9, 0.9, 1)
Window.size = (288, 640)

# Limit the amount of entries produced for speed
entry_limit = 20  # max pokemon available so far
max_entries = min(386, entry_limit)  # If the number is larger than available, pick max

searchbar_offset = {'20': 0.002,
                    '386': 0.0012477825674206}

# Types color codes
color_codes = {'normal': (0.659, 0.659, 0.471, 1),
               'fire': (0.941, 0.502, 0.188, 1),
               'fighting': (0.753, 0.188, 0.157, 1),
               'water': (0.408, 0.565, 0.941, 1),
               'flying': (0.659, 0.565, 0.941, 1),
               'grass': (0.471, 0.784, 0.314, 1),
               'poison': (0.627, 0.251, 0.627, 1),
               'electric': (0.973, 0.816, 0.188, 1),
               'ground': (0.878, 0.753, 0.408, 1),
               'psychic': (0.973, 0.345, 0.533, 1),
               'rock': (0.722, 0.627, 0.22, 1),
               'ice': (0.596, 0.847, 0.847, 1),
               'bug': (0.659, 0.722, 0.125, 1),
               'dragon': (0.439, 0.22, 0.973, 1),
               'ghost': (0.439, 0.345, 0.596, 1),
               'dark': (0.439, 0.345, 0.282, 1),
               'steel': (0.722, 0.722, 0.816, 1),
               'fairy': (0.933, 0.6, 0.675, 1),
               '???': (0.408, 0.627, 0.565, 1),
               '': (0, 0, 0, 0)
               }

# List of Mystery Dungeon Abilities and their effects
md_abilities = {
                'Aftermath': 'When this Pokémon is defeated a small explosion occurs.',
                'Air Lock': 'When this Pokémon enters the floor and every 36 turns thereafter, the weather becomes Clear.',
                'Anger Point': 'When this Pokémon is struck by a critical hit, its Attack and Sp. Atk. are boosted to the maximum stage.',
                'Anticipation': 'Effectively useless.',
                'Arena Trap': 'When another Pokémon deals damage to the wielder, if the attacker isn\'t immune to Ground moves, they may become immobilized (12% chance).',
                'Bad Dreams': 'Pokémon in the vicinity of the wielder, when they\'re asleep, suffer damage every turn.',
                'Battle Armor': 'The wielder of this ability will never suffer a critical hit.',
                'Blaze': 'When this Pokémon falls under 25% HP, the power of the Pokémon\'s Fire-type moves doubles.',
                'Chlorophyll': 'When it is Sunny, after the wielder of this ability attacks, it will use the same attack a second time. No extra PP is consumed. If the move is linked the entire link is still triggered.',
                'Clear Body': 'This Pokémon\'s stats cannot be lowered by its opponents.',
                'Cloud Nine': 'When this Pokémon enters the floor and every 36 turns thereafter, the weather becomes Clear.',
                'Color Change': 'When this Pokémon is attacked, it will adapt the type of the attack used against it provided the move deals any damage.',
                'Compound Eyes': 'This Pokémon has a permanent boost of two stages to its Accuracy.',
                'Cute Charm': 'When this Pokémon suffers from a physical attack that deals damage, there is a 12% chance that the attacker will become infatuated.',
                'Damp': 'Explosions cannot occur while this Pokémon is on the floor.',
                'Download': 'When this Pokémon attacks, it will boost its Attack by one stage if the foe has lower Defense than Sp. Def., and boost its Sp. Atk. instead in the opposite case.',
                'Drizzle': 'When this Pokémon enters the floor and every 36 turns thereafter, the weather becomes Rain.',
                'Drought': 'When this Pokémon enters the floor and every 36 turns thereafter, the weather becomes Sunny.',
                'Early Bird': 'This Pokémon wakes up faster than normal from sleeping statuses.',
                'Effect Spore': 'When this Pokémon is struck by a physical move and suffers damage, it has a 12% chance to paralyze, poison, or put the attacker to sleep.',
                'Filter': 'This Pokémon takes 3/4 of the normal damage from super-effective moves.',
                'Flame Body': 'When this Pokémon is struck by another and suffers damage, the attackerh as a 12% chance to become burned.',
                'Flash Fire': 'This Pokémon is immune to all Fire-type moves. When suffering a Fire attack, further, the wielder will raise one stage, up to two total boosts from Flash Fire, in its Sp. Atk. stat.',
                'Flower Gift': 'When this Pokémon attacks during Sunny weather, it has an Attack stage boost of one. If this Pokémon or an ally is attacked during Sunny weather, their Sp. Def. is boosted by one stage even if the attacker wields Mold Breaker.',
                'Forecast': 'This Pokémon changes type depending on the weather on the floor: Rain and Fog yield Water, Sunny yields Fire, Hail and Snow yield Ice, Clear and Cloudy yield Normal, and Sandstorm yields Ground.',
                'Forewarn': 'Effectively useless.',
                'Frisk': 'Effectively useless.',
                'Guts': 'If this Pokémon is burned, paralyzed, or poisoned, then its Attack stat is doubled. (The Burn stat drop is ignored.)',
                'Huge Power': 'When this Pokémon attacks, there\'s a 33% chance that it will deal 50% extra damage.',
                'Hustle': 'This Pokémon has its Attack stat raised by 50% during damage calculation. However, at the same time, the foe is considered to have an Evasion stat two stages higher than it currently is during accuracy calculation for physical moves.',
                'Hydration': 'This Pokémon cures its status problems when it is Raining.',
                'Hyper Cutter': 'This Pokémon will never have its Attack lowered by opponents\' move or Ability effects.',
                'Illuminate': 'When this Pokémon suffers damage, a wild Pokémon appears on the floor off-screen if less than 10 foes are on the floor. Losing this Ability by any means will not nullify its effect. This Ability is nullified on boss floors.',
                'Immunity': 'This Pokémon cannot become poisoned or badly poisoned.',
                'Inner Focus': 'This Pokémon cannot be made to cringe.',
                'Insomnia': 'This Pokémon will never fall asleep, nap, yawn, or have a nightmare.',
                'Intimidate': 'Physical attackers deal 80% their normal amount of damage against this Pokémon.',
                'Keen Eye': 'Opposing Pokémon cannot lower this Pokémon\'s accuracy.',
                'Levitate': 'This Pokémon becomes immune to Ground type moves.',
                'Lightning Rod': 'When an Electric-type move is used in the same room as the wielder of this Ability, the attack is negated and the wielder gets a one stage boost in Sp. Atk.',
                'Limber': 'This Pokémon is immune to paralysis.',
                'Liquid Ooze': 'If this Pokémon is struct by an effect that drains HP from the target for recovery, the Pokémon draining HP will actually be damaged by the amount they\'d normally recover.',
                'Magma Armor': 'This Pokémon cannot become frozen.',
                'Magnet Pull': 'If a Steel-type Pokémon deals damage to the wielder of this ability, then they have a 12% chance to become immobilized.',
                'Marvel Scale': 'When this Pokémon has a status ailment, its Defense stat is 50% higher.',
                'Minus': 'If this Pokémon has an ally on the floor with the Plus ability, this Pokémon\'s Sp. Atk. is boosted by 50%.',
                'Natural Cure': 'This Pokémon\'s status ailments will last less time and recover naturally if they wouldn\'t normally, lasting at maximum five turns.',
                'Oblivious': 'This Pokémon is unable to become infatuated.',
                'Overgrow': 'Whenever this Pokémon falls under 25% HP, its Grass moves will deal double damage.',
                'Own Tempo': 'This Pokémon cannot become confused.',
                'Pickup': 'When this Pokémon enters a floor, provided it is not holding any item, it will pick up an item. (This item will not be monetary in nature.)',
                'Plus': 'If this Pokémon has an ally on the floor with the Minus ability, this Pokémon\'s Sp. Atk. is boosted by 50%.',
                'Poison Point': 'When this Pokémon suffers damage from another Pokémon, there is a 12% chance that the attacker will become poisoned.',
                'Pressure': 'When this Pokémon is attacked, the attacker consumes one more PP than normal.  This does not stack, i.e. if attacking three Pressure Pokémon two PP not four is lost. Two-turn attacks are immune to this, and Pressure activates regardless of the move dealing damage.',
                'Pure Power': 'When this Pokémon attacks, there\'s a 33% chance that it will deal 50% extra damage.',
                'Rain Dish': 'This Pokémon recovers its HP faster than normal during Rainy weather.',
                'Rivalry': 'When fighting Pokémon of the same gender, this Pokémon deals extra damage (one stage extra for Attack); against Pokémon of the opposite gender, less damage. Genderless Pokémon and targets are exempt.',
                'Rock Head': 'This Pokémon suffers no damage from recoil moves like Double-Edge and Flare Blitz.',
                'Rough Skin': 'When this Pokémon suffers damage from another Pokémon, the attacker will lose HP equal to half the damage dealt.',
                'Run Away': 'When this Pokémon has less than 50% HP, provided it is not the team leader, it becomes Terrified.',
                'Sand Stream': 'When this Pokémon enters the floor and every 36 turns thereafter, the weather becomes Sandstorm.',
                'Sand Veil': 'During Sandstorms, this Pokémon will have an automatic boost in Evasion of two stages.',
                'Scrappy': 'Wielders of this Ability can hit Ghost Pokémon with Normal- and Fighting-type moves.',
                'Serene Grace': 'Moves used by this Pokémon have an extra chance to dole out any of their extra effects.',
                'Shadow Tag': 'When another Pokémon damages the wielder of this ability, the attacker has a 12% chance to become immobilized.',
                'Shed Skin': 'At the end of this Pokémon\'s turn, it has a 50% chance to heal all of its status problems.',
                'Shell Armor': 'This Pokémon cannot suffer the effects of a critical hit.',
                'Shield Dust': 'The additional effects of damaging moves (but not the status effects of Status-class moves like Thunder Wave\'s paralysis) will not affect this Pokémon.',
                'Simple': 'Stat change modifications to this Pokémon are doubled in their magnitude - both in terms of increments and decrements.',
                'Solar Power': 'When this Pokémon attacks during Sunny weather, it has an Attack stage boost of one. The Pokémon also loses some HP on attacking.',
                'Solid Rock': 'This Pokémon takes 3/4 of the normal damage from super-effective moves.',
                'Soundproof': 'Sound based moves do not affect this Pokémon.',
                'Speed Boost': 'Every 250 turns the wielder of this Ability spends on the floor, their movement speed will become raised by one stage.',
                'Static': 'Whenever another Pokémon attacks the wielder of this Ability, the attacker has a 12% chance to become paralyzed.',
                'Steadfast': 'If this Pokémon cringes, it will have its movement speed boosted by one stage.',
                'Stench': 'When another Pokémon deals damage to this Pokémon, the attacker has a 12% chance to become Terrified.',
                'Sticky Hold': 'This Pokémon will not let go of held items, even if a trap tries to remove it or a move like Knock Off tries to remove it.',
                'Storm Drain': 'When a Water-type move is used in the same room as the wielder of this Ability, the attack is negated and the wielder gets a one stage boost in Sp. Atk.',
                'Sturdy': 'This Pokémon will always survive OHKO attacks with 1 HP, provided it has full HP.',
                'Suction Cups': 'This Pokémon will not be able to be thrown wildly by means such as Whirlwind, Roar, Vital Throw, etc. They also nullify warp effects, such as traps and Baton Pass.',
                'Super Luck': 'This Pokémon is more likely to deal critical hits.',
                'Swarm': 'When this Pokémon falls under 25% HP, the power of the Pokémon\'s Bug-type moves doubles.',
                'Swift Swim': 'When it is Rainy, after the wielder of this ability attacks, it will use the same attack a second time. No extra PP is consumed. If the move is linked the entire link is still triggered.',
                'Synchronize': 'Whenever this Pokémon suffers the effects of burns, poisoning, bad poisoning, or paralysis, all its enemies within one tile contract the ailment. Synchronize can chain activate from those foes as well.',
                'Tangled Feet': 'When this Pokémon is confused, its evasion is boosted two stages.',
                'Thick Fat': 'This ability will halve the damage the wielder of this Ability suffers.',
                'Tinted Lens': 'This Pokémon deals 50% extra damage when attacking a Pokémon and dealing not-very-effective damage.',
                'Torrent': 'If this Pokémon has less than 25% HP, then its Water moves deal double damage.',
                'Trace': 'When the wielder of this Pokémon suffers damage from another Pokémon, the wielder of this Ability will copy one of their attacker\'s Abilities and replace this with it.',
                'Truant': 'When this Pokémon uses a move or an Orb, it will become Paused at the end of the turn.',
                'Unaware': 'This Pokémon ignores all stat modifiers on itself and the target for all calculations: positive or negative.',
                'Unburden': 'When this Pokémon loses its hold item its movement speed increases.',
                'Vital Spirit': 'This Pokémon cannot fall asleep, nor be yawning, napping, or having a nightmare.',
                'Volt Absorb': 'If an Electric attack is dealt to this Pokémon, it will be healed, instead of damaged, by the amount of damage it would\'ve dealt otherwise.',
                'Water Absorb': 'If a Water attack is dealt to this Pokémon, it will be healed, instead of damaged, by the amount of damage it would\'ve dealt otherwise.',
                'Water Veil': 'This Pokémon cannot become burned.',
                'White Smoke': 'This Pokémon cannot have its stats lowered by its opponents.',
                'Wonder Guard': 'Only moves which hit this Pokémon super-effectively may be used against it. Typeless moves also deal damage, which includes thrown items.'
}

# IQ String
iq_string = '\n\n'\
            '•1 star: 0-9\n' \
            '•2 stars: 10-49\n' \
            '•3 stars: 50-99\n' \
            '•4 stars: 100-149\n' \
            '•5 stars: 150-199\n' \
            '•6 stars: 200-299\n' \
            '•7 stars: 300-399\n' \
            '•8 stars: 400-499\n' \
            '•9 stars: 500-599\n' \
            '•10 stars: 600-699\n' \
            '•11 stars: 700-989\n' \
            '•MAX: 990 or more (IQ can reach up to 999)\n'

# Dictionary of all evolution items and their descriptions / locations
evo_item_dict = {
                 'Water Stone': '[size=16][color=000011]Location:[/color][/size]\n'
                                '• [u]Northwind Field[/u]\n'
                                '- 29F\n\n'
                                '[size=16]Pokémon[/size]\n'
                                '#061 Poliwhirl -> #062 Poliwrath\n'
                                '#090 Shellder -> #091 Cloyster\n'
                                '#120 Staryu -> #121 Starmie\n'
                                '#133 Eevee -> #134 Vaporeon\n'
                                '#271 Lombre -> #272 Ludicolo',
                 'Thunder Stone': '[size=16][color=000011]Location:[/color][/size]\n'
                                  '• [u]Lightning Field[/u]\n'
                                  '- 29F\n\n'
                                  '[size=16]Pokémon[/size]\n'
                                  '#025 Pikachu -> #026 Raichu\n'
                                  '#133 Eevee -> #135 Jolteon',
                 'Fire Stone': '[size=16][color=000011]Location:[/color][/size]\n'
                               '• [u]Fiery Field[/u]\n'
                               '- 29F\n\n'
                               '[size=16]Pokémon[/size]\n'
                               '#037 Vulpix -> #038 Ninetales\n'
                               '#058 Growlithe -> #059 Arcanine\n'
                               '#133 Eevee -> #136 Flareon',
                 'Leaf Stone': '[size=16][color=000011]Location:[/color][/size]\n'
                               '• [u]Wish Cave[/u] (Kecleon Shop, 3000 gold)\n'
                               '- 13F, 26F, 33F, 41F, 49F, 59F\n'
                               '- 65F, 71F, 78F, 83F, 88F, 93F\n\n'
                               '[size=16]Pokémon[/size]\n'
                               '#044 Gloom -> #045 Vileplume\n'
                               '#070 Weepinbell -> #071 Victreebel\n'
                               '#102 Exeggcute -> #103 Exeggutor\n'
                               '#274 Nuzleaf -> #275 Shiftry',
                 'Moon Stone': '[size=16][color=000011]Location:[/color][/size]\n'
                               '• [u]Solar Cave[/u]\n'
                               '- 1F-20F\n'
                               '• [u]Wish Cave[/u] (Kecleon Shop, 3000 gold)\n'
                               '- 13F, 26F, 33F, 41F, 49F, 59F\n'
                               '- 65F, 71F, 78F, 83F, 88F, 93F\n\n'
                               '[size=16]Pokémon:[/size]\n'
                               '#030 Nidorina -> #031 Nidoqueen\n'
                               '#033 Nidorino -> #034 Nidoking\n'
                               '#035 Clefairy -> #036 Clefable\n'
                               '#039 Jigglypuff -> #040 Wigglytuff\n'
                               '#300 Skitty -> #301 Delcatty',
                 'Sun Stone': '[size=16][color=000011]Location:[/color][/size]\n'
                              '• [u]Solar Cave[/u]\n'
                              '- 1F-20F\n\n'
                              '[size=16]Pokémon[/size]\n'
                              '#044 Gloom - #182 Bellossom\n'
                              '#191 Sunkern - #192 Sunflora',
                 'Link Cable': '[size=16][color=000011]Location:[/color][/size]\n'
                               'Note: All locations require the replaced item to be in the Toolbox or in Kangaskhan Storage\n\n'
                               '• [u]Northwind Field[/u]\n'
                               '- 20F (Replaces Lunar Ribbon, Requires Key)\n'
                               '• [u]Mt. Faraway[/u]\n'
                               '- 30F (Replaces Friend Bow, Requires Key)\n'
                               '• [u]Western Cave[/u]\n'
                               '- 59F (Replaces Beauty Scarf, Requires Key)\n'
                               '• [u]Buried Relic[/u]\n'
                               '- 45F (Replaces HM06 Rock Smash, Requires Key)\n'
                               '- 60F (Replaces HM04 Strength, Requires removing/crossing walls)\n'
                               '- 70F (Replaces HM05 Flash, Requires Key)\n'
                               '- 80F (Replaces HM02 Cut, Requires key, removing/crossing walls and crossing water)\n'
                               '• [u]Wish Cave[/u]\n'
                               '- 50F (Replaces Wish Stone)\n'
                               '• [u]Wyvern Hill[/u]\n'
                               '- 20F (Replaces Sun Ribbon, Requires Key)\n'
                               '- 30F (Replaces HM02 Fly, Requires Key)\n'
                               '• [u]Solar Cave[/u]\n'
                               '- 10F (Replaces HM08 Dive, Requires Key and crossing water\n'
                               '- 15F (Replaces HM07 Waterfall, Requires Key)\n'
                               '- 20F (Replaces HM03 Surf, Requires crossing water\n'
                               '• [u]Grand Sea[/u]\n'
                               '- 15F (Replaces Deepseatooth, Requires crossing water)\n'
                               '- 25F (Replaces Deepseascale, Requires crossing water)\n'
                               '• [u]Far-off Sea[/u]\n'
                               '- 50F (Replaces DM01 Wide Slash, Requires Key)\n'
                               '- 72F (Replaces DM02 Vacuum-Cut, Requires Key)\n\n'
                               '[size=16]Pokémon[/size]\n'
                               '#064 Kadabra -> #065 Alakazam\n'
                               '#067 Machoke -> #068 Machamp\n'
                               '#075 Graveler -> #076 Golem\n'
                               '#093 Haunter -> #094 Gengar\n\n'
                               '#061 Poliwhirl -> #186 Poliwhirl (With King\'s Rock)\n'
                               '#079 Slowpoke -> #199 Slowking (With King\'s Rock)\n'
                               '#095 Onix -> #208 Steelix (With Metal Coat)\n'
                               '#117 Seadra -> #230 Kingdra (With Dragon Scale)\n'
                               '#123 Scyther -> #212 Scizor (With Metal Coat)\n'
                               '#137 Porygon -> #233 Porygon2 (With Upgrade)\n'
                               '#366 Clamperl -> #367 Huntail (With Deepseatooth)\n'
                               '#366 Clamperl -> #368 Gorebyss (With Deepseascale)',
                 'Metal Coat': '[size=16][color=000011]Location:[/color][/size]\n'
                               '• [u]Southern Cave[/u]\n'
                               '- 49F-50F\n\n'
                               '[size=16]Pokémon[/size]\n'
                               '#095 Onix - #208 Steelix (With Link Cable)\n'
                               '#123 Scyther - #212 Scizor (With Link Cable)',
                 'King\'s Rock': '[size=16][color=000011]Location:[/color][/size]\n'
                                 '• [u]Wish Cave[/u] (Kecleon Shop, 3000 gold)\n'
                                 '- 13F, 26F, 33F, 41F, 49F, 59F\n'
                                 '- 65F, 71F, 78F, 83F, 88F, 93F\n\n'
                                 '[size=16]Pokémon[/size]\n'
                                 '#061 Poliwhirl -> #186 Poliwhirl (With Link Cable)\n'
                                 '#079 Slowpoke -> #199 Slowking (With Link Cable)',
                 'Dragon Scale': '[size=16][color=000011]Location:[/color][/size]\n'
                                 '• [u]Wyvern Hill[/u]\n'
                                 '- 29F-30F\n\n'
                                 '[size=16]Pokémon[/size]\n'
                                 '#117 Seadra -> #230 Kingdra (With Link Cable)',
                 'Upgrade': '[size=16][color=000011]Location:[/color][/size]\n'
                            '• [u]Wish Cave[/u] (Kecleon Shop, 3000 gold)\n'
                            '- 88F, 93F\n\n'
                            '[size=16]Pokémon[/size]\n'
                            '#137 Porygon -> #233 Porygon2 (With Link Cable)\n',
                 'Deepseatooth': '[size=16][color=000011]Location:[/color][/size]\n'
                                 '• [u]Grand Sea[/u]\n'
                                 '- 25F'
                                 '- Replaced with a Link Cable if any Deepseatooth is present in the Toolbox or in Kangaskhan Storage\n'
                                 '• [u]Far-Off Sea[/u]\n'
                                 '- 51F-75F (Even when a Deepseatooth is already in Toolbox or Kangaskhan Storage)\n\n'
                                 '[size=16]Pokémon[/size]\n'
                                 '#366 Clamperl -> #367 Huntail (With Link Cable)\n',
                 'Deepseascale': '[size=16][color=000011]Location:[/color][/size]\n'
                                 '• [u]Grand Sea[/u]\n'
                                 '- 15F'
                                 '- Replaced with a Link Cable if any Deepseascale is present in the Toolbox or in Kangaskhan Storage\n'
                                 '• [u]Far-Off Sea[/u]\n'
                                 '- 51F-75F (Even when a Deepseatooth is already in Toolbox or Kangaskhan Storage)\n\n'
                                 '[size=16]Pokémon[/size]\n'
                                 '#366 Clamperl -> #368 Huntail (With Link Cable)\n',
                 'Sun Ribbon': '[size=16][color=000011]Location:[/color][/size]\n'
                               '• [u]Wyvern Hill[/u]\n'
                               '- 20F (Requires Key)\n'
                               '- Replaced with a Link Cable if any Sun Ribbon is present in the Toolbox or in Kangaskhan Storage\n\n'
                               '[size=16]Pokémon[/size]\n'
                               '#133 Eevee -> #196 Espeon (With at least 4* IQ)',
                 'Lunar Ribbon': '[size=16][color=000011]Location:[/color][/size]\n'
                                 '• [u]Northwind Field[/u]\n'
                                 '- 20F (Requires Key)\n'
                                 '- Replaced with a Link Cable if any Lunar Ribbon is present in the Toolbox or in Kangaskhan Storage\n\n'
                                 '[size=16]Pokémon[/size]\n'
                                 '#133 Eevee -> #197 Umbreon (With at least 4* IQ)',
                 'Beauty Scarf': '[size=16][color=000011]Location:[/color][/size]\n'
                                 '• [u]Western Cave[/u]\n'
                                 '- 59F (Requires Key)'
                                 '- Replaced with a Link Cable if any Beauty Scarf is present in the Toolbox or in Kangaskhan Storage\n\n'
                                 '[size=16]Pokémon[/size]\n'
                                 '#349 Feebas -> #350 Milotic (With at least 4* IQ)'}

# Dictionary of all move descriptions
move_description_dict = {
 'Absorb': "Inflicts damage on the target. It also restores the user's HP "
           'based on the damage it inflicted.',
 'Acid': "Inflicts damage on the target. It may also lower the user's Defense "
         'by one level.',
 'Acid Armor': "Boosts the user's Defense by two levels.",
 'Aerial Ace': 'Inflicts damage on the target. It never misses.',
 'Aeroblast': 'Inflicts damage on the target, even at a distance. It has a '
              'high critical-hit rate.',
 'Agility': 'Boosts by one level the Movement Speed of the user and team '
            'members in the same room.',
 'Air Cutter': 'Inflicts damage on the target. It has a high critical-hit '
               'rate.',
 'Amnesia': "Boosts the user's Special Defense by two levels.",
 'Ancientpower': 'Inflicts damage on the target. It may also simultaneously '
                 'raise by one level Attack, Special Attack, Defense, Special '
                 'Defense, and Movement Speed.',
 'Arm Thrust': 'Inflicts damage on the target. It hits two to five times in '
               'succession.',
 'Aromatherapy': 'Heals all status problems of the user and team members in '
                 'the room.',
 'Assist': 'Makes the user randomly use one move out of all the moves of the '
           'Pokémon on the floor.',
 'Astonish': 'Inflicts damage on the target. It may also cause the target to '
             'cringe, making it incapable of action.',
 'Attack': 'NULL',
 'Attract': 'Inflicts the Infatuated status on<p>the target.</p>',
 'Aurora Beam': 'Inflicts damage on the target, even at a distance. It may '
                "also halve the target's Attack.",
 'Barrage': 'Inflicts damage on the target. It hits two to five times in '
            'succession.',
 'Barrier': "Boosts the user's Defense by two levels.",
 'Baton Pass': "Successively switches the user's position with the positions "
               'of other Pokémon in the room.',
 'Beat Up': 'Summons the team members around the user.',
 'Belly Drum': "Boosts the user's Attack to maximum, but empties its Belly to "
               'just one. It has no effect if the Belly is one or less.',
 'Bide': 'The user gains the Bide status. When Bide is released, the user '
         'looses an attack double the damage it took while waiting.',
 'Bind': 'Inflicts damage on the target. It may also cause constriction, '
         'making the foe incapable of movement.',
 'Bite': 'Inflicts damage on the target. It may also cause the target to '
         'cringe, making it incapable of action.',
 'Blast Burn': 'Inflicts damage on the target. However, it also inflicts the '
               'Paused status on the user. It also thaws and frees frozen '
               'Pokémon.',
 'Blaze Kick': 'Inflicts damage on the target. It may also cause a burn. It '
               'thaws and frees frozen Pokémon. It has a high critical-hit '
               'rate.',
 'Blizzard': 'Inflicts damage on the target. It may also leave the target '
             'frozen and incapable of action.',
 'Block': 'Inflicts the Leg Hold status on the target, making it incapable of '
          'movement.',
 'Body Slam': 'Inflicts damage on the target. It may also cause paralysis and '
              'prevent any attacks or moves.',
 'Bone Club': 'Inflicts damage on the target. It may also cause the target to '
              'cringe, making it incapable of action.',
 'Bone Rush': 'Inflicts damage on the target. It hits two to five times in '
              'succession.',
 'Bonemerang': 'Strikes the target twice, even at a distance.',
 'Bounce': 'The user gains the Bouncing status, making it attack strongly on '
           'the next turn. It may also cause paralysis. It is not possible to '
           'link this move.',
 'Brick Break': "Shatters the target's Reflect or Light Screen to inflict "
                'damage.',
 'Bubble': 'Inflicts damage on the target, even at a distance. It may also '
           "lower the target's Movement Speed by one level.",
 'Bubblebeam': 'Inflicts damage on the target, even at a distance. It may also '
               "lower the target's Movement Speed by one level.",
 'Bulk Up': "Raises the user's Attack and Defense by one level.",
 'Bullet Seed': 'Inflicts damage on the target, even at a distance. It hits '
                'two to five times in succession.',
 'Calm Mind': "Boosts the Pokémon's Special Attack and Special Defense by one "
              'level.',
 'Camouflage': "The user's type changes to match the terrain.",
 'Charge': 'The user gains the Charging status. It boosts the power of the '
           'Electric-type move to be used next.',
 'Charm': 'Lowers the Attack of the target by two levels.',
 'Clamp': 'Inflicts damage on the target. It may also cause constriction, '
          'making the foe incapable of movement.',
 'Comet Punch': 'Inflicts damage on the target. It hits two to five times in '
                'succession.',
 'Confuse Ray': 'Inflicts the Confused status on the target, making its '
                'attacks and movements erratic.',
 'Confusion': 'Inflicts damage on the target. It may also leave the target '
              'confused.',
 'Constrict': "Inflicts damage on the target. It may also lower the target's "
              'Movement Speed by one level.',
 'Conversion': "Changes the user's type into the same type as one of its "
               'moves.',
 'Conversion 2': 'The user gains the Conversion 2 status. It changes the '
                 "user's type to one that is strong against the move type it "
                 'took last.',
 'Cosmic Power': "Boosts the user's Defense and Special Defense by one level.",
 'Cotton Spore': "Lowers the target's Movement Speed by one level.",
 'Counter': 'The user gains the Counter status. Any damage from Physical '
            'Attack moves or a regular attack is partially returned.',
 'Covet': "Inflicts damage on the target. It also snatches the target's hold "
          "item to make it the user's.",
 'Crabhammer': 'Inflicts damage on the target. It has a high critical-hit '
               'rate.',
 'Cross Chop': 'Inflicts damage on the target. It has a high critical-hit '
               'rate.',
 'Crunch': "Inflicts damage on the target. It may also lower the target's "
           'Special Defense by one level.',
 'Crush Claw': "Inflicts damage on the target. It may also lower the target's "
               'Defense by one level.',
 'Curse': "Boosts the user's Attack and Defense by one level, but also lowers "
          'Movement Speed by one level. If used by a Ghost type, the target is '
          "cursed, and the user's HP halved.",
 'Cut': 'Damages all foes around the user.',
 'Defense Curl': "Boosts the user's Defense by one level.",
 'Destiny Bond': 'The user and the target gain the Destiny Bond status. The '
                 'target sustains the same damage as the user in this state.',
 'Detect': 'The user gains the Protect status, preventing damage from enemy '
           'attacks and moves.',
 'Dig': 'The user gains the Digging status, and it attacks on the next turn. '
        'It is not possible to link this move.',
 'Disable': 'Causes paralysis in the target. A Pokémon affected by paralysis '
            'is incapable of attacking or using moves.',
 'Dive': 'The user gains the Diving status, making it attack strongly on the '
         "next turn. It is not possible to link this move. It can't be used "
         'without water.',
 'Dizzy Punch': 'Inflicts damage on the target. It may also leave the target '
                'confused.',
 'Doom Desire': 'The user gains the Set Damage status. In this state, all '
                'damage inflicted by the user will remain constant.',
 'Double Kick': 'Attacks the target twice in succession.',
 'Double Team': "Boosts the user's Evasion by one level.",
 'Double-edge': 'Inflicts damage on the target. However, it also damages the '
                'user.',
 'Doubleslap': 'Inflicts damage on the target. It hits two to five times in '
               'succession.',
 'Dragon Claw': 'Inflicts damage on the target.',
 'Dragon Dance': "Boosts the user's Attack and Movement Speed by one level.",
 'Dragon Rage': 'Inflicts a set amount of damage on the<p>target.</p>',
 'Dragonbreath': 'Inflicts damage on the target, even at a distance. It may '
                 'also cause paralysis, preventing any attacks or moves.',
 'Dream Eater': "Inflicts damage on the target and restores the user's HP. "
                'Effective only against sleeping foes.',
 'Drill Peck': 'Inflicts damage on the target.',
 'Dynamicpunch': 'Inflicts damage on the target. It also leaves the target '
                 'confused.',
 'Earthquake': 'Damages all Pokémon in the same room. It inflicts double '
               'damage on any digging Pokémon.',
 'Egg Bomb': 'Inflicts damage on the target.',
 'Ember': 'Inflicts damage on the target. It may also cause a burn. It thaws '
          'and frees frozen Pokémon.',
 'Encore': 'Inflicts the Encore status on the target, making it capable of '
           'using only the move it last used.',
 'Endeavor': "The difference between the foe's HP and the user's HP is applied "
             "as this move's damage.",
 'Endure': 'The user gains the Enduring status. The user will survive any '
           'attack with just one HP.',
 'Eruption': "Inflicts damage on the target. The higher the user's HP, the "
             'greater the damage. It thaws and frees frozen Pokémon.',
 'Explosion': 'Makes the user blow up in a huge explosion, inflicting damage '
              'on all surrounding Pokémon. It also destroys surrounding items '
              'and walls.',
 'Extrasensory': 'Inflicts damage on the target. It may also cause the target '
                 'to cringe, making it incapable of attacking or using moves.',
 'Extremespeed': 'Inflicts damage on a target up to two tiles ahead.',
 'Facade': 'Inflicts damage on the target. If the user is poisoned, badly '
           'poisoned, or has a burn, its power is doubled.',
 'Faint Attack': 'Inflicts damage on the target. It never misses.',
 'Fake Out': 'Inflicts damage on the target. It may also make the target '
             'cringe. It reaches up to two tiles ahead.',
 'Fake Tears': "Lowers the target's Special Defense by two levels.",
 'False Swipe': 'Inflicts damage on the target. It leaves the target with one '
                'HP if its damage would have made the target faint.',
 'Featherdance': "Lowers the target's Attack by two levels.",
 'Fire Blast': 'Inflicts damage on the target. It may also cause a burn. It '
               'thaws and frees frozen Pokémon.',
 'Fire Punch': 'Inflicts damage on the target. It may also cause a burn. It '
               'thaws and frees frozen Pokémon.',
 'Fire Spin': 'Inflicts damage on the target. It may also cause constriction. '
              'It thaws and frees frozen Pokémon.',
 'Fissure': 'Defeats the target in one shot--if it hits. It has no effect on a '
            'flying foe.',
 'Flail': "Inflicts damage on the target. The lower the user's HP, the greater "
          'the damage.',
 'Flame Wheel': 'Inflicts damage on the target. It may also cause a burn. It '
                'thaws and frees frozen Pokémon.',
 'Flamethrower': 'Inflicts damage on the target, even at a distance. It may '
                 'also cause a burn. It thaws and frees frozen Pokémon.',
 'Flash': "Lowers the target's Accuracy by one level.",
 'Flatter': 'Inflicts the Confused status on the target, but also raises its '
            'Special Attack by one level.',
 'Fly': 'The user gains the Flying status,  making it attack strongly on the '
        'next turn. It is not possible to link this move.',
 'Focus Energy': 'The user gains the Focus Energy status, raising its '
                 'critical-hit rate.',
 'Focus Punch': 'The user gains the Focus Punch status, and it attacks on the '
                'next turn. It is not possible to link this move.',
 'Follow Me': 'The user gains the Decoy status, making it the primary target '
              'of foes.',
 'Foresight': 'Resets the boosted Evasion of the target. Ghost-type foes '
              'become exposed.',
 'Frenzy Plant': 'Inflicts damage on the target. However, it also inflicts the '
                 'Paused status on the user, making it incapable of action.',
 'Frustration': 'Inflicts damage on the target. It inflicts greater damage if '
                "the user's IQ is low.<p>Power drops every 100 IQ by 5</p>",
 'Fury Attack': 'Inflicts damage on the target. It hits two to five times in '
                'succession.',
 'Fury Cutter': 'Attacks the target twice in succession.',
 'Fury Swipes': 'Inflicts damage on the target. It hits two to five times in '
                'succession.',
 'Future Sight': 'The user gains the Set Damage status. In this state, all '
                 'damage inflicted by the user will remain constant.',
 'Giga Drain': "Inflicts damage on the target. It also restores the user's HP "
               'based on the damage it inflicted.',
 'Glare': 'Causes paralysis in the target. A Pokémon affected by paralysis is '
          'incapable of attacking or using moves.',
 'Grasswhistle': 'Makes the target go to sleep, causing it to be incapable of '
                 'action.',
 'Growl': 'Lowers the Attack of all foes in the room by one level.',
 'Growth': "Boosts the user's Special Attack by one level.",
 'Grudge': 'The user gains the Grudge status. If the user is defeated, it '
           'zeroes the PP of the move last used by the foe.',
 'Guillotine': 'Defeats the target in one shot--if it hits. It has no effect '
               'on a Ghost-type foe.',
 'Gust': 'Inflicts damage on the target. Doubles damage on a flying or '
         'bouncing Pokémon.',
 'Hail': "Changes the dungeon floor's weather to Hail for several turns.",
 'Harden': "Boosts the user's Defense by one level.",
 'Haze': 'Resets the Attack, Defense, etc., of all Pokémon on the floor '
         'whether they were boosted or lowered.',
 'Headbutt': 'Inflicts damage on the target. It may also cause the target to '
             'cringe, making it incapable of action.',
 'Heal Bell': 'Heals all status problems of the user and team members in the '
              'room.',
 'Heat Wave': 'Inflicts damage on foes in the room. It may also cause a burn. '
              'It thaws and frees frozen Pokémon.',
 'Helping Hand': 'Boosts the Attack and Special Attack of team members in the '
                 'same room by one level.',
 'Hi Jump Kick': 'Inflicts damage on the target, but hurts the user if it '
                 'misses.',
 'Hidden Power': 'Inflicts damage on the target. Its type and power change '
                 'with the dungeon.',
 'Horn Attack': 'Inflicts damage on the target.',
 'Horizontal Cut': 'Inflicts Damage in 3 Directions',
 'Horn Drill': 'Defeats the target in one shot--if it hits. It has no effect '
               'on a Ghost-type foe.',
 'Howl': "Boosts the user's Attack by one level.",
 'Hydro Cannon': 'Inflicts damage on the target, even at a distance. It also '
                 'inflicts the Paused status on the user, making it incapable '
                 'of action.',
 'Hydro Pump': 'Inflicts damage on the target, even at a distance.',
 'Hyper Beam': 'Inflicts damage on the target, even at a distance. It also '
               'inflicts the Paused status on the user, making it incapable of '
               'action.',
 'Hyper Fang': 'Inflicts damage on the target. It may also cause the target to '
               'cringe, making it incapable of action.',
 'Hyper Voice': 'Inflicts damage on the target.',
 'Hypnosis': 'Makes the target go to sleep, causing it to be incapable of '
             'action.',
 'Ice Ball': 'Hits the target in succession until it misses. Its power rises '
             'with every hit. It may hit up to five times.',
 'Ice Beam': 'Inflicts damage on the target, even at a distance. It may also '
             'leave the target frozen and incapable of action.',
 'Ice Punch': 'Inflicts damage on the target. It may also leave the target '
              'frozen and incapable of action.',
 'Icicle Spear': 'Inflicts damage on the target. It hits two to five times in '
                 'succession.',
 'Icy Wind': 'Inflicts damage on the target, even at a distance. It also '
             "lowers the target's Movement Speed by one level.",
 'Imprison': 'Inflicts the Paused status on the target, making it incapable of '
             'action.',
 'Ingrain': 'The user gains the Ingrain status. The user becomes incapable of '
            'moving, but regains HP over several turns.',
 'Iron Defense': "Boosts the user's Defense by two levels.",
 'Iron Tail': "Inflicts damage on the target. It may also lower the target's "
              'Defense by one level.',
 'Jump Kick': 'Inflicts damage on the target, but hurts the user if it misses.',
 'Karate Chop': 'Inflicts damage on the target. It has a high critical-hit '
                'rate.',
 'Kinesis': "Lowers the target's Accuracy by one level.",
 'Knock Off': "Knocks the target's hold item to the ground.",
 'Leaf Blade': 'Inflicts damage on the target. It has a high critical-hit '
               'rate.',
 'Leech Life': "Inflicts damage on the target. It also restores the user's HP "
               'based on the damage it inflicted.',
 'Leech Seed': "Inflicts the Leech Seed status on the target. The target's HP "
               "is leeched every several turns to restore the user's HP.",
 'Leer': "Lowers the target's Defense by one level.",
 'Lick': 'Inflicts damage on the target. It may also cause paralysis and '
         'prevent any attacks or moves.',
 'Light Screen': 'The user gains the Light Screen status. It halves the damage '
                 'from Special Attack moves.',
 'Lock-on': 'Gives the user the Sure Shot status, making all its moves and '
            'attacks completely accurate.',
 'Lovely Kiss': 'Makes all foes around the user go to sleep, causing them to '
                'be incapable of action.',
 'Low Kick': 'Inflicts damage on the target. The heavier the target, the '
             'greater the damage.',
 'Luster Purge': 'Inflicts damage on the target. It may also lower the '
                 "target's Special Defense by one level.",
 'Mach Punch': 'Inflicts damage on a target up to two tiles ahead.',
 'Magic Coat': 'The user gains the Magic Coat status. The user reflects '
               'several moves directly back to the foes.',
 'Magical Leaf': 'Inflicts damage on the target. It never misses.',
 'Magnitude': 'Damages all Pokémon in the same room. The amount of damage '
              'varies. It inflicts double damage on any digging Pokémon.',
 'Mean Look': 'Inflicts the Leg Hold status on the target, making it incapable '
              'of movement.',
 'Meditate': "Boosts the user's Attack by one level.",
 'Mega Drain': "Inflicts damage on the target. It also restores the user's HP "
               'based on the damage it inflicted.',
 'Mega Kick': 'Inflicts damage on the target.',
 'Mega Punch': 'Inflicts damage on the target.',
 'Megahorn': 'Inflicts damage on the target.',
 'Metal Claw': "Inflicts damage on the target. It may also boost the user's "
               'Attack by one level.',
 'Metal Sound': "Reduces the target's Special Defense by three levels.",
 'Meteor Mash': 'Inflicts damage on the target, even at a distance. It may '
                "also boost the user's Attack by one level.",
 'Metronome': 'Randomly looses a move from among all the moves known to '
              'Pokémon.',
 'Milk Drink': 'Restores the HP of the user and its team members on the floor '
               'by one quarter of their maximum HP.',
 'Mimic': 'Makes the user deploy the same move as the one last used by the foe '
          'facing it. Some moves cannot be mimicked.',
 'Mind Reader': 'Gives the user Sure Shot status, making all its moves and '
                'attacks completely accurate.',
 'Minimize': "Boosts the user's Evasion by one level.",
 'Mirror Coat': 'The user gains the Mirror Coat status. The user returns the '
                'damage it takes from any Special Attack moves used by a foe '
                'beside it.',
 'Mirror Move': 'The user gains the Mirror Move status. Any move used against '
                'the user is countered with the same move.',
 'Mist': 'The user gains the Mist status. It prevents Attack, Defense, Special '
         'Attack, Special Defense, Accuracy, and Evasion from being reduced.',
 'Mist Ball': "Inflicts damage on the target. It may lower the target's "
              'Special Attack by one level.',
 'Momento': 'Sharply reduces the Attack and Special Attack of all foes in the '
            "room. It also cuts the user's HP to one and warps the user to a "
            'different place on the floor.',
 'Moonlight': 'Restores the HP of the user and team members on the same floor. '
              'The amount of HP recovered depends on the weather.',
 'Morning Sun': 'Restores the HP of the user and team members on the floor. '
                'The amount of HP regained depends on the weather.',
 'Mud Shot': "Inflicts damage on the target. It also lowers the target's "
             'Movement Speed by one level.',
 'Mud Sport': "Changes the floor's status to Mud Sport, which halves the power "
              'of Electric-type moves.',
 'Mud-Slap': "Inflicts damage on the target. It also lowers the target's "
             'Accuracy by one level.',
 'Muddy Water': "Inflicts damage on the target. It may also lower the target's "
                'Accuracy by one level.',
 'Nature Power': 'Looses a variety of moves depending on the dungeon terrain.',
 'Needle Arm': 'Inflicts damage on the target. It may also cause the target to '
               'cringe, making it incapable of action.',
 'Night Shade': 'Damages all foes around the user. The amount of damage '
                "depends on the user's level.",
 'Nightmare': 'Inflicts the Nightmare status on the target, making it '
              'incapable of action.',
 'Octazooka': 'Inflicts damage on the target, even at a distance. It may also '
              "lower the target's Accuracy by one level.",
 'Odor Sleuth': 'Resets the boosted Evasion of foes in the same room. '
                'Ghost-type foes are exposed.',
 'Outrage': 'Hits the target two to five times in succession. However, it also '
            'makes the user confused.',
 'Overheat': "Damages all foes around the user, but also lowers the user's "
             'Special Defense by two levels and thaws frozen Pokémon.',
 'Pain Split': 'Adds the HP of the user and the target, then shares it '
               'equally.',
 'Pay Day': 'Inflicts damage on the target. If the foe faints, it will drop '
            'money.',
 'Peck': 'Inflicts damage on the target.',
 'Perish Song': 'Inflicts the Perish Song status on all foes on the floor. The '
                'affected foes faint after several turns.',
 'Petal Dance': 'Hits the target two to five times in succession. However it '
                'also makes the user confused.',
 'Pin Missile': 'Inflicts damage on the target, even at a distance. It hits '
                'two to five times in succession.',
 'Poison Fang': 'Inflicts damage on the target. It may also leave the target '
                'badly poisoned, damaging it over several turns.',
 'Poison Gas': 'Poisons the target. If a Pokémon is poisoned, it sustains '
               'damage over several turns.',
 'Poison Sting': 'Inflicts damage on the target. It may also leave the target '
                 'poisoned, damaging it over several turns.',
 'Poison Tail': 'Inflicts damage on the target. It may also leave the target '
                'poisoned. It has a high critical-hit rate.',
 'Poisonpowder': 'Poisons the target. If a Pokémon is poisoned, it sustains '
                 'damage over several turns.',
 'Pound': 'Inflicts damage on the target.',
 'Powder Snow': 'Inflicts damage on the target. It may also leave the target '
                'frozen and incapable of action.',
 'Present': 'Either inflicts damage on the target or restores its HP.',
 'Protect': 'The user gains the Protect status, preventing damage from enemy '
            'attacks and moves.',
 'Psybeam': 'Inflicts damage on the target, even at a distance. It may also '
            'leave the target confused.',
 'Psych Up': "Copies the target's levels for stats such as Attack and Defense.",
 'Psychic': "Inflicts damage on the target. It may also lower the target's "
            'Special Defense by one level.',
 'Psycho Boost': 'Inflicts damage on the target. However, it also lowers the '
                 "user's Special Attack by two levels.",
 'Psywave': 'Inflicts damage on the target, even at a distance. The amount of '
            "damage depends on the user's level.",
 'Pursuit': 'The user gains the Counter status. Any damage from Physical '
            'Attack moves or a regular attack is partially returned.',
 'Quick Attack': 'Inflicts damage on a target up to two tiles ahead.',
 'Rage': 'The user gains the Enraged status. Its Attack rises by one level '
         'every time the user takes damage.',
 'Rain Dance': "Changes the dungeon floor's weather to Rain over several "
               'turns.',
 'Rapid Spin': 'Inflicts damage on the target. It also frees the user from '
               'Leech Seed, Leg Hold, Ingrain, or Constriction.',
 'Razor Leaf': 'Inflicts damage on the target, even at a distance. It has a '
               'high critical-hit rate.',
 'Razor Wind': 'The user gains the Razor Wind status, and it looses a powerful '
               'attack with a high critical-hit rate on the next turn. It is '
               'not possible to link this move.',
 'Recover': "Restores the user's HP by half its maximum HP.",
 'Recycle': 'Repairs the item Used TM and restores it to its original, unused '
            'state.',
 'Reflect': 'The user gains the Reflect status, halving the damage from all '
            'Physical Attack moves and regular attacks.',
 'Refresh': 'Heals all status problems of the user and its team members in the '
            'room.',
 'Rest': 'The user gains the Napping status.<p>Upon awakening, the Pokémon '
         'regains HPand recovers from any status problems.</p>',
 'Return': "Inflicts damage on the target. Its power rises with the user's IQ.",
 'Revenge': 'The user gains the Bide status. When Bide is released, the user '
            'looses an attack double the damage it took while waiting.',
 'Reversal': "Inflicts damage on the target. The lower the user's HP, the "
             'greater the damage it inflicts.',
 'Roar': 'Knocks the target flying. If the target hits a wall or another '
         'Pokémon, it sustains damage.',
 'Rock Blast': 'Inflicts damage on the target. It hits two to five times in '
               'succession.',
 'Rock Slide': 'Inflicts damage on the target. It may also cause the target to '
               'cringe, making it incapable of action.',
 'Rock Smash': 'Digs through the wall the user is facing.',
 'Rock Throw': 'Inflicts damage on the target.',
 'Rock Tomb': "Inflicts damage on the target. It also lowers the target's "
              'Movement Speed by one level.',
 'Role Play': "Copies the target's Special Ability. The user regains its own "
              'Special Ability when it leaves the floor.',
 'Rolling Kick': 'Inflicts damage on the target. It may also cause the target '
                 'to cringe, making it incapable of action.',
 'Rollout': 'Hits the target in succession until it misses. Its power rises '
            'with every hit. It may hit up to five times.',
 'Sacred Fire': 'Inflicts damage on the target. It may also cause a burn.',
 'Safeguard': 'The user and team members in the same room gain the Safeguard '
              'status, which prevents status problems.',
 'Sand Tomb': 'Inflicts damage on the target. It may also cause constriction, '
              'making the foe incapable of movement.',
 'Sand-attack': "Lowers the target's Accuracy by one level.",
 'Sandstorm': "Changes the dungeon floor's weather to Sandstorm for several "
              'turns.',
 'Scary Face': "Lowers the target's Movement Speed by one level.",
 'Scratch': 'Inflicts damage on the target.',
 'Screech': "Sharply lowers the target's Defense.",
 'Secret Power': 'Inflicts damage on the target. It may also trigger other '
                 'effects depending on the terrain.',
 'Seismic Toss': 'Inflicts damage on the target. The amount of damage depends '
                 "on the user's level.",
 'Selfdestruct': 'Makes the user explode, inflicting damage on all surrounding '
                 'Pokémon. It also destroys surrounding items.',
 'Shadow Ball': 'Inflicts damage on the target, even at a distance. It may '
                "also lower the target's Special Defense by one level.",
 'Shadow Punch': 'Inflicts damage on the target. It never misses.',
 'Sharpen': "Boosts the user's Attack by one level.",
 'Sheer Cold': 'Defeats the target in one shot--if it hits.',
 'Shock Wave': 'Inflicts damage on the target, even at a distance. It never '
               'misses.',
 'Signal Beam': 'Inflicts damage on the target, even at a distance. It may '
                'also leave the target confused.',
 'Silver Wind': 'Inflicts damage on foes in the same room. It may also '
                'simultaneously raise by one level Attack, Special Attack, '
                'Defense, Special Defense, and Movement Speed.',
 'Sing': 'Makes the target go to sleep, causing it to be incapable of action.',
 'Sketch': "Copies the move last used by the target and makes it the user's. "
           'Sketch disappears after it copies a move.',
 'Skill Swap': "Switches the user's Special Ability with that of the target.",
 'Skull Bash': 'The user gains the Skull Bash status, causing it to attack '
               'strongly on the next turn. It is not possible to link this '
               'move.',
 'Sky Attack': 'The user gains the Sky Attack status, and it attacks strongly '
               'on the next turn. It is not possible to link this move.',
 'Sky Uppercut': 'Inflicts damage on the target. It hits even a Pokémon that '
                 'is either flying or bouncing.',
 'Slack Off': "Restores the user's HP by half its maximum HP.",
 'Slam': 'Inflicts damage on the target.',
 'Slash': 'Inflicts damage on the target. It has a high critical-hit rate.',
 'Sleep Powder': 'Makes all foes around the user go to sleep, making them '
                 'incapable of action.',
 'Sleep Talk': 'Makes the user deploy one of its moves against a foe that '
               'attacks it while it is sleeping.',
 'Sludge': 'Inflicts damage on the target. It may also leave the target '
           'poisoned, damaging it for several turns.',
 'Sludge Bomb': 'Inflicts damage on the target, even at a distance. It may '
                'also leave the target poisoned, damaging it for several '
                'turns.',
 'Smellingsalt': 'Inflicts damage on the target. It inflicts greater damage if '
                 'the target has paralysis, but it also heals paralysis.',
 'Smog': 'Inflicts damage on the target. It may also leave the target '
         'poisoned, damaging it over several turns.',
 'Smokescreen': 'Inflicts the Whiffer status on the target, making it miss '
                'almost all of its attacks and moves.',
 'Snatch': 'The user gains the Snatch status. It steals the moves of Pokémon '
           'on the same floor.',
 'Snore': 'If the user is attacked while asleep, it counterattacks. It may '
          'also cause the target to cringe, making it incapable of action.',
 'Softboiled': 'Restores the HP of the user and team members in the same room '
               'by one quarter of their maximum HP.',
 'Solarbeam': 'The user gains the Solarbeam status, making it attack strongly '
              'on the next turn. It is not possible to link this move.',
 'Sonicboom': 'Inflicts a set amount of damage on the target, even at a '
              'distance.',
 'Spark': 'Inflicts damage on the target. It may also cause paralysis and '
          'prevent any attacks or moves.',
 'Spider Web': 'Inflicts the Leg Hold status on the target, making it '
               'incapable of movement.',
 'Spike Cannon': 'Inflicts damage on the target, even at a distance. It hits '
                 'two to five times in succession.',
 'Spikes': 'The user places spikes underfoot. The Spiked Tile inflicts damage '
           'on foes that step on it.',
 'Spit Up': 'Inflicts damage on the target. Its power depends on how often the '
            'move Stockpile was used before.',
 'Spite': 'Zeroes the PP of the move last used by the target, making it '
          'unusable.',
 'Splash': 'Makes the user flop around as it moves. If there is another '
           'Pokémon where it lands, both Pokémon are hurt.',
 'Spore': 'Makes all the foes in the room go to sleep.',
 'Steel Wing': "Inflicts damage on the target. It may also raise the user's "
               'Defense by one level.',
 'Stockpile': 'Stockpiles power for up to three turns. The stored power boosts '
              'the performance of the moves Swallow and Spit Up.',
 'Stomp': 'Inflicts damage on the target. It may also cause the target to '
          'cringe, making it incapable of action.',
 'Strength': 'Hurls the target at another hostile Pokémon to inflict damage.',
 'String Shot': "Reduces the target's Movement Speed by one level, even at a "
                'distance.',
 'Struggle': 'Inflicts damage on the target. However, the user also takes '
             'damage one quarter of its maximum HP.',
 'Stun Spore': 'Causes paralysis in surrounding foes. A Pokémon affected by '
               'paralysis is incapable of attacking or using moves.',
 'Submission': 'Inflicts damage on the target. However, it also damages the '
               'user.',
 'Substitute': 'The target gains the Decoy status, making it the target of its '
               'fellow Pokémon.',
 'Sunny Day': "Changes the dungeon floor's weather to Sunny over several "
              'turns.',
 'Super Fang': "Halves the target's HP.",
 'Superpower': 'Inflicts damage on the target. However, it also lowers the '
               "user's Attack and Defense by one level.",
 'Supersonic': 'Inflicts the Confused status on the target, making its attacks '
               'and movements erratic.',
 'Surf': 'Inflicts damage on the target. Inflicts double damage on a diving '
         'foe.',
 'Swagger': 'Inflicts the Confused status on the target, but also raises its '
            'Attack by two levels.',
 'Swallow': "Restores the user's HP. The HP recovered depends on how often the "
            'move Stockpile was used before.',
 'Sweet Kiss': 'Inflicts the Confused status on the target, making its attacks '
               'and movements erratic.',
 'Sweet Scent': 'Lowers the Evasion of foes in the same room by one level.',
 'Swift': 'Inflicts damage on the target. It never misses.',
 'Swords Dance': "Boosts the user's Attack by two levels.",
 'Synthesis': "Restores the user's HP. The amount of HP regained depends on "
              'the weather.',
 'Tackle': 'Inflicts damage on the target.',
 'Tail Glow': "Boosts the user's Special Attack by two levels.",
 'Tail Whip': "Lowers the target's Defense by one level.",
 'Take Down': 'Inflicts damage on the target, but also hurts the user.',
 'Taunt': 'Inflicts the Taunted status on the targeted Pokémon.',
 'Teeter Dance': 'Inflicts the Confused status on all Pokémon on the floor, '
                 'making their attacks and movements erratic.',
 'Teleport': 'Warps the user to another spot on the same floor.',
 'Thief': "Inflicts damage on the target. It also snatches the target's hold "
          "item to make it the user's.",
 'Thrash': 'Attacks three times in random directions.',
 'Thunder': 'Inflicts damage on the target. It may also cause paralysis. Its '
            'accuracy is affected by the weather. It even hits a Pokémon that '
            'is flying or bouncing.',
 'Thunder Wave': 'Causes paralysis in the target. A Pokémon affected by '
                 'paralysis is incapable of attacking or using moves.',
 'Thunderbolt': 'Damages all foes around the user. It may also cause paralysis '
                'and prevent any attacks or moves.',
 'Thunderpunch': 'Inflicts damage on the target. It may also cause paralysis '
                 'and prevent any attacks or moves.',
 'Thundershock': 'Inflicts damage on the target. It may also cause paralysis '
                 'and prevent any attacks or moves.',
 'Tickle': "Reduces the target's Attack and Defense by one level.",
 'Torment': 'Prevents the targeted Pokémon, while it remains on the floor, '
            'from using the last move it used.',
 'Toxic': 'Badly poisons the target. If a Pokémon is badly poisoned, it '
          'sustains damage over several turns.',
 'Transform': 'The user gains the Transformed status. The user transforms into '
              'a hostile Pokémon that appears on the floor.',
 'Tri Attack': 'Inflicts damage on the target. It may also cause a burn, '
               'paralysis, or leave the target frozen.',
 'Trick': "Switches the user's hold item with the target's hold item. It only "
          'works if both Pokémon hold items.',
 'Triple Kick': 'Kicks the target three times. Its power rises with every '
                'kick.',
 'Twineedle': 'Hits the target twice, even at a distance. It may also leave '
              'the target poisoned, damaging it over several turns.',
 'Twister': 'Inflicts damage on the target. It may also cause the target to '
            'cringe, making it incapable of action. Doubles damage on a flying '
            'or bouncing Pokémon.',
 'Uproar': 'The user and team members in the room gain the Sleepless status, '
           'so they cannot fall asleep. It also awakens sleeping team members.',
 'Vacuum Cut': 'Inflicts 30 Damage to any Pokémon in the same room',
 'Vicegrip': 'Inflicts damage on the target.',
 'Vine Whip': 'Inflicts damage on the target.',
 'Vital Throw': 'The user gains the Vital Throw status. Foes that attack the '
                'user are hurled at other foes.',
 'Volt Tackle': 'Inflicts damage on the target, even at a distance. However, '
                'it also hurts the user.',
 'Water Gun': 'Inflicts damage on the target.',
 'Water Pulse': 'Inflicts damage on the target, even at a distance. It may '
                'also leave the target confused.',
 'Water Sport': "Changes the floor's status to Water Sport, which halves the "
                'power of Fire-type moves.',
 'Water Spout': "Inflicts damage on the target. The higher the user's HP, the "
                'greater the damage.',
 'Waterfall': 'Inflicts damage on the target.',
 'Weather Ball': 'Inflicts damage on the target, even at a distance, using the '
                 "weather's power.",
 'Whirlpool': 'Inflicts damage on the target. It may also cause constriction, '
              'making the foe incapable of movement. Inflicts double damage on '
              'a diving foe.',
 'Whirlwind': 'Knocks the target flying. If the target hits a wall or another '
              'Pokémon, it sustains damage.',
 'Wide Slash': 'Inflicts damage on foes on the three tiles diagonally and '
               'directly in front.',
 'Will-o-wisp': 'Inflicts a burn on the target. A burn inflicts damage every '
                'few turns.',
 'Wing Attack': 'Inflicts damage on the target.',
 'Wish': "The user gains the Wish status. It boosts the user's HP recovery "
         'rate.',
 'Withdraw': "Boosts the user's Defense by one level.",
 'Wrap': 'The user gains the Wrap status, and the Wrapped status is inflicted '
         'on the target. Both Pokémon become incapable of action.',
 'Yawn': 'Inflicts the Yawning status on the target. A yawning Pokémon falls '
         'asleep sometime later.',
 'Zap Cannon': 'Inflicts damage on the target, even at a distance. It also '
               'causes paralysis, preventing any attacks or moves.'}

# 0,         1, 2,     3,   4,            5,    6,    7,     8,       9,             10,       11,        12,      13,       14,        15,                16,          17,            18,         19,         20,           21,         22,            23,           24,              25,         26,         27,  28,     29,  30,     31
# Unnamed: 0,id,number,name,japanese_name,type1,type2,joined,favorite,classification,weight_kg,weight_lbs,height_m,height_ft,md_ability,md_evolution_chain,md_body_size,md_friend_area,md_get_rate,md_location,rg_browser_no,rg_location,rg_pkmn_assist,rg_type_group,rg_field_ability,tz_get_rate,tz_location,evo1,evo1how,evo2,evo2how,evo3
