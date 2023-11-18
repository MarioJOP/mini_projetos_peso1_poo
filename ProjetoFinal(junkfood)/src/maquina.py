from src.espiral import Espiral


class Maquina:

    def __init__(self, qtdEspirais: int, maximoProdutos: int):
        self.espirais = [Espiral() for _ in range(qtdEspirais)]
        self.qtdEspirais = qtdEspirais
        self.maxProdutos = maximoProdutos
        self.faturamento = 0
        self.saldo = 0

    def getFaturamento(self) -> float:
        return self.faturamento

    def getMaximoProdutos(self) -> int:
        return self.maxProdutos

    def getSaldoCliente(self) -> float:
        return self.saldo

    def getSizeEspirais(self) -> int:
        return self.qtdEspirais

    def getEspiral(self, indice: int) -> Espiral:
        if 0 < indice <= self.getSizeEspirais() - 1:
            return self.espirais[indice]
        return None

    def inserirDinheiro(self, value: float) -> bool:
        if value > 0:
            self.saldo += value
            return True
        return False

    def receberTroco(self) -> float:
        troco = self.saldo - self.faturamento
        self.saldo = 0
        return troco

    def alterarEspiral(self, indice: int, nome: str, quantidade: int, preco: float) -> bool:
        if quantidade <= self.maxProdutos and 0 <= indice <= self.getSizeEspirais() - 1:
            self.espirais[indice].setNomeDoProduto(nome)
            self.espirais[indice].setPreco(preco)

            self.espirais[indice].setQuantidade(quantidade)
            return True
        return False

    def limparEspiral(self, indice: int) -> bool:
        if 0 <= indice <= self.getSizeEspirais() - 1:
            self.espirais[indice].limpar()
            return True
        return False

    def vender(self, indice: int) -> bool:
        if 0 <= indice <= self.getSizeEspirais() - 1:
            espiral = self.espirais[indice]
            if self.saldo >= espiral.getPreco() and espiral.getQuantidade() > 0:
                espiral.qtdProdutos -= 1
                self.faturamento += espiral.getPreco()
                if espiral.getQuantidade() == 0:
                    self.limparEspiral(indice)
                return True

        return False
