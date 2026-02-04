'''
En este archivo es donde se crea el estilo de los elementos de la ventana Agregar Evento,
esta compuesto en su totalidad en lenguaje kv y forma parte solamente de el diseño de la interfaz grafica
'''

kv2 = ''' 
<Input_Name>:
    hint_text: "Nombre del evento"
    font_size: 20
    background_color: 0,0.3,0,0.4
    foreground_color: 1,1,1,1
    size_hint: None,None
    size: 420,40
    pos_hint: {"center_x": 0.68,"center_y" : 0.83}
    on_text: if len(self.text)>45:self.text = self.text[:45]

<Year_inicio>:
    hint_text: "year"
    size_hint: None,None
    background_color: 0,0.3,0,0.4
    foreground_color: 1,1,1,1
    size: 68,30
    font_size: 16
    pos_hint: {"center_x": 0.56,"center_y" : 0.55}
    on_text: if len(self.text)>4:self.text = self.text[:4]

<Year_fin>:
    hint_text: "year"
    size_hint: None,None
    background_color: 0,0.3,0,0.4
    foreground_color: 1,1,1,1
    size: 68,30
    font_size: 16
    pos_hint: {"center_x": 0.56,"center_y" : 0.43}
    on_text: if len(self.text)>4:self.text = self.text[:4]

<Month_inicio>:
    hint_text: 'month'
    size_hint: None,None
    background_color: 0,0.3,0,0.4
    foreground_color: 1,1,1,1
    size: 68,30
    font_size: 16
    pos_hint: {"center_x": 0.656,"center_y" : 0.55}
    on_text: if len(self.text)>2:self.text = self.text[:2]

<Month_fin>:
    hint_text: 'month'
    size_hint: None,None
    background_color: 0,0.3,0,0.4
    foreground_color: 1,1,1,1
    size: 68,30
    font_size: 16
    pos_hint: {"center_x": 0.656,"center_y" : 0.43}
    on_text: if len(self.text)>2:self.text = self.text[:2]

<Day_inicio>:
    hint_text: "day"
    size_hint: None,None
    cursor_color: 0,0,0,1
    background_color: 0,0.3,0,0.4
    foreground_color: 1,1,1,1
    size: 68,30
    font_size: 16
    pos_hint: {"center_x": 0.75,"center_y" : 0.55}
    on_text: if len(self.text)>2:self.text = self.text[:2]

<Day_fin>:
    hint_text: "day"
    size_hint: None,None
    cursor_color:0,0,0,1
    background_color: 0,0.3,0,0.4
    foreground_color: 1,1,1,1
    size: 68,30
    font_size: 16
    pos_hint: {"center_x": 0.75,"center_y" : 0.43}
    on_text: if len(self.text)>2:self.text = self.text[:2]

<Hora_inicio>:
    font_size: 14
    background_color: 0,0.3,0,0.4
    foreground_color: 1,1,1,1
    size_hint: None,None
    size: 30,30
    pos_hint: {"center_x": 0.85,"center_y" : 0.55}
    on_text: if len(self.text)>2:self.text = self.text[:2]

<Hora_fin>:
    font_size: 14
    background_color: 0,0.3,0,0.4
    foreground_color: 1,1,1,1
    size_hint: None,None
    size: 30,30
    pos_hint: {"center_x": 0.85,"center_y" : 0.43}
    on_text: if len(self.text)>2:self.text = self.text[:2]

<Min_inicio>:
    font_size: 14
    background_color: 0,0.3,0,0.4
    foreground_color: 1,1,1,1
    size_hint: None,None
    size: 30,30
    pos_hint: {"center_x": 0.90,"center_y" : 0.55}
    on_text: if len(self.text)>2:self.text = self.text[:2]

<Min_fin>:
    font_size: 14
    background_color: 0,0.3,0,0.4
    foreground_color: 1,1,1,1
    size_hint: None,None
    size: 30,30
    pos_hint: {"center_x": 0.90,"center_y" : 0.43}
    on_text: if len(self.text)>2:self.text = self.text[:2]

<Text_inicio>:
    text: " Inicio: "
    font_size: 21 
    size_hint: None,None
    size: 50,20
    pos_hint: {"center_x": 0.47,"center_y" : 0.552}
    on_text: if len(self.text)>2:self.text = self.text[:2]

<Text_fin>:
    text: " Fin: "
    font_size: 21 
    size_hint: None,None
    size: 50,20
    pos_hint: {"center_x": 0.47,"center_y" : 0.432}

<Text_hora>:
    text: "Hora : Minutos"
    font_size: 15
    size_hint: None,None
    size: 50,20
    pos_hint: {"center_x": 0.88,"center_y" : 0.64}

<Text_recursos>:
    text: "Seleccione los recursos"
    font_size: 23
    size_hint: None,None
    size: 100,30
    pos_hint: {"center_x": 0.6,"center_y" : 0.25}

<Sala_selec>:
    text: 'Seleccione una sala'
    values: ["Planetario","Cupula de observacion","Cupula de fotografia","Sala de conferencias","Sala de optica"]
    size_hint: None,None
    size: 260,35
    font_size: 23
    background_normal: ""
    pos_hint: {"center_x": 0.21,"center_y" : 0.8}
    background_color: 0,0,0,0.2

<Lbl>:
    size_hint: None,None
    size: 300,400
    pos_hint: {"center_x": 0.21,"top": 0.70}
    

    canvas.before:
        Color:
            rgba: 0,0,0,1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15]

<ButtonGuardar>:
    source: "Imagenes/Copilot_20251117_003303.png"
    size_hint: None,None
    size: 190,80
    pos: 510,120

<ButtonBuscarHueco>:
    source: "Imagenes/Buscar Horario.png"
    size_hint: None,None
    size: 190,80
    pos: 770,120
'''