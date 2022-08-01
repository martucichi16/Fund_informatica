class Statistic:

    def __init__(self, date, dna, blood_sugar_level, emotion_level):
        self.date = date
        self.dna = dna
        self.blood_sugar_level = blood_sugar_level
        self.emotion_level = emotion_level

    def serialize(self):
        return {"date": self.date,
                "dna": self.dna,
                "blood_sugar_level": self.blood_sugar_level,
                "emotion_level": self.emotion_level
                }
