import csv
from node import Node
from package import Package


# Python has a referenced based data structure
# DataManager is like the GPS for the truck
class DataManager:
    def __init__(self):
        # 2D Distance Matrix for Dijkstra's implementation
        self.distance_matrix = []
        # All nodes and packages
        self.nodes_list = []
        self.packages_list = []
        # Get the distance matrix and list of nodes
        with open("distance_table.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for i, row in enumerate(csv_reader):
                self.nodes_list.append(Node(i, row[0], row[1]))
                self.distance_matrix.append([float(value) for value in row[2:]])
        # Initially the location will be the Hub so Node 0 at time 8:00 AM unless the package is on flight
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
                    special_note=row[7] if len(row) > 1 else None,
                    status=f"Location Hub : {self.nodes_list[0].get_name()} | Time : 8:00 AM",
                )
                if (
                    "Delayed on flight---will not arrive to depot until"
                    in package.get_special_note()
                ):
                    package.set_status(package.get_special_note())
                self.packages_list.append(package)

    # Workaround for getting distance because the 2D Distance Matrix is not fully filled in for the other half
    def get_distance_between_nodes(self, node_one_id, node_two_id):
        try:
            return self.distance_matrix[node_one_id][node_two_id]
        except IndexError:
            return self.distance_matrix[node_two_id][node_one_id]
