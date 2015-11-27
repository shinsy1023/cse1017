from tkinter import *

class Box(object):
    def __init__(self,size):
        self.box_size = size
        
    def in_horizontal_contact(self,x):
        return x <= 0 or x >= self.box_size
        
    def in_vertical_contact(self,y):
        return y <= 0 or y >= self.box_size
        
    def size_of(self):
        return self.box_size

class Stake(object):
    def __init__(self, color, size):
        self.x0=200-size
        self.x1=200+size
        self.y0=200-size
        self.y1=200+size
        self.color=color

    def x0(self):
        return self.x0

    def x1(self):
        return self.x1

    def y0(self):
        return self.y0

    def y1(self):
        return self.y1

    def color(self):
        return self.color

    def in_horizontal_contact(self, x ,y):
        return self.x0<=x<=self.x1 and self.y0<=y<=self.y1

    def in_vertical_contact(self, x, y):
        return self.y0<=y<=self.y1 and  self.x0<=x<=self.x1
        
class MovingBall(object):
    def __init__(self,x,y,xv,yv,color,size,box, stake):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.color = color
        self.size = size
        self.box = box
        self.stake=stake
        
    def x_position(self):
        return self.x
        
    def y_position(self):
        return self.y
        
    def color_of(self):
        return self.color
        
    def size_of(self):
        return self.size
        
    def move(self,time_unit):
        self.x = self.x + self.xv * time_unit
        if self.box.in_horizontal_contact(self.x):
            self.xv = - self.xv
        self.y = self.y + self.yv * time_unit
        if self.box.in_vertical_contact(self.y):
            self.yv = - self.yv
        if self.stake.in_horizontal_contact(self.x, self.y):
            self.xv=-self.xv
        if self.stake.in_vertical_contact(self.x, self.y):
            self.yv=-self.yv
            
class AnimationWriter(object):
    def __init__(self,root,ball,box, stake):
        size = box.size_of()
        self.canvas = Canvas(root, width=size, height=size)
        self.canvas.grid()
        self.ball = ball
        self.stake=stake
            
    def animate(self):
        self.canvas.delete(ALL)
        self.ball.move(1)
        x = self.ball.x_position()
        y = self.ball.y_position()
        d = self.ball.size_of() * 2
        c = self.ball.color_of()
        self.canvas.create_rectangle(self.stake.x0, self.stake.y0,\
                                     self.stake.x1, self.stake.y1,\
                                     fill=self.stake.color, outline = self.stake.color)
        self.canvas.create_oval(x, y, x+d , y+d, outline=c, fill=c)
        self.canvas.after(10,self.animate)
        
class BounceController(object):
    def __init__(self):
        box_size = 400
        ball_size = 15
        ball_color = 'purple'
        x_velocity, y_velocity = 5, 3
        root = Tk()
        root.title("Bouncing Ball")
        root.geometry(str(box_size+10)+"x"+str(box_size+10))
        box = Box(box_size)
        stake=Stake("blue", ball_size)
        ball = MovingBall(box_size//10, box_size//2, x_velocity, y_velocity, ball_color,ball_size, box, stake)
        AnimationWriter(root,ball,box, stake).animate()
        root.mainloop()
    
BounceController()
