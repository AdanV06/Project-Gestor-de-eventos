from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Line,Rectangle,Ellipse
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
import math

Window.size = (1600,900)

class Contenedor(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.velocidad_input = TextInput(hint_text = 'Vel',size_hint = (None,None),background_color=(0,0.3,0,0.4),size = (150,50),font_size = 30,pos=(80,840))
        self.angulo_input = TextInput(
            hint_text = "Angulo",
            size_hint = (None,None),
            cursor_color = (0,0,0,1),
            background_color=(0,0.3,0,0.4),
            size = (150,50),
            font_size = 30,
            pos=(250,840),
        )

        self.aceptar = Button(text="Aceptar",size_hint=(None,None),size=(150,50),pos=(420,840))
    
        self.add_widget(self.velocidad_input)
        self.add_widget(self.angulo_input)
        self.add_widget(self.aceptar)
        self.aceptar.bind(on_press=self.animar_trayectoria)

    def puntos_parabola(self):
        puntos = []
        g = 9.81
        angulo_rad = (self.angulo*(math.pi/180))
        Vo_y = self.velocidad*math.sin(angulo_rad)
        

        self.t = (2*Vo_y)/g

        self.Hmax = ((self.velocidad**2)*math.sin(angulo_rad))/(2*g)
        self.alcance = (self.velocidad**2 * math.sin(2*angulo_rad)) / g #((Vo^2) x sen(20))/g
        
        for i in range(101):
            x_porcentaje = i/100
            x_fisico = x_porcentaje * self.alcance
            
            #Calcular la posicion en y, y su altura max
            y_fisico = (x_fisico*math.tan(angulo_rad)-(g*x_fisico**2)/(2*self.velocidad**2*math.cos(angulo_rad)**2))       
            self.altura_maxima = (self.velocidad**2 * math.sin(angulo_rad)**2) / (2 * g)# ((Vo)^2 x sen(0)^2)/2g
            
            #Llevando de la escala  de metros a ps
            escala_x = (1600 * 0.9) / self.alcance
            escala_y = (900 * 0.6) / self.altura_maxima
            escala = min(escala_x, escala_y)
            x_pantalla = 50 + (x_fisico*escala)  
            y_pantalla = 100 + (y_fisico*escala)
            
            #Calcular la velocidad en un punto 
            #Velocidad en X
            Vo_x = self.velocidad*math.cos(self.angulo)
            Vx = Vo_x

            #Velocidad en y
            Vy = Vo_y - (2*g*y_fisico)        

            if y_pantalla >= 100:
                puntos.extend([x_pantalla, y_pantalla])
        
        return puntos

    def animar_trayectoria(self,instance):

        self.velocidad = int(self.velocidad_input.text)
        self.angulo = int(self.angulo_input.text)
        self.puntos = self.puntos_parabola()
        pos_y=0

        self.i = 0

        total_puntos = len(self.puntos)//2

        frame_info = [0]
        puntos_x = []
    

        def animar_frame(dt):
            if frame_info[0] >= total_puntos:
                with self.canvas.after:
                    Color(1,0,0,1)
                    Line(points=(self.puntos[-2],85,self.puntos[-2],35),width=1)

                    Color(1,0,0,1)
                    Line(points=(50,85,50,35),width=1)

                    Color(1,0,0,1)
                    Line(points=((self.puntos[-2]/2)+30,100,(self.puntos[-2]/2)+30,self.puntos[len(self.puntos)//2]),width=1)
                    

                return False

            self.canvas.after.clear()

            with self.canvas.after:
                puntos_ahora = self.puntos[:(frame_info[0]*2)+2]
                puntos_x.append(puntos_ahora[-2])
                puntos_x.append(60)
                print(puntos_x)
                #Trayectoria
                Color(0.7,0.5,0,1)
                Line(points=puntos_ahora,width=3)

                #Punto
                x,y = self.puntos[frame_info[0]*2],self.puntos[frame_info[0]*2+1]
                Color(1,0,0,1)
                Ellipse(pos=(x-8,y-8),size=(16,16))

                Color(1,0,0,1)
                Line(points=puntos_x,width=1)

            frame_info[0] += 1                        

        
            return True
        
        self.canvas.clear()
        self.canvas.after.clear()

        with self.canvas:
            Color(0.9,0.9,0.9,1)
            Line(points=[0,100,1600,100])

            
            

        time = Label(text=f"Tiempo de vuelo: {str(round(self.t,3))}s",size_hint=(None,None),size={300,150},pos=(1000,800),color=(1,0,0,1),font_size=30)
        altura_max = Label(text=f"Altura maxima: {str(round(self.Hmax,3))}m",size_hint=(None,None),size={300,150},pos=(1000,760),color=(1,0,0,1),font_size=30)
        alcane_max = Label(text=f"Alcance maximo: {str(round(self.alcance,3))}m",size_hint=(None,None),size={300,150},pos=(1000,720),color=(1,0,0,1),font_size=30)

        self.add_widget(time)
        self.add_widget(altura_max)
        self.add_widget(alcane_max)

        
        Clock.schedule_interval(animar_frame,0.05)
        



class ProyectilApp(App):
    def build(self):
        return Contenedor()

if __name__ == '__main__':
    ProyectilApp().run()
