class Palindrome:
    def __init__(self, text: str):
        self.text = text

    def palindrome_check(self):
        self.mylist = [x for x in self.text if x.isalnum()]
        self.joinedlist = ''.join(self.mylist).lower()
        self.reversedlist = self.joinedlist[::-1]
        if self.joinedlist == self.reversedlist:
            return True
        else:
            return False

if __name__ == '__main__':
    text = Palindrome(input("Enter text to be tested: "))
    if text.palindrome_check():
        print("it is a palindrome!")
    else:
        print("it is not a palindrome!")
