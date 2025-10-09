# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")

def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x,y)
    window.update()
    return sprite

def get_distance(s1, s2):
    dx = s1.xcor() - s2.xcor()
    dy = s1.ycor() - s2.ycor()
    return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)


######################################################################
# Section 2 - Your code
set_background("images (1)")
sprite1 = create_sprite("snoopy", -200, -180)

sprite2 = create_sprite("alien",-200,150)
sprite2.color("red")
sprite2.write("Hi, I'm snoopy",font = ("Arial", 20, "normal"))
sprite2.hideturtle()

sprite2 = create_sprite("alien",-150,100)
sprite2.color("red")
sprite2.write("and welcome to my house!!",font = ("Arial", 20, "normal"))
sprite2.hideturtle()
######################################################################


# Section 3 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()
