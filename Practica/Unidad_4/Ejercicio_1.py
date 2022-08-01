# Ejercicio 1
print("***********************")
print("Welcome to DISNEY WORLD")
print("***********************")

print("\n")
while True:
    age = input("Buy a ticket, please enter your age: \n>> ")

    if age == "quit":
        print("Thank you for your purchase")
        break

    age = int(age)

    if age < 5:
        print("Free ticket")
    elif (age >= 5) and (age < 9):
        print("Ticket price: U$s 15")
    elif (age >= 9) and (age < 14):
        print("Ticket price: U$s 23")
    elif (age >= 14) and (age < 100):
        print("Ticket price: U$s 35")
    else:
        print("You are awesome!! Free ticket for you")

    print("\n(If you want to finish your purchase, write quit)")
