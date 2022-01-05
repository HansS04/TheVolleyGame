from kivy.config import Config

height = 720
width = 1280

Config.set('graphics', 'width', width)
Config.set('graphics', 'height', height)


from kivy.app import App
from kivy.uix.widget import Widget


class MainWidget(Widget):
    pass

class TheVolleyGameApp(App):
    pass

TheVolleyGameApp().run()