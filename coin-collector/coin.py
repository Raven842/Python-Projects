import pgzrun
import pygame
from random import randint

# screen declare
WIDTH = 400
HEIGHT = 400

# vars && starting pos
fox = Actor("fox")
fox.pos = 100, 100
coin = Actor("coin")
coin.pos = 200, 200
score = 0
game_over = False
key_set = input("WASD or Arrows? ")

# begin code 
def draw():
    screen.fill("purple")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
    if game_over == True:
        screen.fill("green")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10),  fontsize=60)


def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT- 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if key_set.lower() == "arrows":
        if keyboard.left:
            fox.x -= 2
        elif keyboard.right:
            fox.x += 2
        elif keyboard.down:
            fox.y += 2
        elif keyboard.up:
            fox.y -= 2
    if key_set.lower() == "wasd":
        if keyboard.a:
            fox.x -= 2
        elif keyboard.d:
            fox.x += 2
        elif keyboard.s:
            fox.y += 2
        elif keyboard.w:
            fox.y -= 2
    coin_collected = fox.colliderect(coin)
    if coin_collected:
        score += 10
        place_coin()

clock.schedule(time_up, 7.0)
place_coin()