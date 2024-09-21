import turtle
#NIJOPVARGHESE
s = turtle.Turtle()
s.speed(200)

# Function to create a filled circle with multiple layers
def create_layered_circle(colors, sizes):
    for color, size in zip(colors, sizes):
        s.color(color, color)
        s.begin_fill()
        for _ in range(12):
            s.circle(size)
            s.left(30)
        s.end_fill()
        s.left(45)

# Create the layered circle
colors = ['maroon', 'brown', 'crimson', 'orange', 'gold', 'yellow', 'white']
sizes = [150, 145, 140, 135, 130, 125, 120]
create_layered_circle(colors, sizes)

# Create the green base
s.color('darkgreen', 'darkgreen')
s.begin_fill()
s.forward(240)
s.left(90)
s.circle(240)
s.end_fill()

s.left(90)
s.forward(240)

# Create the orange, yellow, and white layers
for color, size in zip(['orange', 'yellow', 'white'], [240, 220, 200]):
    s.color(color, color)
    s.begin_fill()
    for _ in range(8):
        s.left(15)
        s.forward(size)
        s.left(90)
        s.circle(size, 30)
        s.left(90)
        s.forward(size)
    s.end_fill()

# Create the light green and pale yellow circles (changed colors here)
s.forward(180)
s.left(90)
s.color('green', 'green')
s.begin_fill()
s.circle(180)
s.end_fill()

s.left(90)
s.forward(10)
s.right(90)
s.color('lightyellow', 'lightyellow')
s.begin_fill()
s.circle(170)
s.end_fill()

# Create the purple, darkmagenta, magenta, pink, and lavender squares
s.left(90)
s.forward(170)
for color, size in zip(['purple', 'darkmagenta', 'magenta', 'pink', 'lavender'], [120, 110, 100, 90, 85]):
    s.color(color, color)
    s.begin_fill()
    for _ in range(30):
        s.left(12)
        for _ in range(4):
            s.forward(size)
            s.left(90)
    s.end_fill()
    s.left(30)

# Create the light blue circles
s.color('blue', 'blue')
s.right(90)
s.penup()
s.forward(100)
s.left(90)
s.circle(100)
s.pendown()
for _ in range(5):
    s.begin_fill()
    s.circle(50)
    s.end_fill()
    s.penup()
    s.circle(100, 70)
    s.pendown()

# Create the pastel yellow, light orange, light pink, and pale pink circles (changed colors here)
s.left(90)
s.penup()
s.forward(27)
s.pendown()
s.right(90)
for color, size in zip(['palegoldenrod', 'peachpuff', 'pink', 'mistyrose'], [75, 55, 35, 15]):
    s.color(color, color)
    s.begin_fill()
    s.circle(size)
    s.end_fill()
    s.left(90)
    s.forward(20)
    s.right(90)

# Keep the window open
turtle.done()