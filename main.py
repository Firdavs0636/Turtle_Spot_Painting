# Below code is to extract colors from a picture saved inside a project

# import colorgram
#
# colors = colorgram.extract('spot_painting.jpg', 35)
# rgba =[]
# for _ in colors:
#     r = _.rgb.r
#     g = _.rgb.g
#     b = _.rgb.b
#     rgb = (r, g, b)
#     rgba.append(rgb)
# print(rgba)


import turtle
from turtle import Turtle
import random

turtle.colormode(255)
downy = Turtle()
downy.speed("fastest")
downy.penup()
downy.hideturtle()
downy.setpos(-200, -200)
# below code is taken from the extraction of the colors from the picture
pallet = [(212, 154, 97), (239, 246, 243), (52, 108, 132), (178, 78, 33), (198, 143, 34), (123, 80, 97),
          (235, 240, 244), (116, 155, 171), (124, 175, 158), (228, 197, 129), (194, 85, 105), (54, 38, 20),
          (12, 51, 65), (189, 123, 142), (54, 120, 115), (41, 169, 126), (167, 21, 31), (225, 94, 78), (4, 30, 28),
          (39, 32, 34), (243, 163, 159), (81, 148, 168), (164, 27, 22), (239, 163, 167), (104, 123, 159),
          (164, 209, 193), (21, 81, 93), (29, 85, 81), (162, 206, 212), (53, 62, 81), (183, 190, 206), (85, 74, 35)]

for y in range(1, 16):
    for _ in range(15):
        downy.dot(20, random.choice(pallet));
        downy.fd(40);
    downy.setpos(-200, -200 + (y * 40))

screen = turtle.Screen()
screen.exitonclick()
