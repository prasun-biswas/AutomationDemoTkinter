from tkinter import *
from Ball import *
from Rectangle import *
from WSFunctions import *
import time

window = Tk()

WIDTH = 700
HEIGHT = 280

# visual elements outside of Workstation


# at first declare fram where the other elements will be organized
frame_number = LabelFrame(window,padx=5, pady =5)
frame_number.grid(row = 0, column = 0, sticky=W+E+N+S, columnspan = 2)
frame_Coat = LabelFrame(window,padx=5, pady =5)
frame_Coat.grid(row = 1, column = 0, sticky=W+E+N+S)
frame_Package = LabelFrame(window,padx=5, pady =5)
frame_Package.grid(row = 1, column = 1, sticky=W+E+N+S)
frame_Button = LabelFrame(window,padx=5, pady =5)
frame_Button.grid(row = 0, column = 2,rowspan = 2, sticky=W+E+N+S)
frame_Display = LabelFrame(window,padx=5, pady =5)
frame_Display.grid(row = 0, column = 3, rowspan = 2, sticky=W+E+N+S)

# declare and organize the label and entry for number of balls
label_Enter_Number = Label(frame_number,bg = "linen",fg ="black",bd= 5, padx = 5, pady = 5,relief=RIDGE,text ="Number(1-10)")
label_Enter_Number.grid(row = 0, column = 0)
# enter_Number = Entry(frame_number, width = 5, bg = "white",fg ="black")
# enter_Number.grid(row = 0, column = 1)
enter_Number = Spinbox(frame_number, width = 5, bg = "white",fg ="black", from_ = 1, to =10)
enter_Number.grid(row = 0, column = 1)


# build the options for selecting coating options
coat = StringVar()
coat.set('red')
def setCoat():
    coat.get()

label_Select_Coat = Label(frame_Coat,bg = "linen",fg ="black", bd = 5, padx = 5, pady = 5,relief=RIDGE,text ="Select Coat")
label_Select_Coat.grid(row = 0, column = 0)

Radiobutton(frame_Coat,text ="R", variable =coat, value="red", command = setCoat).grid(row = 1)
Radiobutton(frame_Coat,text ="G", variable =coat, value="green", command = setCoat).grid(row = 2)
Radiobutton(frame_Coat,text ="B", variable =coat, value="blue", command = setCoat).grid(row = 3)

# build the options for selecting packing size options
pack = IntVar()
pack.set(1)

def setBoxSize():
    pack.get()

label_Select_Package = Label(frame_Package,bg = "linen",fg ="black",bd = 5, padx = 5, pady = 5,relief=RIDGE,text ="Box size")
label_Select_Package.grid(row = 0, column = 0)

Radiobutton(frame_Package,text ="1", variable =pack, value=1, command = setBoxSize).grid(row = 1)
Radiobutton(frame_Package,text ="2", variable =pack, value=2, command = setBoxSize).grid(row = 2)
Radiobutton(frame_Package,text ="3", variable =pack, value=3, command = setBoxSize).grid(row = 3)

# start and stop button
processRunning = True
def startProcess():
    global processRunning
    processRunning = True
    Ball.Running = True
    button_Start["state"]=DISABLED
    processInSequence()

def stopProcess():
    global processRunning
    Ball.Running= False
    processRunning=False
    button_Start["state"]=NORMAL



button_Start = Button(frame_Button, text = "Start",fg = "olive drab",padx= 20, pady = 20,bd= 5, command =startProcess )
button_Start.grid(row = 0, column =0,sticky=W+E+N+S)
button_Stop = Button(frame_Button, text = "Stop",fg = "tomato",padx= 20, pady = 20,bd= 5, command =stopProcess )
button_Stop.grid(row = 1, column =0,sticky=W+E+N+S)


# display status of the workstation
conv_rect1 = Label(frame_Display,bg = "white",fg ="black", bd=3,padx = 5, pady = 5,relief=GROOVE,text ="Conveyor 1")
conv_rect1.grid(row = 0, column = 0,sticky=W+E+N+S)
conv_rect2 = Label(frame_Display,bg = "white",fg ="black",bd=3, padx = 5, pady = 5,relief=GROOVE,text ="Conveyor 2")
conv_rect2.grid(row = 1, column = 0,sticky=W+E+N+S)
conv_rect1_end = Label(frame_Display,bg = "white",fg ="black", bd=3,padx = 5, pady = 5,relief=GROOVE,text ="Base Coating")
conv_rect1_end.grid(row = 0, column = 1,sticky=W+E+N+S)
conv_rect2_end = Label(frame_Display,bg = "white",fg ="black", bd=3,padx = 5, pady = 5,relief=GROOVE,text ="Main Coating")
conv_rect2_end.grid(row = 1, column = 1,sticky=W+E+N+S)
conv_rect_spray1 = Label(frame_Display,bg = "white",fg ="black", bd=3,padx = 5, pady = 5,relief=GROOVE,text ="Spray 1")
conv_rect_spray1.grid(row = 0, column = 2,sticky=W+E+N+S)
conv_rect_spray2 = Label(frame_Display,bg = "white",fg ="black",bd=3, padx = 5, pady = 5,relief=GROOVE,text ="Spray 2")
conv_rect_spray2.grid(row = 1, column = 2,sticky=W+E+N+S)
conv_rect_unloader = Label(frame_Display,bg = "white",fg ="black",bd=3, padx = 5, pady = 5,relief=GROOVE,text ="Unloading")
conv_rect_unloader.grid(row = 0, column = 3,sticky=W+E+N+S)
conv_packing_box = Label(frame_Display,bg = "white",fg ="black",bd=3, padx = 5, pady = 5,relief=GROOVE,text ="Packing")
conv_packing_box.grid(row = 1, column = 3,sticky=W+E+N+S)

def changeLabelColorTimer(item,color,time):
    if(processRunning):
        item.configure(item,bg=color)
        item.after(time,changeLabelColorTimer, item,'white',time)

def startConveyor(rect,ip_Ball,label,time):
    if(processRunning):
        changeLabelColorTimer(label,"green",time)
        rect.runConveyorX(ip_Ball, window)


# display_Canvas = Canvas(frame_Display,width =340, height = 160, bg = "white")
# display_Canvas.grid(row = 0, column = 0)
# main workstation area as canvas
my_canvas = Canvas(window,width=WIDTH,height=HEIGHT,bg = "white", bd = 5)
my_canvas.grid(row = 5, column =0, columnspan = 6)



# number_of_ball = int(enter_Number.get())

# text = my_canvas.create_text(220+10,180+10,text ='1')
# rect_spray1 = Rectangle(my_canvas,300,160,400,170,"yellow","wsSpr1")
rect_spray1 = my_canvas.create_rectangle(100,160,200,170,fill="yellow") #first spray
rect_spray2 = my_canvas.create_rectangle(350,160,450,170,fill="yellow") #second spray

# this following rectangles are different workstations
rect1 = Rectangle(my_canvas,20,200,300,220,"red","ws1")
rect1_end = Rectangle(my_canvas,300,170,305,220,"yellow","es1")
rect2 = Rectangle(my_canvas,305,200,500,220,"cyan","ws2")
rect2_end = Rectangle(my_canvas,500,170,505,220,"green","es2")

# my_canvas.itemconfigure(rect_spray1, fill='red')

# create balls and store

def startSpray(item,color):
    if(processRunning):
        my_canvas.itemconfig(item,fill=color)
        my_canvas.after(1500,startSpray, item,'yellow')
# hello

def turnOnWorkStation():
    count =0
    rect_loader= Rectangle(my_canvas,20,200-int(enter_Number.get())*20,40,200,"white","ws1") # balls stays on this loader
    store_ball_objects = WSFunctions.loadBallinContainer(int(enter_Number.get()),my_canvas)
    rect_unloader = Rectangle(my_canvas,505,200,525,200+20*pack.get(),"white","ws1") #balls stays in this unloader
    for i in range(int(enter_Number.get())):
        if(processRunning):
            ip_Ball = store_ball_objects[i]
            rect_loader.runConveyorY(ip_Ball,window)
            my_canvas.after(500,startSpray,rect_spray1,'red')
            changeLabelColorTimer(conv_rect_spray1,"green",1500)
            startConveyor(rect1,ip_Ball, conv_rect1, 3000)#rect1.runConveyorX(ip_Ball, window)
            startConveyor(rect1_end,ip_Ball, conv_rect1_end, 500)#rect1_end.runConveyorX(ip_Ball, window)
            if(processRunning):
                rect1_end.changeObjectColor(ip_Ball,"yellow")

            my_canvas.after(300,startSpray,rect_spray2,'red')
            changeLabelColorTimer(conv_rect_spray2,"green",1500)
            startConveyor(rect2,ip_Ball, conv_rect2, 2500)#rect2.runConveyorX(ip_Ball, window)
            startConveyor(rect2_end,ip_Ball, conv_rect2_end, 500)#rect2_end.runConveyorX(ip_Ball, window)
            if(processRunning):
                rect2_end.changeObjectColor(ip_Ball, coat.get())
            rect_unloader.runConveyorYToSlot(ip_Ball,window,count)
            count+=1
            if((count==pack.get()) or (i+1==int(enter_Number.get()))):
                WSFunctions.moveMultipleObject(window,my_canvas,"packed",25,0)
                changeLabelColorTimer(conv_packing_box,"green",1000)
            if(count==pack.get()):
                count=0

def processInSequence():
    turnOnWorkStation()
    button_Start["state"]=NORMAL



# turnOnWorkStation()



#

# def printGlobalVarStartingPos():
#     print("global start pos"+GlobalVariables.starting_Pos)

window.mainloop()

