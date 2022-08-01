

class Booking:
    def __init__(self, name, phone, booked_date, tickets, visiting_animals):
        self.name = name
        self. phone = phone
        self.booked_date = booked_date
        self.tickets = tickets
        self.visiting_animals = visiting_animals

    def serialize(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "booked_date": self.booked_date,
            "tickets": self.tickets,
            "visiting_animals": self.visiting_animals
        }
