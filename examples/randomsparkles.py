from tree import RGBXmasTree
from colorzero import Hue
from random import random

tree = RGBXmasTree()
tree.brightness = 0.1

def random_color():
    r = random()
    g = random()
    b = random()
    return (r, g, b)

def random_colors(n):
    return [random_color() for i in range(n)]

while True:
    tree.value = random_colors(25)
