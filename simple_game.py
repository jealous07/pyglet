import pyglet

# Create a window
window = pyglet.window.Window(800, 600,"Simple Game")

#Define an event handler for the window's on_draw event
@window.event
def on_draw():
    window.clear()  #clear the window
    pyglet.text.Label('Hello, Pyglet!',
    front_name='Times New Roman',
    front_size=36,
    x=window.width // 2,
y=window.height // 2,
        anchor_x='center', anchor_y='center') . draw()
    
    
    pyglet.app.run()
    