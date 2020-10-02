from tkinter import *
from Ball import *
from Rectangle import *
from WSFunctions import *
import threading
import time

window = Tk()

WIDTH = 1000
HEIGHT = 500

my_canvas = Canvas(window,width=WIDTH,height=HEIGHT,bg = "white", bd = 5)
my_canvas.pack()

number_of_ball = 3
rect_loader= Rectangle(my_canvas,220,200-number_of_ball*20,240,200,"white","ws1")


store_ball_objects = WSFunctions.loadBallinContainer(number_of_ball,my_canvas)


# text = my_canvas.create_text(220+10,180+10,text ='1')
rect_spray1 = Rectangle(my_canvas,300,160,400,170,"yellow","wsSpr1")
rect1 = Rectangle(my_canvas,220,200,500,220,"red","ws1")
rect1_end = Rectangle(my_canvas,500,170,505,220,"green","es1")
rect2 = Rectangle(my_canvas,505,200,700,220,"cyan","ws2")
rect2_end = Rectangle(my_canvas,700,170,705,220,"yellow","es2")
rect_unloader= Rectangle(my_canvas,705,200,720,200+20*number_of_ball,"white","ws1")



# this part represents process on conveyer



def turnOnWorkStation():
    for i in range(number_of_ball):
        ip_Ball = store_ball_objects[i]
        rect_loader.runConveyorY(ip_Ball,window)
        my_canvas.itemconfig(rect_spray1,fill = "red")

        rect1.runConveyorX(ip_Ball, window)
        rect1_end.runConveyorX(ip_Ball, window)
        rect1_end.changeObjectColor(ip_Ball, "red")

        rect2.runConveyorX(ip_Ball, window)
        rect2_end.runConveyorX(ip_Ball, window)
        rect2_end.changeObjectColor(ip_Ball, "blue")
        rect_unloader.runConveyorYToSlot(ip_Ball,window,i)

turnOnWorkStation()
WSFunctions.moveMultipleObject(window,my_canvas,"packed",30,0)

window.mainloop()

