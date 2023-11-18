class Espiral:
    def __init__(self):
        self.nomeProduto = ' - '
        self.qtdProdutos = 0
        self.preco = 0

    def getNomeDoProduto(self):
        return self.nomeProduto

    def setNomeDoProduto(self, nome: str):
        self.nomeProduto = nome

    def getQuantidade(self) -> int:
        return self.qtdProdutos

    def setQuantidade(self, qtd: int):
        self.qtdProdutos = qtd

    def getPreco(self) -> float:
        return self.preco

    def setPreco(self, preco: float):
        self.preco = preco

    def limpar(self):
        self.nomeProduto, self.qtdProdutos, self.preco = ' - ', 0, 0