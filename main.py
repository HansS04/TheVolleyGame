from random import random

from kivy.config import Config
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen


#nastavení do proměních velikost hrací plochy v pixelech
height = 720
width = 1280

Config.set('graphics', 'width', width)
Config.set('graphics', 'height', height)


from kivy.app import App
from kivy.uix.widget import Widget

#třída pro obrazuvku MENU
class MainWidget(Screen):
    playerName1 = StringProperty("Player1")
    playerName2 = StringProperty("Player2")
    index = 11
    index2 = 11
    STATES = ['ARG', 'AUS', 'AUT', 'BEL', 'BLR', 'BRA', 'BUL', 'CAN', 'COL', 'CRO', 'CUB', 'CZE', 'DEN', 'EGY', 'ESP',
              'EST', 'FIN', 'FRA', 'GBR', 'GER', 'GRE', 'HUN', 'CHN', 'IND', 'IRL', 'IRN', 'ISL', 'ISR', 'ITA', 'JAP',
              'KOR', 'LAT', 'LIT', 'MAR', 'MEX', 'NED', 'NGR', 'NOR', 'NZL', 'PAK', 'POL', 'POR', 'ROM', 'RUS', 'SLO',
              'SRB', 'SUI', 'SVK', 'SWE', 'TUN', 'TUR', 'UKR', 'URU', 'USA']

    #definice pro funkci na nastavení jmen jednotlivých hráčů
    def on_text_validate(self, widget):
        self.playerName1 = widget.text

    def on_text_validate2(self, widget):
        self.playerName2 = widget.text

class TheVolleyGameApp(App):
    pass

TheVolleyGameApp().run()