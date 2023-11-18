from src.item import Item
from src.moeda import Moeda

class Cofre:
    def __init__(self, volumeMaximo: int):
        self.__volumeMaximo = volumeMaximo
        self.volume = 0
        self.taInt = True
        self.moedas = []
        self.itens = []
    def getVolume(self):
        return self.volume

    def getVolumeMaximo(self):
        return self.__volumeMaximo

    def getVolumeRestante(self):
        return self.__volumeMaximo - self.volume

    def add(self, item: Item):
        if self.taInt:
            if item.getVolume() <= self.getVolumeRestante():
                self.volume += item.getVolume()
                self.itens.append(item)
                return True
            else:
                print('Volume do item maior que o volume restante.')
                return False
        else:
            print('Cofre não está inteiro')
            return False

    def addMoeda(self, moeda: Moeda):
        if self.taInt:
            if moeda.getVolume() <= self.getVolumeRestante():
                self.volume += moeda.getVolume()
                self.moedas.append(moeda.getValor())
                return True
            else:
                print('Volume da moeda maior que o volume restante.')
                return False
        else:
            print('Cofre não está inteiro')
            return False
    def obterItens(self):
        if not self.taInt:
            if len(self.itens) == 0:
                return 'vazio'
            descs = [item.getDescrição() for item in self.itens]
            txt = ''
            for desc in descs:
                txt += desc + ', ' if desc != descs[-1] else desc
            return txt

    def obterMoedas(self):
        if not self.taInt:
            if len(self.moedas) == 0:
                return 0
            return sum(self.moedas)
        return -1

    def taInteiro(self):
        return self.taInt

    def quebrar(self):
        if self.taInt:
            self.taInt = False
            return True
        return False