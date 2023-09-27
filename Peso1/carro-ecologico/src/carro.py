class Carro:

    def __init__(self):
        self.tanque = 0
        self.passageiros = 0
        self.quilometragem = 0

    def getPassageiros(self):
        return self.passageiros

    def getCombustivel(self):
        return self.tanque

    def getQuilometragem(self):
        return self.quilometragem

    def embarcar(self):
        if self.passageiros < 2:
            print('Embarcando uma pessoa')
            self.passageiros += 1
            return True
        else:
            print('Não é possível embarcar')
            return False

    def desembarcar(self):
        if self.passageiros == 0:
            print('Sem passageiros')
            return False
        else:
            print('Desembarcando um passageiro')
            self.passageiros -= 1
            return True

    def dirigir(self, distancia):
        if distancia <= self.tanque:
            if self.passageiros > 0 and self.tanque > 0:
                self.quilometragem += distancia
                self.tanque -= distancia
                return True
            if self.passageiros > 0 and self.tanque == 0:
                print('Sem combustível')
                return False
        else:
            if self.passageiros > 0:
                self.quilometragem += self.tanque
                self.tanque = 0
                print(f'Acabou o combustivel. Foram percorridos {self.quilometragem}km')
                return False

    def abastecer(self, quantidade):
        if quantidade > 0:
            if self.tanque == 0:
                if quantidade <= 100:
                    self.tanque = quantidade
                    return True
                else:
                    self.tanque = 100
                    return True
            else:
                if self.tanque+quantidade >= 100:
                    self.tanque = 100
                    return True
                else:
                    self.tanque += quantidade
                    return True
        else:
            print('quantidade invalida')
            return False