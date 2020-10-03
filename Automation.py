from tkinter import *
from Ball import *
from Rectangle import *
from WSFunctions import *
import time

window = Tk()

WIDTH = 1000
HEIGHT = 500

my_canvas = Canvas(window,width=WIDTH,height=HEIGHT,bg = "white", bd = 5)
my_canvas.pack()

number_of_ball = 2
rect_loader= Rectangle(my_canvas,220,200-number_of_ball*20,240,200,"white","ws1") # balls stays on this loader

# text = my_canvas.create_text(220+10,180+10,text ='1')
# rect_spray1 = Rectangle(my_canvas,300,160,400,170,"yellow","wsSpr1")
rect_spray1 = my_canvas.create_rectangle(300,160,400,170,fill="yellow") #first spray
rect_spray2 = my_canvas.create_rectangle(550,160,650,170,fill="yellow") #second spray

# this following rectangles are different workstations
rect1 = Rectangle(my_canvas,220,200,500,220,"red","ws1")
rect1_end = Rectangle(my_canvas,500,170,505,220,"green","es1")
rect2 = Rectangle(my_canvas,505,200,700,220,"cyan","ws2")
rect2_end = Rectangle(my_canvas,700,170,705,220,"yellow","es2")
rect_unloader= Rectangle(my_canvas,705,200,720,200+20*number_of_ball,"white","ws1") #balls stays in this unloader


# my_canvas.itemconfigure(rect_spray1, fill='red')

# this part represents process on conveyer

# item = my_canvas.create_rectangle(50, 25, 150, 75, fill="blue")
# taskStarted = False

# create balls and store
store_ball_objects = WSFunctions.loadBallinContainer(number_of_ball,my_canvas)

def startSpray(item,color):
    my_canvas.itemconfig(item,fill=color)
    my_canvas.after(1500,startSpray, item,'yellow')
# hello

def turnOnWorkStation():
    for i in range(number_of_ball):
        ip_Ball = store_ball_objects[i]
        rect_loader.runConveyorY(ip_Ball,window)
        my_canvas.after(500,startSpray,rect_spray1,'red')
        rect1.runConveyorX(ip_Ball, window)
        rect1_end.runConveyorX(ip_Ball, window)
        rect1_end.changeObjectColor(ip_Ball, "red")

        my_canvas.after(300,startSpray,rect_spray2,'red')
        rect2.runConveyorX(ip_Ball, window)
        rect2_end.runConveyorX(ip_Ball, window)
        rect2_end.changeObjectColor(ip_Ball, "blue")
        rect_unloader.runConveyorYToSlot(ip_Ball,window,i)
    WSFunctions.moveMultipleObject(window,my_canvas,"packed",30,0)

turnOnWorkStation()



#

# def printGlobalVarStartingPos():
#     print("global start pos"+GlobalVariables.starting_Pos)



window.mainloop()

