class ReverseString:
    def __init__(self, createstr):
        self.mystring = createstr
        self.mylist = list(self.mystring)

    def strR(self):
        n = len(self.mystring) - 1
        for i in self.mystring:
            self.mylist[n] = i
            n -= 1
        return "".join(self.mylist)
