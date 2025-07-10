from math import sqrt, e, cos, sin

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        if type(other) is int:
            other = ComplexNumber(other, 0)
        real_sum = self.real + other.real
        imaginary_sum = self.imaginary + other.imaginary
        return ComplexNumber(real = real_sum, imaginary = imaginary_sum)
    
    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if type(other) is int:
            other = ComplexNumber(other, 0)
        real_mul = self.real * other.real - self.imaginary * other.imaginary
        imaginary_mul = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real = real_mul, imaginary = imaginary_mul)
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        if type(other) is int:
            other = ComplexNumber(other, 0)
        real_sub = self.real - other.real
        imaginary_sub = self.imaginary - other.imaginary
        return ComplexNumber(real = real_sub, imaginary = imaginary_sub)
    
    def __rsub__(self, other):
        if type(other) is int:
            other = ComplexNumber(other, 0)
        real_sub = other.real - self.real
        imaginary_sub = other.imaginary - self.imaginary
        return ComplexNumber(real = real_sub, imaginary = imaginary_sub)

    def __truediv__(self, other):
        if type(other) is int:
            other = ComplexNumber(other, 0)
        common_denominator = (other.real**2 + other.imaginary**2)
        real_div = (self.real * other.real + self.imaginary * other.imaginary) / common_denominator
        imaginary_div = (self.imaginary * other.real - self.real * other.imaginary) / common_denominator
        return ComplexNumber(real = real_div, imaginary = imaginary_div)
    
    def __rtruediv__(self, other):
        if type(other) is int:
            other = ComplexNumber(other, 0)
        common_denominator = (self.real**2 + self.imaginary**2)
        real_div = (other.real * self.real + other.imaginary * self.imaginary) / common_denominator
        imaginary_div = (other.imaginary * self.real - other.real * self.imaginary) / common_denominator
        return ComplexNumber(real = real_div, imaginary = imaginary_div)

    def __abs__(self):
        absolute_value = sqrt(self.real**2 + self.imaginary**2)
        return absolute_value

    def conjugate(self):
        return ComplexNumber(real = self.real, imaginary = -self.imaginary)

    def exp(self):
        real_exp = e**self.real * cos(self.imaginary)
        imaginary_exp = e**self.real * sin(self.imaginary)
        return ComplexNumber(real = real_exp, imaginary = imaginary_exp)
