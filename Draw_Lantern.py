# Author: Ahmad_Ibrahim_AbuDanckash
# This code draws Lantern
import turtle as tr
s=tr.getscreen()
# make the background is black to good vision
s.bgcolor("black")

p=tr.Turtle()
# Draw the first part
p.pencolor("blue")
p.fd(75)
p.lt(135)
p.pencolor("white")
p.fd(45)
p.pencolor("yellow")
p.rt(60)
p.fd(150)
p.pencolor("violet")
p.lt(60)
p.fd(63)
p.pencolor("violet")
p.lt(90)
# Draw the second part
p.fd(63)
p.lt(60)
p.pencolor("yellow")
p.fd(150)
p.rt(60)
p.pencolor("white")
p.fd(45)
p.lt(135)
p.penup()
p.fd(37.5)
p.lt(90)
p.pendown()
p.pencolor("brown")
p.fd(220.5)
p.pencolor("blue")
p.rt(90)
p.penup()
# Draw the crescent moon
for i in range(16):
    p.fd(1)
    p.lt(3)
p.pendown()
p.lt(180)
for i in range(16):
    p.fd(1)
    p.rt(3)

def qc(num=30,px=2):
    p.pencolor("blue")
    for i in range(num):
        p.fd(px)
        p.rt(210/num)
    p.rt(135)
    px -= .6
    for i in range(num):
        p.fd(px)
        p.lt(190/num)
qc()

p.penup()
p.fd(100)
tr.mainloop()