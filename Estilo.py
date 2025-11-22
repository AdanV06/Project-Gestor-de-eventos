kv = '''
<BoxL>:
    size_hint: None,None 
    size: 900,700
    pos_hint: {"center_x": 0.5, "center_y": 0.5}
    orientation: "vertical"

    canvas.before:
        Color:
            rgba: 0.2,0,0.7,0.65
        
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15]

    canvas.after:
        Color:
            rgba: 0,0,0,1
        Line:
            rounded_rectangle: (self.x,self.y,self.width,self.height,15)
            width: 1.2

<BoxButtons>:
    size_hint: None,None
    size: 800,50


    canvas.before:
        Color:
            rgba: 0,0,0,0
        RoundedRectangle:
            pos: self.pos
            size: self.size

<Buttons>:
    background_color: 0,0,0,0

    font_size: 20

    canvas.after:
        Color:
            rgba: 1,1,1,1
        Line: 
            points: (self.x+1,self.y,self.x+self.width-1,self.y)
            width: 1.5
        
    
<Titulo>:
    size_hint: None,None
    size: 800,60


    canvas.before:
        Color:
            rgba: 0,0,0,0.1
        RoundedRectangle:
            pos: self.pos
            size: self.size
<Texto>:
    markup: True
    text: "[b] Observatorio de Astrofisica [/b]"
    font_size: 36
    pos_hint: {"center_x": 0,"center_y": 0.35}
    size_hint: None,None
    size: self.texture_size

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

<menu>:
    size_hint: None,None
    size: 725,768
    pos: 100,290
    orientation: "vertical"
    index:0

    canvas.before:
        Color:
            rgba: 0.2,0,0.55,0.1
        Rectangle:
            pos: self.pos
            size: self.size
            
<filas>:
    size_hint: None,None
    padding: 0,0

    canvas.before:
        Color: 
            rgba: 0,0,0,0.3
        Rectangle:
            pos: self.pos
            size: self.size
<TiposPersonal>:
    markup: True
    font_size: 22
    pos_hint: {"x": 0.0,"top":1} 
    size_hint: None,None
    size: 724,40

    canvas.before:
        Color:
            rgba: 0,0,0,0.5
        RoundedRectangle:
            pos: self.pos
            size: self.size
        
<Contenedor_Recursos>:
    size_hint: None,None
    size: 725,768
    padding: 20,0
    orientation: "vertical"

    canvas.before:
        Color: 
            rgba: 0.2,0,0.8,0.1,
        Rectangle:
            pos: self.pos
            size: self.size

<informacion_personaje>:
    size_hint: None,None 
    size: 700,210   

    canvas.before:
        Color: 
            rgba: 0,0,0,0.3
        Rectangle:
            pos: self.pos
            size: self.size

<informacion>:
    canvas.before:
        Color: 
            rgba: 0.2,0,0.5,0.2
        Rectangle:
            pos: self.pos
            size: self.size

<vent_cant>:
    canvas.before:
        Color:
            rgba: 0,0,0,0
        Rectangle:
            pos:self.pos
            size: self.size      


'''