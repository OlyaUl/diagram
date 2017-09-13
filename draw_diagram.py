from django.shortcuts import render
import json
import random
import re
import turtle
import argparse


if __name__ == "__main__":
    text = input()

    # словарь для диаграммы
    def dict_for_diagram(text):
        # text = "hello test test"
        lst = text.split()
        dct = {}
        dct_re = {}
        print(lst)
        # считает количесвто каждой буквы в тексте
        for i in lst:
            counter = dct.get(i, 0)
            counter += 1
            dct[i] = counter
            dct_re[i] = counter

        # считает частоту каждой буквы в тексте
        for i in dct:
            dct[i] = round((dct[i]*100/len(lst)), 2)

        letters = list(dct.keys())
        lst_len = len(letters)
        return dct, lst_len, dct_re


    def rays():
        dct, len_st, dict_c = dict_for_diagram(text)
        colors = ["red", "green", "gray", "blue", "orange",
                  "purple", "pink", "yellow",
                  "black"]
        angle = 180/len_st
        turtle.setpos(0, 0)

        for i in dct:
            color = random.choice(colors)
            turtle.color(color)
            turtle.forward(dct[i]*100)
            turtle.circle(4)

            turtle.write("     " + str(i))
            turtle.pd()
            turtle.goto(0, 0)
            turtle.pu()
            turtle.left(180-angle)
        return angle


    def sectors():
        dct, len_st, dct_r = dict_for_diagram(text)

        colors = ["#a0c8f0",
                  "black", "#ADFF2F", "#00FF00", "#32CD32",
                  "#CD5C5C", "#008000", "#B22222", "#000080"]
        new_color = []
        dist_x = 150
        dist_y = 150
        for i in dct:
            dist_y -= 20
            turtle.pu()
            turtle.setpos(0, 0)
            turtle.pd()
            while True:
                color = random.choice(colors)
                if color not in new_color:
                    new_color.append(color)
                    ccc = color
                    break
                if len(colors) == len(new_color):
                    new_color = []
            turtle.color(ccc)
            turtle.begin_fill()
            angle = dct[i] * 360 / 100
            turtle.forward(100)
            turtle.left(90)
            turtle.circle(100, angle)
            turtle.goto(0,0)
            turtle.left(-90)
            turtle.pu()
            turtle.setpos(dist_x, dist_y)
            turtle.pd()
            turtle.circle(3)

            turtle.write("  " + i + " - " + str(dct_r[i]))
            turtle.end_fill()

    diagrams = {rays.__name__: rays,
                sectors.__name__: sectors}

    parser = argparse.ArgumentParser()
    parser.add_argument("--diagram", choices=("rays", "sectors"))

    args = parser.parse_args()
    print(args.diagram)
    diagrams[args.diagram]()

    input()


