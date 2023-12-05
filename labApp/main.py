from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (350, 580)


class MyApp(MDApp):
    def build(self):
        pass

if __name__ == '__main__':
    MyApp().run()