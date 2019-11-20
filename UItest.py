from kivy.app import App

from kivy.uix.label import Label

class Simplekivy(App):
    def build(self):
        return Label(text="touch my balls")

if __name__ == "__main__":
    Simplekivy().run() 