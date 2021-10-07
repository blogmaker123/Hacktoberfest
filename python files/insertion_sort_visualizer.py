# Insertion sort visualizer using pygame

import pygame, sys, random

WIDTH = 640
HEIGHT = 480

pygame.init()

win  = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Insertion Sort')
clock = pygame.time.Clock()

# Bar Width
n = 4
w = int(WIDTH/n)

h_arr = []

for i in range(w):
    h_arr.append(random.randint(10, 450))

counter = 0
j = 0

while True:
    win.fill((10, 10, 10))

    if counter < len(h_arr):
        key = h_arr[counter]
        j = counter - 1
        while j >= 0 and key < h_arr[j]:
            h_arr[j+1] = h_arr[j]
            j -= 1
        h_arr[j+1] = key
    else:
        print('Done')
    counter+=1

    for i in range(len(h_arr)):
        pygame.draw.rect(win, (255, 255, 255), (i*n, HEIGHT - h_arr[i], n, h_arr[i]))

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    pygame.display.flip()
