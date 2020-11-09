import pickle
import re
from pprint import pprint
import variables as v
import requests
from bs4 import BeautifulSoup

#### SOUP

# headers = {
#     'Access-Control-Allow-Origin': '*',
#     'Access-Control-Allow-Methods': 'GET',
#     'Access-Control-Allow-Headers': 'Content-Type',
#     'Access-Control-Max-Age': '3600',
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
#     }
#
# # for linko in (v.soup_moves):
# move_dicto = {}
# page_nr = 1
# page_max = 356
# for move in v.soup_moves:
#     print(str((page_nr/page_max)*100)[:4] + '%')
#     url = move
#     req = requests.get(url, headers)
#     soup = BeautifulSoup(req.content, 'html.parser')
#     count = (str(soup.find_all("div", class_="pi-data-value pi-font")).count('<div class="pi-data-value pi-font">'))
#
#     move_name = url.partition('https://pmd-rt.fandom.com/wiki/')[2]
#
#     if '_' in move_name:
#         move_name = (move_name.replace('_', ' '))
#     descript = (str(soup.find_all("div", class_="pi-data-value pi-font")[count-1]).partition('pi-font">')[2].partition('</div>')[0])
#
#     move_dicto[move_name] = descript
#     page_nr += 1
# pprint(move_dicto)

#print(resulta.partition('</div>')[2].partition('</div>')[2].partition('</div>')[2].partition('</div>')[2].partition('</div>')[2])
#print(soup.prettify())

####

def regex_partition(content, separator):
    separator_match = re.search(separator, content)
    if not separator_match:
        return content, '', ''

    matched_separator = separator_match.group(0)
    parts = re.split(matched_separator, content, 1)

    return parts[0], matched_separator, parts[1]

################
# Add Column to CSV
################

# Open the input_file in read mode and output_file in write mode
# with open('csv\\spinoffDexDataset.csv', 'r', encoding='utf-8') as read_obj, \
#         open('csv\\spinoffDexDatasetBackup.csv', 'w', newline='', encoding='utf-8') as write_obj:
#     # Create a csv.reader object from the input file object
#     csv_reader = reader(read_obj)
#     # Create a csv.writer object from the output file object
#     csv_writer = writer(write_obj)
#     # Read each row of the input csv file as list
#
#     pokemon_nr = 0
#     for row in csv_reader:
#         # Append stuff here
#         for list_index in range(1, 8):
#             if pokemon_nr < 387:
#                 row.append(v.supercheats_data[pokemon_nr][list_index])
#         # Add the updated row / list to the output file
#         csv_writer.writerow(row)
#         pokemon_nr += 1
#
###############################
# ######## TAZOS ############ #
###############################

# new_tazos = 40
# total_tazos = 40
# old_chance = 1
# for i in range(40, 0, -1):
#     print('new tazos:', new_tazos, '/', total_tazos)
#     new_chance = new_tazos/total_tazos
#     print('new_chance:', new_chance, '/// old new_chance:', old_chance)
#     total_chance = old_chance * new_chance
#     print(' * total_chance:', old_chance, '*', new_chance, '=', total_chance*100, '%')
#     old_chance = new_chance
#     new_tazos -= 1
#     print('\n')



################
# Supercheats Dex Data
################

# url = "https://www.supercheats.com/gameboyadvance/walkthroughs/pokemonmysteriousdungeonredrescueforce-walkthrough03.txt"
# response = requests.get(url)
# start_6 = (response.text.partition('T H E   P O K E D E X')[2])
# print(start_6.count('ID'))

# text_file = open("supercheats.txt", "w", encoding='utf-8')
# text_file.write(start_6)
# # text_file.close()

# ### ---- Actual working part  vvv

# with open('data gathering\\supercheats.txt', 'r', encoding='utf-8') as file:
#     contents = file.read()
#     contents = contents.partition('ID')[2]
#     dex = []
#     for i in range(386):
#         entry = []
#         page = contents.partition('ID')[0]
#         contents = contents.partition('ID')[2]
#
#         # Index [0]
#         entry.append('id_' + str(i+1))
#
#         # Base EXP Value [1]
#         entry.append(page.partition('Base EXP Value:')[2].partition('\n\n=')[0].strip())
#
#         # Base Stats [2] Base Stats: Att/Def/SpA/SpD:
#         entry.append(page.partition('Att/Def:')[1]+page.partition('Att/Def:')[2].partition('Body Size:')[0])
#         base_stats = (str(int(entry[2].partition('Att/Def:')[2][:4])) + '/' +
#                       str(int(entry[2].partition('Att/Def:')[2][5:8])) + '/' +
#                       str(int(entry[2].partition('SpA/SpD:')[2][:4])) + '/' +
#                       str(int(entry[2].partition('SpA/SpD:')[2][5:8])))
#         entry[2] = base_stats
#
#         # Preferred Gummi [3]
#         entry.append((page.partition('Preferred Gummi:')[2].partition('Stat Growth')[0]).strip())
#
#         # Stat Growth [4]
#         stat_growth = page.partition('Stat Growth')[1]+page.partition('Stat Growth')[2].partition('Recruiting')[0].strip()
#         sg_stats = (stat_growth.partition('Stat Growth')[2][:46])
#         sg_stats = [sg_stats[:3], sg_stats[9:11], sg_stats[16:19], sg_stats[20:23], sg_stats[26:29], sg_stats[30:33], sg_stats[39:]]
#         sg1 = (stat_growth.partition('  1')[1] + stat_growth.partition('  1')[2])
#         sg_r1 = [int(sg1[:46][:3]), int(sg1[:46][8:11]), int(sg1[:46][16:19]), int(sg1[:46][20:23]), int(sg1[:46][26:29]), int(sg1[:46][30:33]), int(sg1[:46][34:])]
#         entry.append([sg_stats])
#         entry[4].append(sg_r1)
#
#         row_start = sg1
#         for stat_row in range(10):
#             sg_r2 = [int(row_start.partition('\n')[2][18:21]), int(row_start.partition('\n')[2][26:30]), int(row_start.partition('\n')[2][34:37]), int(row_start.partition('\n')[2][38:41]), int(row_start.partition('\n')[2][44:47]), int(row_start.partition('\n')[2][48:51]), int(row_start.partition('\n')[2][52:].partition('\n')[0])]
#             entry[4].append(sg_r2)
#             row_start = row_start.partition('\n')[2].partition('\n')[2]
#
#         # Recruiting Minimum Levels [5]
#         if page.partition('Recruit Rate')[2][4:14] != 'Impossible':
#             entry.append(page.partition('Recruit Rate')[2].partition('% ')[2][:9])
#         else:
#             entry.append('[Imp/Imp]')
#
#         # Location [6]
#         entry.append(page.partition('Where To Get')[2].partition('============')[2].partition('Abilities')[0].strip())
#
#         start_6 = entry[6]
#         six_total = ''
#         for sixo in range(90):
#             if not regex_partition(start_6, "\w")[1]:
#                 break
#             six_total += (regex_partition(start_6, "\w")[1] + regex_partition(start_6, "\w")[2].partition('\n')[0] + '---')
#             start_6 = regex_partition(start_6, "\w")[2].partition('\n')[2]
#         entry[6] = six_total
#
#         # Quotes [7]
#         entry.append('  ' + page.partition('Quotes')[2].partition('======')[2].partition('==================================')[0].strip())
#
#         start_7 = entry[7]
#         seven_total = ''
#         for seveno in range(90):
#             if not regex_partition(start_7, "\w")[1]:
#                 break
#             seven_total += (regex_partition(start_7, "\w")[1] + regex_partition(start_7, "\w")[2].partition('\n')[0] + '---')
#             start_7 = regex_partition(start_7, "\w")[2].partition('\n')[2]
#         entry[7] = seven_total
#
#         # print('****', i, '****')
#         #print(page)
#         # print('*****************************************\n' * 3)
#         for e in entry:
#             pass#print(e)
#
#
#
#         dex.append(entry)
#     print(dex)
#     file.close()

################
# Evo Data Transformation
################

# with open('ughspinoffDexDatasetBackup.csv', 'r', newline='', encoding='utf-8') as file:
#     with open('ughspinoffDexDatasetBackup.csv', 'w', encoding='utf-8') as csvoutput:
#         writer = csv.writer(csvoutput, lineterminator='\n')
#         reader = csv.reader(file)
#         alls = []
#
#
#         data = list(csv.reader(file))
#
#         writer.writerows(alls)
#         for row in data:
#             evos = ['No Evolution']
#             if row[15][0] not in ['S', 'N', 'm']:
#                 evo1 = data[abs(int(row[15][:3]))][3]
#                 print(row[15])
#                 evos[0] = evo1
#                 lv1 = row[15].partition('--> ')[2].partition('--> ')[0][:-1]
#                 evos.append(lv1)
#                 evo2 = data[abs(int(row[15].partition('--> ')[2].partition('--> ')[2][:3]))][3]
#                 evos.append(evo2)
#                 if row[15].partition('--> ')[2].partition('--> ')[2].partition('--> ')[1]:
#                     lv2 = row[15].partition('--> ')[2].partition('--> ')[2].partition('--> ')[2].partition('--> ')[0][:-1]
#                     evos.append(lv2)
#                     evo3 = data[abs(int(row[15].partition('--> ')[2].partition('--> ')[2].partition('--> ')[2].partition('--> ')[2][:3]))][3]
#                     evos.append(evo3)
#                 else:
#                     evos.append('')
#                     evos.append('')
#             else:
#                 evos.append('')
#                 evos.append('')
#                 evos.append('')
#                 evos.append('')
#
#             row.append(evos[0])
#             row.append(evos[1])
#             row.append(evos[2])
#             row.append(evos[3])
#             row.append(evos[4])
#
#             alls.append(row)
#
#             #print(evos)
#         writer.writerows(alls)

################
# Location Data Transformation
################
# with open('ughspinoffDexDatasetBackup.csv', 'r', newline='', encoding='utf-8') as file:
#     with open('delete_later.csv', 'w', encoding='utf-8') as csvoutput:
#         writer = csv.writer(csvoutput, lineterminator='\n')
#         reader = csv.reader(file)
#
#         data = list(csv.reader(file))
#         #reado = csv.reader(file)
#         #writer.writerows(alls)
#         for row in data:
#             if re.search(r"..F-..F", row[19]):
#                 print(row[19].rstrip())
#                 # writer.writerow(row)


md_nr_name_type1_type2_ability = '''
#	Pokémon	Typing	Abilities
#001	Bulbasaur	Grass/Poison	Overgrow
#002	Ivysaur	Grass/Poison	Overgrow
#003	Venusaur	Grass/Poison	Overgrow
#004	Charmander	Fire	Blaze
#005	Charmeleon	Fire	Blaze
#006	Charizard	Fire/Flying	Blaze
#007	Squirtle	Water	Torrent
#008	Wartortle	Water	Torrent
#009	Blastoise	Water	Torrent
#010	Caterpie	Bug	Shield Dust
#011	Metapod	Bug	Shed Skin
#012	Butterfree	Bug/Flying	Compoundeyes
#013	Weedle	Bug/Poison	Shield Dust
#014	Kakuna	Bug/Poison	Shed Skin
#015	Beedrill	Bug/Poison	Swarm
#016	Pidgey	Normal/Flying	Keen Eye, Tangled Feet
#017	Pidgeotto	Normal/Flying	Keen Eye, Tangled Feet
#018	Pidgeot	Normal/Flying	Keen Eye, Tangled Feet
#019	Rattata	Normal	Guts, Run Away
#020	Raticate	Normal	Guts, Run Away
#021	Spearow	Normal/Flying	Keen Eye
#022	Fearow	Normal/Flying	Keen Eye
#023	Ekans	Poison	Intimidate, Shed Skin
#024	Arbok	Poison	Intimidate, Shed Skin
#025	Pikachu	Electric	Static
#026	Raichu	Electric/Psychic	Static
#027	Sandshrew	Ground	Sand Veil
#028	Sandslash	Ground	Sand Veil
#029	Nidoran♀	Poison	Poison Point, Rivalry
#030	Nidorina	Poison	Poison Point, Rivalry
#031	Nidoqueen	Poison/Ground	Poison Point, Rivalry
#032	Nidoran♂	Poison	Poison Point, Rivalry
#033	Nidorino	Poison	Poison Point, Rivalry
#034	Nidoking	Poison/Ground	Poison Point, Rivalry
#035	Clefairy	Normal	Cute Charm
#036	Clefable	Normal	Cute Charm
#037	Vulpix	Fire	Flash Fire
#038	Ninetales	Fire	Flash Fire
#039	Jigglypuff	Normal	Cute Charm
#040	Wigglytuff	Normal	Cute Charm
#041	Zubat	Poison/Flying	Inner Focus
#042	Golbat	Poison/Flying	Inner Focus
#043	Oddish	Grass/Poison	Chlorophyll
#044	Gloom	Grass/Poison	Chlorophyll
#045	Vileplume	Grass/Poison	Chlorophyll
#046	Paras	Bug/Grass	Dry Skin, Effect Spore
#047	Parasect	Bug/Grass	Dry Skin, Effect Spore
#048	Venonat	Bug/Poison	Compoundeyes, Tinted Lens
#049	Venomoth	Bug/Poison	Shield Dust, Tinted Lens
#050	Diglett	Ground/Steel	Arena Trap, Sand Veil
#051	Dugtrio	Ground/Steel	Arena Trap, Sand Veil
#052	Meowth	Normal	Pickup, Technician
#053	Persian	Normal	Limber, Technician
#054	Psyduck	Water	Cloud Nine, Damp
#055	Golduck	Water	Cloud Nine, Damp
#056	Mankey	Fighting	Anger Point, Vital Spirit
#057	Primeape	Fighting	Anger Point, Vital Spirit
#058	Growlithe	Fire	Flash Fire, Intimidate
#059	Arcanine	Fire	Flash Fire, Intimidate
#060	Poliwag	Water	Damp, Water Absorb
#061	Poliwhirl	Water	Damp, Water Absorb
#062	Poliwrath	Water/Fighting	Damp, Water Absorb
#063	Abra	Psychic	Inner Focus, Synchronize
#064	Kadabra	Psychic	Inner Focus, Synchronize
#065	Alakazam	Psychic	Inner Focus, Synchronize
#066	Machop	Fighting	Guts, No Guard
#067	Machoke	Fighting	Guts, No Guard
#068	Machamp	Fighting	Guts, No Guard
#069	Bellsprout	Grass/Poison	Chlorophyll
#070	Weepinbell	Grass/Poison	Chlorophyll
#071	Victreebel	Grass/Poison	Chlorophyll
#072	Tentacool	Water/Poison	Clear Body, Liquid Ooze
#073	Tentacruel	Water/Poison	Clear Body, Liquid Ooze
#074	Geodude	Rock/Ground	Rock Head, Sturdy
#075	Graveler	Rock/Ground	Rock Head, Sturdy
#076	Golem	Rock/Ground	Rock Head, Sturdy
#077	Ponyta	Fire	Flash Fire, Run Away
#078	Rapidash	Fire	Flash Fire, Run Away
#079	Slowpoke	Water/Psychic	Oblivious, Own Tempo
#080	Slowbro	Water/Psychic	Oblivious, Own Tempo
#081	Magnemite	Steel/Electric	Magnet Pull, Sturdy
#082	Magneton	Steel/Electric	Magnet Pull, Sturdy
#083	Farfetch'd	Normal/Flying	Inner Focus, Keen Eye
#084	Doduo	Normal/Flying	Early Bird, Run Away
#085	Dodrio	Normal/Flying	Early Bird, Run Away
#086	Seel	Water	Hydration, Thick Fat
#087	Dewgong	Water	Hydration, Thick Fat
#088	Grimer	Poison	Stench, Sticky Hold
#089	Muk	Poison	Stench, Sticky Hold
#090	Shellder	Water	Shell Armor
#091	Cloyster	Water/Ice	Shell Armor
#092	Gastly	Ghost/Poison	Levitate
#093	Haunter	Ghost/Poison	Levitate
#094	Gengar	Ghost/Poison	Levitate
#095	Onix	Rock/Ground	Rock Head, Sturdy
#096	Drowzee	Psychic	Forewarn, Insomnia
#097	Hypno	Psychic	Forewarn, Insomnia
#098	Krabby	Water	Hyper Cutter, Shell Armor
#099	Kingler	Water	Hyper Cutter, Shell Armor
#100	Voltorb	Electric	Soundproof, Static
#101	Electrode	Electric	Soundproof, Static
#102	Exeggcute	Grass/Psychic	Chlorophyll
#103	Exeggutor	Grass/Psychic	Chlorophyll
#104	Cubone	Ground	Lightning Rod, Rock Head
#105	Marowak	Ground	Lightning Rod, Rock Head
#106	Hitmonlee	Fighting	Limber, Reckless
#107	Hitmonchan	Fighting	Iron Fist, Keen Eye
#108	Lickitung	Normal	Oblivious, Own Tempo
#109	Koffing	Poison	Levitate
#110	Weezing	Poison	Levitate
#111	Rhyhorn	Ground/Rock	Lightning Rod, Rock Head
#112	Rhydon	Ground/Rock	Lightning Rod, Rock Head
#113	Chansey	Normal	Natural Cure, Serene Grace
#114	Tangela	Grass	Chlorophyll
#115	Kangaskhan	Normal	Early Bird, Scrappy
#116	Horsea	Water	Sniper, Swift Swim
#117	Seadra	Water	Poison Point, Sniper
#118	Goldeen	Water	Swift Swim, Water Veil
#119	Seaking	Water	Swift Swim, Water Veil
#120	Staryu	Water	Illuminate, Natural Cure
#121	Starmie	Water/Psychic	Illuminate, Natural Cure
#122	Mr. Mime	Psychic	Filter, Soundproof
#123	Scyther	Bug/Flying	Swarm, Technician
#124	Jynx	Ice/Psychic	Forewarn, Oblivious
#125	Electabuzz	Electric	Static
#126	Magmar	Fire	Flame Body
#127	Pinsir	Bug	Hyper Cutter, Mold Breaker
#128	Tauros	Normal	Anger Point, Intimidate
#129	Magikarp	Water	Swift Swim
#130	Gyarados	Water/Flying	Intimidate
#131	Lapras	Water/Ice	Shell Armor, Water Absorb
#132	Ditto	Normal	Limber
#133	Eevee	Normal	Adaptability, Run Away
#134	Vaporeon	Water	Water Absorb
#135	Jolteon	Electric	Volt Absorb
#136	Flareon	Fire	Flash Fire
#137	Porygon	Normal	Download, Trace
#138	Omanyte	Rock/Water	Shell Armor, Swift Swim
#139	Omastar	Rock/Water	Shell Armor, Swift Swim
#140	Kabuto	Rock/Water	Battle Armor, Swift Swim
#141	Kabutops	Rock/Water	Battle Armor, Swift Swim
#142	Aerodactyl	Rock/Flying	Pressure, Rock Head
#143	Snorlax	Normal	Immunity, Thick Fat
#144	Articuno	Ice/Flying	Pressure
#145	Zapdos	Electric/Flying	Pressure
#146	Moltres	Fire/Flying	Pressure
#147	Dratini	Dragon	Shed Skin
#148	Dragonair	Dragon	Shed Skin
#149	Dragonite	Dragon/Flying	Inner Focus
#150	Mewtwo	Psychic	Pressure
#151	Mew	Psychic	Synchronize
#152	Chikorita	Grass	Overgrow
#153	Bayleef	Grass	Overgrow
#154	Meganium	Grass	Overgrow
#155	Cyndaquil	Fire	Blaze
#156	Quilava	Fire	Blaze
#157	Typhlosion	Fire	Blaze
#158	Totodile	Water	Torrent
#159	Croconaw	Water	Torrent
#160	Feraligatr	Water	Torrent
#161	Sentret	Normal	Keen Eye, Run Away
#162	Furret	Normal	Keen Eye, Run Away
#163	Hoothoot	Normal/Flying	Insomnia, Keen Eye
#164	Noctowl	Normal/Flying	Insomnia, Keen Eye
#165	Ledyba	Bug/Flying	Early Bird, Swarm
#166	Ledian	Bug/Flying	Early Bird, Swarm
#167	Spinarak	Bug/Poison	Insomnia, Swarm
#168	Ariados	Bug/Poison	Insomnia, Swarm
#169	Crobat	Poison/Flying	Inner Focus
#170	Chinchou	Water/Electric	Illuminate, Volt Absorb
#171	Lanturn	Water/Electric	Illuminate, Volt Absorb
#172	Pichu	Electric	Static
#173	Cleffa	Normal	Cute Charm
#174	Igglybuff	Normal	Cute Charm
#175	Togepi	Normal	Hustle, Serene Grace
#176	Togetic	Normal/Flying	Hustle, Serene Grace
#177	Natu	Psychic/Flying	Early Bird, Synchronize
#178	Xatu	Psychic/Flying	Early Bird, Synchronize
#179	Mareep	Electric	Static
#180	Flaaffy	Electric	Static
#181	Ampharos	Electric	Static
#182	Bellossom	Grass	Chlorophyll
#183	Marill	Water	Huge Power, Thick Fat
#184	Azumarill	Water	Huge Power, Thick Fat
#185	Sudowoodo	Rock	Rock Head, Sturdy
#186	Politoed	Water	Water Absorb, Damp
#187	Hoppip	Grass/Flying	Chlorophyll
#188	Skiploom	Grass/Flying	Chlorophyll
#189	Jumpluff	Grass/Flying	Chlorophyll
#190	Aipom	Normal	Pickup, Run Away
#191	Sunkern	Grass	Chlorophyll, Solar Power
#192	Sunflora	Grass	Chlorophyll, Solar Power
#193	Yanma	Bug/Flying	Compoundeyes, Speed Boost
#194	Wooper	Water/Ground	Damp, Water Absorb
#195	Quagsire	Water/Ground	Damp, Water Absorb
#196	Espeon	Psychic	Synchronize
#197	Umbreon	Dark	Synchronize
#198	Murkrow	Dark/Flying	Insomnia, Super Luck
#199	Slowking	Water/Psychic	Oblivious
#200	Misdreavus	Ghost	Levitate
#201	Unown	Psychic	Levitate
#202	Wobbuffet	Psychic	Shadow Tag
#203	Girafarig	Normal/Psychic	Early Bird, Inner Focus
#204	Pineco	Bug	Sturdy
#205	Forretress	Bug/Steel	Sturdy
#206	Dunsparce	Normal	Run Away, Serene Grace
#207	Gligar	Ground/Flying	Hyper Cutter, Sand Veil
#208	Steelix	Steel/Ground	Rock Head, Sturdy
#209	Snubbull	Normal	Intimidate, Run Away
#210	Granbull	Normal	Intimidate, Quick Feet
#211	Qwilfish	Water/Poison	Poison Point, Swift Swim
#212	Scizor	Bug/Steel	Swarm, Technician
#213	Shuckle	Bug/Rock	Gluttony, Sturdy
#214	Heracross	Bug/Fighting	Guts, Swarm
#215	Sneasel	Ice/Dark	Inner Focus, Keen Eye
#216	Teddiursa	Normal	Pickup, Quick Feet
#217	Ursaring	Normal	Guts, Quick Feet
#218	Slugma	Fire	Flame Body, Magma Armor
#219	Magcargo	Fire/Rock	Flame Body, Magma Armor
#220	Swinub	Ice/Ground	Oblivious, Snow Cloak
#221	Piloswine	Ice/Ground	Oblivious, Snow Cloak
#222	Corsola	Water/Rock	Hustle, Natural Cure
#223	Remoraid	Water	Hustle, Sniper
#224	Octillery	Water	Sniper, Suction Cups
#225	Delibird	Ice/Flying	Hustle, Vital Spirit
#226	Mantine	Water/Flying	Swift Swim, Water Absorb
#227	Skarmory	Steel/Flying	Keen Eye, Sturdy
#228	Houndour	Fire/Dark	Early Bird, Flash Fire
#229	Houndoom	Fire/Dark	Early Bird, Flash Fire
#230	Kingdra	Water/Dragon	Sniper, Swift Swim
#231	Phanpy	Ground	Pickup
#232	Donphan	Ground	Sturdy
#233	Porygon2	Normal	Download, Trace
#234	Stantler	Normal	Frisk, Intimidate
#235	Smeargle	Normal	Own Tempo, Technician
#236	Tyrogue	Fighting	Guts, Steadfast
#237	Hitmontop	Fighting	Intimidate, Steadfast
#238	Smoochum	Ice/Psychic	Forewarn, Oblivious
#239	Elekid	Electric	Static
#240	Magby	Fire	Flame Body
#241	Miltank	Normal	Scrappy, Thick Fat
#242	Blissey	Normal	Natural Cure, Serene Grace
#243	Raikou	Electric	Pressure
#244	Entei	Fire	Pressure
#245	Suicune	Water	Pressure
#246	Larvitar	Rock/Ground	Guts
#247	Pupitar	Rock/Ground	Shed Skin
#248	Tyranitar	Rock/Dark	Sand Stream
#249	Lugia	Psychic/Flying	Pressure
#250	Ho-Oh	Fire/Flying	Pressure
#251	Celebi	Psychic/Grass	Natural Cure
#252	Treecko	Grass	Overgrow
#253	Grovyle	Grass	Overgrow
#254	Sceptile	Grass	Overgrow
#255	Torchic	Fire	Blaze
#256	Combusken	Fire/Fighting	Blaze
#257	Blaziken	Fire/Fighting	Blaze
#258	Mudkip	Water	Torrent
#259	Marshtomp	Water/Ground	Torrent
#260	Swampert	Water/Ground	Torrent
#261	Poochyena	Dark	Quick Feet, Run Away
#262	Mightyena	Dark	Intimidate, Quick Feet
#263	Zigzagoon	Normal	Gluttony, Pickup
#264	Linoone	Normal	Gluttony, Pickup
#265	Wurmple	Bug	Shield Dust
#266	Silcoon	Bug	Shed Skin
#267	Beautifly	Bug/Flying	Swarm
#268	Cascoon	Bug	Shed Skin
#269	Dustox	Bug/Poison	Shield Dust
#270	Lotad	Water/Grass	Rain Dish, Swift Swim
#271	Lombre	Water/Grass	Rain Dish, Swift Swim
#272	Ludicolo	Water/Grass	Rain Dish, Swift Swim
#273	Seedot	Grass	Chlorophyll, Early Bird
#274	Nuzleaf	Grass/Dark	Chlorophyll, Early Bird
#275	Shiftry	Grass/Dark	Chlorophyll, Early Bird
#276	Taillow	Normal/Flying	Guts
#277	Swellow	Normal/Flying	Guts
#278	Wingull	Water/Flying	Keen Eye, Hydration
#279	Pelipper	Water/Flying	Keen Eye, Hydration
#280	Ralts	Psychic	Synchronize, Trace
#281	Kirlia	Psychic	Synchronize, Trace
#282	Gardevoir	Psychic	Synchronize, Trace
#283	Surskit	Bug/Water	Swift Swim
#284	Masquerain	Bug/Flying	Intimidate
#285	Shroomish	Grass	Effect Spore, Poison Heal
#286	Breloom	Grass/Fighting	Effect Spore, Poison Heal
#287	Slakoth	Normal	Truant
#288	Vigoroth	Normal	Vital Spirit
#289	Slaking	Normal	Truant
#290	Nincada	Bug/Ground	Compoundeyes
#291	Ninjask	Bug/Flying	Speed Boost
#292	Shedinja	Bug/Ghost	Wonder Guard
#293	Whismur	Normal	Soundproof
#294	Loudred	Normal	Soundproof
#295	Exploud	Normal	Soundproof
#296	Makuhita	Fighting	Guts, Thick Fat
#297	Hariyama	Fighting	Guts, Thick Fat
#298	Azurill	Normal	Huge Power, Thick Fat
#299	Nosepass	Rock	Magnet Pull, Sturdy
#300	Skitty	Normal	Cute Charm, Normalize
#301	Delcatty	Normal	Cute Charm, Normalize
#302	Sableye	Dark/Ghost	Keen Eye, Stall
#303	Mawile	Steel	Hyper Cutter, Intimidate
#304	Aron	Rock/Steel	Rock Head, Sturdy
#305	Lairon	Steel/Rock	Rock Head, Sturdy
#306	Aggron	Steel/Rock	Rock Head, Sturdy
#307	Meditite	Fighting/Psychic	Pure Power
#308	Medicham	Fighting/Psychic	Pure Power
#309	Electrike	Electric	Lightning Rod, Static
#310	Manectric	Electric	Lightning Rod, Static
#311	Plusle	Electric	Lightning Rod
#312	Minun	Electric	Volt Absorb
#313	Volbeat	Bug	Illuminate, Swarm
#314	Illumise	Bug	Oblivious, Tinted Lens
#315	Roselia	Grass/Poison	Natural Cure, Poison Point
#316	Gulpin	Poison	Liquid Ooze, Sticky Hold
#317	Swalot	Poison	Liquid Ooze, Sticky Hold
#318	Carvanha	Water/Dark	Rough Skin
#319	Sharpedo	Water/Dark	Rough Skin
#320	Wailmer	Water	Oblivious, Water Veil
#321	Wailord	Water	Oblivious, Water Veil
#322	Numel	Fire/Ground	Oblivious, Simple
#323	Camerupt	Fire/Ground	Magma Armor, Solid Rock
#324	Torkoal	Fire	White Smoke
#325	Spoink	Psychic	Own Tempo, Thick Fat
#326	Grumpig	Psychic	Own Tempo, Thick Fat
#327	Spinda	Normal	Own Tempo, Tangled Feet
#328	Trapinch	Ground	Arena Trap, Hyper Cutter
#329	Vibrava	Ground/Dragon	Levitate
#330	Flygon	Ground/Dragon	Levitate
#331	Cacnea	Grass	Sand Veil
#332	Cacturne	Grass/Dark	Sand Veil
#333	Swablu	Normal/Flying	Natural Cure
#334	Altaria	Dragon/Flying	Natural Cure
#335	Zangoose	Normal	Immunity, Thick Fat
#336	Seviper	Poison	Shed Skin
#337	Lunatone	Rock/Psychic	Levitate
#338	Solrock	Rock/Psychic	Levitate
#339	Barboach	Water/Ground	Anticipation, Oblivious
#340	Whiscash	Water/Ground	Anticipation, Oblivious
#341	Corphish	Water	Hyper Cutter, Shell Armor
#342	Crawdaunt	Water/Dark	Hyper Cutter, Shell Armor
#343	Baltoy	Ground/Psychic	Levitate
#344	Claydol	Ground/Psychic	Levitate
#345	Lileep	Rock/Grass	Suction Cups
#346	Cradily	Rock/Grass	Suction Cups
#347	Anorith	Rock/Bug	Battle Armor, Swift Swim
#348	Armaldo	Rock/Bug	Battle Armor, Swift Swim
#349	Feebas	Water	Swift Swim
#350	Milotic	Water	Marvel Scale
#351	Castform	Normal	Forecast
#352	Kecleon	Normal	Color Change
#353	Shuppet	Ghost	Frisk, Insomnia
#354	Banette	Ghost	Frisk, Insomnia
#355	Duskull	Ghost	Levitate
#356	Dusclops	Ghost	Pressure
#357	Tropius	Grass/Flying	Chlorophyll, Solar Power
#358	Chimecho	Psychic	Levitate
#359	Absol	Dark	Pressure, Super Luck
#360	Wynaut	Psychic	Shadow Tag
#361	Snorunt	Ice	Ice Body, Inner Focus
#362	Glalie	Ice	Ice Body, Inner Focus
#363	Spheal	Ice/Water	Ice Body, Thick Fat
#364	Sealeo	Ice/Water	Ice Body, Thick Fat
#365	Walrein	Ice/Water	Ice Body, Thick Fat
#366	Clamperl	Water	Shell Armor
#367	Huntail	Water	Swift Swim
#368	Gorebyss	Water	Swift Swim
#369	Relicanth	Water/Rock	Rock Head, Swift Swim
#370	Luvdisc	Water	Swift Swim
#371	Bagon	Dragon	Rock Head
#372	Shelgon	Dragon	Rock Head
#373	Salamence	Dragon/Flying	Intimidate
#374	Beldum	Steel/Psychic	Clear Body
#375	Metang	Steel/Psychic	Clear Body
#376	Metagross	Steel/Psychic	Clear Body
#377	Regirock	Rock	Clear Body
#378	Regice	Ice	Clear Body
#379	Registeel	Steel	Clear Body
#380	Latias	Dragon/Psychic	Levitate
#381	Latios	Dragon/Psychic	Levitate
#382	Kyogre	Water	Drizzle
#383	Groudon	Ground	Drought
#384	Rayquaza	Dragon/Flying	Air Lock
#385	Jirachi	Steel/Psychic	Serene Grace
#386	Deoxys	Psychic	Pressure
#387	Turtwig	Grass	Overgrow
#388	Grotle	Grass	Overgrow
#389	Torterra	Grass/Ground	Overgrow
#390	Chimchar	Fire	Blaze
#391	Monferno	Fire/Fighting	Blaze
#392	Infernape	Fire/Fighting	Blaze
#393	Piplup	Water	Torrent
#394	Prinplup	Water	Torrent
#395	Empoleon	Water/Steel	Torrent
#396	Starly	Normal/Flying	Keen Eye
#397	Staravia	Normal/Flying	Intimidate
#398	Staraptor	Normal/Flying	Intimidate
#399	Bidoof	Normal	Simple, Unaware
#400	Bibarel	Normal	Simple, Unaware
#401	Kricketot	Bug	Shed Skin
#402	Kricketune	Bug	Swarm
#403	Shinx	Electric	Intimidate, Rivalry
#404	Luxio	Electric	Intimidate, Rivalry
#405	Luxray	Electric	Intimidate, Rivalry
#406	Budew	Grass/Poison	Natural Cure, Poison Point
#407	Roserade	Grass/Poison	Natural Cure, Poison Point
#408	Cranidos	Rock	Mold Breaker
#409	Rampardos	Rock	Mold Breaker
#410	Shieldon	Rock/Steel	Sturdy
#411	Bastiodon	Rock/Steel	Sturdy
#412	Burmy	Bug	Shed Skin
#413	Wormadam (Plant)	Bug/Grass	Anticipation
#413	Wormadam (Sandy)	Bug/Ground	Anticipation
#413	Wormadam (Trash)	Bug/Steel	Anticipation
#414	Mothim	Bug/Flying	Swarm
#415	Combee	Bug/Flying	Honey Gather
#416	Vespiquen	Bug/Flying	Pressure
#417	Pachirisu	Electric	Pickup
#418	Buizel	Water	Swift Swim
#419	Floatzel	Water	Swift Swim
#420	Cherubi	Grass	Chlorophyll
#421	Cherrim	Grass	Flower Gift
#422	Shellos	Water	Sticky Hold, Storm Drain
#423	Gastrodon	Water/Ground	Sticky Hold, Storm Drain
#424	Ambipom	Normal	Pickup, Technician
#425	Drifloon	Ghost/Flying	Aftermath, Unburden
#426	Drifblim	Ghost/Flying	Aftermath, Unburden
#427	Buneary	Normal	Klutz, Run Away
#428	Lopunny	Normal	Cute Charm, Klutz
#429	Mismagius	Ghost	Levitate
#430	Honchkrow	Dark/Flying	Insomnia, Super Luck
#431	Glameow	Normal	Limber, Own Tempo
#432	Purugly	Normal	Own Tempo, Thick Fat
#433	Chingling	Psychic	Levitate
#434	Stunky	Poison/Dark	Aftermath, Stench
#435	Skuntank	Poison/Dark	Aftermath, Stench
#436	Bronzor	Steel/Psychic	Heatproof, Levitate
#437	Bronzong	Steel/Psychic	Heatproof, Levitate
#438	Bonsly	Rock	Rock Head, Sturdy
#439	Mime Jr.	Psychic	Filter, Soundproof
#440	Happiny	Normal	Natural Cure, Serene Grace
#441	Chatot	Normal/Flying	Keen Eye, Tangled Feet
#442	Spiritomb	Ghost/Dark	Pressure
#443	Gible	Dragon/Ground	Sand Veil
#444	Gabite	Dragon/Ground	Sand Veil
#445	Garchomp	Dragon/Ground	Sand Veil
#446	Munchlax	Normal	Pickup, Thick Fat
#447	Riolu	Fighting	Inner Focus, Steadfast
#448	Lucario	Fighting/Steel	Inner Focus, Steadfast
#449	Hippopotas	Ground	Sand Stream
#450	Hippowdon	Ground	Sand Stream
#451	Skorupi	Poison/Bug	Battle Armor, Sniper
#452	Drapion	Poison/Dark	Battle Armor, Sniper
#453	Croagunk	Poison/Fighting	Anticipation, Dry Skin
#454	Toxicroak	Poison/Fighting	Anticipation, Dry Skin
#455	Carnivine	Grass	Levitate
#456	Finneon	Water	Swift Swim, Storm Drain
#457	Lumineon	Water	Swift Swim, Storm Drain
#458	Mantyke	Water/Flying	Swift Swim, Water Absorb
#459	Snover	Grass/Ice	Snow Warning
#460	Abomasnow	Grass/Ice	Snow Warning
#461	Weavile	Dark/Ice	Pressure
#462	Magnezone	Electric/Steel	Magnet Pull, Sturdy
#463	Lickilicky	Normal	Oblivious, Own Tempo
#464	Rhyperior	Ground/Rock	Lightning Rod, Solid Rock
#465	Tangrowth	Grass	Chlorophyll
#466	Electivire	Electric	Motor Drive
#467	Magmortar	Fire	Flame Body
#468	Togekiss	Normal/Flying	Hustle, Serene Grace
#469	Yanmega	Bug/Flying	Speed Boost, Tinted Lens
#470	Leafeon	Grass	Leaf Guard
#471	Glaceon	Ice	Snow Cloak
#472	Gliscor	Ground/Flying	Hyper Cutter, Sand Veil
#473	Mamoswine	Ice/Ground	Oblivious, Snow Cloak
#474	Porygon-Z	Normal	Adaptability, Download
#475	Gallade	Psychic/Fighting	Steadfast
#476	Probopass	Rock/Steel	Magnet Pull, Sturdy
#477	Dusknoir	Ghost	Pressure
#478	Froslass	Ice/Ghost	Snow Cloak
#479	Rotom	Electric/Ghost	Levitate
#480	Uxie	Psychic	Levitate
#481	Mesprit	Psychic	Levitate
#482	Azelf	Psychic	Levitate
#483	Dialga	Steel/Dragon	Pressure
#484	Palkia	Water/Dragon	Pressure
#485	Heatran	Fire/Steel	Flash Fire
#486	Regigigas	Normal	Slow Start
#487	Giratina	Ghost/Dragon	Pressure
#488	Cresselia	Psychic	Levitate
#489	Phione	Water	Hydration
#490	Manaphy	Water	Hydration
#491	Darkrai	Dark	Bad Dreams
#492	Shaymin	Grass	Natural Cure
#492	Shaymin (Sky)	Grass/Flying	Serene Grace
'''
