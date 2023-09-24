import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
color_list = [(245, 243, 238), (246, 241, 243), (204, 165, 109), (239, 244, 239), (236, 239, 244), (149, 72, 49), (55, 94, 124), (225, 202, 133), (163, 150, 46), (131, 33, 25), (135, 163, 183), (198, 93, 72), (51, 122, 90), (60, 50, 46), (16, 100, 72), (147, 177, 150), (232, 176, 165), (164, 144, 155), (113, 73, 77), (184, 204, 174), (154, 17, 21), (24, 82, 87), (49, 62, 71), (53, 64, 76), (183, 87, 90), (97, 144, 126), (180, 192, 206), (218, 175, 179), (111, 126, 149), (175, 198, 204)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=100

for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count %10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()


