import csv
from node import Node
from package import Package

# Python has a referenced based data structure
# DataManager is like the GPS for the truck
class DataManager:
    def __init__(self):
        self.distance_matrix = []
        self.nodes = []
        self.packages = []


        with open("distance_table.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for i, row in enumerate(csv_reader):
                self.nodes.append(Node(i, row[0], row[1]))
                self.distance_matrix.append([float(value) for value in row[2:]])
        