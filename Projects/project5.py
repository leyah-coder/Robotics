# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle
import math
import time
import random


def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(
		    f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(
		    f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")


def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)


def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x, y)
    window.update()
    return sprite


def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)


def draw_rectangle(color="black", x=0, y=0, width=100, height=100,):
	sprite = turtle.Turtle()
	sprite.speed(0)
	sprite.pencolor(color)
	sprite.color(color)
	sprite.penup()
	sprite.goto(x - (width*0.5), y + (height*0.5))
	sprite.pendown()
	sprite.begin_fill()
	for i in range(2):
		sprite.forward(width)
		sprite.right(90)
		sprite.forward(height)
		sprite.right(90)
	sprite.end_fill()
	sprite.hideturtle()


window = turtle.Screen()
window.tracer(0)


# Section 2: Setup
set_background("s")
s1 = create_sprite("puddle", 0, 0)


def move_up():
    s1.setheading(90)
    s1.forward(10)


def move_down():
    s1.setheading(270)
    s1.forward(10)


def move_left():
    s1.setheading(180)
    s1.forward(10)


def move_right():
    s1.setheading(0)
    s1.forward(10)


s2 = create_sprite("fish", 0, 0)
s2look = "fish"


def switch_look():
      global s2look
      if s2look == "fish":
            set_image(s2, "dolphiny")
            s2look = "dolphiny"
      elif s2look == "dolphiny":
            set_image(s2, "octo")
            s2look = "octo"
      elif s2look == "octo":
            set_image(s2, "fish")
            s2look = "fish"


window.onkeypress(switch_look, "h")


def move_up():
    s2.setheading(90)
    s2.forward(10)


def move_down():
    s2.setheading(270)
    s2.forward(10)


def move_left():
    s2.setheading(180)
    s2.forward(10)


def move_right():
    s2.setheading(0)
    s2.forward(10)


window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")


# TODO - set the starting value for your variable

# Section 3: Controls
# TODO - define your controls
# TODO - pick keys for each control

# Section 4: Game Loop
window.listen()
timer = 0
while True:
    time.sleep(0.1)
    timer += 1
    # make the puddle move randomly
    s1.setheading(random.randint(0,290))
    s1.forward(5)
    window.update()
    if get_distance (s1,s2) > 90: 
         break
	

print(f"Game Over, you lasted {timer} seconds!")