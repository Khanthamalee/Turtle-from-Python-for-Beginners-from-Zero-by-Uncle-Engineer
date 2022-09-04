import turtle
import random
import math #เอาไปคำนวนเพื่อวาดเส้นของรูปเหลี่ยม

randomcolors = [] #ฟังก์ชันสุ่มสี
for y in range(1,100):
    colors = ['#']
    for i in range(0,6):
        sum = random.choice('ABCDEF0123456789') #ให้สุ่มตัวอักษรพวกนี้ 6 รอบ มันจะได้รหัสสี
        colors.append(sum)
    allcolors = (''.join(colors)) #เคยใช้ allcolors ไปแทนค่าสีเลย ทั้งที่ใส่ '' แต่ไม่ได้เลยสุ่มสีอีกรอบ
    qq = allcolors
    randomcolors.append(qq)
print(randomcolors)

turtle.bgcolor('black') #ทำให้ background สีดำ จะได้มีเงาสะท้อนสวยๆ
#ฟังชั่นสร้างรูปแปดเหลี่ยม 4 รูป
def TT():
    for j in range(2):
        for k in range(2):
            T = turtle.Pen()
            T.speed(100) #อยากได้ความเร็วเร็วๆ ไม่รู้ว่าช่วยได้ไหม
            T.penup()   #เอาปากกาขึ้นก่อน
            #ตำแหน่งที่แน่นอนสามารถใช้ goto(x,y),setpos(x,y) ได้
            T.setpos(-110+j*200,40-k*190)
            T.pendown() #อยากให้มีเส้นปากกา
            T.color(random.choice(randomcolors)) #เติมสีปากจากฟังก์ชันที่สุ่มได้
            for i in range(95):
                #วาดเส้นวนตามรูปเหลี่ยมตามหารคำนวน
                size = (math.pi)*(i/16)**2
                #สามารถเปลี่ยนจำนวนเหลี่ยมได้ T.circle(ขนาด,วาดเต็มวงคือ 360,จำนวนเหลี่ยม)
                T.circle(size,360,8)               
def TTcenter(): #ฟังชั้นสร้างรูปวงกลมตรงกลาง
    T = turtle.Pen()
    T.speed(100)
    T.penup()
    T.setpos(-12,-60)
    T.pendown()
    T.color(random.choice(randomcolors))
    for i in range(95):
        size = (math.pi)*(i/15)**2
        T.circle(size,360)      
for i in range(100): #อยากให้มันรันเพื่อดูความสวยงามเวลาวาดเลยเอา for มาใส่รันนานก็ช้าได้ 5555  
    #เรียกฟังชันมาจ้า
    TTcenter()
    TT()




#ทด
        
    # tao = turtle.Pen()
    # tao.speed(0)
    # tao.penup()
    # tao.setpos(-120,40)
    # tao.pendown()
    # tao.color(random.choice(randomcolors))


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



