# Simple Star

import turtle
star = turtle.Turtle()
star.right(75)
star.forward(100)

for i in range(4):
    star.right(144)
    star.forward(100)
turtle.done()

print('----------------------------------------------------')

# Coloured Star

import turtle
t = turtle.Turtle()

# taking input for the side of the star
s = int(input("Enter the length of the side of the star: "))

# taking the input for the color
col = input("Enter the color name or hex value of color(# RRGGBB): ")
t.fillcolor(col)
t.begin_fill()

for _ in range(5):       # sides=5
    t.forward(s)
    t.right(144)
    t.end_fill()