from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import random
from time import sleep

snake_length = 5
snake = {'x': 100, 'y': 100}
food = []
snake_body = [snake]
score = 0
old_move = 'd'
updated = False
speed = 0.05
wall_hack = False
speed_hack = False
flag = True
imageFile = Image.open("snakegame_app/img/Untitled.png")
fill_color = 'black'
power_time = 0
image = True
width = 800
height = 500


class Move(object):
    char = old_move


def is_over():
    global snake_body, wall_hack
    if width-10 > snake['x'] > 15 and height-10 > snake['y'] > 15:
        return False
    elif wall_hack:
        h1 = snake_body[-1]
        h2 = snake_body[-2]
        h1x1, h1x2, h1y1, h1y2 = canvas.coords(h1)
        h2x1, h2x2, h2y1, h2y2 = canvas.coords(h2)
        if h1x1 == h2x1 and h1y2 == h2x2 and h1y1 == h2y1:
            snake['y'] = height-10
        elif h1x2 == h2x2 and h1y2 == h2y2 and h1y1 == h2x1:
            snake['x'] = width-10
        elif h1x1 == h2y1:
            snake['x'] = 20
        elif h1x1 == h2x1 and h1x2 == h2y2:
            snake['y'] = 20
        return False
    else:
        return True


def is_snake_body(coords=None):
    global snake_body
    if len(snake_body) <= 2:
        return False
    head = coords
    s = snake_body
    if not coords:
        head = canvas.coords(snake_body[-1])
        s = snake_body[:-1]
    for i in s:
        if head == canvas.coords(i):
            return True
    return False


def is_valid_food(i, j):
    for f in food:
        x1, x2, y1, y2 = canvas.coords(f)
        if i - 5 < x1 or x2 < i + 5 and j - 5 < y1 or y2 < j + 5:
            return True
    for s in snake_body:
        x1, x2, y1, y2 = canvas.coords(s)
        if i - 5 < x1 or x2 > i + 5 and j - 5 < y1 or y2 > j + 5:
            return True
    return False


def is_eaten():
    global snake_length, score, speed, wall_hack, fill_color, speed_hack
    head = canvas.coords(snake_body[-1])

    for f in food:
        if head == canvas.coords(f):
            if canvas.itemcget(f, "fill") == 'red':
                wall_hack = True
                score += 10
                fill_color = 'red'
            elif canvas.itemcget(f, "fill") == 'green':
                speed_hack = True
                speed -= 0.02
                score += 10
                fill_color = 'green'
            else:
                score += 5
                rand_food()
            snake_length += 1
            canvas.delete(f)


def rand_food(pow_up=None):
    i = random.randint(20, width-20)
    j = random.randint(20, height-20)

    while i % 10 != 0:
        i = random.randint(20, width-20)
    while j % 10 != 0:
        j = random.randint(20, height-20)

    if is_snake_body(coords=[i + 5, j + 5, i - 5, j - 5]):
        rand_food()

    if pow_up == 'wall_hack':
        fd = canvas.create_rectangle(i + 5, j + 5, i - 5, j - 5, fill="red", outline="black")
    elif pow_up == 'speed_hack':
        fd = canvas.create_rectangle(i + 5, j + 5, i - 5, j - 5, fill="green", outline="black")
    else:
        fd = canvas.create_rectangle(i + 5, j + 5, i - 5, j - 5, fill="orange", outline="black")

    food.append(fd)


def power_timeout():
    global image, i
    global power_time, wall_hack, fill_color, speed_hack, speed
    if power_time < 5 and wall_hack:
        power_time += speed
        if image:
            canvas.image = ImageTk.PhotoImage(imageFile)
            i = canvas.create_image(0, 0, image=canvas.image, anchor='nw')
            image = False
        else:
            canvas.delete(i)
            image = True
    elif power_time < 5 and speed_hack:
        power_time += speed
    elif power_time >= 5:
        power_time = 0
        if wall_hack:
            wall_hack = False
            if not image:
                canvas.delete(i)
                image = True
            rand_food('wall_hack')
        elif speed_hack:
            speed_hack = False
            rand_food('speed_hack')
            speed = 0.05
        fill_color = 'black'


def movement(event=None):
    global old_move
    if event:
        old_move = event.char
    power_timeout()
    sleep(speed)
    move_a(old_move)
    game_window.update()


def end():
    global flag, snake_length, food, snake_body, score, old_move, updated, speed, wall_hack, snake, fill_color
    if is_over() or is_snake_body():
        flag = False
        sleep(.5)
        message = messagebox.askretrycancel("Game over", "Your score is {} !".format(score))
        if message:
            snake_length = 5
            snake = {'x': 100, 'y': 100}
            food = []
            snake_body = [snake]
            score = 0
            old_move = 's'
            updated = False
            speed = 0.05
            wall_hack = False
            flag = True
            fill_color = 'black'
            reset()
        else:
            exit()


def move_a(move):
    if move == 'd':
        snake['x'] += 10
    elif move == 'a':
        snake['x'] -= 10
    elif move == 's':
        snake['y'] += 10
    elif move == 'w':
        snake['y'] -= 10

    snake_body.append(
        canvas.create_rectangle(snake['x'] + 5, snake['y'] + 5, snake['x'] - 5, snake['y'] - 5, fill=fill_color,
                                outline="yellow"))

    is_eaten()
    if len(snake_body) >= snake_length:
        canvas.delete(snake_body[(len(snake_body) - snake_length)])


def reset():
    global speed_hack, wall_hack, power_time
    canvas.grid(row=0, column=0)
    canvas.create_rectangle(5, 5, width-5, height-5, fill='red')
    canvas.create_rectangle(10, 10, width-10, height-10, fill='white')
    wall_hack = False
    speed_hack = False
    power_time = 0
    rand_food()
    rand_food()
    rand_food(pow_up='wall_hack')
    rand_food(pow_up='speed_hack')


def main():
    global canvas, game_window
    game_window = Tk()
    game_window.title('Snake')
    canvas = Canvas(game_window, width=width, height=height, background='white')

    reset()

    game_window.bind('d', movement)
    game_window.bind('s', movement)
    game_window.bind('w', movement)
    game_window.bind('a', movement)

    while flag:
        end()
        movement()

    game_window.mainloop()
