# -*- coding: utf-8 -*-

class Fraction:
    def __gcd(self, a, b):
        while b != 0:
            t = b
            b = a % b
            a = t
        return a

    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError
        GCD = self.__gcd(numerator, denominator)
        if denominator < 0:
            denominator *= -1
            numerator *= -1

        self.n = numerator // GCD
        self.d = denominator // GCD

    def approx(self):
        return self.n/self.d

    def numden(self):
        return self.n, self.d

    def __add__(self, o):
        if isinstance(o, Fraction):
            n, d = self.n*o.d + o.n*self.d, self.d*o.d
            GCD = self.__gcd(n, d)
            n, d = n//GCD, d//GCD
            return Fraction(n, d)
        elif isinstance(o, int):
            return self + Fraction(o)

    def __radd__(self, o):
        return self + o

    def __neg__(self):
        return Fraction(-self.n, self.d)

    def __rsub__(self, o):
        return -self + o

    def __sub__(self, o):
        return self + (-o)

    def __repr__(self):
        if self.d == 1 or self.n == 0:
            return "{}".format(self.n)
        return "{}/{}".format(self.n, self.d)

    def __mul__(self, o):
        if isinstance(o, Fraction):
            n, d = self.n * o.n, self.d*o.d
            GCD = self.__gcd(n, d)
            n, d = n//GCD, d//GCD
            return Fraction(n, d)
        elif isinstance(o, int):
            return self * Fraction(o)

    def __rmul__(self, o):
        return self * o

    def __pow__(self, o):
        n, d = self.n, self.d
        if o < 0:
            n, d, o = d, n, -o
        return Fraction(n**o, d**o)

    def __truediv__(self, o):
        if isinstance(o, Fraction):
            return self * (o**(-1))
        elif isinstance(o, int):
            return self * (Fraction(o)**(-1))

    def __rtruediv__(self, o):
        if isinstance(o, Fraction):
            return o * (self**(-1))
        elif isinstance(o, int):
            return Fraction(o) * (self**(-1))

    def __lt__(self, o):
        if isinstance(o, Fraction):
            return self.n * o.d < self.d * o.n
        elif isinstance(o, int):
            return self < Fraction(o)

    def __rt__(self, o):
        return o < self

    def __le__(self, o):
        if isinstance(o, Fraction):
            return self.n * o.d <= self.d * o.n
        elif isinstance(o, int):
            return self <= Fraction(o)

    def __re__(self, o):
        return o <= self

    def __eq__(self, o):
        return self.n == o.n and self.d == o.d

    def __ne__(self, o):
        return not (self == o)

    def __hash__(self):
        return hash((self.n, self.d))
