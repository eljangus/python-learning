class EvenNumbers:
    number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > 8:
            raise StopIteration
        current = self.number
        self.number += 2
        return current
