from tree import RGBXmasTree
from colorzero import Hue,Color

tree = RGBXmasTree()

tree.color = Color('red')
tree.brightness = 0.1

while True:
    tree.color += Hue(deg=5)
