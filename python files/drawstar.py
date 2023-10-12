'''
Program: drawflower.py
Author: Binayak Jha
'''

import sys
import turtle


def draw_square(t, side_length):
    """
    Draws a square with side length side_length
    t: the turtle to draw with
    side_length: the length of each side
    return: None
    """
    for i in range(4):
        t.forward(side_length)
        t.right(90)


def main():
    # setup the window and the turtle
    window = turtle.Screen()
    window.setup(600, 600)
    t = turtle.Turtle()
    t.speed(5)
    # get input from the user
    num_squares = int(sys.argv[1])
    side_length = int(sys.argv[2])

    # draw the flower consisting of num_squares squares
    # each square is side_length long
    # TODO: write the code using at least 1 for loop!
    for i in range(num_squares):
        draw_square(t, side_length)
        t.left(360/num_squares)

    # To put the turtle back to the initial position
    t.penup()
    turtle.exitonclick()


if __name__ == "__main__":
    main()
