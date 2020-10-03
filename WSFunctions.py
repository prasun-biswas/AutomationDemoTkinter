from Ball import *
import GlobalVariables

class WSFunctions:

    @staticmethod
    def loadBallinContainer(number,my_canvas):
        store_ball_objects=[]
        for i in range(number):
            container_Height = 180
            ball = Ball(my_canvas,220,container_Height-20*i,20,0,0,"white",("ball",str(i),"packed"))
            store_ball_objects.append(ball)
        return store_ball_objects

    @staticmethod
    def moveObject_X(window,my_canvas,object,distance):

        count =0
        while (count<distance):
            my_canvas.move(object,1,0)
            window.update()
            time.sleep(0.01)
            count+=1

    @staticmethod
    def moveObject_Y(window,my_canvas,object,distance):

        count =0
        while (count<distance):
            my_canvas.move(object,0,1)
            window.update()
            time.sleep(0.01)
            count+=1

    @staticmethod
    def moveMultipleObject(window, my_canvas,tag,disX,disY):

        countX = 0
        while (countX<disX):
            my_canvas.move(tag,1,0)
            window.update()
            time.sleep(0.01)
            countX+=1
        # my_canvas.move(tag,disX,disX)


