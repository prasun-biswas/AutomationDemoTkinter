from tkinter import *
root = Tk()
root.title("tkinter")

# button_quit = Button(root, text = "exit",command = root.quit)
# button_quit.pack()

w = 300
h = 200
x = w//2
y = h//2
my_canvas = Canvas(root, width = w, height = h,  bg = "white", bd = 5)
my_canvas.pack(pady = 20)

#create line on canvas create_line(x1,y1,x2,y2, fill=color)

my_circle = my_canvas.create_oval(x,y,x+10,y+10)
# create function to move circle

def left(event):
    x=-10
    y=0
    coordinate = my_canvas.coords(my_circle)

    if(coordinate[0]<=0):
        my_canvas.move(my_circle,0,0)
        my_canvas.itemconfig(my_circle,fill = "red")
    else:
        my_canvas.move(my_circle,x,y)
#
# def right(event):
#     x=10
#     y=0
#     coordinate = my_canvas.coords(my_circle)
#     if(coordinate[2]<my_canvas.winfo_width()):
#         my_canvas.move(my_circle,x,y)
#
# def up(event):
#     x=0
#     y=-10
#     coordinate = my_canvas.coords(my_circle)
#     if(coordinate[1]>0):
#         my_canvas.move(my_circle,x,y)
#
# def down(event):
#     x=0
#     y=10
#     coordinate = my_canvas.coords(my_circle)
#     if(coordinate[3]<=my_canvas.winfo_height()):
#         my_canvas.move(my_circle,x,y)


# bind keyboard event with function
root.bind("<Left>",left)
# root.bind("<Right>",right)
# root.bind("<Up>",up)
# root.bind("<Down>", down)



root.mainloop()
