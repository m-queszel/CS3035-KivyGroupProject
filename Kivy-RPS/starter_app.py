from kivy.app import App
from kivy.uix.label import Label

def testLabel():
    return Label(text="CS3035 Group Project")

class TestApp(App):
    def build(self):
        return testLabel()

if __name__ == '__main__':
    TestApp().run()
