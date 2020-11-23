import pickle
import re
from _csv import reader
from pprint import pprint
import variables as v
import requests
from bs4 import BeautifulSoup

# Open the input_file in read mode and output_file in write mode
with open('SpinoffDex Project\\csv\\spinoffDexDataset.csv', 'r', encoding='utf-8') as read_obj:
    # Create a csv.reader object from the input file object
    csv_reader = reader(read_obj)
    # Create a csv.writer object from the output file object
    # Read each row of the input csv file as list

    pokemon_nr = 0
    for row in csv_reader:
        print(row)

### SOUP
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
# # page_nr = 1
# # page_max = 356
# # print(str((page_nr/page_max)*100)[:4] + '%')
# url = 'https://bulbapedia.bulbagarden.net/wiki/Scarf_(Mystery_Dungeon)'
# req = requests.get(url, headers)
# soup = BeautifulSoup(req.content, 'html.parser')
#
# items = soup.find_all("table", class_="roundy expandable")
# x = 0
#
# accessories = []
# for item in range(len(items)):
#     if 'GEN III' in str(items[item]):
#         item_name = (str(items[item]).partition('<big><big><b>')[2].partition('</b>')[0])
#         japanese_item_name = (str(items[item]).partition('</big><br/><small><b>')[2].partition('</i>')[0].replace('</b> <i>', ' / ').replace('<a href="/wiki/Munchlax_(Pok%C3%A9mon)" title="Munchlax (Pokémon)">Gonbe</a> Stomach Band', 'Gonbe Stomach Band'))
#         if 'Blue Rescue' in (str(items[item]).partition('currency.png" width="18"/></a>')[2].partition('Sell')[0]):
#             buy_price = (str(items[item]).partition('<span class="explain" title="Red Rescue Team and Blue Rescue Team">')[0][-4:])
#         else:
#             buy_price = (str(items[item]).partition('currency.png" width="18"/></a>')[2].partition('</small>')[0])
#         if 'Blue Rescue' in (str(items[item]).partition('Sell')[2].partition('</small>')[0]):
#             sell_price = (str(items[item]).partition('Sell')[2].partition('<span class="explain" title="Red')[0][-4:].replace('>', '').replace('/', '').replace('a', ''))
#         elif 'All games except' in (str(items[item]).partition('Sell')[2].partition('</small>')[0]):
#             sell_price = (str(items[item]).partition('Sell')[2].partition('<span class="explain" title="All games except')[0][-4:].replace('>', '').replace('/', '').replace('a', ''))
#         else:
#             sell_price = (str(items[item]).partition('Sell')[2].partition('currency.png" width="18"/></a>')[2].partition('<')[0])
#         effect = (str(items[item]).partition('Effect:</b>\n</td>\n<td>')[2].partition('</td>')[0].partition('<b>')[0][1:]
#                   .replace('<a href="/wiki/Statistic#Belly" title="Statistic">', '').replace('</a>', '')
#                   .replace('<a href="/wiki/Adventure_Log" title="Adventure Log">', '').replace('<br/>', ' ')
#                   .replace('<a class="new" href="/w/index.php?title=Status_ailments_in_Mystery_Dungeon&amp;action=edit&amp;redlink=1" title="Status ailments in Mystery Dungeon (page does not exist)">', '')
#                   .replace('<a class="mw-redirect" href="/wiki/Status_conditions_in_the_Mystery_Dungeon_series#Immobilized_by_hunger" title="Status conditions in the Mystery Dungeon series">', '')
#                   .replace('Prevents Attack and Special Attack lowering', 'Prevents Attack and Special Attack lowering.')
#                   .replace('Its Belly will go down by 5', 'Its Belly will go down by 5 every time it walks through a wall tile. If player takes it down while in wall, Pokémon will randomly warp out of wall.')
#                   .replace(' In all games except Explorers of Sky, this item can be used for a <a href="/wiki/List_of_glitches_in_spin-off_games#Kecleon_team_member_glitch" title="List of glitches in spin-off games">glitch.', '')
#                   .replace('\n', ''))
#         locations = []
#         loc_string = (str(items[item]).partition('Red Rescue Team and Blue Rescue Team"><span style="color:#000000;">MD</span><span style="color:#C50C50;">R</span><span style="color:#095BAF;">B</span></a></b>\n</td>')[2].partition('<tr style="vertical-align:top">')[0].split('<br/>'))
#         for br in loc_string:
#             br = br.replace('</td></tr>', '').replace('\n', '')
#             br = br.replace('First part only', 'first part only')
#
#             if 'Kecleon Shop' in br:
#                 br = br.replace('<td style="border-top: 1px solid #7C4B2D"> ', '')
#                 prev = br
#                 br_str = ''
#                 if '<a ' in br:
#                     br_str += br.partition('<a ')[0]
#
#                 if br.count('<a '):
#                     for href in range(br.count('<a ')):
#                         br_str += prev.partition('title="')[2].partition('"')[0]
#                         prev = prev.partition('</a>')[2]
#                         br_str += prev.partition('<a ')[0]
#                 else:
#                     br_str = br
#
#                 if '(' in br_str and ')' not in br_str:
#                     br_str += ')'
#                 if 'Kecleon Shop (Purity Forest)</table><tr><td class="roundy" colspan="5" ' in br_str:
#                     br_str = 'Kecleon Shop (Purity Forest)'
#                 locations.append([br_str])
#             elif 'Buried items' in br:
#                 prev = br
#                 br_str = ''
#                 if '<a class=' in br:
#                     br_str += br.partition('<a ')[0]
#
#                 if br.count('<a '):
#                     for hclass in range(br.count('<a ')):
#                         br_str += prev.partition('title="')[2].partition('"')[0]
#                         prev = prev.partition('</a>')[2]
#                         br_str += prev.partition('<a ')[0]
#                 else:
#                     br_str = br
#
#                 if 'Pokémon Mystery Dungeon: Red Rescue Team and Blue Rescue Team</b></td><td style="border-top: 1px solid #7C4B2D"> A hold item that makes' in br_str:
#                     br_str = 'Buried items (Far-off Sea)'
#                 elif '7C4B2D"> A hold item that slows how quickly the Pokémo' in br:
#                     br_str = 'Buried items (Far-off Sea)'
#                 locations.append([br_str])
#             elif 'Job ' in br:
#                 locations.append([('Job' + br.partition('</a>')[2])])
#             elif 'Reward from Gengar' in br:
#                 locations.append([('Reward from Gengar after escorting him through Murky Cave')])
#             else:
#                 if 'Pokemon Square' in br and 'shop' in br:
#                     shop = ' shop'
#                 else:
#                     shop = ''
#                 prev = br
#                 br_str = br.partition('<')[0]
#
#                 for hclass in range(br.count('title')):
#                     if 'shop' not in br_str:
#                         br_str += prev.partition('title="')[2].partition('"')[0] + shop + ', '
#                     else:
#                         br_str += prev.partition('title="')[2].partition('"')[0] + ', '
#                     br_str = br_str.replace(', first part only', ' (First part only)').replace('\n', '')
#                     prev = prev.partition('title=')[2]
#                 if br_str[-2:] == ', ':
#                     br_str = br_str[:-2]
#                 if 'Diglett' in br:
#                     br_str = 'Reward for saving Diglett'
#                 if 'Munchlax' in br:
#                     br_str = 'Give food to Munchlax, which appears at one point in Pokémon Square'
#                 locations.append([br_str])
#         description = (str(items[item]).partition('Description')[2].partition('<td style="border-top: 1px solid #7C4B2D"> ')[2].partition('</td>')[0].replace('\n', ''))
#         item_data = [[item_name], [japanese_item_name], [buy_price], [sell_price], [effect], [locations], [description]]
#         accessories.append([item_data])
#
# print(accessories)
#######################
#######################

# if '_' in move_name:
#     move_name = (move_name.replace('_', ' '))
# descript = (str(soup.find_all("div", class_="pi-data-value pi-font")[count-1]).partition('pi-font">')[2].partition('</div>')[0])

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


