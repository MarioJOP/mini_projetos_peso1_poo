from enum import Enum


class Moeda(Enum):
    M10 = (.10, 1)
    M25 = (.25, 2)
    M50 = (.50, 3)
    M100 = (1.00, 4)

    def __init__(self, valor: float, volume: int):
        self.volume = volume
        self.valor = valor

    def getVolume(self):
        return self.volume

    def getValor(self):
        return self.valor