class Teglalap:
    def __init__(self, a: float, b: float, rounding: int = 2):
        self.a = a
        self.b = b
        self.rounding = rounding

    def kerulet(self) -> float:
        return round(2 * (self.a + self.b), self.rounding)

    def terulet(self) -> float:
        return round(self.a * self.b, self.rounding)

    def __str__(self):
        return f"A téglalap kerülete: {self.kerulet()}, területe: {self.terulet()}"


def main():
    t = Teglalap(5.543, 10.123, 2)
    print(t)


if __name__ == "__main__":
    main()