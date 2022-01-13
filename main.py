from random import random

from kivy.config import Config
from kivy.graphics import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp
from kivy.properties import NumericProperty, StringProperty, Clock
from kivy.uix.screenmanager import Screen


#nastavení do proměních velikost hrací plochy v pixelech
height = 720
width = 1280
FPS = 60
Config.set('graphics', 'width', width)
Config.set('graphics', 'height', height)


from kivy.app import App
from kivy.uix.widget import Widget

#třída pro obrazuvku MENU
class MainWidget(Screen):
    playerName1 = StringProperty("Player1")
    playerName2 = StringProperty("Player2")
    index = 11
    right_index = 11
    STATES = ['ARG', 'AUS', 'AUT', 'BEL', 'BLR', 'BRA', 'BUL', 'CAN', 'COL', 'CRO', 'CUB', 'CZE', 'DEN', 'EGY', 'ESP',
              'EST', 'FIN', 'FRA', 'GBR', 'GER', 'GRE', 'HUN', 'CHN', 'IND', 'IRL', 'IRN', 'ISL', 'ISR', 'ITA', 'JAP',
              'KOR', 'LAT', 'LIT', 'MAR', 'MEX', 'NED', 'NGR', 'NOR', 'NZL', 'PAK', 'POL', 'POR', 'ROM', 'RUS', 'SLO',
              'SRB', 'SUI', 'SVK', 'SWE', 'TUN', 'TUR', 'UKR', 'URU', 'USA']

    #definice pro funkci na nastavení jmen jednotlivých hráčů
    def on_text_validate(self, widget):
        self.playerName1 = widget.text

    def on_text_validate2(self, widget):
        self.playerName2 = widget.text
class CanvasExample3(Widget):
        pass

class CanvasExample2(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(30)
        self.vx = dp(5)
        self.vy = dp(5)
        self.gravity = dp(1)
        with self.canvas:
          self.ball = Ellipse(pos= self.center, size=(self.ball_size, self.ball_size))
          self.rect = Rectangle(pos=(dp(300), dp(300)), size=(dp(100), dp(100)))
        Clock.schedule_interval(self.update, 1/FPS)


    def on_size(self, *args):
        # print("on size :" + str(self.width) + " ," + str(self.height))
        self.ball.pos = (self.center_x-self.ball_size/2,self.center_y-self.ball_size/2)
    def update(self, dt):
        #print("update")
        x, y = self.ball.pos
        xr, yr = self.rect.pos
        x += self.vx
        y += self.vy
        y -= self.gravity
        self.gravity += 1
        self.ball.pos = (x, y)




        if x + self.ball_size > self.width:
            x = self.width-self.ball_size
            self.vx = -self.vx
        if y < 0:
            y = 0
            self.vy = -self.vy + self.gravity
            self.gravity = dp(1)
        if x < 0:
            x = 0
            self.vx = -self.vx




# class CanvasExample(Widget):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         with self.canvas:
#             Line(points=(100, 100, 400, 500), width=2)
#             Color(0, 1, 0)
#             Line(circle=(400, 200, 80), width=2)
#             Line(rectangle=(700, 500, 150, 100), width=5)
#             self.rect = Rectangle(pos=(700,200), size=(150,100))
#
#     def on_button_a_click(self):
#         #print("click")
#         x, y = self.rect.pos
#         w, h = self.rect.size
#         inc = dp(10)
#
#
#         diff = self.width -(x+w)
#         if diff < inc:
#             inc = diff
#
#         x += inc
#         self.rect.pos = (x, y)


class TheVolleyGameApp(App):
    pass

TheVolleyGameApp().run()