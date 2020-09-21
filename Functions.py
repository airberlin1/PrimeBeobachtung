class MathematicalFunction:

    def __init__(self, name, func_type, grad, koeffizienten=None):
        self.name = name
        if func_type == "ganzrational":
            self.term = GanzrationalTerm(grad, koeffizienten)
        else:
            self.term = "hey"


class GanzrationalTerm:

    def __init__(self, grad, koeffizienten):
        self.grad = grad
        if koeffizienten is None:
            self.koeffizienten = ["unknown"]
            for i in range(grad):
                self.koeffizienten.append("unknown")
        else:
            self.koeffizienten = koeffizienten

    def show(self, console=True):
        text = ""
        for i, j in enumerate(self.koeffizienten):
            text += str(j) + " * x^" + str(self.grad - i)
            if self.grad - i > 0:
                text += " + "
        if console:
            print(text)

    def ableiten(self):
        new_koeffizienten = []
        for i, j in enumerate(self.koeffizienten):
            new_koeffizienten.append((self.grad - i) * j)
        ableitungsfunktion = MathematicalFunction("Ableitung" + self.name, "ganzrational", self.grad - 1,
                                                  new_koeffizienten)
        return ableitungsfunktion


class Matrix:

    def __init__(self, columns, rows):
        self.matrix = [[None for _ in range(rows)] for _ in range(columns)]  # empty matrix filled with None

    def show(self, console=True):
        if console:
            print(self.matrix)

    def fill(self, bedingung, function):
        """
        füllt matrix mit Bedingung

        :param bedingung: list[int, int]; Stelle, Funktionswert
        :param function: MathematicalFunction; Funktion zu der Bedingung
        """
        for row in self.matrix:
            if row[0] is not None:  # next row that is filled
                pass

    def solve(self):
        pass
