import csv
import random
from functools import partial
import variables as v

import pandas as pd
from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from csv import reader

from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView


class SpinoffDex(Screen):
    manager = ObjectProperty(None)
    dex_page = ObjectProperty(None)
    theGrid = ObjectProperty(None)
    test = ObjectProperty(None)
    md_ability = ObjectProperty(None)
    md_joined = ObjectProperty(None)
    md_body_size = ObjectProperty(None)
    md_location = ObjectProperty(None)
    md_layout = ObjectProperty(None)
    md_get_rate = ObjectProperty(None)
    md_evo_box = ObjectProperty(None)
    md_moves_names = ObjectProperty(None)
    md_moves_levels = ObjectProperty(None)
    md_tm_nrs = ObjectProperty(None)
    md_tm_names = ObjectProperty(None)
    md_gummis_box = ObjectProperty(None)
    general_type1 = ObjectProperty(None)
    general_type2 = ObjectProperty(None)
    type_box = ObjectProperty(None)

    def add_dex_entries(self):
        # skip first line i.e. read header first and then iterate over each row od csv as a list
        with open('csv/spinoffDexDataset.csv', 'r', encoding='utf-8') as read_obj:
            csv_reader = reader(read_obj)
            header = next(csv_reader)
            # Check file as empty
            if header:
                # Iterate over each row after the header in the csv
                max_entries = 25  # Limit the amount of entries produced for speed
                current_entries = 0
                for row in csv_reader:
                    if current_entries < max_entries:
                        # Entry ID
                        dex_entry = DexEntry(id=row[1])
                        self.ids.theGrid.add_widget(dex_entry)

                        # Entry Dex Number
                        dex_number = Label(text=row[2])
                        dex_entry.add_widget(dex_number)

                        # Entry Pokemon Name
                        dex_name = Label(text=row[3])
                        dex_entry.add_widget(dex_name)

                        # Entry Pokemon Types
                        dex_type1 = Label(text=row[5])
                        dex_entry.add_widget(dex_type1)
                        dex_type2 = Label(text=row[6])
                        dex_entry.add_widget(dex_type2)

                        # Entry Joined
                        dex_joined = Label(text=row[7])
                        dex_entry.add_widget(dex_joined)

                        # Entry Favorite
                        dex_favorite = Label(text=row[8])
                        dex_entry.add_widget(dex_favorite)

                        current_entries += 1


    @staticmethod
    def read_csv(row, column):
        with open('csv/spinoffDexDataset.csv', encoding='utf-8') as read_obj:
            csv_reader = reader(read_obj)
            rows = list(csv_reader)
            return rows[row][column]

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


    @staticmethod
    def set_md_body_size(pokedex_nr):
        df = pd.read_csv("csv/spinoffDexDataset.csv")
        return 'img\\misc\\size' + (str(len(str(df.loc[int(pokedex_nr)-1, 'md_body_size'])))) + '.png'

    def set_abilities(self, abilities):
        self.ids.md_ability.clear_widgets()  # Reset widget in case a previous page added to it

        ability_1 = abilities.partition(' & ')[0]  # Partition the string to exclude a potential second ability
        md_ability_1 = Button(text=ability_1, background_normal='img\\misc\\bg_gray7.png')  # Ability name
        md_ability_1.bind(on_release=partial(self.popup, ability_1, v.md_abilities[ability_1], '14sp'))  # Popup window with description
        self.ids.md_ability.add_widget(md_ability_1)

        # If there are two abilities, add another
        if '&' in abilities:
            ability_2 = abilities.partition(' & ')[2]
            md_ability_2 = Button(text=ability_2, background_normal='img\\misc\\bg_gray7.png')
            md_ability_2.bind(on_release=partial(self.popup, ability_2, v.md_abilities[ability_2], '14sp'))
            self.ids.md_ability.add_widget(md_ability_2)

    def set_location(self, pokedex_nr):
        self.ids.md_location.clear_widgets()  # Reset location widget
        df = pd.read_csv("csv/spinoffDexDataset.csv")
        parts = df.loc[int(pokedex_nr)-1, 'md_location'].partition(', ')
        if parts[1]:
            loc_1 = Button(text=parts[0], size_hint=(None, None), size=(self.ids.md_location.width, '25dp'), font_size=dp(14))
            self.ids.md_location.add_widget(loc_1)
            location_string = parts[2].partition(', ')
            for i in range(df.loc[int(pokedex_nr)-1, 'md_location'].count(', ')):
                loc_x = Button(text=location_string[0], size_hint=(None, None), size=(self.ids.md_location.width, '25dp'), font_size=dp(14))
                self.ids.md_location.add_widget(loc_x)
                location_string = location_string[2].partition(', ')
        else:
            loc_else = Button(text=(parts[0] + parts[1] + parts[2]), size_hint=(None, None), size=(self.ids.md_location.width, '25dp'), font_size=dp(14))
            self.ids.md_location.add_widget(loc_else)

    @staticmethod
    def check_joined(pokedex_nr):
        df = pd.read_csv("csv/spinoffDexDataset.csv")
        if str(df.loc[int(pokedex_nr)-1, 'joined']) == 'True':
            return 'img\\misc\\joined.png'
        else:
            return 'img\\misc\\not_joined.png'

    def md_join(self, pokedex_nr):
        df = pd.read_csv("csv/spinoffDexDataset.csv")
        df.loc[int(pokedex_nr)-1, 'joined'] = not(df.loc[int(pokedex_nr)-1, 'joined'])
        df.to_csv("csv/spinoffDexDataset.csv", index=False)
        self.ids.md_joined.text = str(df.loc[int(pokedex_nr)-1, 'joined'])
        if str(df.loc[int(pokedex_nr)-1, 'joined']) == 'True':
            self.ids.md_joined.source = 'img\\misc\\joined.png'
        else:
            self.ids.md_joined.source = 'img\\misc\\not_joined.png'

    def unown_check(self, pokedex_nr):
        # Set font size lower for Unown's Location text because it contains a shitload of locations
        # Also makes the app choose a random friend area as the collective Unown species has 2 (Aged Chamber AN / O?)
        if pokedex_nr == '201':
            self.ids.md_get_rate.font_size = '10dp'

            flip = random.randint(0, 1)  # Flip a 'coin' to pick a friend area
            if flip:
                self.ids.md_friend_area.background_normal = 'img\\friend areas\\Aged Chamber AN.png'
            else:
                self.ids.md_friend_area.background_normal = 'img\\friend areas\\Aged Chamber O.png'
        else:
            self.ids.md_get_rate.font_size = '14dp'

    def set_gummis(self, pokedex_nr):
        self.md_gummis_box.clear_widgets()  # Reset Widget

        # Strings from the csv file
        gummi_string = self.read_csv(int(pokedex_nr), 34)                       # Entire Favourite Gummis string from csv file
        gummi_1 = (gummi_string.partition(', ')[0])                             # Gummi 1 string
        gummi_2 = (gummi_string.partition(', ')[2])                             # Gummi 2 string (Empty if not applicable)
        gummi_1_color = gummi_1.partition(' (')[0]                              # Gummi 1 string with IQ amount removed
        gummi_1_amount = gummi_1.partition('(')[1] + gummi_1.partition('(')[2]  # Gummi 1 string, only IQ amount
        gummi_2_color = gummi_2.partition(' (')[0]                              # Gummi 2 string with IQ amount removed
        gummi_2_amount = gummi_1.partition('(')[1] + gummi_2.partition('(')[2]  # Gummi 2 string, only IQ amount

        # Gummi Image and IQ amount Buttons
        md_gummi_1_color = ImageButton(source='img\\gummis\\' + gummi_1_color + '_gummi.png', size_hint=(0.25, 1))
        md_gummi_1_amount = Button(text=gummi_1_amount, background_color=(0, 0, 0, 0), size_hint=(0.25, 1))

        # Binding for Popup with IQ information
        md_gummi_1_color.bind(on_release=partial(self.popup, gummi_1_color + ' Gummi', 'IQ Gained: ' + gummi_1_amount + v.iq_string, '12sp'))
        md_gummi_1_amount.bind(on_release=partial(self.popup, gummi_1_color + ' Gummi', 'IQ Gained: ' + gummi_1_amount + v.iq_string, '12sp'))

        md_gummi_1_box = BoxLayout(orientation='horizontal')   # Boxlayout to contain the above 2
        md_gummi_1_padding_left = Label(size_hint=(0.25, 1))   # These 2 are to center the other elements in the box, otherwise
        md_gummi_1_padding_right = Label(size_hint=(0.25, 1))  # the gummi image and the label are too far apart, should find a better way later

        md_gummi_1_box.add_widget(md_gummi_1_padding_left)   # Empty label to center other 2 widgets, and make them smaller
        md_gummi_1_box.add_widget(md_gummi_1_color)          # Add the gummi image
        md_gummi_1_box.add_widget(md_gummi_1_amount)         # Add the IQ amount label
        md_gummi_1_box.add_widget(md_gummi_1_padding_right)  # Empty label to center other 2 widgets, and make them smaller

        self.md_gummis_box.add_widget(md_gummi_1_box)        # Add all the stuff to the box to contain it all

        # If applicable, do the same for second gummi
        if gummi_2:
            md_gummi_2_color = ImageButton(source='img\\gummis\\' + gummi_2_color + '_gummi.png', size_hint=(0.25, 1))
            md_gummi_2_amount = Button(text=gummi_2_amount, background_color=(0, 0, 0, 0), size_hint=(0.25, 1))
            md_gummi_2_color.bind(on_release=partial(self.popup, gummi_2_color + ' Gummi', 'IQ Gained: ' + gummi_2_amount + v.iq_string, '12sp'))
            md_gummi_2_amount.bind(on_release=partial(self.popup, gummi_2_color + ' Gummi', 'IQ Gained: ' + gummi_2_amount + v.iq_string, '12sp'))
            md_gummi_2_box = BoxLayout(orientation='horizontal')
            md_gummi_2_padding_left = Label(size_hint=(0.25, 1))
            md_gummi_2_padding_right = Label(size_hint=(0.25, 1))
            md_gummi_2_box.add_widget(md_gummi_2_padding_left)
            md_gummi_2_box.add_widget(md_gummi_2_color)
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
                evo_mon_img = ImageButton(source='img\\portraits\\' + evo_mon + '.png', on_release=self.change_page)  # Stage 1 mon img
                self.ids.md_evo_box.add_widget(evo_lvl)
                self.ids.md_evo_box.add_widget(evo_mon_img)
            else:
                print('Probably delete later, just seeing if this ever gets triggered\n'*500)

        # Non level based evos
        else:
            evo_box = BoxLayout()  # Widget to contain multiple evo items and '+' Label
            evo1_iq_amount_label = ''  # Empty placeholder string used as boolean to check for IQ based evos
            evo_mon_img = ImageButton(source='img\\portraits\\' + evo_mon + '.png', on_release=self.change_page)  # Stage 1 mon img

            # Check if evo method is not IQ / Evo item
            if 'IQ' not in evo_method:

                evo_item = evo_method.partition(' + ')[0]
                evo_item_img = ImageButton(source='img\\evo\\' + evo_item + '.png')  # First evo item img
                evo_item_img.bind(on_release=partial(self.popup, evo_item, v.evo_item_dict[evo_item], '12sp'))  # Popup with item name / location
            # If evo method is IQ
            else:
                iq_required = evo_method.partition('IQ')[2][:3]
                '''
                Need to change this later: Sets gummi image based on stage 1 mon, which may potentially use a non matching image
                For example Azurill gets a blue gummi from Marill though it is Normal type, not a huge deal and this might be the one exception
                But leaving this here just in case anyway
                '''
                evo_item_img = ImageButton(source='img\\gummis\\' + self.read_csv(int(evo_mon), 34).partition(' (')[0] + '_gummi.png')
                evo_item_img.bind(on_release=partial(self.popup, 'IQ', 'IQ level required: ' + iq_required[1:2], '14sp'))  # Popup explaining IQ
                evo1_iq_amount_label = Label(text=iq_required)  # IQ level string; (4)/(5)/(6)
                evo_box.add_widget(evo_item_img)
                evo_box.add_widget(evo1_iq_amount_label)

            # Check if evo data string contains '+' / if second evo item exists
            if '+' in evo_method:
                evo1_label = Label(text='+')                    # Label '+' for between evo items
                if not evo_box.children:                       # If boxlayout is still empty (Espeon and Umbreon edge cases)
                    evo_box.add_widget(evo_item_img)       # Add first evolution data to boxlayout
                    if evo1_iq_amount_label:                    # Only add IQ amount required string if it was changed from empty string
                        evo_box.add_widget(evo1_iq_amount_label)
                evo_box.add_widget(evo1_label)                 # Add '+' string label

                # Evos with with 2 requirements, either 2 items (Steelix / Kingdra etc.)
                # or IQ + Item (Espeon / Umbreon; IQ + Ribbon)
                if 'IQ' not in evo_method or evo1_iq_amount_label:
                    evo_item2 = evo_method.partition(' + ')[2].partition(' --> ')[0]
                    evo1_image_item2 = ImageButton(source='img\\evo\\' + evo_item2 + '.png')  # Second evo item img
                    evo1_image_item2.bind(on_release=partial(self.popup, evo_item2, v.evo_item_dict[evo_item2], '12sp'))  # Popup with item name / location
                    evo_box.add_widget(evo1_image_item2)
                # If IQ required for evo and it is the first occurrence in current evo line (Azurill, IQ -> Level up evo?)
                else:
                    print('Don\'t think I need this? Delete later probably\n'*50)
                    # iq_required = evo_method.partition('IQ')[2][:3]
                    # evo1_image_item2 = ImageButton(source='img\\gummis\\' + self.read_csv(int(evo_mon), 34).partition(' (')[0] + '_gummi.png')  # IQ (Gummi) img
                    # evo1_image_item2.bind(on_release=partial(self.Popup, 'IQ level required:::::' + iq_required[1:2], 'IQ', '24sp'))  # Popup explaining IQ
                    # evo1_iq_amount_label = Label(text=evo_method.partition('IQ(')[2][:3])  # IQ level string
                    #
                    # evo_box.add_widget(evo1_image_item2)
                    # evo_box.add_widget(evo1_iq_amount_label)

                self.ids.md_evo_box.add_widget(evo_box)  # Add box widget containing evo items and label

            # If only 1 item in current evolution (Not necessarily whole line), add only an image not a boxlayout
            elif not evo_box.children:
                self.ids.md_evo_box.add_widget(evo_item_img)
            # Otherwise add created boxlayout containing several Images and Label
            else:
                self.ids.md_evo_box.add_widget(evo_box)

            # Finally, add last portrait image
            self.ids.md_evo_box.add_widget(evo_mon_img)

    def set_evos(self, pokedex_nr):
        self.ids.md_evo_box.clear_widgets()  # Clear widgets from potential previously entered dex page
        self.ids.md_evo_box.height = dp(55)  # Reset values to default, to reset any changes from previous page
        self.ids.md_evo_box.cols = 5         # Reset
        self.ids.md_evo_box.rows = 2         # Reset

        with open('csv/spinoffDexDataset.csv', 'r', encoding='utf-8') as read_obj:
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

            '''Debug print command'''
            # print('evo1[0]:', evo1[0] + '\n',
            #       'evo1lv[0]:', evo1lv[0] + '\n',
            #       'evo2[0]:', evo2[0] + '\n',
            #       'evo2lv[0]:', evo2lv[0] + '\n',
            #       'evo3[0]:', evo3[0] + '\n',
            #       'evo_rows_cols[0]:', evo_rows_cols[0] + '\n',
            #       'evo_lv_alt1[0]:', evo_lv_alt1[0] + '\n',
            #       'evo_alt1[0]:', evo_alt1[0] + '\n',
            #       'evo_lv_alt2[0]:', evo_lv_alt2[0] + '\n',
            #       'evo_alt2[0]:', evo_alt2[0] + '\n',
            #       'evo_lv_alt3[0]:', evo_lv_alt3[0] + '\n',
            #       'evo_alt3[0]:', evo_alt3[0] + '\n',
            #       'evo_lv_alt4[0]:', evo_lv_alt4[0] + '\n',
            #       'evo_alt4[0]:', evo_alt4[0] + '\n')

            # Check if current mon has any evolutions
            if evo_string != 'No Evolution':
                # Regular evolutions
                evo1_image = ImageButton(source='img\\portraits\\' + evo1[0] + '.png', on_release=self.change_page)  # Base mon portrait, go to mon on select
                self.ids.md_evo_box.add_widget(evo1_image)  # Add base mon portrait
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
                    evo1_image = ImageButton(source='img\\portraits\\' + evo1[0] + '.png', on_release=self.change_page)
                    self.ids.md_evo_box.add_widget(evo1_image)  # Add base mon portrait again, second row
                    if evo_cols == 5:  # Skip if there is only 1 evo / cols is 3
                        self.evolve(evo1lv[0], evo2[0])  # Add first evo data again, second row
                    self.evolve(evo_lv_alt1[0], evo_alt1[0])  # Add alternate evo path, second row
                    if evo_rows > 2:  # If there are 3 or more evo paths (Tyrogue, Eevee)
                        evo1_image = ImageButton(source='img\\portraits\\' + evo1[0] + '.png', on_release=self.change_page)
                        self.ids.md_evo_box.add_widget(evo1_image)  # Add base mon portrait again, third row
                        self.evolve(evo_lv_alt2[0], evo_alt2[0])  # Add alternate evo path, third row
                        if evo_rows > 3:  # 4 or more evo paths, just Eevee in gen 3, maybe more with forms later?
                            evo1_image = ImageButton(source='img\\portraits\\' + evo1[0] + '.png', on_release=self.change_page)
                            self.ids.md_evo_box.add_widget(evo1_image)  # Add base mon portrait again, third row
                            self.evolve(evo_lv_alt3[0], evo_alt3[0])  # Add alternate evo path, third row
                            if evo_rows > 4:  # 5 or more evo paths, still just Eevee in gen 3
                                evo1_image = ImageButton(source='img\\portraits\\' + evo1[0] + '.png', on_release=self.change_page)
                                self.ids.md_evo_box.add_widget(evo1_image)  # Add base mon portrait again, third row
                                self.evolve(evo_lv_alt4[0], evo_alt4[0])  # Add alternate evo path, third row

            # Non evolving mons
            else:
                evo1_image = ImageButton(source='img\\portraits\\' + pokedex_nr + '.png', on_release=self.change_page)
                self.ids.md_evo_box.add_widget(evo1_image)  # add non evolving mon portrait

    def set_moves(self, pokedex_nr):
        self.ids.md_moves_levels.clear_widgets()
        self.ids.md_moves_names.clear_widgets()
        self.ids.md_tm_nrs.clear_widgets()
        self.ids.md_tm_names.clear_widgets()

        # Levelup moves
        with open('PokemonMovesets\\#' + pokedex_nr + '_levelup_moves.csv', 'r') as file:  # Use file to refer to the file object
            lvlup_reader = csv.reader(file)
            for row in lvlup_reader:
                move_level = Button(text=row[0], size_hint=(None, None), size=(self.ids.md_moves_levels.width, '20dp'))
                move_name = Button(text=row[1], size_hint=(None, None), size=(self.ids.md_moves_names.width, '20dp'))
                self.ids.md_moves_levels.add_widget(move_level)
                self.ids.md_moves_names.add_widget(move_name)

        # TMs
        with open('PokemonMovesets\\#' + pokedex_nr + '_tm_moves.csv', 'r') as file:  # Use file to refer to the file object
            tm_reader = csv.reader(file)
            for row in tm_reader:
                move_nr = Button(text=row[0], size_hint=(None, None), size=(self.ids.md_moves_levels.width, '20dp'))
                move_name = Button(text=row[1], size_hint=(None, None), size=(self.ids.md_moves_names.width, '20dp'))
                self.ids.md_tm_nrs.add_widget(move_nr)
                self.ids.md_tm_names.add_widget(move_name)

    def change_page(self, image_button_object):
        # Only change page if the selected image isn't the page the user is already on
        if not abs(int(image_button_object.source[-7:-4])) == self.ids.dex_page.number:
            self.ids.manager.current = 'empty'
            self.ids.dex_page.number = abs(int(image_button_object.source[-7:-4]))  # absolute value of pokedex nr; '001' = 1
            self.ids.manager.current = 'dex_page'

    @staticmethod
    def popup(title, text, text_font_size='14sp', image_button_object=None):
        return Pop(title, text, text_font_size, alpha=0.5, width=None, height=None)


class SpinoffDexApp(App):
    def build(self):
        dex = SpinoffDex()
        dex.add_dex_entries()
        return dex


class DexEntry(GridLayout, Button):
    pass


class DexPage(Screen):
    pass


class ImageButton(ButtonBehavior, Image):
    pass


class Pop(ModalView):
    def __init__(self, title, txt, text_font_size='14sp', alpha=0.5,
                 width=None, height=None, **kwargs):
        super(Pop, self).__init__(**kwargs)

        self.auto_dismiss = False
        self.background = "img\\misc\\bg_gray2.png"
        self.background_color = (0, 0, 0, alpha)
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
                           color=(0.1, 0.1, 0.1, 1),
                           markup=True)

        self.separator = BoxLayout(size_hint_y=None, height="1dp")

        self.pscroll = ScrollView(do_scroll_x=False)

        # The title string is used to distinguish if the popup should be title + text, or an image
        if 'image_' not in title:
            self.content = Label(size_hint_y=None,
                                 text=txt,
                                 halign='left',
                                 font_size=text_font_size,
                                 color=(0.1, 0.1, 0.2, 1),
                                 markup=True,
                                 text_size=(self.width - dp(20), None))

        else:
            # Remove the 'image_' from title string if present;
            # used as condition to choose between adding an Image or Label Widget in popup content
            self.title.text = title.partition('image_')[2]
            self.content = Image(source=txt)  # txt should be path to image

            # print(self.size)
            # print(self.content.texture_size)
            # print(self.size[0], self.content.texture_size[1]*(self.size[0]/self.content.texture_size[0]))

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

        self.pbutton = Button(text='Close',
                              size_hint_y=None, height="25dp",
                              background_normal="atlas://data/images/defaulttheme/vkeyboard_background")
        self.pbutton.bind(on_release=self.close)

        self.add_widget(self.playout)
        self.playout.add_widget(self.title)
        self.playout.add_widget(self.separator)

        self.playout.add_widget(self.pscroll)
        self.pscroll.add_widget(self.content)
        self.playout.add_widget(self.pbutton)

        self.title.bind(texture_size=self.update_height)
        self.content.bind(texture_size=self.update_height)

        with self.separator.canvas.before:
            Color(0.7, 0.7, 0.9, 1)
            self.rect = Rectangle(pos=self.separator.pos,
                                  size=self.separator.size)

        self.separator.bind(pos=self.update_separator,
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
        self.rect.pos = self.separator.pos
        self.rect.size = self.separator.size

    def close(self, instance):
        self.dismiss(force=True)


if __name__ == '__main__':
    SpinoffDexApp().run()
'''
0 id
1 number
2 name
3 japanese_name
4 type1
5 type2
6 joined
7 favorite
8 classification
9 weight_kg
10 weight_lbs
11 height_m
12 height_ft
13 md_ability
14 md_evolution_chain
15 md_body_size
16 md_friend_area
17 md_get_rate
18 md_location
19 rg_browser_no
20 rg_location
21 rg_pkmn_assist
22 rg_type_group
23 rg_field_ability
24 tz_get_rate
25 tz_location
'''

# SQL Query
# SELECT 'id_' || id as id,
# CASE
# 	WHEN pokedex_number < 10 THEN '#00' || pokedex_number
# 	WHEN pokedex_number < 100 AND pokedex_number >= 10 THEN '#0' || pokedex_number
# 	ELSE '#' || pokedex_number
# END AS number, name, type1, type2, joined, favorite, md_ability, md_evolution_chain, md_body_size, md_friend_area, md_get_rate, md_location FROM spinoff_dex
