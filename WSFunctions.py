from Ball import *

class WSFunctions:

#hello
    @staticmethod
    def loadBallinContainer(number,my_canvas):
        """ creates object of Ball class, stores in a list and returns the list"""
        store_ball_objects=[]
        for i in range(number):
            container_Height = 180
            ball = Ball(my_canvas,20,container_Height-20*i,20,0,0,"white",("ball",str(i)))
            store_ball_objects.append(ball)
        return store_ball_objects

    @staticmethod
    def moveMultipleObject(window, my_canvas,tag,disX,disY):
        """ this method can move any object on canvas with the 'tag' attribute """
        countX = 0
        while (countX<disX):
            my_canvas.move(tag,1,0)
            window.update()
            time.sleep(0.01)
            countX+=1
        # my_canvas.move(tag,disX,disX)


