import turtle
pen1 = turtle.Turtle()
screen = turtle.Screen()
screen.tracer(0,0)
def hole(pen,r,angle):
    if r >=0:
        pen.right(angle)
        pen.circle(r,360)
        hole(pen,r-10,angle)

def spin():
    while True:
        for i in range(360*3):
            hole(pen1,200,i/3)
            screen.update()
            pen1.reset()
if __name__ == '__main__':
    spin()
