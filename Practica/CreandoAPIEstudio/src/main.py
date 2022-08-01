from flask import Flask, jsonify, request
from src.db.db_manager import load_animals, save_booking, load_bookings
app = Flask(__name__)

animals = load_animals()
bookings = load_bookings()


@app.route("/api/zoo/animals", methods=["GET"])
def get_animals():
    carnivorous_animals = []
    food_param = request.args.get("food")

    if food_param == "meat" or food_param == "fish":
        for animal in animals:
            if animal.food == food_param:
                carnivorous_animals.append(animal)

        return jsonify([animal.serialize() for animal in carnivorous_animals])

    else:
        return jsonify([animal.serialize() for animal in animals])


@app.route("/api/zoo/animals/<animal_name>", methods=["GET"])
def animal_detail(animal_name):
    for animal in animals:
        if animal.name == animal_name:
            return jsonify(animal.serialize())

    return jsonify(status=404, description="Animal no available"), 404


@app.route("/api/zoo/bookings", methods=["POST"])
def new_booking():
    new_booking = request.json
    save_booking(new_booking)

    return jsonify(
        {"status": "booked",
         "your_booking": new_booking}
                   )


@app.route("/api/zoo/bookings", methods=["GET"])
def get_bookings():
    return jsonify([booking.serialize() for booking in bookings])

