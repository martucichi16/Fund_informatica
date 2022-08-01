import csv
from src.models.statistic_class import Statistic


def save_statistics(statistic):

    with open("src/db/statistics.csv", "a") as statistics_file:
        headers = ["date", "dna", "blood_sugar_level", "emotion_level"]
        writer = csv.DictWriter(statistics_file, fieldnames=headers)

        if statistics_file.tell() == 0:
            writer.writeheader()

        writer.writerow(statistic)


def load_statistics():
    statistics = []

    with open("src/db/statistics.csv", "r") as statistics_file:
        rows = csv.DictReader(statistics_file)

        for row in rows:
            statistic = Statistic(row["date"],
                                  row["dna"],
                                  row["blood_sugar_level"],
                                  row["emotion_level"])

            statistics.append(statistic)

    return statistics
