# Ejercicio 5

print("{:>75}".format("**********************************************"))
print("{:>75}".format("************   Banco Digital LA   ************"))
print("{:>75}".format("**********************************************"))

accounts = []

account_1 = {"user_id": "44816202",
             "password": "ABCdef",
             "saving_bank": {"account_num": "1234", "amount": 100000.00},
             "current_account": {"account_num": "9876", "amount": 5000.00},
             "last_trxs": [3500.00, 6000.00, -5000.00]
             }

account_2 = {"user_id": "43243792",
             "password": "holaxd",
             "saving_bank": {"account_num": "1235", "amount": 20000},
             "current_account": {"account_num": "8520", "amount": 15000},
             "last_trxs": [100.00, 20000.00, -3000.00, 900]
             }

accounts.append(account_1)
accounts.append(account_2)

while True:
    print("\nLOGIN")
    id_usuario = input("Ingrese su id\n>> ")
    contrasena = input("Por favor, ingrese su contraseña a continuación\n>> ")

    for cuenta in accounts:
        if (cuenta["user_id"] == id_usuario) and (contrasena == cuenta["password"]):
            while True:
                indice = accounts.index(cuenta)

                print("\nMenú de opciones:")
                print("\t1) Acreditar en CA")
                print("\t2) Acreditar en CC")
                print("\t3) Consultar saldo en CA")
                print("\t4) Consultar saldo en CC")
                print("\t5) Consultar Trx")
                print("\t6) Salir")

                opcion = input("\nSeleccione opción\n>> ")

                if opcion == "1":
                    while True:
                        try:
                            credito = float(input("\nMonto a acreditar en CA\n>> La$ "))

                            cuenta["saving_bank"]["amount"] += credito
                            cuenta["last_trxs"].append(float(credito))

                            print("\n+ CUENTA ACTUALIZADA")
                            print("---------------------------------------------")
                            break
                        except ValueError:
                            print("Debe ingresar un monto numerico")

                elif opcion == "2":
                    while True:
                        try:
                            credito_2 = float(input("\nMonto a acreditar en CC\n>> La$ "))

                            cuenta["current_account"]["amount"] += credito_2
                            cuenta["last_trxs"].append(float(credito_2))

                            print("\n+ CUENTA ACTUALIZADA")
                            print("---------------------------------------------")
                            break
                        except ValueError:
                            print("Debe ingresar un monto numerico")

                elif opcion == "3":
                    print("\n*** Resumen de CA ***")
                    print(f"Número de cuenta:", cuenta["saving_bank"]["account_num"])
                    print(f"Saldo actualizado: La$", cuenta["saving_bank"]["amount"])
                    print("---------------------------------------------")

                elif opcion == "4":
                    print("\n*** Resumen de CC ***")
                    print(f"Número de cuenta:", cuenta["current_account"]["account_num"])
                    print(f"Saldo actualizado: La$", cuenta["current_account"]["amount"])
                    print("---------------------------------------------")

                elif opcion == "5":
                    print("\nUltimas transacciones realizadas:")
                    for trx in cuenta["last_trxs"]:
                        print("\tLa$ ", trx)
                    print("---------------------------------------------")

                elif opcion == "6":
                    break

                else:
                    print("\nOpción no válida, por favor vuelva a intentarlo")

    boolean = True
    for cuenta in accounts:
        if (cuenta["user_id"] != id_usuario) or (contrasena != cuenta["password"]):
            boolean = boolean and True
        else:
            boolean = boolean and False

    if boolean:
        print("Permiso denegado - Usuario invalido")

    print("\nSi desea finalizar ingrese \"quit\", sino ingrese \"continue\"")
    logout = input(">> ")

    if logout == "quit":
        break

'''
Cómo hacer que al escribir la contraseña aparezca como **********?
import getpass
http://pymotw.com/2/getpass/

(Lo hago en el otro archivo)
'''