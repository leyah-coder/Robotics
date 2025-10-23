import turtle
t1 = turtle.Turtle()

t1.speed (10)
t1.goto(0,0)


colors = ["pink", "red", "yellow"]
#these colors are some of my favorites 
for i in range (500):
    t1.color( colors[ i % 3])
    t1.forward(10)
    t1.left(40)
    t1.forward(10)
    t1.right(20)



t2.hideturtle()
#I don't really like the turtle look
turtle.exitonclick()