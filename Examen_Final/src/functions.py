# Funcion para calcular el promedio en el endpoint /statistics/reports con método GET

def average_statistics(statistics):  # Recibirá la lista de blood_sugar_levels y emotion_levels

    sum_statistics = 0

    for statistic in statistics:
        sum_statistics += int(statistic)

    average_statistic = sum_statistics / len(statistics)

    return average_statistic
