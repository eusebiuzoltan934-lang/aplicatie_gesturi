from kivy.app import App
from kivy.uix.button import Button

class AplicatieGesturiApp(App):
    def build(self):
        return Button(text='Aplicația funcționează!')

if __name__ == '__main__':
    AplicatieGesturiApp().run()
