# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 09:33:42 2020

@author: giga
"""

from tkinter import *

win = Tk()
win.geometry("600x600")
win.title("the center of the mass")
canvas_width = 500
canvas_height = 200

def get_point(event):
    """baraye gereftan noghate marzi be soorate dasti az karbar"""
     
    points = []
    mass = []
    points.append(event.x)
    points.append(event.y)
    mass.append(event.x)
    mass.append(200-event.y)
    print(points)


    
canvas_shape = Canvas(win, width = canvas_width, height = canvas_height, bg = 'white')
canvas_shape.pack()
point_lists = []
point_lists.append(canvas_shape.bind('<B1-Motion>', get_point))
print(point_lists)
win.mainloop()





