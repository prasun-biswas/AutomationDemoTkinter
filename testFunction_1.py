# from tkinter import *
# from Ball import *
# from Rectangle import *
# import time
#
# window = Tk()
#
# WIDTH = 700
# HEIGHT = 500
#
# canvas = Canvas(window,width=WIDTH,height=HEIGHT,bg = "white", bd = 5)
# canvas.pack()
#
# tennis_ball = Ball(canvas,0,0,50,4,0,"yellow")
# rect = Rectangle(canvas,0,100,500,80,"red")
#
# while True:
#     tennis_ball.move()
#     window.update()
#     time.sleep(0.01)
#
# window.mainloop()
#
#
# class Ball:
#
#
#     def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
#         self.canvas = canvas
#         self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
#         self.xVelocity = xVelocity
#         self.yVelocity = yVelocity
#
#     def move(self):
#         coordinates = self.canvas.coords(self.image)
#
#         if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
#             self.xVelocity = -self.xVelocity
#         if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
#             self.yVelocity = -self.yVelocity
#
#         self.canvas.move(self.image,self.xVelocity,self.yVelocity)

# threading with tkinter
# import tkinter as tk
# from threading import Thread
# import time
#
# class Sleep:
#
#     def __init__(self, wait):
#         self.wait = wait
#
#     def __enter__(self):
#         self.start = self.__t()
#         self.finish = self.start + self.wait
#
#     def __exit__(self, type, value, traceback):
#         while self.__t() < self.finish:
#             time.sleep(1./1000.)
#
#     def __t(self):
#         return int(round(time.time() * 1000))
#
#
# def after(t, fun, *args):
#     global finish
#     if not finish:
#         root.after(t, fun, *args)
#
# def run():
#     global finish
#     x = -200
#     while not finish:
#         with Sleep(100):
#             after(0, lambda : canvas.delete('all'))
#             after(0, lambda : canvas.create_rectangle(x,0,x+200,200, fill='red'))
#         x += 10
#         if x > 400:
#             x = -200
#
# def quit():
#     global finish
#     finish = True
#     root.destroy()
#
# root = tk.Tk()
#
# root.title("Test")
# root.protocol("WM_DELETE_WINDOW", quit)
#
# canvas = tk.Canvas(root, width=400, height=200, bd=0,
#                    highlightthickness=0, bg='white')
# canvas.pack()
#
# global finish
# finish = False
#
# control_thread = Thread(target=run, daemon=True)
# control_thread.start()
#
# root.mainloop()
# control_thread.join()

#itemconfig tkinter

import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()
item = canvas.create_rectangle(50, 25, 150, 75, fill="blue")

def callback():
    canvas.itemconfig(item,fill='red')

button = tk.Button(root,text='Push me!',command=callback)
button.pack()

root.mainloop()
