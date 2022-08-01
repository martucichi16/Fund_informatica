# Ejercicio 4

recipes = [
    {'recipe': 'Arroz con Verduras', 'ingredients': ['arroz', 'cebolla', 'morron', 'zanahoria', 'castañas', 'zuchini']},
    {'recipe': 'Ensalada de Quinoa', 'ingredients': ['quinoa', 'huevo', 'cebolla morada', 'tomate', 'morron', 'almendras']},
    {'recipe': 'Carne al Horno', 'ingredients': ['colita', 'papa', 'zanahoria', 'batata', 'cebolla', 'ajo']},
    {'recipe': 'Fideos al Pesto', 'ingredients': ['fideos', 'queso', 'nueces', 'albahaca', 'ajo', 'aceite de oliva']},
    {'recipe': 'Guiso de Lentejas', 'ingredients': ['lentejas', 'cebolla', 'zanahoria', 'papa', 'carne', 'puerro', 'morron']},
]

ingredients = []

def recipe_recommender():
    enough_ingredients = False
    for recipe_dict in recipes:
        cant_ingredients = 0

        for input_ingredient in ingredients:
            if input_ingredient in recipe_dict["ingredients"]:
                cant_ingredients += 1

        if cant_ingredients >= 2:
            print("Receta recomendada:", recipe_dict["recipe"])
            enough_ingredients = enough_ingredients or True

    if not enough_ingredients:
        print("\n[!!!] No cuenta con los ingredientes suficientes para cocinar")

def main_menu():
    print("*****************")
    print("¿Qué cocinar hoy?")
    print("*****************")

    while True:
        print("\nMENÚ")
        print("1) Ingresar ingredientes")
        print("2) Mostrar ingredientes ingresados")
        print("3) Buscar receta")
        print("4) A cocinar...\n")

        print("Elija una opcion a continuación:")
        option = input(">> ")

        if option == "1":
            print("\nIngrese los ingredientes disponibles:")
            print("(Una vez finalizada la entrada de ingredientes escriba \"quit\")")
            while True:
                ingridient = input(">> ")

                if ingridient == "quit":
                    if len(ingredients) < 2:
                        print("Es necesario ingresar 2 ingredientes o más")
                    else:
                        break
                else:
                    ingredients.append(ingridient)

        elif option == "2":
            print(f"\nSus ingredientes son: {ingredients}")

        elif option == "3":
            print("\n")
            recipe_recommender()

        elif option == "4":
            print("BUEN PROVECHO!!!")
            break

        else:
            print("Opcion no valida")

main_menu()

# Hacerlo mas prolijo por consola
# Chequear el recipe_recommender
# Reemplazar todos los ingridients por ingredients
# En el main_menu agregar un mensaje si ingresa menos de 2 ingredientes
