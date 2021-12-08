import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import math

from tkinter import *
from tkinter import ttk

from ui import *

val = int(input("Enter the garage you would like to monitor: "))
val = val - 1
server = DATA(val)
server.refresh_data()
CreateGraph(server.data, val)