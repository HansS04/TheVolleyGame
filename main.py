import random

from kivy.config import Config
from kivy.core.window import Window
from kivy.graphics import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp
from kivy.properties import NumericProperty, StringProperty, Clock, ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager

#nastavení do proměních velikost hrací plochy v pixelech
height = 720
width = 1280
FPS = 60
vx = dp(5)
vy = dp(6)
gravity = dp(1)
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
class VolleyPlayer(Widget):
    up = False
    down = False
    right = False
    left = False
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos = (width - (width / 4) * 3, 0)
        self.gravity = dp(15)

    def move(self):
        self.y -= self.gravity
        if self.up:
            while (self.y <= 200):
                self.y += dp(1)

        if self.y == dp(200):
            while (self.y > 0):
                self.y -= self.gravity
        if self.right:
            self.x += dp(15)
            self.y -= self.gravity
        if self.left:
            self.x -= dp(15)
            self.y -= self.gravity
        if self.x >= width / 2 - dp(120):
            self.x = width / 2 - 120
        if self.x < 0:
            self.x = 0
        if self.y <= 0:
            self.y = 0
class VolleyPlayer2(Widget):
    up = False
    down = False
    right = False
    left = False
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos = (width - width / 4 , 0)
        self.gravity = dp(15)
    def move(self):
        self.y -= self.gravity
        if self.up:
            while (self.y <= 200):
                self.y += dp(1)


        if self.right:
            self.x += dp(15)
            self.y -= self.gravity
        if self.left:
            self.x -= dp(15)
            self.y -= self.gravity
        if self.x <= width/2 +20:
                self.x = width/2 + 20
        if self.x > self.width - 120:
                self.x = width - 120
        if self.y <= 0:
            self.y = 0
class Net(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos = (width/2, 0)

class Ball(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(30)
        self.width = self.ball_size
        self.pos = (width /2 - self.ball_size /2, height/2 - self.ball_size / 2 + 200)

class Game(Screen):
    ball = ObjectProperty(None)
    vp = ObjectProperty(None)
    vp2 = ObjectProperty(None)
    net = ObjectProperty(None)
    score1 = NumericProperty(0)
    score2 = NumericProperty(0)




    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)
        self.n = random.randint(0, 1)
        self.gravity = gravity
        self.vx = vx
        self.vy = vy
        self.ball_size = dp(30)
        self.score1 = 0
        self.score2 = 0

    def start(self):
        Clock.schedule_interval(self.update, 1 / self.vp.speed)
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        # print(keycode)
        # Testy pro tlačítka, která nás zajímají
        if keycode[1] == 'w':
            self.vp.up = True
            self.vp.down = False
        if keycode[1] == 'up':
            self.vp2.up = True
            self.vp2.down = False
        if keycode[1] == 's':
            self.vp.down = True
            self.vp.up = False
        if keycode[1] == 'down':
            self.vp2.down = True
            self.vp2.up = False
        if keycode[1] == 'a':
            self.vp.left = True
            self.vp.right = False
        if keycode[1] == 'left':
            self.vp2.left = True
            self.vp2.right = False
        if keycode[1] == 'd':
            self.vp.right = True
            self.vp.left = False
        if keycode[1] == 'right':
            self.vp2.right = True
            self.vp2.left = False

    def _on_keyboard_up(self, keyboard, keycode):
        # print("---------")
        # print(keycode)
        # Testy pro tlačítka, která nás zajímají
        if keycode[1] == 'w':
            self.vp.up = False
        if keycode[1] == 'up':
            self.vp2.up = False
        if keycode[1] == 's':
            self.vp.down = False
        if keycode[1] == 'down':
            self.vp2.down = False
        if keycode[1] == 'a':
            self.vp.left = False
        if keycode[1] == 'left':
            self.vp2.left = False
        if keycode[1] == 'd':
            self.vp.right = False
        if keycode[1] == 'right':
            self.vp2.right = False

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None
    def bounce_of_ball(self):

        x, y = self.ball.pos
        netx, nety = self.net.pos
        px, py = self.vp.pos
        px2, py2 = self.vp2.pos

        if self.n == 0:
            x += self.vx
        else:
            x -= self.vx
        y -= self.gravity
        y += self.vy
        self.gravity += 1
        self.ball.pos = (x, y)
        if x + self.ball_size > width:
            x = width - self.ball_size
            self.vx = -self.vx
        if y < 0:
            y = 0
            self.vy = -self.vy + self.gravity
            self.gravity = dp(1)
            if x > width/2:
                self.score1 += 1
            else:
                self.score2 += 1
        if x < 0:
            x = 0
            self.ball.pos = (x,y)
            self.vx = -self.vx
        if y > height - dp(100):
            y = height - dp(100)
            self.ball.pos = (x,y)

        #kolize se sítí

        if y >= dp(320) and y <= dp(350)  and x>= netx - self.ball_size and x< netx + 20:
            print("narazil jsem zezhora")
            y = 350 + self.ball_size
            self.vy = -self.vy + self.gravity
            self.gravity = dp(1)
            self.ball.pos=(x,y)

        if x == netx - self.ball_size and y <= dp(350):
            print("narazil jsem z leva")
            x = netx - self.ball_size
            self.vx = -self.vx
            self.ball.pos = (x, y)

        if x == netx + 40 - self.ball_size and y <= dp(350):
            print("narazil jsem z prava")
            x = netx + 40 - self.ball_size
            self.vx = -self.vx
            self.ball.pos = (x, y)

        # kolize s hráčem zezhora
        if x >= px - self.ball_size  and x <= px - self.ball_size + dp(120) and y <= py + dp(220) and y >= py + dp(190):
            print("narazil jsi zezhora hráče")
            y = py + dp(210) + self.ball_size
            self.gravity = dp(1)
            self.vy = - self.vy + self.gravity
            self.ball.pos = (x,y)

        if x >= px2 - self.ball_size  and x <= px2 - self.ball_size + dp(120) and y <= py2 + dp(220) and y >= py2 + dp(190):
            print("narazil jsi zezhora hráče")
            y = py2 + dp(210) + self.ball_size
            self.gravity = dp(1)
            self.vy = - self.vy + self.gravity
            self.ball.pos = (x,y)



        #kolize s hráčem
        if y >= py and y <= py + dp(200) and x >= px - self.ball_size  and x <= px - self.ball_size + dp(30):
            x = px  - self.ball_size
            self.ball.pos = (x, y)
            self.vx = -self.vx

        if y >= py and y <= py + dp(200) and x >= px + dp(95) and x <= px + dp(120):
            x = px + dp(120)
            self.ball.pos = (x,y)
            self.vx = -self.vx

        #kolize s druhym hracem
        if y >= py2 and y <= py2 + dp(200) and x >= px2 - self.ball_size and x <= px2 - self.ball_size + dp(60):
            x = px2 - self.ball_size
            self.ball.pos = (x, y)
            self.vx = -self.vx

        if y >= py2 and y <= py2 + dp(200) and x >= px2 + dp(95) and x <= px2 + dp(120):
            x = px2 + dp(120)
            self.ball.pos = (x, y)
            self.vx = -self.vx

        if self.vx != vx or self.vx != -vx:
            if self.vx < 0:
                self.vx = -vx
            if self.vx > 0:
                self.vx = vx

    def update(self, dt):
        self.vp.move()
        self.vp2.move()
        self.bounce_of_ball()


class TheVolleyGameApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWidget(name='menu'))
        sm.add_widget(Game(name='canvas'))
        Config.set('graphics', 'width', width)
        Config.set('graphics', 'height', height)
        Config.write()
        return sm

TheVolleyGameApp().run()