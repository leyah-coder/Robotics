import turtle
t1 = turtle.Turtle()

t1.speed (10)
t1.goto(0,0)


colors = ["pink", "red", "yellow"]
#these colors are some of my favorites 
for i in range (500):
    t1.color( colors[ i % 3])
    t1.forward(20 + i)
    t1.left(100)

t1.hideturtle()

t2 = turtle.Turtle()

t2.speed (10)
t2.goto(0,0)


colors = ["light pink", "crimson", "khaki"]
#I thought these colors went well with the first
for i in range (500):
    # Maya told me to make this one bigger
    t2.color( colors[ i % 3])
    t2.forward(10 + i)
    t2.left(110)

t2.hideturtle()
#I don't really like the turtle look
turtle.exitonclick()