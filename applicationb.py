import random
import numpy as np
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader
import arabic_reshaper
from bidi.algorithm import get_display


son = SoundLoader.load("cache/sound.wav")
class Mouna(FloatLayout):
    vd = ObjectProperty("welcome")
    vc = ObjectProperty("cache/hungry.jpg")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def afficheur(self):
        A = np.array([
            ["كسكسي بالخضرة", "طبيخة", "كسكسي ازعر بالفول", "مقرونة فل بالتن", "مقرونة بالدجاج", "تسطيرة", "مصلي بالدجاج", "عجة مرقاز",
             "ملوخية", "مرقة بالكعابر", "حوت و بطاطا فريت", "حلالم", "نواصر", "روز احمر", "قلايا كبدة",
             "جلبانة بالسيبيا", "شربة و بريك", "رشتة", "مرقة لوبيا", "مرقة بطاطا", "طاجين امك حورية", "روز بالخضرة النية", "مقرونة بالشوفرات", "عين صبنيورية",
             "كسكسي بالمناني", "مقرونة بالموزاريلا", "شربة شعير", "شربة لسان عصفور", "كفتة", "لبلابي", "لازانيا", "دويدة", "سردينة مشوية"],
            ["cache/c1.jpg", "cache/c2.jpg", "cache/c3.jpg", "cache/c4.jpg", "cache/c5.jpg", "cache/c6.jpg", "cache/c7.jpg", "cache/c8.jpg", "cache/c9.jpg",
             "cache/c10.jpg", "cache/c11.jpg", "cache/c12.jpg", "cache/c13.jpg", "cache/c14.jpg", "cache/c15.jpg", "cache/c16.jpg", "cache/c17.jpg", "cache/c18.jpg",
             "cache/c19.jpg", "cache/c20.jpg", "cache/c21.png", "cache/c22.jpg", "cache/c23.jpg", "cache/c24.jpg", "cache/c25.jpg", "cache/c26.png", "cache/c27.jpg",
             "cache/c28.jpg", "cache/c29.jpg", "cache/c30.png", "cache/c31.jpg", "cache/c32.jpg", "cache/c33.jpg"]
        ])

        c = str(A.shape)
        x = c.replace('(2, ', '')
        x = x.replace(')', '')
        N = int(x)
        i = random.randrange(0, N)
        y = arabic_reshaper.reshape(A[0,i])
        t = get_display(y)
        z = A[1,i]

        self.vd = t
        self.vc = z



class applicationb(App):
    def build(self):
        self.icon = "cache/logo.png"
        son.play()
        return Mouna()

if __name__ == '__main__':
    applicationb().run()




