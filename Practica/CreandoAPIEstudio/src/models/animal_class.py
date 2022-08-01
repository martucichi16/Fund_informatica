class Animal:

    def __init__(self, name, quantity, age, weight, food):
        self.name = name
        self.quantity = quantity
        self.age = age
        self.weight = weight
        self.food = food

    def serialize(self):
        return {"name": self.name,
                "quantity": self.quantity,
                "age": self.age,
                "weight": self.weight,
                "food": self.food}
