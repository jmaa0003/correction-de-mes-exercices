"""
MABHOUMA JOSHUA
classe Polynome qui va définir un polynômes sur base d'une classe Monôme.
21/11/2023
"""
class DegreeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(Exception)


class Monome:
    def __init__(self, degre, coef):
        degre = self._degre
        coef = self.coef
        if type(degre) != int:
            raise ValueError

        if type(coef) != float:
            raise ValueError

    def get_coefficient(self):
        return self.coef

    def get_degre(self):
        return self.degre

    def __repr__(self):
        return "Monome(%f,%d)" % (self.coef, self._degre)

    def __str__(self):
        if not self._degre:
            res = str(self.coef)
        elif self._degre == 1:
            res = str(self._coef) + "x"
        elif self._degre >= 2:
            res = str(self._coef) + "x^" + str(self._degre)

    def __add__(self, other):
        if self._degre != other._degre:
            pass
        else:
            return Monome(self.coef + other.coef, self._degre)

    def __sub__(self, other):
        if self._degre != other._degre:
            pass
        else:
            return Monome(self.coef - other.coef, self._degre)

    def __mul__(self, other):
        return Monome(self.coef * other.coef, self._degre)

    def __floordiv__(self, other):
        return Monome(self.coef // other.coef, self._degre)

    def __truediv__(self, other):
        return Monome(self.coef / other.coef, self._degre)

    def __lt__(self, other):
        return self.coef < other.coef

    def __le__(self, other):
        return self.coef <= other.coef

    def __gt__(self, other):
        return self.coef == other.coef

    def __ge__(self, other):
        return self.coef > other.coef

    def __eq__(self, other):
        return self.coef == other.coef

class Polynome:
    def __init__(self,*m):
        self.polynomes =list(m)
        self.polynomes.sort(key= lambda i : i.get_degre, reverse=True)
    
        i, new_list = 0, []
        while self.polynomes[i].get_degre() == self.polynomes[i+1].get_degre()\
              and i+1 < len(self.polynomes):
            new_list.append(__add__(self.polynomes[i], self.polynomes[i+1]))
            
        self.polynomes = new_list
        
        
        
   # def __reduce__(self):
       # """additionne les monomes du polynomes dont les exposants sont egaux"""
        
    