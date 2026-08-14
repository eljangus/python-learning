class Name:
    def __init__(self, fullname):
        self.name = fullname

    def splitname(self):
        vor, nach = self.name.split()
        return vor, nach


hey = Name("Elias Schlosser")
print(hey.splitname())
