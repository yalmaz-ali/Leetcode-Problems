class stringParser:
    seperatedList = []

    name = ''
    birthDate = ''
    email = ''

    def __init__(self, string: str):
        self.birthDate, self.name, self.email = string.split(',')

    def __str__(self):
        return f"Your birthdate is {self.birthDate}\nYour name is {self.name}\nYour email is {self.email}"


string = input('Enter your DOB, Name, and email: ')
you = stringParser(string)
print(you)
