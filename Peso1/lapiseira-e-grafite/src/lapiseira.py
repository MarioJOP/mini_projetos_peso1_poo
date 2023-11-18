from src.grafite import Grafite


class Lapiseira:

    def __init__(self, calibre:float):
        self.calibre = calibre
        self.grafite = None
        self.folhas_escritas = 0

    def inserir (self, grafite: Grafite):
        if grafite.getCalibre() == self.calibre and self.grafite is None:
            self.folhas_escritas = 0
            self.grafite = grafite
            return True
        return False

    def remover(self):
        if self.grafite is not None:
            self.grafite = None
            return True
        return False

    def escrever(self, folhas: int):
        for _ in range(folhas):
            if self.grafite is not None:
                self.folhas_escritas += 1
                self.grafite.tamanho -= self.grafite.desgaste
                if self.grafite.tamanho <= 0:
                    self.grafite = None
            else:
                return False
        return True

    def getGrafite(self):
        return self.grafite

    def getCalibre(self):
        return self.calibre

    def getFolhasEscritas(self):
        return self.folhas_escritas