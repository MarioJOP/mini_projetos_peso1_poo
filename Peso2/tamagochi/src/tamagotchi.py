class Tamagotchi:

    def __init__(self, energiaMax: int, saciedadeMax: int, limpezaMax: int, idadeMax: int):
        self.energiaMax = energiaMax
        self.energia = energiaMax
        self.saciedadeMax = saciedadeMax
        self.saciedade = saciedadeMax
        self.limpezaMax = limpezaMax
        self.limpeza = limpezaMax
        self.idadeMax = idadeMax
        self.diamantes = 0
        self.idade = 0

    def getEnergiaMax(self):
        return self.energiaMax

    def getSaciedadeMax(self):
        return self.saciedadeMax

    def getLimpezaMax(self):
        return self.limpezaMax

    def getIdadeMax(self):
        return self.idadeMax

    def getEnergiaAtual(self):
        return self.energia

    def getSaciedadeAtual(self):
        return self.saciedade

    def getLimpezaAtual(self):
        return self.limpeza

    def getIdadeAtual(self):
        return self.idade

    def getDiamantes(self):
        return self.diamantes

    def getEstaVivo(self):
        if self.energia <= 0:
            self.energia = 0
            return False

        elif self.limpeza <= 0:
            self.limpeza = 0
            return False

        elif self.saciedade <= 0:
            self.saciedade = 0
            return False

        elif self.idade > self.idadeMax:
            self.idade = self.idadeMax
            return False
        return True

    def brincar(self):
        if self.getEstaVivo():
            self.energia -= 2

            self.saciedade -= 1

            self.limpeza -= 3

            self.idade += 1

            self.diamantes += 1
            return True
        return False

    def comer(self):
        if self.getEstaVivo():
            self.energia -= 1

            if self.saciedadeMax > self.saciedade + 4:
                self.saciedade += 4
            else:
                self.saciedade = self.saciedadeMax

            self.limpeza -= 2

            self.idade += 1
            return True
        return False

    def dormir(self):
        if self.getEstaVivo():
            if self.energiaMax - self.energia >= 5:
                n_turnos = self.energiaMax - self.energia
                self.energia = self.energiaMax

                self.saciedade -= 2

                self.idade += n_turnos

                return True
        return False

    def banhar(self):
        if self.getEstaVivo():
            self.energia -= 3

            self.saciedade -= 1

            self.limpeza = self.limpezaMax

            self.idade += 2

            self.diamantes += 0
            return True
        return False
