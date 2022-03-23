import turtle
t = turtle.Turtle()

# taking input from user for the radius of the circle
r = int(input("Enter the radius of the circle: "))

# taking the input from user for the color
col = input("Enter the color name or hex value of color (# For Ex: RRGGBB): ")

t.fillcolor(col)
t.begin_fill()
t.circle(r)
t.end_fill()