from tkinter import *
from Ball import *
from testFunction_1 import Timer
from Rectangle import *
from WSFunctions import *
import time

window = Tk() #Tkinter default window required for placing any visual object from Tkinter widgets

# visual elements outside of Workstation
""" Frames are a very useful tool to lockup space within Tkinter window where other visual elements
    can be placed with pack()  or grid() function for this program 4 frame is defined where other 
    widgets such as Label, Radio button, Spinbox have been placed. Those are defined below with necessary
    parameter for geomatric shape, color, text, fit etc. """

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

# declare and organize the label and entry for number of balls, from Spinbox user can choose
# number of ball within the range of (1-10). The default value is 1
label_Enter_Number = Label(frame_number,bg = "linen",fg ="black",bd= 5, padx = 5, pady = 5,relief=RIDGE,text ="Number(1-10)")
label_Enter_Number.grid(row = 0, column = 0)
enter_Number = Spinbox(frame_number, width = 5, bg = "white",fg ="black", from_ = 1, to =10)
enter_Number.grid(row = 0, column = 1)


"""Following snippet builds the option for selecting coating color using radio button and label the 
   default value is 'red' and the selected option by user is changed with setCoat() function"""

coat = StringVar()
coat.set('red')
def setCoat():
    coat.get()

label_Select_Coat = Label(frame_Coat,bg = "linen",fg ="black", bd = 5, padx = 5, pady = 5,relief=RIDGE,text ="Select Coat")
label_Select_Coat.grid(row = 0, column = 0)

Radiobutton(frame_Coat,text ="R", variable =coat, value="red", command = setCoat).grid(row = 1)
Radiobutton(frame_Coat,text ="G", variable =coat, value="green", command = setCoat).grid(row = 2)
Radiobutton(frame_Coat,text ="B", variable =coat, value="blue", command = setCoat).grid(row = 3)

"""Following snippet builds the option for selecting Packing size using radio button and label the 
   default value is 1 and the selected option by user is changed with setCoat() function"""
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

# Global variable in boolean to indicate if process is started or stopped

processRunning = True # true when the process is running
TimerState = True # true when process is running(used for the timer)

def startProcess():
    """ this mehtod is called with the press of the start button where it changes the boolean value
    of some variable and start the movement process for the visualization by calling processInSequence()
    method. """
    global processRunning
    global TimerState
    processRunning = True
    TimerState = True
    Ball.Running = True
    button_Start["state"]=DISABLED
    processInSequence()

def stopProcess():
    """ this mehtod is called with the press of the stop button where it changes the boolean value
    of some variable and stop the movement process for the visualization"""
    global processRunning
    global TimerState
    Ball.Running= False
    processRunning=False
    TimerState = False
    button_Start["state"]=NORMAL


# start and stop button with geometric parameter, text, color and function
button_Start = Button(frame_Button, text = "Start",fg = "olive drab",padx= 20, pady = 20,bd= 5, command =startProcess )
button_Start.grid(row = 0, column =0,sticky=W+E+N+S)
button_Stop = Button(frame_Button, text = "Stop",fg = "tomato",padx= 20, pady = 20,bd= 5, command =stopProcess )
button_Stop.grid(row = 1, column =0,sticky=W+E+N+S)

# this sinppet create label to display status of the workstation by changing color
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

# this label shows the runtime in seconds.
Time_label = Label(frame_Display,bg = "white",fg ="black",bd=3, padx = 5, pady = 5,relief=GROOVE,text ="time")
Time_label.grid(row = 3, column = 0, rowspan= 2,columnspan = 3,sticky=W+E+N+S)

def changeLabelColorTimer(item,color,time):
    """ this method changes label (display LED)color to show active process status
    here item can be any widget """
    if(processRunning):
        item.configure(item,bg=color)
        item.after(time,changeLabelColorTimer, item,'white',time)

def startConveyor(rect,ip_Ball,label,time):
    """ for the conveyor(1 and 2), coating(base and main) this function turns on the
    movement by calling runConveyorX() method from rectangle class and also changes the
    label for display LED"""
    if(processRunning):
        changeLabelColorTimer(label,"green",time)
        rect.runConveyorX(ip_Ball, window)

def refresh_label(seconds):
        """ refresh the content of the Timer label every second """
        # increment the time
        seconds += 1
        # display the new time
        Time_label.configure(text="%i s" % seconds)
        # request tkinter to call self.refresh after 1s (the delay is given in ms)
        if(TimerState):
            Time_label.after(1000, refresh_label,seconds)

# main workstation area as canvas
# size of the
WIDTH = 700
HEIGHT = 280
my_canvas = Canvas(window,width=WIDTH,height=HEIGHT,bg = "white", bd = 5)
my_canvas.grid(row = 5, column =0, columnspan = 6)

rect_spray1 = my_canvas.create_rectangle(100,160,200,170,fill="yellow") #first spray
rect_spray2 = my_canvas.create_rectangle(350,160,450,170,fill="yellow") #second spray

# this following rectangles are different part of the workstations
rect1 = Rectangle(my_canvas,20,200,300,220,"red","ws1") #conveyor 1
rect1_end = Rectangle(my_canvas,300,170,305,220,"yellow","es1") # base coating machine
rect2 = Rectangle(my_canvas,305,200,500,220,"cyan","ws2") #conveyor 2
rect2_end = Rectangle(my_canvas,500,170,505,220,"green","es2") # main coating machine

# my_canvas.itemconfigure(rect_spray1, fill='red')
# text in the canvas to indicate some key parts
my_canvas.create_text(150, 250, text =" conveyor 1")
my_canvas.create_text(400, 250, text =" conveyor 2")
my_canvas.create_text(150, 150, text =" Spray 1")
my_canvas.create_text(400, 150, text =" spray 2")
my_canvas.create_text(300, 230, text =" base")
my_canvas.create_text(493, 230, text =" main")
my_canvas.create_text(52, 160, text =" load")
my_canvas.create_text(520, 160, text =" unload")

def startSpray(item,color):
    """ this method runs the spray for rect_spray1 and rect_spray2"""
    if(processRunning):
        my_canvas.itemconfig(item,fill=color)
        my_canvas.after(1500,startSpray, item,'yellow')

def turnOnWorkStation():
    """ this the function where all the sequence of the two workstation is executed based on the option
    selected by user. The method is called from processInSequence() function"""
    if(TimerState):
        Time_label.after(1000,refresh_label,1) #start the timer

    count =0
    rect_loader= Rectangle(my_canvas,20,200-int(enter_Number.get())*20,40,200,"white","ws1") # balls stays on this loader
    #creates ball object using staticmethod from WSFunctions class
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
                rect1_end.changeObjectColor(ip_Ball,"yellow") # changes the color of the ball

            my_canvas.after(300,startSpray,rect_spray2,'red')
            changeLabelColorTimer(conv_rect_spray2,"green",1500)
            startConveyor(rect2,ip_Ball, conv_rect2, 2500)#rect2.runConveyorX(ip_Ball, window)
            startConveyor(rect2_end,ip_Ball, conv_rect2_end, 500)#rect2_end.runConveyorX(ip_Ball, window)
            if(processRunning):
                rect2_end.changeObjectColor(ip_Ball, coat.get())#changes the color of the ball with selected color
            rect_unloader.runConveyorYToSlot(ip_Ball,window,count) # unloads the ball to the box
            changeLabelColorTimer(conv_rect_unloader,"green",1000)
            count+=1
            if(((count==pack.get()) or (i+1==int(enter_Number.get()))) and processRunning):
                WSFunctions.moveMultipleObject(window,my_canvas,"packed",25,0) # release the balls in when pack size reached
                changeLabelColorTimer(conv_packing_box,"green",1000)
            if(count==pack.get()):
                count=0

def processInSequence():
    """turns on workstations by calling the method and changes global variable to represent change of state"""
    turnOnWorkStation()
    global TimerState
    TimerState = False
    button_Start["state"]=NORMAL

window.mainloop() # keeps the window visible throughout the process

