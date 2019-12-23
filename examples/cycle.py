from tree import RGBXmasTree
from colorzero import Hue,Color
from random import random
from time import sleep
import time

tree = RGBXmasTree()
tree.brightness = 0.1
ShowFor = 60
Period = 1

def huecycle():
	tree.color = Color('red')

	timeout = time.time() + ShowFor
	while True:
		tree.color += Hue(deg=5)
		if time.time() > timeout:
			break;

def onebyone():
	colors = [Color('red'), Color('green'), Color('blue')] # add more if you like

	timeout = time.time() + ShowFor
	while True:
		for color in colors:
			for pixel in tree:
				pixel.color = color
		if time.time() > timeout:
			break;

def random_color():
	r = random()
	g = random()
	b = random()
	return (r, g, b)

def random_colors(n):
	return [random_color() for i in range(n)]

def randomsparkles():
	timeout = time.time() + ShowFor
	while True:
		tree.value = random_colors(25)
		if time.time() > timeout:
			break;

def rgb():
	colors = [Color('red'), Color('green'), Color('blue')] # add more if you like

	timeout = time.time() + ShowFor
	while True:
		for color in colors:
			tree.color = color
		if time.time() > timeout:
			break;

def wait():
	sleep(Period)

def go():
	while True:
		huecycle()
		wait()
		onebyone()
		wait()
		randomsparkles()
		wait()
		rgb()

go()
