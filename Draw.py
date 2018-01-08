import turtle


def draw_square(brad):
    brad.shape("turtle")
    brad.color("yellow")
    for i in range(1, 5):
        brad.forward(200)
        brad.right(90)


def draw_circle():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(100)

    for i in range(180):
        brad.right(i*2)
        draw_square(brad)

    window.exitonclick()

draw_circle()
