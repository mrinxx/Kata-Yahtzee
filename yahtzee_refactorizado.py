#hacemos cambios en las variables _x y otros aspectos 06-05
#resolucion de problemas con self y @staticmethod

class Yahtzee:
    """
    autor: Marina Ocaña / Sergio Moreno

    """
    def __init__(self, d1, d2, d3, d4, d5):
        """Agrupacion de la inicializacion""" 
        self.dice = [d1, d2, d3, d4, d5]

    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        """Se agrupa la creación de total en una sola linea"""

        total = d1 + d2 + d3 + d4 + d5 
        return total

    @staticmethod
    def yahtzee(dice):
        counts = [0]*(len(dice)+1)
        for die in dice:
            counts[die-1] += 1 

        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0
    
    @staticmethod
    def ones( d1,  d2,  d3,  d4,  d5): #cambio 06-05
        """Se eliminan bucles y condicionales utilizando métodos de listas
            en varias funciones""" 

        sum=[d1,  d2,  d3,  d4,  d5].count(1)
        return sum

    @staticmethod
    def twos( d1,  d2,  d3,  d4,  d5):
        sum=[d1,  d2,  d3,  d4,  d5].count(2)*2

        return sum
        
    @staticmethod
    def threes( d1,  d2,  d3,  d4,  d5):
        sum=[d1,  d2,  d3,  d4,  d5].count(3)*3
        
        return sum

    def fours(self):
        """Al igual que en las funciones fives y sixes, se ha simplificado el bucle for"""
        sum=self.dice.count(4)*4
        return sum

    def fives(self):
        s=self.dice.count(5)*5
        return s
    
    def sixes(self):
        sum = self.dice.count(6)*6
        return sum

    @staticmethod
    def score_pair(d1,  d2,  d3,  d4,  d5):
        counts = fill(d1,  d2,  d3,  d4,  d5)

        for at in range(6):
            if counts[6-at-1] == 2:
                return (6-at)*2
        return 0
    
    @staticmethod
    def two_pair( d1,  d2,  d3,  d4,  d5):
        counts = fill(d1,  d2,  d3,  d4,  d5)
        n = 0
        score = 0

        for i in range(6):
            if (counts[6-i-1] >= 2):
                n = n+1
                score += (6-i)
                    
        if n == 2:
            return score * 2
        else:
            return 0
    
    @staticmethod
    def four_of_a_kind( d1,  d2,  d3,  d4,  d5):
        tallies = fill( d1,  d2,  d3,  d4,  d5)

        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0

    @staticmethod
    def three_of_a_kind( d1,  d2,  d3,  d4,  d5):
        t = fill( d1,  d2,  d3,  d4,  d5)

        for i in range(6):
            if (t[i] >= 3):
                return (i+1) * 3
        return 0

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = fill( d1,  d2,  d3,  d4,  d5)

        if tallies.count(1)==5: 
            return 15
        return 0

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = fill( d1,  d2,  d3,  d4,  d5)

        if tallies.count(1)==5:
            return 20
        return 0

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):

        """Se ha eliminado creación de variables innecesarias en este punto.
        Se crean en la función variables_generation"""
        
        tallies = fill( d1,  d2,  d3,  d4,  d5)

        generation= variable_generation(tallies)
        _2=generation[0]
        _2_at=generation[1]
        _3=generation[2]
        _3_at=generation[3]

        if _2 and _3:
            return _2_at * 2 + _3_at * 3
        else:
            return 0

def fill(a1,  a2,  a3,  a4,  a5): 
    """Se llaman "aX" porque es más genérico. 
    Se refiere a parte del código de score_pairs, three_of_a_kind,four_of_a_kind..."""
    counts = [0]*6
    counts[a1-1] += 1
    counts[a2-1] += 1
    counts[a3-1] += 1
    counts[a4-1] += 1
    counts[a5-1] += 1

    return counts

def variable_generation(tallies):
    """Se refiere a los bucles for de la función Yahtzee.fullHouse """
    _2 = False
    _2_at = 0
    _3 = False
    _3_at = 0

    for i in range(6):
        if (tallies[i] == 2): 
            _2 = True
            _2_at = i+1

        if (tallies[i] == 3): 
            _3 = True
            _3_at = i+1

    return (_2,_2_at,_3,_3_at)