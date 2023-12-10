from graphics import Canvas
import math as mt
import time as t

    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
delay=.000001
Pi=3.1416
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO: your code here!
    canvas.create_rectangle(0,0,400,400,'black')
    canvas.create_line(0,200,400,200,'white')
    ratio=input('Enter basic trigometric ratio(sin,cos,tan) to watch the graph 📉 :')
    
    if ratio=='sin':
        canvas.create_text(300, 20, font='Arial', font_size = 20, text='Sine wave', color='white')
        sin(canvas)
        
    if ratio=='tan':
        canvas.create_text(150, 20, font='Arial', font_size = 20, text='tangent function', color='white')
        tan(canvas)
    if ratio=='cos':
        canvas.create_text(270, 20, font='Arial', font_size = 20, text='Cosine wave', color='white')
        cos(canvas)
        
    
    
def tan(canvas):
    radian=0
    y=200
    while True:
        oval = canvas.create_oval(radian, y,radian+1,y+1,'white')
        y=100*(mt.tan(.1*radian))+200
        radian+=Pi/30
        t.sleep(delay)


def sin(canvas):
    radian=0
    y=200
    oval = canvas.create_oval(radian, y,radian+.1,y+.1,'white')
    while True:
        canvas.moveto(oval,radian)
       
        y=100*((mt.sin(1*radian)))+100*(mt.sin(3*radian))+100*(mt.sin(5*radian))+100*(mt.sin(7*radian))
        radian+=Pi/30
        t.sleep(delay)
        
def cos(canvas):
    radian=0
    y=200
    while True:
        oval = canvas.create_oval(radian, y,radian+1,y+1,'white')
        y=100*(mt.cos(.1*radian))+200
        radian+=Pi/30
        t.sleep(delay)
    

if __name__ == '__main__':
    main()