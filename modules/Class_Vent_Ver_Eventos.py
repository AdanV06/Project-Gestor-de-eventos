from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button,ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from modules.Backend1 import *

#BoxLayout que contiene la informacion del evento
class Item_event(ButtonBehavior,BoxLayout):
    def __init__(self,parent,evento,nombre,info,hora):
        super().__init__()
        self.evento = evento
        self.pnt = parent
        self.pos = self.center
        self.nombre = nombre
        self.info = info
        recursos = ""
        self.hora = hora



        for rec in self.info:
            if rec[1] > 1:
                recursos += f" {str(rec[0])} : {str(rec[1])},"
            else:
                recursos += f" {str(rec[0])},"

        informacion = Label(text=f"                  Recursos:\n{recursos}",font_size=14,text_size=(280,160),pos_hint={"center_x":0,"center_y":0.7},color=(1,1,1,1))
        inf_hora = Label(text=f"       Fecha inicio    :      Fecha fin:\n{self.hora}",color=(1,1,1,1),size_hint=(None,None),size=(240,80),font_size=16,pos_hint={"center_x":0, "center_y":0.5})
        delete_button = Delete(self.pnt,self)

        self.add_widget(Label(text= self.nombre,font_size=20,text_size=(200,80),valign="center",size_hint=(None,None),size=(230,120)))
        self.add_widget(inf_hora)
        self.add_widget(informacion)
        self.add_widget(delete_button)

class Delete(ButtonBehavior,Image):
        def __init__(self,parent,child):
            super().__init__()
            self.pnt = parent
            self.child = child
            self.source = "Imagenes/Button Delete.png"

        def on_touch_down(self,touch):
            if self.collide_point(*touch.pos):
                self.pnt.remove_widget(self.child)

                eventos = leer_json(ruta_eventos)
                eventos["eventos"].remove(self.child.evento)
                
                with open(ruta_eventos, "w") as data:
                    json.dump(eventos, data, indent=4)
                
        


            