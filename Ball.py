import time
import GlobalVariables
class Ball:

    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color,tag):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,x+diameter,y+diameter,fill=color, tags=tag)
        self.tag = tag
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def moveBall_X(self,window,distance,xVel):
        count =0
        while (count<distance):
            self.canvas.move(self.image,xVel,0)
            window.update()
            time.sleep(0.01)
            count+=1

    def moveBall_Y(self,window, distance,yVel):
        count = 0
        coordinates = self.canvas.coords(self.image)
        relative_distance = abs(distance-coordinates[3])
        while(count<relative_distance):
            self.canvas.move(self.image,0,yVel)
            window.update()
            time.sleep(0.01)
            count+=1


    def changeBallColor(self,color):
        self.canvas.itemconfig(self.image,fill = color)




