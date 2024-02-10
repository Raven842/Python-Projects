import pygame
import pgzrun
from random import randint

# Screen Declare\
WIDTH = 400
HEIGHT = 400

# Vars 
dots = []
lines = []
next_dot = 0

# Code
for dot in range(0, 10):
    actor = Actor("dot")
    actor.pos = randint(20, (WIDTH - 20)), randint(20, (HEIGHT - 20))
    dots.append(actor)

def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number += 1