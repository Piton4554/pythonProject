from turtle import *


class fractal:

    def __init__(self, t, axiom, km, angle):
        self.axiom = axiom
        self.angle = angle
        self.km = km
        self.state = axiom
        self.t = t
        t.width(12)
        t.color("red")
        t.shape("turtle")

    def draww(self, start_x_y, start_angle):
        self.t.up()
        self.t.setpos(start_x_y)
        self.t.seth(start_angle)
        self.t.down()
        for i in self.state:
            if i == "F":
                self.t.fd(self.km)
            elif i == "+":
                self.t.lt(self.angle)
            elif i == "-":
                self.t.rt(self.angle)
            elif i == "":
                self.t.up()
                self.t.fd(self.km)
                self.t.down()


t = Turtle()
rab = fractal(t, "F+F--F+F", 100, 60)
rab.draww((-100, 100), 0)
mainloop()