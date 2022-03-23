import turtle
n = 10     # n represents number of sides

pen = turtle.Turtle()

for i in range(n):
	# drawing side of
	# length i*10
	pen.forward(i * 10)
	pen.right(144)

turtle.done()         # closing the instance