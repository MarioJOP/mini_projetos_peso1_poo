from src.dureza import Dureza


class Grafite:

    def __init__(self, calibre: float, dureza: Dureza, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

        if self.dureza.value == 1 or self.dureza.value == 2:
            self.desgaste = self.dureza.value
        elif self.dureza.value == 3:
            self.desgaste = 4
        else:
            self.desgaste = 6

    def desgastePorFolha(self):
        return self.desgaste

    def getDureza(self):
        return self.dureza

    def getCalibre(self):
        return self.calibre

    def getTamanho(self):
        return self.tamanho

    def setTamanho(self, tamanho:int):
        self.tamanho = tamanho