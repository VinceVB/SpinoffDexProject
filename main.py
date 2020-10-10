from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from csv import reader
from kivy.uix.screenmanager import Screen

Window.clearcolor = (1, 1, 1, 1)
Window.size = (288, 640)


#
#  TO FIX: - Nidoran male/female signs
#


class SpinoffDex(Screen):
    manager = ObjectProperty(None)
    theGrid = ObjectProperty(None)
    test = ObjectProperty(None)

    def add_dex_entries(self):
        # skip first line i.e. read header first and then iterate over each row od csv as a list
        with open('spinoffDexDataset.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            header = next(csv_reader)
            # Check file as empty
            if header != None:
                # Iterate over each row after the header in the csv
                for row in csv_reader:
                    # Entry ID
                    dex_entry = DexEntry(id=row[0])
                    self.ids.theGrid.add_widget(dex_entry)

                    # Entry Dex Number
                    dex_number = Label(text=row[1])
                    dex_entry.add_widget(dex_number)

                    # Entry Pokemon Name
                    dex_name = Label(text=row[2])
                    dex_entry.add_widget(dex_name)

                    # Entry Pokemon Types
                    dex_type1 = Label(text=row[3])
                    dex_entry.add_widget(dex_type1)
                    dex_type2 = Label(text=row[4])
                    dex_entry.add_widget(dex_type2)

                    # Entry Joined
                    dex_joined = Label(text=row[5])
                    dex_entry.add_widget(dex_joined)

                    # Entry Favorite
                    dex_favorite = Label(text=row[6])
                    dex_entry.add_widget(dex_favorite)


    def set_text(self, row, column):
        dex = SpinoffDex()

        with open('spinoffDexDataset.csv') as read_obj:
            csv_reader = reader(read_obj)
            rows = list(csv_reader)
            return rows[row][column]
            # self.id = 'id_1', 'id_20', 'id_300', etc.
            # slice the 'id_' and convert to int, to use as index
            #DatasetRow = rows[int(self.id[3:])]
            #return DatasetRow[1]



class SpinoffDexApp(App):
    def build(self):
        dex = SpinoffDex()
        dex.add_dex_entries()
        return dex


class DexEntry(GridLayout, Button):
    pass


class DexPage(Screen):
    pass


if __name__ == '__main__':
    SpinoffDexApp().run()
