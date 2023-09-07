from hashtable import HashTable
from datetime import datetime, timedelta
from datamanager import DataManager

class Truck(DataManager):
    def __init__(self, start_time, capacity=16):
        self.start_time = start_time
        self.capacity = capacity
        