import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import math

from tkinter import *
from tkinter import ttk

from ui import *

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


			
