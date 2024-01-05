from math import gcd
# ex 1
class Fractie:
    def __init__(self, numarator, numitor):
        if numitor == 0:
            raise ValueError

        common = gcd(abs(numarator), abs(numitor))
        self.numarator = numarator // common
        self.numitor = numitor // common

    def __str__(self):
        return f"{self.numarator}/{self.numitor}"

    def __add__(self, other):
        new_numarator = self.numarator * other.numitor + other.numarator * self.numitor
        new_numitor = self.numitor * other.numitor
        return Fractie(new_numarator, new_numitor)

    def __sub__(self, other):
        new_numarator = self.numarator * other.numitor - other.numarator * self.numitor
        new_numitor = self.numitor * other.numitor
        return Fractie(new_numarator, new_numitor)

    def inverse(self):
        if self.numarator == 0:
            raise ValueError

        return Fractie(self.numitor, self.numarator)

fractie1 = Fractie(5, 12)
fractie2 = Fractie(77, 9)

print("Fractie 1:", fractie1)
print("Fractie 2:", fractie2)

sum_fractie = fractie1 + fractie2
print("Suma fractiilor:", sum_fractie)

difference_fractie = fractie1 - fractie2
print("Diferenta fractiilor:", difference_fractie)

inverse_fractie = fractie1.inverse()
print("Inversa fractiei 1:", inverse_fractie)