import paho.mqtt.client as mqtt
import random
import time
import json


class node(object):
    def __init__(self, payload):
        self.number = payload["node"]
        self.garage = payload["garage"]
        self.LED = payload["LED"]

    def print_stats(self):
        print("Node: {} Garage: {} New Status: {}".format(self.number, self.garage, self.LED))

    def change_status(self,status):
        if self.LED != status:
            self.LED = status
            self.print_stats()
            return 1

        return 0

def search_node_list(node_list, node, garage):
    if(node_list):
        for index, i in enumerate(node_list):
            if node == i.number and garage == i.garage:
                return index
    return -1


def on_message(client, userdata, message):
    x = json.loads(message.payload)
    print(x)
    new_node = node(x)
    new_node.print_stats()

if __name__ == "__main__":
    global_node = 1
    global_garage = 1
    global_node_list = []

    client = mqtt.Client("TestNodeYes")

    client.connect("192.168.1.110")

    client.subscribe("node_red_out")

    client.on_message = on_message

    client.loop_forever()
