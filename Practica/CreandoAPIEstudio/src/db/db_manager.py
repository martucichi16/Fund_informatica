import csv
from src.models.animal_class import Animal
from src.models.booking_class import Booking


def load_animals():
    animals = []

    with open("src/db/animals.csv", "r") as animals_file:
        rows = csv.DictReader(animals_file)

        for row in rows:
            animal = Animal(
                row["name"],
                row["quantity"],
                row["age"],
                row["weight"],
                row["food"]
            )

            animals.append(animal)

    return animals


def save_booking(booking):

    with open("src/db/bookings.csv", "a") as bookings_file:
        headers = ["name", "phone", "booked_date", "tickets", "visiting_animals"]
        writer = csv.DictWriter(bookings_file, fieldnames=headers)

        if bookings_file.tell() == 0:
            writer.writeheader()

        writer.writerow(booking)


def load_bookings():
    bookings = []

    with open("src/db/bookings.csv", "r") as bookings_file:
        rows = csv.DictReader(bookings_file)

        for row in rows:
            booking = Booking(row["name"],
                              row["phone"],
                              row["booked_date"],
                              row["tickets"],
                              row["visiting_animals"])

            bookings.append(booking)

    return bookings
