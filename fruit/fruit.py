score = 0
total_attempts = 3

import pygame
import pgzrun
from random import randint

pgzrun.go()

apple = Actor("apple")


def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    global score
    global total_attempts
    if apple.collidepoint(pos):
        score += 1
        print("Good shot!")
        print("Your Score is:", str(score))
        place_apple()
    else:
        if  total_attempts > 0:
            total_attempts -= 1
            print ("Not quite, Try again, you have:", str(total_attempts), "Attempts left.")
            place_apple()
        else:
            print("Game Over")
            quit()

place_apple()