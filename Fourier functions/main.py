from graphics import Canvas
import math as mt
import time as t
    
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
delay=0.0001
Pi=3.1416
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO: your code here!
    canvas.create_rectangle(0,0,600,600,'black')
    canvas.create_line(0,300,600,300,'white')
    sin(canvas)
    #ratio=input('Enter basic trigometric ratio(sin,cos,tan) to watch the graph 📉 :')
    
    #if ratio=='sin':
        #canvas.create_text(300, 20, font='Arial', font_size = 20, text='Sine wave', color='white')
        #sin(canvas)
    
    # TODO: your code here!

def sin(canvas):
    radian=1
    y=0
    f_x=300
    n=10
    k=.01
    oval = canvas.create_oval(radian,f_x,radian+10,f_x+10,'white')
    while True:
        canvas.moveto(oval,radian,f_x)
        canvas.create_oval(radian,f_x,radian+1,f_x+1,'white')
        
        f_x=.4*(mt.sin(n*k*radian))
        
        for i in range(1):
            n=2*i+1
            y=.4*(mt.sin(n*k*radian))
            f_x+=y
            print(n)
        radian+=Pi/180
        t.sleep(delay)


if __name__ == '__main__':
    main()