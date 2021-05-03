import turtle
import pyautogui


def fg_check(title):
    if pyautogui.getActiveWindowTitle() == title:
        return True


class Web:
    screen = turtle.Screen()
    canvas = screen.getcanvas()
    screen.tracer(0, 0)
    screen.title("web")
    screen.bgcolor("black")


    def __init__(self):
        self.pen = turtle.Turtle()
        self.npen = 20
        self.radius = 360
        self.pens = list()
        self.border()


    def border(self):
        self.pen.penup()
        self.pen.setpos(0, -self.radius)
        self.pen.pendown()
        self.pen.hideturtle()
        self.pen.color("cyan")
        for i in range(self.npen):
            self.pen.circle(self.radius,self.radius/self.npen)
            pen2=self.pen.clone()
            self.pens.append(pen2)


    @staticmethod
    def transformpos(screen_title): #ekran bazli mouse koordinatlarini cizim ekranina gore ayarliyor.
        if fg_check(screen_title):
            hwnd = pyautogui.getActiveWindow()
            x, y, width, height = hwnd.left, hwnd.top, hwnd.width, hwnd.height
            mposx, mposy = Web.canvas.winfo_pointerx(), Web.canvas.winfo_pointery() #tum ekrana gore alinan koordinatlar
            mposx -= x + width / 2
            mposy -= y + height / 2
            return mposx, -mposy

        else: return 0, 0


    def main(self):
        while True:
            x, y = Web.transformpos("web")
            for p in self.pens:
                p.goto(x,y)

            Web.screen.update()
            for p in self.pens:
                p.undo()


if __name__ == '__main__':
    web1=Web()
    web1.main()
