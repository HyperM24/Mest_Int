class FizzBuzz:
    def __init__(self, szam):
        self.szam = szam

    def start(self):
        for i in range(1, self.szam + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("fizzbuzz")
            elif i % 3 == 0:
                print("fizz")
            elif i % 5 == 0:
                print("buzz")
            else:
                print(i)


if __name__ == "__main__":
    fb = FizzBuzz(15)
    fb.start()