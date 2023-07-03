from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.uix.image import Image
from kivymd.uix.list import OneLineAvatarListItem, ImageLeftWidget
import time

Window.size = (360, 800)


class Homescreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mycamera = self.ids.camera
        self.myimage = Image()
        self.resultbox = self.ids.resultbox
        self.mybox = self.ids.mybox

    def captureyouface(self):

        timenow = time.strftime("%Y%m%d_%H%M%S")
        self.mycamera.export_to_png("image_{}.png".format(timenow))
        self.myimage.source = "image_{}.png".format(timenow)
        self.resultbox.add_widget(
            OneLineAvatarListItem(
                ImageLeftWidget(
                    source="image_{}.png".format(timenow),
                    size_hint_x=0.3,
                    size_hint_y=1,
                    size=(300, 300)

                ),
                text=self.ids.name.text
            )

        )

class MyApp(MDApp):
    def build(self):
        Builder.load_file("camera.kv")
        return Homescreen()


if __name__ == "__main__":
    MyApp().run()