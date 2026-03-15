class RideService:

    def __init__(self):
        self.rides = {}
        self.ride_id = 0

    def request_ride(self, rider, location):

        self.ride_id += 1

        ride = {
            "ride_id": self.ride_id,
            "rider": rider,
            "location": location,
            "status": "REQUESTED"
        }

        self.rides[self.ride_id] = ride

        return ride

    def update_status(self, ride_id, status):

        if ride_id in self.rides:
            self.rides[ride_id]["status"] = status
