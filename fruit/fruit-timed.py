score = 0
total_attempts = 3
t_check = 0
import pygame
import pgzrun
from random import randint
import time

pgzrun.go()

apple = Actor("apple")

while t_check == 0:
    t_option = input("Select the starting time you would like to play(15s, 30s or random): ")
    if t_option == "15s":
        t_option=15
        t_check =1
    elif t_option == "30s":
        t_option = 30
        t_check = 1
    elif t_option == "random":
        t_option = randint(7, 27)
        t_check = 1
    else:
        print("Invalid Option")
        t_check =0

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    global score
    global total_attempts
    global t_option

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

clock.schedule(quit, int(t_option))
place_apple()