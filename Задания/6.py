'''
#пересечение это новая фигура
#объединение это все фигуры
from turtle import * #импорт черепахи со всеми фнкциями из-за '*'
tracer(0) #максимальная скорость
c=45 #масштаб
screensize(2000,2000) #двигать рисунок
lt(90) #в питоне черепаха всегда повернута вправо, по заданию нужно вверх, поэтому вращаем

rt(45) #условие из задания
for i in range (7):
    fd(5*c)
    rt(45)
    fd(12*c)
    rt(135)
up()

for x in range (-40,40): #строим точки поля
    for y in range (-40,40): #строим точки поля
        goto(x*c,y*c) #перемещение в точку
        dot(3,'red') #толщина и цвет точки
done()'''
####################
'''from turtle import*
tracer(0)
c=40
screensize(2000,2000)
lt(90)

for i in range (2):
    rt(120)
    fd(7*c)
rt(300)

for i in range (2):
    rt(120)
    fd(7*c)
up()

for x in range (-40,40):
    for y in range(-40, 40):
        goto(x*c,y*c)
        dot(3,'red')
done()'''
####################
'''from turtle import*
tracer(0)
c=30
lt(90)
screensize(2000,2000)

for i in range (2):
    fd(7*c)
    rt(90)
    fd(20*c)
    rt(90)
up()
fd(3*c)
rt(90)
fd(7*c)
lt(90)
down()
for i in range (4):
    rt(90)
    fd(7*c)
up()

for x in range (-40,40):
    for y in range(-40, 40):
        goto(x*c,y*c)
        dot(3,'red')
done()'''
####################
'''from turtle import*
tracer(0)
c=30
lt(90)
screensize(2000,2000)

rt(300)
for i in range (6):
    fd(5*c)
    rt(120)
    fd(5*c)
    rt(330)
up()

for x in range (-40,40):
    for y in range(-40, 40):
        goto(x*c,y*c)
        dot(3,'red')
done()'''
####################
'''from turtle import*
tracer(0)
c=25
lt(90)
screensize(2000,2000)

rt(300)
for i in range (8):
    fd(10*c)
    rt(120)
    fd(10*c)
    rt(330)
up()

for x in range (-40,40):
    for y in range(-40, 40):
        goto(x*c,y*c)
        dot(3,'red')
done()'''
####################
'''from turtle import*
tracer(0)
c=30
lt(90)
screensize(2000,2000)

for i in range (3):
    fd(7*c)
    rt(90)
fd(10*c)
for i in range (3):
    lt(90)
    fd(6*c)
up()

for x in range (-40,40):
    for y in range(-40, 40):
        goto(x*c,y*c)
        dot(3,'red')
done()'''
####################
'''from turtle import*
tracer(0)
c=30
lt(90)
screensize(2000,2000)

for i in range (8):
    rt(45)
    fd(8*c)
up()

for x in range (-40,40):
    for y in range(-40, 40):
        goto(x*c,y*c)
        dot(3,'red')
done()'''
####################
'''from turtle import *
tracer(0)
lt(90)
c=20
screensize(2000,2000)

for i in range (4):
    fd (9*c)
    lt(180)
    back(10*c)
    rt(90)
up()

back(7*c)
lt(90)
fd(3*c)
rt(90)
down()

for i in range(2):
    fd (17*c)
    lt(90)
    fd(20*c)
    lt(90)
up()

for x in range (-40,40):
    for y in range (-40,40):
        goto(x*c,y*c)
        dot(3,"red")
done()'''
####################
'''from turtle import*
tracer(0)
screensize(2000,2000)
c=30

for i in range (2):
    fd(8*c)
    rt(90)
    fd(18*c)
    rt(90)
up()

fd(4*c)
rt(90)
fd(10*c)
lt(90)
down()

for i in range (2):
    fd(17*c)
    rt(90)
    fd(7*c)
    rt(90)
up()

for x in range (-40,40):
    for y in range (-40,40):
        goto(x*c,y*c)
        dot(3,"red")
done()'''
####################
from turtle import*
tracer(0)
c=30
lt(90)
screensize(5000,5000)
x=2
for i in range (4):
    fd(x*c)
    rt(90)
    fd(x*c)
    lt(90)
    fd(x*c)
    rt(90)
up()
for x in range (-40,40):
    for y in range (-40,40):
        goto(x*c,y*c)
        dot(3,"red")
done()