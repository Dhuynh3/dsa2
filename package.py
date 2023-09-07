# Representing individual packages for delivery
class Package:
    def __init__(self, **kargs):
        self.package_id = kargs.get("package_id", None)
        self.address = kargs.get("address", None)
        self.city = kargs.get("city", None)
        self.state = kargs.get("state", None)
        self.zip = kargs.get("zip", None)
        self.deadline = kargs.get("deadline", None)
        self.weight_kg = kargs.get("weight_kg", None)
        self.special_note = kargs.get("special_note", None)
        self.status = kargs.get("status", None)

    # Getters
    def get_package_id(self):
        return self.package_id
    def get_address(self):
        return self.address
    def get_city(self):
        return self.city
    def get_state(self):
        return self.state
    def get_zip(self):
        return self.zip
    def get_deadline(self):
        return self.deadline
    def get_weight_kg(self):
        return self.weight_kg
    def get_special_note(self):
        return self.special_note
    def get_status(self):
        return self.status
    # Setters
    def set_package_id(self, new_id):
        self.package_id = new_id
    def set_address(self, new_address):
        self.address = new_address
    def set_city(self, new_city):
        self.city = new_city
    def set_state(self, new_state):
        self.state = new_state
    def set_zip(self, new_zip):
        self.zip = new_zip
    def set_deadline(self, new_deadline):
        self.deadline = new_deadline
    def set_weight_kg(self, new_weight_kg):
        self.weight_kg = new_weight_kg
    def set_special_note(self, new_special_note):
        self.special_note = new_special_note
    def set_status(self, new_status):
        self.status = new_status
    # Utils and Prints
    def snapshot(self):
        return Package(
            package_id=self.package_id,
            address=self.address,
            city=self.city,
            state=self.state,
            zip=self.zip,
            deadline=self.deadline,
            weight_kg=self.weight_kg,
            special_notes=self.special_note,
            status=self.status,
        )
    def display(self):
        return f"Package {self.package_id} | Address {self.address} | City: {self.city} | State: {self.state} | Zip: {self.zip} | Deadline: {self.deadline} | Weight: {self.weight_kg} | Notes: {self.special_note} | Delivery Status: {self.status}"
