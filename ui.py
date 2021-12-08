# Import the required libraries
from tkinter import *
from tkinter import ttk
import math
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import math



class DATA():
   def __init__(self, garage):
      self.garage = garage

   def refresh_data(self):
      client = influxdb_client.InfluxDBClient(
         url="http://192.168.1.226:8086",
         token="L5VC97xU3BJwZaFTu8gZkaIL2teFOior9QNG4R4WlBGVuK9U6-TXD4cHMXuKqhlf5DI2YmMGEmp4UhDYhx34FQ==",
         org="Home"
      )

      nodes = 50
      garages = 4
      row_width = int(math.sqrt(nodes))

      data = [[] for i in range(garages)]
      for index, i in enumerate(data):
         data[index] = [-1 for i in range(nodes)]

      for i in range(1,nodes+1):
         for j in range(1,garages+1):
            query ='from(bucket: "NodeRed")\
              |> range(start: -30d)\
              |> filter(fn: (r) => r["_measurement"] == "test")\
              |> filter(fn: (r) => r["Garage"] == "{}")\
              |> filter(fn: (r) => r["ParkingSpot"] == "{}")\
              |> last()'.format(j,i)


            query_api = client.query_api()

            result = query_api.query(org="Home",query=query)


            results = []
            for table in result:
              for record in table.records:
                results.append((record.get_field(), record.get_value()))
            results[0][-1] 
            data[j-1][i-1] = results[0][-1] 
      self.data = data[self.garage]

class CreateGraph():
   def __init__(self, garage_data, garage_number):
      data = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0], [0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]]
      data = garage_data
      nodes = len(garage_data)
      self.data = data
      self.nodes = nodes
      self.garage_number = garage_number
      # Create an instance of Tkinter Frame
      #win = window
      win = Tk()
      self.win = win
      self.refresh_delay = 10000
      width = 300
      height = 160

      # Set the geometry
      win.title('Garage {} plot'.format(garage_number+1))
      win.geometry("{}x{}".format(width, height))

      # Define a function to change the state of the Widget
      def change_color():
         canvas.itemconfig(rectangle, fill='green')

      # Define a Canvas Widget
      canvas = Canvas(win, width=width, height=height)
      canvas.pack()
      self.canvas = canvas
      self.write_canvas()

      # Create a Button to Disable the Combobox Widget
      #ttk.Button(win, text="Change Color", command=change_color).pack()
      win.after(self.refresh_delay, self.refresh_canvas)
      win.mainloop()


   def refresh_canvas(self):
      self.write_blank_canvas()
      server = DATA(self.garage_number)
      server.refresh_data()
      self.data = server.data
      self.write_canvas()
      self.win.after(self.refresh_delay, self.refresh_canvas)


   def write_canvas(self):
      canvas = self.canvas 
      nodes = self.nodes   
      data = self.data  
      row_width = int(math.sqrt(nodes))   
      square_start = [0, 20]
      square = square_start
      square_size = 20
      square_row = 0
      nodecount = 0

      while nodecount < nodes:
         square = [0, 20]
         for i in range(row_width):
            if nodecount >= nodes:
               break
            color = "green"
            if data[nodecount]:
               color = "red"
            rectangle = canvas.create_rectangle(square[0], square_row, square[1], square_row + square_size, fill=color)
            square[0] += square_size
            square[1] += square_size
            nodecount += 1
         square_row += square_size

   def write_blank_canvas(self):
      canvas = self.canvas 
      nodes = self.nodes   
      data = self.data  
      row_width = int(math.sqrt(nodes))   
      square_start = [0, 20]
      square = square_start
      square_size = 20
      square_row = 0
      nodecount = 0

      while nodecount < nodes:
         square = [0, 20]
         for i in range(row_width):
            color = "black"
            rectangle = canvas.create_rectangle(square[0], square_row, square[1], square_row + square_size, fill=color)
            square[0] += square_size
            square[1] += square_size
            nodecount += 1
         square_row += square_size