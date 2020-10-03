import time

class Rectangle:


    def __init__(self,canvas,xTL,yTL,xBR,yBR,color, tag):
        self.canvas = canvas
        self.image = canvas.create_rectangle(xTL,yTL,xBR,yBR,fill=color,tags = tag)

    def runConveyorX(self, ip_Ball, window):

        coordinates = self.canvas.coords(self.image)
        # print(coordinates)
        ip_Ball.moveBall_X(window,coordinates[2]-coordinates[0],1)
#hello
    def runConveyorY(self, ip_Ball, window):

        coordinates = self.canvas.coords(self.image)
        # print(coordinates)
        ip_Ball.moveBall_Y(window,coordinates[3],1)

    def runConveyorYToSlot(self, ip_Ball, window,i):

        coordinates = self.canvas.coords(self.image)
        # print(coordinates)
        ip_Ball.moveBall_Y(window,coordinates[3]-i*20,1)

    def changeObjectColor(self, ip_Ball, color):
        ip_Ball.changeBallColor(color)

    def changeOwnColor(self,color):
        self.canvas.itemconfig(self.image,fill = color)





