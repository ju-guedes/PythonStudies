
# import App, Builder (GUI)
from kivy.app import App
from kivy.lang import Builder

# Connect screen.kv to main
GUI = Builder.load_file("screen.kv")

# Create app class
class FirstApp(App):
    def build(self):
        return GUI

# loop for app
FirstApp().run()

