
# https://raw.githack.com/HeaTTheatR/KivyMD-data/master/sweetalert-doc/unincluded/sweetalert/sweetalert/index.html
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDFlatButton

from kivymd.components.sweetalert import SweetAlert

KV = '''
MDScreen:

    MDRaisedButton:
        text: "EXAMPLE"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.show_dialog()
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_dialog(self):
        button_ok = MDRaisedButton(
            text='OK',
            font_size=16,
            on_release=self.callback,
        )
        button_cancel = MDFlatButton(
            text='CANCEL',
            font_size=16,
            on_release=self.callback,
        )
        self.alert = SweetAlert()
        self.alert.fire(
            'Your public IP', buttons=[button_ok, button_cancel],
        )

    def callback(self, instance_button):
        print(self.alert, instance_button)


Test().run()