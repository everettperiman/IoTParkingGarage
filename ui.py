# Import the required libraries
from tkinter import *
from tkinter import ttk
import math

class CreateGraph():
   def __init__(self, garage_data, garage_number):
      data = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0], [0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]]
      data = garage_data
      nodes = 50
      garages = 4
      row_width = int(math.sqrt(nodes))

      # Create an instance of Tkinter Frame
      #win = window
      win = Tk()

      width = 300
      height = 160
      square_start = [0, 20]
      square = square_start
      square_size = 20
      square_row = 0
      nodecount = 0
      # Set the geometry
      win.title('Garage {} plot'.format(garage_number))
      win.geometry("{}x{}".format(width, height))

      # Define a function to change the state of the Widget
      def change_color():
         canvas.itemconfig(rectangle, fill='green')

      # Define a Canvas Widget
      canvas = Canvas(win, width=width, height=height)
      canvas.pack()

      while nodecount < nodes:
         square = [0, 20]
         for i in range(row_width):
            if nodecount >= nodes:
               break
            color = "red"
            if data[nodecount]:
               color = "blue"
            rectangle = canvas.create_rectangle(square[0], square_row, square[1], square_row + square_size, fill=color)
            square[0] += square_size
            square[1] += square_size
            nodecount += 1
         square_row += square_size
         
      # Create a Button to Disable the Combobox Widget
      #ttk.Button(win, text="Change Color", command=change_color).pack()
      win.mainloop()