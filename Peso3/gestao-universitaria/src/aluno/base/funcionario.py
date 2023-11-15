class Funcionario:
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def getNome(self) -> str:
        return self.nome

    def getCpf(self) -> str:
        return self.cpf

    def getSalario(self) -> float:
        return self.salario

    def getTipo(self):
        return self.tipo

    def getClasse(self):
        return self.classe

    def getInsalubre(self):
        return self.insalubre

    def getNivel(self):
        return self.nivel