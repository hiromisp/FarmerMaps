from kivymd.app import MDApp
from farmersmapview import FarmersMapView
from searchpopupmenu import SearchPopupMenu
import sqlite3

class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None

    def on_start(self):
        #Initialize Gps

        #Connect to database
        self.connection = sqlite3.connect("markets.db")
        self.cursor = self.connection.cursor()

        #Instantiate SearchPopupMenu
        self.search_menu = SearchPopupMenu()

MainApp().run()