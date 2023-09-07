import csv
from node import Node
from package import Package
from datetime import datetime, timedelta

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
        
        with open("package_data.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                package = Package(
                    package_id=row[0],
                    address=row[1],
                    city=row[2],
                    state=row[3],
                    zip=row[4],
                    deadline=row[5],
                    weight_kg=row[6],
                    special_note=row[7] if len(row) > 7 else None,
                    status= f"Location : {self.nodes[0]} | Time : "
                    #"At the Hub Node 0 at : 8:00 AM"
                )
                if package.get_package_special_note() and "Delayed" in package.get_package_special_note():
                    package.set_delivery_status("On flight until 9:05 AM")
                self.packages.append(package)