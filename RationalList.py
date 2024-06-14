import math
from Rational import Rational


class RationalList:
    def __init__(self):
        self.data = []

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        if isinstance(value, Rational):
            self.data[index] = value
        elif isinstance(value, int):
            self.data[index] = Rational(value)


    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        if isinstance(other, RationalList):
            return RationalList.from_list(self.data + other.data)
        elif isinstance(other, Rational):
            return RationalList.from_list(self.data + [other])
        elif isinstance(other, int):
            return RationalList.from_list(self.data + [Rational(other)])


    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.data.extend(other.data)
        elif isinstance(other, Rational):
            self.data.append(other)
        elif isinstance(other, int):
            self.data.append(Rational(other))


    def append(self, value):
        if isinstance(value, Rational):
            self.data.append(value)
        elif isinstance(value, int):
            self.data.append(Rational(value))



    def from_list(cls, lst):
        instance = cls()
        for item in lst:
            instance.append(item)
        return instance

    def sum(self):
        total = Rational(0)
        for item in self.data:
            total += item
        return total

    def __iter__(self):
        sorted_data = sorted(self.data, key=lambda r: (-r.denominator, -r.numerator))
        return iter(sorted_data)






