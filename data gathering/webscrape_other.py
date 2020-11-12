import pickle
import re
from pprint import pprint
import variables as v
import requests
from bs4 import BeautifulSoup

### SOUP

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

# for linko in (v.soup_moves):
move_dicto = {}
# page_nr = 1
# page_max = 356
# print(str((page_nr/page_max)*100)[:4] + '%')
url = 'https://bulbapedia.bulbagarden.net/wiki/Scarf_(Mystery_Dungeon)'
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

items = soup.find_all("table", class_="roundy expandable")
x = 0

# print(str(items[1]).partition('Sell')[2].partition('<span class="explain" title="Red')[0][:-4])

for item in range(len(items)):
    if 'GEN III' in str(items[item]):
        pass
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


# 29 GEN III

'''

'''

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


