import json
from cityyouthmatrix.apps.trips.models import Trip

class SerializedTrip():
    date: str
    time: str
    family: str
    num_adults: int
    num_kids: int
    pickup_address: str
    dropoff_addresss: str
    contact_number: str
    is_returned: bool

    def __init__(self, trip: Trip) -> None:
        self.date = f"{trip.event.event_datetime.month}-{trip.event.event_datetime.day}-{trip.event.event_datetime.year}"
        self.time = f"{trip.event.event_datetime.hour}:{trip.event.event_datetime.minute}"
        self.family = str(trip.family)
        # passengers = list(trip.passengers) todo make this work
        self.num_adults = 0 # len([f for f in passengers if f.member_type == "A"])
        self.num_kids = 0 # len([f for f in passengers if f.member_type == "C"])
        self.pickup_address = f"{trip.pickup_address.address_1} {trip.pickup_address.address_2} {trip.pickup_address.city} {trip.pickup_address.state}, {trip.pickup_address.zip_code}"
        self.contact_number = f"{trip.family.user.contact_number}"
        self.is_returned = trip.return_completed
    def to_json(self):
        return self.__dict__


