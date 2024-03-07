import colorgram
import random
from turtle import colormode
colormode(255)

# colors_raw = colorgram.extract('dots_paint.jpg', 30)
# rgb_colors = []
# for color in colors_raw:
#     rgb_color = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(rgb_color)
# print(rgb_colors)
color_list = [(192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123),
              (182, 154, 42),
              (61, 22, 11), (182, 146, 165), (142, 177, 151), (72, 117, 81), (58, 15, 26), (126, 79, 102),
              (130, 30, 16),
              (15, 39, 23), (24, 53, 127), (177, 188, 215), (164, 104, 134), (115, 31, 46), (97, 150, 100),
              (98, 121, 172),
              (210, 178, 197), (174, 105, 93), (74, 150, 165), (25, 91, 65), (172, 205, 180)]

from turtle import Turtle as t
from turtle import Screen

screen = Screen()
pen = t()
dot_size = 20
space_between_dots = 50
dots_no = 12
painting_length = (dots_no * dot_size) + ((dots_no - 1) * space_between_dots)
screen.screensize(1200, 1200)


def initiate_painting():
    pen.penup()
    pen.right(90)
    pen.forward(painting_length / 2)
    pen.right(90)
    pen.forward(painting_length / 2)
    pen.right(180)
    pen.pendown()


def paint_line():
    pen.forward(1)
    for x in range(dots_no-1):
        dot_color = random.choice(color_list)
        pen.pencolor()
        pen.pencolor(dot_color)
        pen.penup()
        pen.forward(space_between_dots)
        pen.pendown()
        pen.forward(1)

def move_up_right_side():
    pen.penup()
    pen.left(90)
    pen.forward(space_between_dots)
    pen.left(90)
    pen.pendown()

def move_up_left_side():
    pen.penup()
    pen.right(90)
    pen.forward(space_between_dots)
    pen.right(90)
    pen.pendown()


def paint_dots():
    pen.pensize(dot_size)
    for y in range (int(dots_no / 2)):
        paint_line()
        move_up_right_side()
        paint_line()
        move_up_left_side()



initiate_painting()
paint_dots()

screen.exitonclick()
