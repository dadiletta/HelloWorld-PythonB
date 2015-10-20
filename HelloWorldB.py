import turtle
screen = turtle.Screen()
screen.title('Square Demo')
t = turtle.Turtle()
for i in range(400):
    t.goto(i,i)
    if i % 20 == 0:
        t.write(str(i), font=("Arial",12,"normal"))
d = input()

