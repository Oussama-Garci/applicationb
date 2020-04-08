import random
import numpy as np
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout


class Mouna(FloatLayout):
    vd = ObjectProperty("welcome")
    vc = ObjectProperty("hungry.jpg")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def afficheur(self):
        A = np.array([["hfnt", "ngjfht", "jfkfi", "nfbgh", "nngjth"],
                     ["hfnr", "jgnh", "ngj", "ngjfhr", "nfh"]])

        i = random.randrange(0, len(A))
        y = A[0,i]
        x = A[i,0]
        self.vd = x
        self.vc = y

class applicationb(App):
    def build(self):
        self.icon = "logo.png"
        return Mouna()

if __name__ == '__main__':
    applicationb().run()