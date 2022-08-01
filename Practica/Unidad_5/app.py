import modulo

sueldos_mes = [10000, 10000, 10000, 15000, 10000, 17500, 10000, 15000, 15000, 20000, 20000, 30000]

ingreso_anual = modulo.suma_lista(sueldos_mes)


print(f"Mi ingreso al finalizar el año fue de ${ingreso_anual}")

print("\n--------------------------------------------------------------")
print("¿Cuanto más gané en la segunda mitad del año?")

primer_semestre = modulo.suma_lista(sueldos_mes[0:6])
segundo_semestre = modulo.suma_lista(sueldos_mes[6:])

print(modulo.resta(segundo_semestre, primer_semestre))


print("\n--------------------------------------------------------------")
print("Me pagaron bien el aguinaldo de junio?")

sueldo_junio = 10000
max_sueldo = max(sueldos_mes[0:5])
aguinaldo = modulo.multiplicacion(max_sueldo, 0.5)

if sueldos_mes[5] == sueldo_junio + aguinaldo:
    print("El aguinaldo ha sido abonado correctamente")
else:
    print("No se ha calculado el aguinaldo correctamente")
