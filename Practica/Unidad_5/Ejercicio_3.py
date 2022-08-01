# Ejercicio 3
students = [{"id": 44569812, "parcial_1": 8, "parcial_2": 7, "final": 9, "concepto": 9},
            {"id": 43650012, "parcial_1": 6, "parcial_2": 5, "final": 5, "concepto": 7},
            {"id": 39851264, "parcial_1": 10, "parcial_2": 9, "final": 9},
            {"id": 44511215, "parcial_1": 7, "parcial_2": 6, "final": 8, "concepto": 6},
            {"id": 44123456, "parcial_1": 2, "parcial_2": 2, "final": 4, "concepto": 5},
            {"id": 42015203, "parcial_1": 9, "parcial_2": 10, "final": 10},
            {"id": 44896107, "parcial_1": 7, "parcial_2": 6, "final": 7, "concepto": 7},
            {"id": 40254980, "parcial_1": 8, "parcial_2": 8, "final": 9}]

notes = []


def average_notes(student_id):
    final_note = dict()
    for student in students:
        if student_id == student["id"]:
            if "concepto" in student.keys():
                average = round((student["parcial_1"] + student["parcial_2"] + student["final"] +
                                 student["concepto"]) / 4, 2)
                final_note["student_id"] = student_id
                final_note["average"] = average
                return final_note

            else:
                average = round((student["parcial_1"] + student["parcial_2"] + student["final"]) / 3, 2)
                final_note["student_id"] = student_id
                final_note["average"] = average
                return final_note


def final_notes(students_list):
    for student in students_list:
        notes.append(average_notes(student["id"]))

    for note in notes:
        print(f"El promedio del estudiante con id {note['student_id']} es de {note['average']}")


print("------------------------")
print("| CIERRE DE LA MATERIA |")
print("------------------------")
final_notes(students)
