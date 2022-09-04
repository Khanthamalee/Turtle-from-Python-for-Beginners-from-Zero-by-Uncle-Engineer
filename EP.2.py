import turtle
import random
import math

randomcolors = []
for y in range(1,100):
    colors = ['#']
    for i in range(0,6):
        sum = random.choice('ABCDEF0123456789')
        colors.append(sum)
    allcolors = (''.join(colors))
    qq = allcolors
    randomcolors.append(qq)
print(randomcolors)


turtle.bgcolor('black')

def TT():
    for j in range(2):
        for k in range(2):
            T = turtle.Pen()
            T.speed(100)
            T.penup()
            T.setpos(-110+j*200,40-k*190)
            T.pendown()
            T.color(random.choice(randomcolors))
            for i in range(95):
                size = (math.pi)*(i/16)**2
                T.circle(size,360,8)
def TTcenter():
    T = turtle.Pen()
    T.speed(100)
    T.penup()
    T.setpos(-12,-60)
    T.pendown()
    T.color(random.choice(randomcolors))
    for i in range(95):
        size = (math.pi)*(i/15)**2
        T.circle(size,360)
        
for i in range(100):       
    TTcenter()
    TT()





        
       # tao+i = turtle.Pen()
        # tao+i.speed(0)
        # tao+i.penup()
        # tao+i.setpos(-120,40)
        # tao+i.pendown()
        # tao+i.color(random.choice(randomcolors))


    # tao1 = turtle.Pen()
    # tao1.speed(0)
    # tao1.penup()
    # tao1.setpos(-120,-150)
    # tao1.pendown()
    # tao1.color(random.choice(randomcolors))


    # tao2 = turtle.Pen()
    # tao2.speed(0)
    # tao2.penup()
    # tao2.setpos(120,-150)
    # tao2.pendown()
    # tao2.color(random.choice(randomcolors))

    # tao3 = turtle.Pen()
    # tao3.speed(0)
    # tao3.penup()
    # tao3.setpos(120,40)
    # tao3.pendown()
    # tao3.color(random.choice(randomcolors))

    # tao4 = turtle.Pen()
    # tao4.speed(0)
    # tao4.penup()
    # tao4.setpos(0,-50)
    # tao4.pendown()
    # tao4.color(random.choice(randomcolors))'''



