kv4 = '''
<Item_event>:
    orientation: "horizontal"
    size_hint: None,None
    size: 870,80

    canvas.before:
        Color:
            rgba: 0.3,0,0.8,0.7
        Rectangle:
            pos: self.pos
            size: self.size

<cont_event>:
    orientation: 'vertical'
    size_hint: None,None
    spacing: 8

    canvas.before:
        Color:
            rgba: 1,0,0,0
        Rectangle:
            pos: self.pos
            size: self.size


'''