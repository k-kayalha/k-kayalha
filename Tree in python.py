import turtle
t = turtle.Turtle()
t.speed('fastest')
t.left(90)
t.pensize(5)
t.pencolor('green')

def shakhe(lenght, level) :
    if level == 0 :
        return
    t.forward(lenght)
    t.left(45)
    shakhe(lenght * 0.5 , level - 1)
    t.right(90)
    shakhe(lenght * 0.5 , level - 1)
    t.left(45)
    t.backward(lenght)



shakhe(150 , 8)

turtle.exitonclick()