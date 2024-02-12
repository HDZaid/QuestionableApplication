'''
FLOR 1 
import turtle

turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()

colors = ["yellow", "pink", "yellow", "pink"]

for i in range(120):
    for c in colors:
        turtle.color(c)
        turtle.circle(150-i, 70)
        turtle.lt(90)
        turtle.circle(150-i, 70)
        turtle.rt(60)
        turtle.end_fill()
        
turtle.mainloop()

'''
'''
FLOR 2 
import turtle

turtle.bgcolor("white")
turtle.speed(0)
turtle.hideturtle()

colors = ["red"]

def draw_petal():
    turtle.begin_fill()
    turtle.circle(200, 100)
    turtle.lt(90)
    turtle.circle(200, 100)
    turtle.end_fill()
    turtle.rt(36)  # Angulo para pasar al siguiente pétalo

for _ in range(100):  # 10 pétalos
    for c in colors:
        turtle.color(c)
        draw_petal()

turtle.mainloop()
'''
'''
FLOR 3
import turtle

turtle.bgcolor("skyblue")
turtle.speed(30)
turtle.hideturtle()

def draw_petal():
    turtle.color("white")
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.circle(200, 60)
    turtle.left(120)
    turtle.circle(200, 60)
    turtle.end_fill()

# Dibujar pétalos
for _ in range(21):
    draw_petal()
    turtle.right(360/7)

# Calcular las coordenadas del centro de la flor
x_center, y_center = turtle.position()

# Mover un poco hacia abajo desde el centro
y_center -= 30  # Ajusta según tus preferencias

# Dibujar círculo amarillo en el centro ajustado
turtle.penup()
turtle.goto(x_center, y_center)
turtle.pendown()
turtle.color("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

turtle.mainloop()
'''
from turtle import * 
import colorsys

#parte echa con pycharm

header_text = ""
color("white")
penup()
goto(-180,250)
pendown()
write(header_text, align="left", font=("Arial", 12, "normal"))

speed(100)
bgcolor("black")
h = 0
#PARTE DEL TALLO

penup()
goto(0, 100)
pendown()
color("green")
begin_fill()
rt(90)
fd(400)
lt(90)
fd(20)
lt(90)
fd(400)
lt(90)
fd(20)
end_fill()

#DIBUJA GIRASOL

penup()
goto(10,120)
pendown()
for i in range(16):
    for j in range(18):
        color("yellow")
        h += 0.005
        rt(90)
        circle(150-j*6,90)
        lt(90)
        circle(150-j*6, 90)
        rt(180)
    circle(40,24)

#PARTE DEL COLOR DEL CENTRO

penup()
goto(-5,120)
pendown()
color("brown")
begin_fill()
circle(44)
end_fill()
done()
