import math

class Rational:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError()
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __repr__(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        else:
            return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if isinstance(other, Rational):
            numerator = self.numerator * other.denominator + other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            return Rational(self.numerator + other * self.denominator, self.denominator)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)