import colorgram

rgb_colors = []
colors = colorgram.extract('D:\MyVsCode\My VS Code\Python\GameTime\image.jpg',30)
print(colors)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)



# import turtle as t
# import random


# t.speed(0)  
# t.bgcolor("white") 

# def draw_color_dot(x, y, radius, color):
#     t.penup()
#     t.goto(x, y - radius)
#     t.pendown()
#     t.begin_fill()
#     t.fillcolor(color)
#     t.circle(radius)
#     t.end_fill()


# num_rows = 10
# num_columns = 10


# dot_radius = 20

# spacing = dot_radius * 2

# colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]


# for row in range(num_rows):
#     for col in range(num_columns):
#         x = col * spacing - (num_columns - 1) * spacing / 2
#         y = (num_rows - row - 1) * spacing - (num_rows - 1) * spacing / 2
#         color = random.choice(colors)  
#         draw_color_dot(x, y, dot_radius, color)


# t.exitonclick()
