# Library for opening url and creating
# requests
import urllib.request

# pretty-print python data structures 
from pprint import pprint

# for parsing all the tables present  
# on the website
from html_table_parser import HTMLTableParser

# for converting the parsed data in a 
# pandas dataframe 
import pandas as pd


# Opens a website and read its 
# binary contents (HTTP Response Body) 
def url_get_contents(url):
    # Opens a website and read its
    # binary contents (HTTP Response Body) 

    # making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)

    # reading contents of the website
    return f.read()


# defining the html contents of a URL.
xhtml = url_get_contents('https://www.serebii.net/spindex/001.shtml').decode('cp1252')

# define string
substring = 'size.png'
size_count = xhtml.count(substring) # To deterimine if pokemon is size *, or size ****

# Defining the HTMLTableParser object
p = HTMLTableParser()

# feeding the html contents in the 
# HTMLTableParser object 
p.feed(xhtml)

# Now finally obtaining the data of 
# the table required
#nr = 9  # 6-11
general_info_dict = {}
mystery_dungeon_dict = {}
ranger_dict = {}
get_dict = {}
dungeon_levelup_moves_dict = {}
tms_hms_dict = {}

dicts = {6: general_info_dict,
         7: mystery_dungeon_dict,
         8: ranger_dict,
         9: get_dict,
         10: dungeon_levelup_moves_dict,
         11: tms_hms_dict}

def remove_unneeded_rows():
    for x in range(6, 12):
        if x != 6:
            del p.tables[x][0]

def generate():
    remove_unneeded_rows()
    for x in range(6, 12):
        for y in range(0, len(p.tables[x])-1, 2):
            if x == 6:
                # print(p.tables[6][0])  # first 5 names
                # print(p.tables[6][1])  # first 5 data
                # print(p.tables[6][2])  # ability
                # print(p.tables[6][3])  # Ability description
                # print(p.tables[6][4])  # second 5 names
                # print(p.tables[6][5])  # second 5 data
                # print(p.tables[6][6])  # evo
                # print(p.tables[6][7])  # evo data
                for lists_counter in range(1, 8, 2):
                    nested_list = []
                    col_name = p.tables[x][lists_counter - 1]
                    if lists_counter in (1, 5):
                        for sublist_counter in range(5):
                            nested_list = []
                            # print(col_name[sublist_counter], sublist_counter)
                            # print(p.tables[x][lists_counter][sublist_counter], '\n')
                            nested_list.append(p.tables[x][lists_counter][sublist_counter])
                            dicts[x][col_name[sublist_counter]] = nested_list
                    else:
                        # print(str(col_name[0]), lists_counter)
                        # print(p.tables[x][lists_counter][0], '\n')
                        if lists_counter == 3:
                            nested_list.append(p.tables[x][lists_counter][0])
                        else:
                            nested_list.append(p.tables[x][lists_counter][0])
                        dicts[x][col_name[0]] = nested_list

            if x in (7, 8, 9, 10, 11):
                for lists_counter in range(len(p.tables[x][0])):
                    nested_list = []
                    for moves_counter in range(len(p.tables[x])):
                        col_name = p.tables[x][0][lists_counter]
                        if moves_counter > 0:
                            nested_list.append(p.tables[x][moves_counter][lists_counter])
                        if x == 1:
                            print('wtf')
                        else:
                            dicts[x][col_name] = nested_list
                    if x == 7 and col_name == 'Body Size':
                        dicts[x][col_name] = '*' * size_count


#pprint(p.tables[11][0][2])

# for x in (p.tables[11]):
#     print(x)

# for lists_counter in range(len(p.tables[11][0])):
#     nested_list = []
#     for moves_counter in (p.tables[11]):
#         print(moves_counter[0])


def print_dicts():
    for i in range(6, 12):
        print('===', i, '===')
        for j in dicts[i].items():
            print(j)

generate()
# === Print Dicts ===
print_dicts()

# === Save to CSV ===
#pd.DataFrame(dicts[6]).to_csv('out.csv', index=False)
