# -*- coding: utf-8 -*-

class Mod:
  
    def __init__(self, n, mod):
        if mod == 0:
            raise ZeroDivisionError              
        self.n = n % mod
        self.mod = mod
    
    def mod(self):
        return self.mod
    
    def n(self):
        return self.n
    
    def __add__(self, o):
        if isinstance(o, Mod):
            if o.mod != self.mod:
                raise ValueError("Incompatible sum, different mod")
            return Mod(self.n%self.mod + o.n%o.mod, self.mod)
        elif isinstance(o, int):
            return self + Mod(o, self.mod)
    
    def __radd__(self, o):
        return self + o
    
    def __neg__(self):
        return Mod(-self.n,self.mod)
    
    def __rsub__(self, o):
        return -self + o
    
    def __sub__(self, o):
        return self + (-o)
    
    def __repr__(self): 
        return "{}".format(self.n)
    
    def __mul__(self, o):
        if isinstance(o, Mod):
            if o.mod != self.mod:
                raise ValueError("Incompatible multiplication, different mod")
            return Mod((self.n%self.mod) * (o.n%o.mod), self.mod)
        elif isinstance(o, int):
            return self * Mod(o, self.mod)
    
    def __rmul__(self, o):
        return self * o
    
    def __inverse(self, a, n):
        t, newt = 0, 1
        r, newr = n, a

        while newr != 0:
            quotient = r // newr
            (t, newt) = (newt, t - quotient * newt) 
            (r, newr) = (newr, r - quotient * newr)

        if r > 1:
            raise ValueError("Not invertible")
        if t < 0:
            t = t + n
        return t
    
    def __pow__(self, exp):
        if isinstance(exp, int):
            if exp >= 0:
                ret = Mod(1,self.mod)
                base = self
                while exp:
                    if exp & 1:
                        ret = ret * base
                    base = base * base
                    exp >>= 1
                return ret
            elif exp == -1:
                return Mod(self.__inverse(self.n, self.mod),self.mod)
            else:
                return (self**(-1))**(-exp)
        raise ValueError("Exponientiation only with integer values")
        
    def __truediv__(self, o):
        if isinstance(o, Mod):
            return self * (o**(-1))
        elif isinstance(o, int):
            return self * (Mod(o,self.mod)**(-1))
    
    def __rtruediv__(self, o):
        if isinstance(o, Mod):
            return o * (self**(-1))
        elif isinstance(o, int):
            return Mod(o) * (self**(-1))

