import pgzrun,random
TITLE="Good Shot game"
WIDTH=500
HEIGHT=500
alien=Actor("alien")
message=""
def draw():
    screen.fill("light pink")
    alien.draw()
    screen.draw.text(message,center=(400,30),fontsize=30)
def update():
    pass

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        alien.x=random.randint(50,450)
        alien.y=random.randint(50,450)
        message="Good Shot!" 
    else:
        message="Bad Shot!"
pgzrun.go()

