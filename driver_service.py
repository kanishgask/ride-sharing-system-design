class DriverService:

    def __init__(self):
        self.drivers = {}

    def register_driver(self, driver_id, location):

        self.drivers[driver_id] = {
            "location": location,
            "available": True
        }

    def get_available_drivers(self):

        return [
            driver for driver, data in self.drivers.items()
            if data["available"]
        ]
