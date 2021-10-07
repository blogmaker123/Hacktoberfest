#Selection Sort visualization using pygame
import pygame as pg, sys, random
from pygame.locals import *


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

WIDTH = 640
HEIGHT = 480
win_size = (WIDTH, HEIGHT)

pg.init()

win = pg.display.set_mode(win_size)
pg.display.set_caption('Selection Sort Visualization')
clock = pg.time.Clock()

n = 4

w = int(WIDTH/n)
h_arr = []
state = []
for i in range(w):
    height = random.randint(10, 450)
    h_arr.append(height)
    state.append(1)


counter = 0

while True:
    win.fill((10, 10, 10))

    if counter < len(h_arr):

        min_idx = counter
        for j in range(counter+1, len(h_arr)):
            if h_arr[min_idx] > h_arr[j]:
                state[j] = 0
                min_idx = j
            else:
                state[j] = 1
                state[min_idx] = 1
        h_arr[counter], h_arr[min_idx] = h_arr[min_idx], h_arr[counter]

    else:
        print('Done')
    counter+=1

    if counter - 1 < len(h_arr):
        state[counter - 1] = 2


    for i in range(len(h_arr)):
        if state[i] == 0:
            color = RED
        elif state[i] == 2:
            color = GREEN  
        else:
            color = WHITE
        pg.draw.rect(win, color, pg.Rect(int(i*n), HEIGHT - h_arr[i], n, h_arr[i]))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    clock.tick(30)
    pg.display.flip()         
