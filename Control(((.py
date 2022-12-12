 #Билет номер 8
 class Wizard:
    def __int__(self, name, rating, age):
        self.name = name
        self.rating = rating
        self.age = age

    def change_rating(self, value):
        if value >= 1 and value <= 100:
            True
        else:
            False

    def change(self, value):
        while self.age < 18:
            if value >= 47:
                return self.age - (value // 10)
            else:
                return self.age + (value // 10)

    def id(self, _id):
        return (_id - self.age) * self.rating

    def __str__(self):
        return 'Wizard with rating looks years old'