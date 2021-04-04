import os

# Part 1 - The import​
import tkinter
import PySimpleGUI as sg

def Hello():
    print("Hello World from: " + __name__)
    print(f"DISPLAY is {os.environ['DISPLAY']}")

# Part 2 - The Layout​
layout = [  [sg.Text("What's your name?")],
            [sg.Input()],
            [sg.Button('Ok')] ]

# Part 3 - Window Defintion​
window = sg.Window('Window Title', layout)

# Part 4 - Event loop or Window.read call​
(event, values) = window.read()

# Do something with the information gathered​
print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Part 5 - Close the Window​
window.close()