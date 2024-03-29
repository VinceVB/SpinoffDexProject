import os
import random
from functools import partial
from csv import reader

from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout

import variables as v

from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.metrics import dp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView


class SpinoffDex(Screen):
    def __init__(self, **kwargs):
        super(SpinoffDex, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.on_back_btn)

    def on_back_btn(self, window, key, *args):
        # If user presses Back/Esc Key
        if key == 27:
            # Check if any previous screens are in the list
            if self.ids.manager.list_of_prev_screens:
                # If there are, go to the previous and remove it from the list
                self.ids.manager.current = self.ids.manager.list_of_prev_screens.pop()
                return True
            return False
        return False

    def add_dex_entries(self):
        # skip first line i.e. read header first and then iterate over each row od csv as a list
        with open('csv/SpinoffDexDataset.csv', 'r', encoding='utf-8') as read_obj:
            csv_reader = reader(read_obj)
            header = next(csv_reader)
            # Check file as empty
            if header:
                # Iterate over each row after the header in the csv
                current_entries = 0
                for row in csv_reader:
                    if current_entries < v.max_entries:
                        # Entry ID
                        dex_entry = DexEntry()
                        dex_entry.page = row[1]

                        # Remove default grey button background if joined; color becomes brighter
                        if row[7] == 'True':
                            dex_entry.background_normal = ''
                        else:
                            dex_entry.background_normal = 'atlas://data/images/defaulttheme/button'
                        dex_entry.background_color = v.color_codes[row[5]]
                        self.ids.md_dex_grid.add_widget(dex_entry)

                        # # Entry Image
                        dex_image_box = AnchorLayout(size_hint_x=0.25, anchor_x='center', anchor_y='center')
                        dex_image = Image(source='img//portraits//' + row[2][1:] + '.png', size_hint_x=None, width=dp(40), allow_stretch=True)
                        dex_image_box.add_widget(dex_image)
                        dex_entry.add_widget(dex_image_box)

                        # GridLayout containing the non-portrait widgets
                        dex_grid = GridLayout(cols=2, size_hint_x=0.75)
                        dex_entry.add_widget(dex_grid)
                        # Entry Dex Number / Pokemon Name
                        dex_number = Label(text=row[2], size_hint_x=0.25)
                        dex_grid.add_widget(dex_number)
                        dex_name = Label(text=row[3], size_hint_x=0.75)
                        dex_grid.add_widget(dex_name)

                        # Entry Pokemon Types
                        dex_type1 = Label(text=row[5], size_hint_x=0.25)
                        dex_grid.add_widget(dex_type1)
                        dex_type2 = Label(text=row[6], size_hint_x=0.75)
                        dex_grid.add_widget(dex_type2)

                        current_entries += 1

    def dex_search(self, query):
        print(self.ids.manager.list_of_prev_screens)
        scroller = self.ids.dex_list_scroller
        dropdown = DropDown()
        self.ids.dex_searchbar.text = ''  # Reset searchbar

        # If query is numerical (a pokedex nr)
        if str.isdigit(query):
            # If nr is not in available pokedex
            if int(query) > v.max_entries or int(query) <= 0:
                self.popup('Error: Number not found', '')

            # Valid nrs
            elif v.max_entries >= int(query) > 0:
                self.ids.dex_searchbar.text = ''
                scroller.scroll_to(scroller.children[0].children[v.max_entries-int(query)])  # scroll to searched mon
            # Probably unnecessary but just in case
            else:
                self.ids.dex_searchbar.text = ''
                self.popup('Unknown Error', '')

        # Non numerical queries / strings
        else:
            with open('csv/SpinoffDexDataset.csv', 'r', encoding='utf-8') as read_obj:
                csv_reader = reader(read_obj)
                next(csv_reader, None)  # Skip header
                query_hits = []  # Whatever matches with the query goes in here

                for row in csv_reader:
                    # A complete match e.g. 'bulbasaur' == 'bulbasaur'
                    if query.lower() == row[3].lower():
                        # break out of loop (No further searching required)
                        query_hits.append([row[2], row[3]])
                        break
                    # A partial match e.g. 'bulb' is in 'bulbasaur'
                    elif query.lower() in row[3].lower():
                        # Add whatever was partially matched to the list, continue loop
                        query_hits.append([row[2], row[3]])

                # If there is at least one match
                if len(query_hits) != 0:
                    for hit in query_hits:
                        '''Should find a less spaghetti way to to style the dropdown widgets (BoxButton), couldn't get
                           a proper background for them as regular BoxLayouts containing an Image and a Label, so it
                           now inherits from Button to not make the whole thing transparent for now'''

                        # Height needs to be set manually for dropdown elements, size_hint_y must be None
                        hit_box = BoxButton(size_hint=(None, None), height=dp(50), width=self.ids.dex_searchbar.width)
                        # # Entry Image
                        hit_image_box = AnchorLayout(size_hint_x=0.25, anchor_x='center', anchor_y='center')
                        hit_image = Image(source='img//portraits//' + hit[0][1:] + '.png', size_hint_x=None, width=dp(40), allow_stretch=True)
                        hit_image_box.add_widget(hit_image)
                        hit_btn = Label(text=hit[0] + ' ' + hit[1], text_size=hit_box.size, valign='center', padding_x=5, size_hint_x=0.75)
                        hit_btn.bind(size=hit_btn.setter('text_size'))
                        hit_box.add_widget(hit_image_box)
                        hit_box.add_widget(hit_btn)

                        # Call the select() method on the dropdown, pass the text of the Label as the selection data
                        hit_box.bind(on_release=lambda hit_box2: dropdown.select(hit_box2.children[0].text))

                        # Add the BoxLayout containing the other content as a dropdown element
                        dropdown.add_widget(hit_box)

                # If nothing is found
                else:
                    self.popup('Error: No matches', '')

                dropdown.bind(on_select=lambda instance, x: self.change_page(int(x[1:4])))  # Change to selected mon's page
                dropdown.open(self.ids.dex_searchbar)  # Open dropdown menu below searchbar
                query_hits.clear()  # Reset query results

    @staticmethod
    def read_csv(row, column):
        with open('csv/SpinoffDexDataset.csv', encoding='utf-8') as read_obj:
            csv_reader = reader(read_obj)
            rows = list(csv_reader)
            return rows[row][column]

    def set_stats(self, pokedex_nr):
        self.ids.dex_base_stats.clear_widgets()
        prev_stat = self.read_csv(int(pokedex_nr), 35).partition('],  [1, ')[2].partition('],  [')[0]
        for stat_lbl in range(5):
            next_stat = prev_stat.partition(',')
            stat_label = Label(text=next_stat[0], font_size='14sp', text_size=self.ids.dex_base_stats.size, halign='center', valign='top')
            prev_stat = next_stat[2]
            self.ids.dex_base_stats.add_widget(stat_label)
        stat_label = Label(text=self.read_csv(int(pokedex_nr), 32), font_size='14sp', text_size=self.ids.dex_base_stats.size, halign='center', valign='top')
        self.ids.dex_base_stats.add_widget(stat_label)

    def set_types(self, pokedex_nr):
        # Reset type Label heights
        self.general_type1.height = self.general_type1.parent.height/2
        self.general_type2.height = self.general_type2.parent.height/2

        type1 = self.read_csv(int(pokedex_nr), 5)
        type2 = self.read_csv(int(pokedex_nr), 6)
        self.general_type1.text = type1
        self.general_type2.text = type2

        # Get color values from variables
        self.general_type1.background_color = v.color_codes[type1]
        self.general_type2.background_color = v.color_codes[type2]

        # If there is no type2, set type1 to full height instead of half, and type2 to 0
        if not type2:
            self.general_type1.height = self.general_type1.parent.height
            self.general_type2.height = 0

    def set_md_body_size(self, pokedex_nr):
        body_size = self.read_csv(int(pokedex_nr), 16)
        body_size_str = str(len(body_size))
        self.ids.md_body_size.source = 'img//misc//size' + body_size_str + '.png'
        self.ids.md_body_size.width = dp(15 * int(body_size_str))

    def set_abilities(self, abilities):
        ability_1 = abilities.partition(' & ')[0]  # Partition the string to exclude a potential second ability
        self.ids.md_ability1.text = ability_1              # Ability name
        self.ids.md_ability1.bind(on_release=partial(self.popup, ability_1, v.md_abilities[ability_1], '14sp'))  # Popup window with description

        # If there are two abilities, add another
        if '&' in abilities:
            ability_2 = abilities.partition(' & ')[2]
            self.ids.md_ability2.text = ability_2
            self.ids.md_ability2.bind(on_release=partial(self.popup, ability_2, v.md_abilities[ability_2], '14sp'))

            # Reset ability 2 and separator_y in case they were shrunk
            self.ids.md_ability2.size_hint = (1, 1)
            self.ids.md_ability_sep.width = '2dp'
        else:
            # Make ability 2 and separator_y 0 in size so ability 1 takes up full space
            self.ids.md_ability2.text = ''
            self.ids.md_ability2.size_hint = (None, None)
            self.ids.md_ability2.size = 0, 0
            self.ids.md_ability_sep.width = '0dp'

    def set_location(self, pokedex_nr):
        self.ids.md_location.clear_widgets()  # Reset location widget
        lvl_string = self.read_csv(int(pokedex_nr), 37)
        current_string = lvl_string
        for loc in range(max(1, current_string.count('/_/'))):
            if 'Floor' in current_string.partition('/_/')[0]:
                loc_1 = BoxLayout(size_hint=(None, None), size=(self.ids.md_location.width, '25dp'))
                loc_1_zone = Label(text=current_string.partition(' - ')[2].partition(' (')[0], size_hint=(None, None), size=(self.ids.md_location.width*0.45, '25dp'))
                loc_1_lv = Label(text=current_string.partition(' - ')[0], size_hint=(None, None), size=(self.ids.md_location.width*0.175, '25dp'))
                loc_1_floors = Button(text=current_string.partition(' (')[2].partition(')')[0], size_hint=(None, None), size=(self.ids.md_location.width*0.375, '25dp'), background_color=(0, 0, 0, 0))
                loc_1_floors.bind(on_release=partial(self.popup, loc_1_zone.text, ('Found ' + loc_1_floors.text + ' at ' + loc_1_lv.text), '12sp'))

                floor_copy = loc_1_floors.text

                if len(loc_1_floors.text) > 15:
                    loc_1_floors.font_size = '12sp'
                    if len(loc_1_floors.text) > 17:
                        loc_1_floors.text = floor_copy[:17] + '...'

                if 'Unown' in loc_1_zone.text:
                    unown_letter = loc_1_lv.text.partition(' Lv')[0]
                    loc_1_lv.text = loc_1_lv.text.partition(') ')[2]
                    loc_1_zone.width = self.ids.md_location.width*0.30
                    loc_1_zone.font_size = '12sp'
                    loc_1_letter = Label(text=unown_letter, size_hint=(None, None),
                                         size=(self.ids.md_location.width * 0.15, '25dp'), font_size='12sp')
                    loc_1.add_widget(loc_1_letter)
                    sep = SeparatorY()
                    loc_1.add_widget(sep)
                    loc_1_floors.bind(on_release=partial(self.popup, loc_1_zone.text,
                                                         ('Found ' + floor_copy + ' at ' + loc_1_lv.text.partition('(')[0] + loc_1_lv.text.partition(')')[2]),
                                                         '12sp'))

                loc_1.add_widget(loc_1_zone)
                sep = SeparatorY(size_hint_y=None, height=loc_1.height-dp(2), pos_hint={'top': 1})
                loc_1.add_widget(sep)
                loc_1.add_widget(loc_1_lv)
                sep = SeparatorY(size_hint_y=None, height=loc_1.height-dp(2), pos_hint={'top': 1})
                loc_1.add_widget(sep)
                loc_1.add_widget(loc_1_floors)

                is_box = True

            else:
                loc_1 = Button(text=current_string.partition('/_/')[0], size_hint=(None, None),
                               size=(self.ids.md_location.width, '25dp'), font_size=dp(14), background_color=(0, 0, 0, 0))
                is_box = False

            if not is_box:
                # Reduce font_size for larger strings
                if len(loc_1.text) > 40:
                    loc_1.font_size = dp(12)
                sep = SeparatorX()
                if loc_1.text[:6] == 'Evolve':
                    if lvl_string.count('/_/') == 0:
                        self.ids.md_location.add_widget(loc_1)
                        self.ids.md_location.add_widget(sep)
                else:
                    self.ids.md_location.add_widget(loc_1)
                    self.ids.md_location.add_widget(sep)
            else:
                self.ids.md_location.add_widget(loc_1)
                sep = SeparatorX()
                self.ids.md_location.add_widget(sep)

            current_string = current_string.partition('/_/')[2]

    def check_joined(self, pokedex_nr):
        joined = self.read_csv(int(pokedex_nr), 7)

        if joined == 'True':
            return 'img//misc//joined.png'
        else:
            return 'img//misc//not_joined.png'

    def md_join(self, pokedex_nr):
        with open('csv//SpinoffDexDataset.csv', 'r', encoding='utf-8') as readFile, open(
                'csv//temp_SpinoffDexDataset.csv', 'w', encoding='utf-8') as writeFile:
            cnt = 0
            for row in readFile:
                if cnt == int(pokedex_nr):
                    str1 = row.partition(',')
                    str2 = str1[2].partition(',')
                    str3 = str2[2].partition(',')
                    str4 = str3[2].partition(',')
                    str5 = str4[2].partition(',')
                    str6 = str5[2].partition(',')
                    str7 = str6[2].partition(',')
                    str_joined = str7[2].partition(',')
                    if str_joined[0] == 'True':
                        joined = 'False'
                    else:
                        joined = 'True'

                    str_all = str1[0] + ',' + str2[0] + ',' + str3[0] + ',' + str4[0] + ',' + str5[0] + ',' + str6[
                        0] + ',' + str7[0] + ',' + joined + ',' + str_joined[2]
                    writeFile.write(str_all)
                else:
                    writeFile.write(row)
                cnt += 1
        os.remove('csv//SpinoffDexDataset.csv')
        os.rename('csv//temp_SpinoffDexDataset.csv', 'csv//SpinoffDexDataset.csv')

        if self.read_csv(int(pokedex_nr), 7) == 'True':
            self.ids.md_joined.source = 'img//misc//joined.png'  # Set joined image
            self.ids.md_dex_grid.children[v.max_entries - int(pokedex_nr)].background_normal = ''  # set brighter background color
        else:
            self.ids.md_joined.source = 'img//misc//not_joined.png'  # set not joined image
            self.ids.md_dex_grid.children[v.max_entries - int(pokedex_nr)].background_normal =\
                'atlas://data/images/defaulttheme/button'  # set darker background color

    def unown_check(self, pokedex_nr):
        # Set font size lower for Unown's Location text because it contains a shitload of locations
        # Also makes the app choose a random friend area as the collective Unown species has 2 (Aged Chamber AN / O?)
        if pokedex_nr == '201':
            self.ids.md_get_rate.font_size = '11dp'
            flip = random.randint(0, 1)  # Flip a 'coin' to pick a friend area
            if flip:
                self.ids.md_friend_area.background_normal = 'img//friend areas//Aged Chamber AN.png'
            else:
                self.ids.md_friend_area.background_normal = 'img//friend areas//Aged Chamber O.png'

        else:
            self.ids.md_get_rate.font_size = '12dp'

    def set_accessories(self):
        self.md_accessories.clear_widgets()  # Reset Widget

        for acc in v.md_accessories:
            row_top = TintedLabel(size_hint=(1, None), height=dp(50), text=acc[0][0][0])
            self.md_accessories.add_widget(row_top)

            box = BoxLayout(orientation='vertical', size_hint=(1, None), height=dp(40))
            row1 = BoxLayout(orientation='horizontal', size_hint=(1, 0.25))

            icon_anch = AnchorLayout(anchor_x='center', anchor_y='center', size_hint=(None, None), size=(self.width*0.15-dp(2), dp(40)))
            icon = Image(source='img//items//scarf.png', size_hint_x=None, width=dp(20), allow_stretch=True)
            icon_anch.add_widget(icon)
            buy = Label(text='Buy: ' + acc[0][2][0], size_hint=(None, None), size=(self.width*0.45-dp(2), dp(40)))
            sell = Label(text='Sell: ' + acc[0][3][0], size_hint=(None, None), size=(self.width*0.45-dp(2), dp(40)))
            # jname = Button(text=acc[0][1][0], size_hint=(0.45, 1), font_size='12sp')

            row1.add_widget(icon_anch)
            sep = SeparatorY(size_hint_y=None, height=icon_anch.height-dp(2), pos_hint={'top': 1})
            row1.add_widget(sep)
            row1.add_widget(buy)
            sep = SeparatorY(size_hint_y=None, height=icon_anch.height-dp(2), pos_hint={'top': 1})
            row1.add_widget(sep)
            row1.add_widget(sell)

            sep = SeparatorY(size_hint_y=None, height=icon_anch.height-dp(2), pos_hint={'top': 1})
            row1.add_widget(sep)
            sep = SeparatorY(size_hint_y=None, height=icon_anch.height-dp(2), pos_hint={'top': 1})
            row1.add_widget(sep)
            # row1.add_widget(jname)

            box.add_widget(row1)
            self.md_accessories.add_widget(box)

            sep = SeparatorX()
            self.md_accessories.add_widget(sep)

            # Description
            row_2_desc = TintedLabel(text='Description', size_hint=(1, None), height=dp(30), font_size='12sp')
            self.md_accessories.add_widget(row_2_desc)
            row2 = WrapLabel(text=acc[0][6][0], size_hint=(None, None), size=(self.width*1, dp(40)), font_size='12sp')
            self.md_accessories.add_widget(row2)

            # Effect
            sep = SeparatorX()
            self.md_accessories.add_widget(sep)
            row_3_desc = TintedLabel(text='Effect', size_hint=(1, None), height=dp(30), font_size='12sp')
            self.md_accessories.add_widget(row_3_desc)
            row3 = WrapLabel(text=acc[0][4][0], size_hint=(None, None), size=(self.width*1, dp(40)), font_size='12sp')
            self.md_accessories.add_widget(row3)
            sep = SeparatorX()
            self.md_accessories.add_widget(sep)

            row_4_desc = TintedLabel(text='Location', size_hint=(1, None), height=dp(30), font_size='12sp')
            self.md_accessories.add_widget(row_4_desc)
            row4 = WrapLabel(text=acc[0][5][0][0][0], size_hint=(None, None), size=(self.width*1, dp(40)), font_size='12sp')
            self.md_accessories.add_widget(row4)

            if(len(acc[0][5][0])) > 1:
                row4_1 = WrapLabel(text=acc[0][5][0][1][0], size_hint=(None, None), size=(self.width * 1, dp(40)),
                                 font_size='12sp')
                self.md_accessories.add_widget(row4_1)
                if (len(acc[0][5][0])) > 2:
                    row4_2 = WrapLabel(text=acc[0][5][0][2][0], size_hint=(None, None), size=(self.width * 1, dp(40)),
                                       font_size='12sp')
                    self.md_accessories.add_widget(row4_2)
                    if (len(acc[0][5][0])) > 3:
                        row4_3 = WrapLabel(text=acc[0][5][0][3][0], size_hint=(None, None),
                                           size=(self.width * 1, dp(40)),
                                           font_size='12sp')
                        self.md_accessories.add_widget(row4_3)
                        if (len(acc[0][5][0])) > 4:
                            row4_4 = WrapLabel(text=acc[0][5][0][4][0], size_hint=(None, None),
                                               size=(self.width * 1, dp(40)),
                                               font_size='12sp')
                            self.md_accessories.add_widget(row4_4)

            sep = SeparatorX()
            self.md_accessories.add_widget(sep)
            whitespace = WhiteLabel(size_hint=(1, None), height=dp(20))
            self.md_accessories.add_widget(whitespace)

    def set_gummis(self, pokedex_nr):
        self.md_gummis_box.clear_widgets()  # Reset Widget

        # Strings from the csv file
        gummi_string = self.read_csv(int(pokedex_nr), 34).lower()               # Entire Favourite Gummis string from csv file
        gummi_1 = (gummi_string.partition(', ')[0])                             # Gummi 1 string
        gummi_2 = (gummi_string.partition(', ')[2])                             # Gummi 2 string (Empty if not applicable)
        gummi_1_color = gummi_1.partition(' (')[0]                              # Gummi 1 string with IQ amount removed
        gummi_1_amount = gummi_1.partition('(')[1] + gummi_1.partition('(')[2]  # Gummi 1 string, only IQ amount
        gummi_2_color = gummi_2.partition(' (')[0]                              # Gummi 2 string with IQ amount removed
        gummi_2_amount = gummi_1.partition('(')[1] + gummi_2.partition('(')[2]  # Gummi 2 string, only IQ amount

        # Gummi Image and IQ amount Buttons
        md_gummi_1_anc = AnchorLayout(anchor_x='center', anchor_y='center', size_hint=(0.25, 1))
        md_gummi_1_color = ImageButton(source='img//gummis//' + gummi_1_color + '_gummi.png', size_hint_x=None, width=dp(12), allow_stretch=True)
        md_gummi_1_anc.add_widget(md_gummi_1_color)
        md_gummi_1_amount = Button(text=gummi_1_amount, background_color=(0, 0, 0, 0), size_hint=(0.25, 1), font_size='14sp')

        # Binding for Popup with IQ information
        md_gummi_1_color.bind(on_release=partial(self.popup, gummi_1_color + ' Gummi', 'IQ Gained: ' + gummi_1_amount + v.iq_string, '12sp'))
        md_gummi_1_amount.bind(on_release=partial(self.popup, gummi_1_color + ' Gummi', 'IQ Gained: ' + gummi_1_amount + v.iq_string, '12sp'))

        md_gummi_1_box = BoxLayout(orientation='horizontal')   # Boxlayout to contain the above 2
        md_gummi_1_padding_left = Label(size_hint=(0.25, 1))   # These 2 are to center the other elements in the box, otherwise
        md_gummi_1_padding_right = Label(size_hint=(0.25, 1))  # the gummi image and the label are too far apart, should find a better way later

        md_gummi_1_box.add_widget(md_gummi_1_padding_left)   # Empty label to center other 2 widgets, and make them smaller
        md_gummi_1_box.add_widget(md_gummi_1_anc)            # Add the gummi image
        md_gummi_1_box.add_widget(md_gummi_1_amount)         # Add the IQ amount label
        md_gummi_1_box.add_widget(md_gummi_1_padding_right)  # Empty label to center other 2 widgets, and make them smaller

        self.md_gummis_box.add_widget(md_gummi_1_box)        # Add all the stuff to the box to contain it all
        # If applicable, do the same for second gummi
        if gummi_2:
            md_gummi_2_anc = AnchorLayout(anchor_x='center', anchor_y='center', size_hint=(0.25, 1))
            md_gummi_2_color = ImageButton(source='img//gummis//' + gummi_2_color + '_gummi.png', size_hint_x=None, width=dp(12), allow_stretch=True)
            md_gummi_2_anc.add_widget(md_gummi_2_color)
            md_gummi_2_amount = Button(text=gummi_2_amount, background_color=(0, 0, 0, 0), size_hint=(0.25, 1))
            md_gummi_2_color.bind(on_release=partial(self.popup, gummi_2_color + ' Gummi', 'IQ Gained: ' + gummi_2_amount + v.iq_string, '12sp'))
            md_gummi_2_amount.bind(on_release=partial(self.popup, gummi_2_color + ' Gummi', 'IQ Gained: ' + gummi_2_amount + v.iq_string, '12sp'))
            md_gummi_2_box = BoxLayout(orientation='horizontal')
            md_gummi_2_padding_left = Label(size_hint=(0.25, 1))
            md_gummi_2_padding_right = Label(size_hint=(0.25, 1))
            md_gummi_2_box.add_widget(md_gummi_2_padding_left)
            md_gummi_2_box.add_widget(md_gummi_2_anc)
            md_gummi_2_box.add_widget(md_gummi_2_amount)
            md_gummi_2_box.add_widget(md_gummi_2_padding_right)
            self.md_gummis_box.add_widget(md_gummi_2_box)

    def evolve(self, evo_method, evo_mon):
        # evo_method = 'Lv. xx' / 'Water Stone' /
        # evo_mon = 005 / 032 / 236 etc.

        # Check if level based evo, but first evo isn't IQ based (e.g. Azurill)
        if 'Lv' in evo_method:
            if 'IQ' not in evo_method.partition(' -->')[0]:
                evo_lvl = Label(text=evo_method, font_size=dp(11))  # Label with text of evolution level
                evo_mon_anch = AnchorLayout(anchor_x='center', anchor_y='center')
                evo_mon_img = ImageButton(source='img//portraits//' + evo_mon + '.png', size_hint_x=None, width=dp(40),
                                          allow_stretch=True, on_release=self.change_page_image)  # Stage 1 mon img
                evo_mon_anch.add_widget(evo_mon_img)
                self.ids.md_evo_box.add_widget(evo_lvl)
                self.ids.md_evo_box.add_widget(evo_mon_anch)
            else:
                print('Probably delete later, just seeing if this ever gets triggered\n'*500)

        # Non level based evos
        else:
            evo_box = BoxLayout()  # Widget to contain multiple evo items and '+' Label
            evo1_iq_amount_label = ''  # Empty placeholder string used as boolean to check for IQ based evos

            evo_mon_anch = AnchorLayout(anchor_x='center', anchor_y='center')
            evo_mon_img = ImageButton(source='img//portraits//' + evo_mon + '.png', size_hint_x=None, width=dp(40),
                                      allow_stretch=True, on_release=self.change_page_image)  # Stage 1 mon img
            evo_mon_anch.add_widget(evo_mon_img)

            # Check if evo method is not IQ / Evo item
            if 'IQ' not in evo_method:

                evo_item = evo_method.partition(' + ')[0]
                evo_item_anch = AnchorLayout(anchor_x='center', anchor_y='center')
                evo_item_img = ImageButton(source='img//evo//' + evo_item + '.png', size_hint_x=None, width=dp(12),
                                      allow_stretch=True)  # First evo item img
                evo_item_anch.add_widget(evo_item_img)
                evo_item_img.bind(on_release=partial(self.popup, evo_item, v.evo_item_dict[evo_item], '12sp'))  # Popup with item name / location
            # If evo method is IQ
            else:
                iq_required = evo_method.partition('IQ')[2][:3]
                '''
                Need to change this later: Sets gummi image based on stage 1 mon, which may potentially use a non matching image
                For example Azurill gets a blue gummi from Marill though it is Normal type, not a huge deal and this might be the one exception
                But leaving this here just in case anyway
                '''
                evo_item_anch = AnchorLayout(anchor_x='center', anchor_y='center')
                evo_item_img = ImageButton(source='img//gummis//' + self.read_csv(int(evo_mon), 34).partition(' (')[0]
                                           .lower() + '_gummi.png', size_hint_x=None, width=dp(12), allow_stretch=True)
                evo_item_anch.add_widget(evo_item_img)
                evo_item_img.bind(on_release=partial(self.popup, 'IQ', 'IQ level required: ' + iq_required[1:2], '14sp'))  # Popup explaining IQ
                evo1_iq_amount_label = Label(text=iq_required)  # IQ level string; (4)/(5)/(6)
                evo_box.add_widget(evo_item_anch)
                evo_box.add_widget(evo1_iq_amount_label)

            # Check if evo data string contains '+' / if second evo item exists
            if '+' in evo_method:
                evo1_label = Label(text='+')                    # Label '+' for between evo items
                if not evo_box.children:                       # If boxlayout is still empty (Espeon and Umbreon edge cases)
                    evo_box.add_widget(evo_item_anch)       # Add first evolution data to boxlayout
                    if evo1_iq_amount_label:                    # Only add IQ amount required string if it was changed from empty string
                        evo_box.add_widget(evo1_iq_amount_label)
                evo_box.add_widget(evo1_label)                 # Add '+' string label

                # Evos with with 2 requirements, either 2 items (Steelix / Kingdra etc.)
                # or IQ + Item (Espeon / Umbreon; IQ + Ribbon)
                if 'IQ' not in evo_method or evo1_iq_amount_label:
                    evo_item2 = evo_method.partition(' + ')[2].partition(' --> ')[0]
                    evo_item_anch = AnchorLayout(anchor_x='center', anchor_y='center')
                    evo1_image_item2 = ImageButton(source='img//evo//' + evo_item2 + '.png', size_hint_x=None,
                                                   width=dp(12), allow_stretch=True)  # Second evo item img
                    evo_item_anch.add_widget(evo1_image_item2)
                    evo1_image_item2.bind(on_release=partial(self.popup, evo_item2, v.evo_item_dict[evo_item2], '12sp'))  # Popup with item name / location
                    evo_box.add_widget(evo_item_anch)
                # If IQ required for evo and it is the first occurrence in current evo line (Azurill, IQ -> Level up evo?)
                else:
                    print('Don\'t think I need this? Delete later probably\n'*50)
                    # iq_required = evo_method.partition('IQ')[2][:3]
                    # evo1_image_item2 = ImageButton(source='img//gummis//' + self.read_csv(int(evo_mon), 34).partition(' (')[0] + '_gummi.png')  # IQ (Gummi) img
                    # evo1_image_item2.bind(on_release=partial(self.Popup, 'IQ level required:::::' + iq_required[1:2], 'IQ', '24sp'))  # Popup explaining IQ
                    # evo1_iq_amount_label = Label(text=evo_method.partition('IQ(')[2][:3])  # IQ level string
                    #
                    # evo_box.add_widget(evo1_image_item2)
                    # evo_box.add_widget(evo1_iq_amount_label)

                self.ids.md_evo_box.add_widget(evo_box)  # Add box widget containing evo items and label

            # If only 1 item in current evolution (Not necessarily whole line)
            elif not evo_box.children:
                self.ids.md_evo_box.add_widget(evo_item_anch)
            # Otherwise add created boxlayout containing several Images and Label
            else:
                self.ids.md_evo_box.add_widget(evo_box)

            # Finally, add last portrait image
            self.ids.md_evo_box.add_widget(evo_mon_anch)

    def set_evos(self, pokedex_nr):
        self.ids.md_evo_box.clear_widgets()  # Clear widgets from potential previously entered dex page
        self.ids.md_evo_box.height = dp(55)  # Reset values to default, to reset any changes from previous page
        self.ids.md_evo_box.cols = 5         # Reset
        self.ids.md_evo_box.rows = 2         # Reset

        with open('csv/SpinoffDexDataset.csv', 'r', encoding='utf-8') as read_obj:
            csv_reader = reader(read_obj)
            rows = list(csv_reader)
            evo_string = rows[int(pokedex_nr)][15]  # Full evolution data string from csv file

            evo1 = evo_string.partition(' --> ')  # Base mon nr (e.g. 001)
            evo1lv = evo1[2].partition(' --> ')  # Base mon evo method (e.g. Lv. xx / Water Stone)
            evo2 = evo1lv[2].partition(' --> ')  # Stage 1 mon nr
            evo2lv = evo2[2].partition(' --> ')  # Stage 1 evo method
            evo3 = evo2lv[2].partition(' --> ')  # Stage 2 mon nr
            evo_rows_cols = evo3[2].partition(' --> ')  # rows and cols needed for evo lines, only for non regular evos
            evo_lv_alt1 = evo_rows_cols[2].partition(' --> ')  # Alternate evo method 1
            evo_alt1 = evo_lv_alt1[2].partition(' --> ')  # Alternate mon nr 1
            evo_lv_alt2 = evo_alt1[2].partition(' --> ')  # Alternate evo method 2
            evo_alt2 = evo_lv_alt2[2].partition(' --> ')  # Alternate mon nr 2
            evo_lv_alt3 = evo_alt2[2].partition(' --> ')  # ... and so on
            evo_alt3 = evo_lv_alt3[2].partition(' --> ')  # ...
            evo_lv_alt4 = evo_alt3[2].partition(' --> ')  # ...
            evo_alt4 = evo_lv_alt4[2].partition(' --> ')  # ...

            # Check if current mon has any evolutions
            if evo_string != 'No Evolution':
                # Regular evolutions
                evo1_anch = AnchorLayout(anchor_x='center', anchor_y='center')
                evo1_image = ImageButton(source='img//portraits//' + evo1[0] + '.png', size_hint_x=None, width=dp(40),
                                         allow_stretch=True, on_release=self.change_page_image)  # Base mon portrait, go to mon on select
                evo1_anch.add_widget(evo1_image)
                self.ids.md_evo_box.add_widget(evo1_anch)  # Add base mon portrait
                self.evolve(evo1lv[0], evo2[0])  # Add first evo data

                if evo3[0]:  # If data for a second evo exists / Not a 1 evo mon
                    self.evolve(evo2lv[0], evo3[0])  # Add second evo data

                # Check if data specifying rows & cols exists / mons with several evo paths
                # In gen 3 only Oddish, Gloom, Poliwag, Poliwhirl, Slowpoke, Eevee, Tyrogue and Clamperl are affected
                if evo_rows_cols[1]:
                    evo_rows = int(evo_rows_cols[0].partition(' rows')[0][-1:])  # total rows / evo paths
                    evo_cols = int(evo_rows_cols[0].partition(' cols')[0][-1:])  # total cols / evo stages

                    self.ids.md_evo_box.height = (dp(45) * evo_rows)  # Add extra height to widget per extra row

                    self.ids.md_evo_box.rows = evo_rows  # Change rows
                    self.ids.md_evo_box.cols = evo_cols  # and cols

                    '''
                    May have to revisit this bit later if new generation has different evo path patterns
                    e.g. 3+ paths with 3 pokémon per path instead of 2
                    also no way to handle forms yet
                    '''
                    evo1_anch = AnchorLayout(anchor_x='center', anchor_y='center')

                    evo1_image = ImageButton(source='img//portraits//' + evo1[0] + '.png', size_hint_x=None,
                                             width=dp(40), allow_stretch=True, on_release=self.change_page_image)
                    evo1_anch.add_widget(evo1_image)
                    self.ids.md_evo_box.add_widget(evo1_anch)  # Add base mon portrait again, second row
                    if evo_cols == 5:  # Skip if there is only 1 evo / cols is 3
                        self.evolve(evo1lv[0], evo2[0])  # Add first evo data again, second row
                    self.evolve(evo_lv_alt1[0], evo_alt1[0])  # Add alternate evo path, second row
                    if evo_rows > 2:  # If there are 3 or more evo paths (Tyrogue, Eevee)
                        evo1_anch = AnchorLayout(anchor_x='center', anchor_y='center')
                        evo1_image = ImageButton(source='img//portraits//' + evo1[0] + '.png', size_hint_x=None,
                                                 width=dp(40), allow_stretch=True, on_release=self.change_page_image)
                        evo1_anch.add_widget(evo1_image)
                        self.ids.md_evo_box.add_widget(evo1_anch)  # Add base mon portrait again, third row
                        self.evolve(evo_lv_alt2[0], evo_alt2[0])  # Add alternate evo path, third row
                        if evo_rows > 3:  # 4 or more evo paths, just Eevee in gen 3, maybe more with forms later?
                            evo1_anch = AnchorLayout(anchor_x='center', anchor_y='center')
                            evo1_image = ImageButton(source='img//portraits//' + evo1[0] + '.png', size_hint_x=None,
                                                     width=dp(40), allow_stretch=True, on_release=self.change_page_image)
                            evo1_anch.add_widget(evo1_image)
                            self.ids.md_evo_box.add_widget(evo1_anch)  # Add base mon portrait again, third row
                            self.evolve(evo_lv_alt3[0], evo_alt3[0])  # Add alternate evo path, third row
                            if evo_rows > 4:  # 5 or more evo paths, still just Eevee in gen 3
                                evo1_anch = AnchorLayout(anchor_x='center', anchor_y='center')
                                evo1_image = ImageButton(source='img//portraits//' + evo1[0] + '.png', size_hint_x=None,
                                                         width=dp(40), allow_stretch=True, on_release=self.change_page_image)
                                evo1_anch.add_widget(evo1_image)
                                self.ids.md_evo_box.add_widget(evo1_anch)  # Add base mon portrait again, third row
                                self.evolve(evo_lv_alt4[0], evo_alt4[0])  # Add alternate evo path, third row

            # Non evolving mons
            else:
                evo1_anch = AnchorLayout(anchor_x='center', anchor_y='center')
                evo1_image = ImageButton(source='img//portraits//' + pokedex_nr + '.png', size_hint_x=None, width=dp(40), allow_stretch=True)
                evo1_anch.add_widget(evo1_image)
                self.ids.md_evo_box.add_widget(evo1_anch)  # add non evolving mon portrait

    def set_moves(self, pokedex_nr):
        self.ids.md_moves_levels.clear_widgets()
        self.ids.md_moves_names.clear_widgets()
        self.ids.md_tm_nrs.clear_widgets()
        self.ids.md_tm_names.clear_widgets()

        # Levelup moves
        for row in v.md_movesets[int(pokedex_nr)-1][0]:
            move_level = Label(text=row[0], size_hint=(None, None), size=(self.ids.md_moves_levels.width, '20dp'))
            move_name = Button(text=row[1], size_hint=(None, None), size=(self.ids.md_moves_names.width, '20dp'),
                               background_color=(0, 0, 0, 0))
            if move_name.text != 'Move':
                move_name.bind(on_release=partial(self.popup, move_name.text, v.move_description_dict[move_name.text], '12sp'))
            self.ids.md_moves_levels.add_widget(move_level)
            self.ids.md_moves_names.add_widget(move_name)

            sep = SeparatorX()
            self.ids.md_moves_levels.add_widget(sep)
            sep = SeparatorX()
            self.ids.md_moves_names.add_widget(sep)
            sep = SeparatorY()
            self.ids.md_moves_separators.add_widget(sep)

        # TMs
        for row in v.md_movesets[int(pokedex_nr)-1][1]:
            move_nr = Label(text=row[0], size_hint=(None, None), size=(self.ids.md_moves_levels.width, '20dp'))
            move_name = Button(text=row[1], size_hint=(None, None), size=(self.ids.md_moves_names.width, '20dp'),
                               background_color=(0, 0, 0, 0))
            self.ids.md_tm_nrs.add_widget(move_nr)
            self.ids.md_tm_names.add_widget(move_name)

            sep = SeparatorX()
            self.ids.md_tm_nrs.add_widget(sep)
            sep = SeparatorX()
            self.ids.md_tm_names.add_widget(sep)
            sep = SeparatorY()
            self.ids.md_tm_separators.add_widget(sep)

    def change_page(self, nr):
        self.ids.dex_page_main.number = abs(nr)  # absolute value of pokedex nr; '001' = 1
        self.ids.manager.list_of_prev_screens.append(self.ids.manager.current)
        self.ids.manager.current = 'dex_page_main'

    def change_page_image(self, image_button_object):
        # Only change page if the selected image isn't the page the user is already on
        if not abs(int(image_button_object.source[-7:-4])) == self.ids.dex_page_main.number:
            self.ids.manager.current = 'empty'
            self.ids.dex_page_main.number = abs(int(image_button_object.source[-7:-4]))  # absolute value of pokedex nr; '001' = 1
            self.ids.manager.current = 'dex_page_main'

    @staticmethod
    def popup(title, text, text_font_size='14sp', image_button_object=None):
        return Pop(title, text, text_font_size, alpha=0.5)

    def create_box(self, pokedex_nr, index, delimiter, where, cols, rows, font_size='14sp', irregular_col_width=None):
        where.clear_widgets()  # Reset stat widget
        stat_list = self.read_csv(int(pokedex_nr), index).split(delimiter)  # Turn string of list into list
        for row in range(rows):
            big_box = BoxLayout(size_hint=(None, None), size=(self.parent.width, dp(30)), orientation='horizontal')
            for col in range(cols):
                row_list = stat_list[row].split(', ')  # turn string of list into list again (nested list)
                col_string = row_list[col]
                if not irregular_col_width:
                    label = Label(size_hint=(None, None), size=((self.parent.width/cols) - dp(2), big_box.height),
                                  text=col_string.replace('[', '').replace(']', ''),  # remove '[' and ']' from relevant strings
                                  font_size=font_size)

                # If the width of all cols can't be uniform, they can be individually supplied here
                else:
                    label = Label(size_hint=(None, None), size=((irregular_col_width[col]) - dp(2), big_box.height),
                                  text=col_string.replace('[', '').replace(']', ''),  # remove '[' and ']' from relevant strings
                                  font_size=font_size)

                sep = SeparatorY()
                big_box.add_widget(label)
                big_box.add_widget(sep)
            where.add_widget(big_box)
            sep = SeparatorX()
            where.add_widget(sep)


class SpinoffDexApp(App):
    def build(self):
        dex = SpinoffDex()
        dex.add_dex_entries()
        return dex


class DexEntry(BoxLayout, Button):
    pass


class DexPage(Screen):
    pass


class ImageButton(ButtonBehavior, Image):
    pass


class BoxButton(BoxLayout, Button):
    pass


class Pop(ModalView):
    def __init__(self, title, txt, text_font_size='14sp', alpha=0.5,
                 width=None, height=None, **kwargs):
        super(Pop, self).__init__(**kwargs)

        self.auto_dismiss = True
        self.size_hint = (0.98, None)
        self.preferred_width = width
        self.preferred_height = height
        self.text_font_size = text_font_size

        if self.preferred_width:
            self.width = self.preferred_width
        elif v.Window.width > 500:  # Big screen?
            self.width = 0.7 * v.Window.width
        else:
            self.width = v.Window.width - 2

        self.playout = BoxLayout(orientation='vertical',
                                 padding=["2dp", "5dp",
                                          "2dp", "5dp"],
                                 spacing="5dp")

        self.title = Label(size_hint_y=None,
                           text_size=(self.width - dp(20), None),
                           text=title,
                           halign='center',
                           font_size="16sp",
                           color=(0.9, 0.9, 0.9, 1),
                           markup=True)

        self.separators = BoxLayout(orientation='horizontal', size_hint=(1, None), height="1dp")
        self.separator1 = BoxLayout(size_hint_x=0.05)
        self.separator2 = BoxLayout(size_hint_x=0.9)
        self.separator3 = BoxLayout(size_hint_x=0.05)
        self.separators.add_widget(self.separator1)
        self.separators.add_widget(self.separator2)
        self.separators.add_widget(self.separator3)


        self.pscroll = ScrollView(do_scroll_x=False)

        # The title string is used to distinguish if the popup should be title + text, or an image
        if 'image_' not in title:
            self.content = Label(size_hint_y=None,
                                 text=txt,
                                 halign='left',
                                 font_size=text_font_size,
                                 color=(0.9, 0.9, 0.9, 1),
                                 markup=True,
                                 text_size=(self.width - dp(20), None))

        else:
            # Remove the 'image_' from title string if present;
            # used as condition to choose between adding an Image or Label Widget in popup content
            self.title.text = title.partition('image_')[2]
            self.content = Image(source=txt)  # txt should be path to image

            '''
            Probably should find a less spaghetti code way to make the popup window be the correct size
            in case of Images instead of Labels, but at least I got it to work now.
            The Popup calculates size based on the size of the original image, not whatever shrunk size gets displayed
            in case of smaller screens (especially phones which are significantly smaller horizontally than vertically),
            so here that original image's height gets divided by whatever ratio (original image width / popup width) is,
            and the image's width is set to the popup window width, making it as large as the current screen allows.
            Without all this the default behaviour creates large white space around the image.
            I sure hope I don't forget to remove this if I ever make this publicly available, but otherwise hi stranger.
            '''
            # Popup window width, original image height * (Popup window width / original image width; ie. ratio)

            self.content.texture_size = (self.size[0], self.content.texture_size[1]*(self.size[0]/self.content.texture_size[0]))

        self.pbutton = Button(text='Close', size_hint=(0.9, None), height="25dp", pos_hint={'center_x': 0.5},
                              background_normal="atlas://data/images/defaulttheme/vkeyboard_background")
        self.pbutton.bind(on_release=self.close)

        self.add_widget(self.playout)
        self.playout.add_widget(self.title)
        self.playout.add_widget(self.separators)

        self.playout.add_widget(self.pscroll)
        self.pscroll.add_widget(self.content)
        self.playout.add_widget(self.pbutton)

        self.title.bind(texture_size=self.update_height)
        self.content.bind(texture_size=self.update_height)

        with self.separator2.canvas.before:
            Color(0.7, 0.7, 0.9, 1)
            self.rect = Rectangle(pos=self.separator2.pos,
                                  size=self.separator2.size)

        self.separator2.bind(pos=self.update_separator,
                             size=self.update_separator)

        v.Window.bind(size=self.update_width)

        self.open()

    def update_width(self, *args):
        # hack to resize dark background on window resize
        self.center = v.Window.center
        self._window = None
        self._window = v.Window

        if self.preferred_width:
            self.width = self.preferred_width
        elif v.Window.width > 500:  # Big screen?
            self.width = 0.7 * v.Window.width
        else:
            self.width = v.Window.width - 2

        self.title.text_size = (self.width - dp(30), None)
        self.content.text_size = (self.width - dp(30), None)

    def update_height(self, *args):
        self.title.height = self.title.texture_size[1]
        self.content.height = self.content.texture_size[1]
        temp = self.title.height + self.content.height + dp(56)
        if self.preferred_height:
            self.height = self.preferred_height
        elif temp > v.Window.height - dp(40):
            self.height = v.Window.height - dp(40)
        else:
            self.height = temp
        self.center = v.Window.center

    def update_separator(self, *args):
        self.rect.pos = self.separator2.pos
        self.rect.size = self.separator2.size

    def close(self, instance):
        self.dismiss(force=True)


class SeparatorX(Widget):
    def __init__(self, **kwargs):
        super(SeparatorX, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 1, 1, 0.2)
            self.rect = Rectangle(pos=self.pos,
                                  size=(self.width, dp(2)))

        self.bind(pos=self.update_rect,
                  size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.width, dp(2)


class SeparatorY(Widget):
    def __init__(self, **kwargs):
        super(SeparatorY, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 1, 1, 0.2)
            self.rect = Rectangle(pos=self.pos,
                                  size=(dp(2), self.height))

        self.bind(pos=self.update_rect,
                  size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = dp(2), self.height


class WrapLabel(Label):
    pass


class WhiteLabel(Label):
    pass


class TintedLabel(Label):
    pass


if __name__ == '__main__':
    SpinoffDexApp().run()