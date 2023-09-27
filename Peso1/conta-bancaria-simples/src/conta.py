class Conta:
    def __init__(self, numero:int, saldo:float):
        self.limite = 100
        self.extrato = []
        self.numero = numero
        self.saldo = saldo + self.limite

    def getNumero(self):
        return self.numero

    def getSaldo(self):
        return self.saldo

    def getLimite(self):
        return self.limite

    def sacar(self, valor: float):
        if valor > 0:
            if valor > self.saldo:
                print('Não é possível realizar a operação')
            else:
                if valor > self.saldo - self.limite:
                    self.limite = self.saldo - valor
                    self.saldo -= valor
                    self.extrato.append(-valor)
                    return True
                else:
                    self.saldo -= valor
                    self.extrato.append(-valor)
                    return True
        else:
            print('Não é possível realizar a operação')

    def depositar(self, valor: float):
        if valor > 0:
            if (self.limite+valor) < 100:
                self.limite = valor
                self.saldo += valor
                self.extrato.append(+valor)
                return True
            elif (self.limite+valor) >= 100:
                self.limite = 100
                self.saldo += valor
                self.extrato.append(+valor)
                return True
        else:
            print('Não é possível realizar a operação')

    def transferir(self, destino, valor:float):
        if destino:
            if valor < 0:
                print('Transferir valores negativos nao e permitido')
            else:
                if valor < self.saldo - self.limite:
                    destino.depositar(valor)
                    self.saldo -= valor
                    self.extrato.append(-valor)
                    return True
                elif self.saldo - self.limite < valor < self.saldo:
                    destino.depositar(valor)
                    self.limite = self.saldo - valor
                    self.saldo -= valor
                    self.extrato.append(-valor)
                    return True
        else:
            print('Não é possível realizar a operação')

    def verExtrato(self):
        return self.extrato