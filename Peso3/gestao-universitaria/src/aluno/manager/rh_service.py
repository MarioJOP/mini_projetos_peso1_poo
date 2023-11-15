from src.aluno.base.funcionario import Funcionario
from src.cliente.irh_service import IRHService
from src.cliente.tipo import Tipo

class RHService(IRHService):
    def __init__(self):
        self.funcionarios = []
        self.diarias = {}
        self.partilha = 0

    def cadastrar(self, funcionario: Funcionario):
        if funcionario.getTipo() == Tipo.PROF:
            if funcionario.getClasse() not in ['A', 'B', 'C', 'D', 'E']:
                return False
        if funcionario.getTipo() == Tipo.STA:
            if funcionario.getNivel() not in range(1, 31):
                return False
        for cpf in [funcionario_cadastrado.getCpf() for funcionario_cadastrado in self.funcionarios]:
            if cpf == funcionario.getCpf():
                return False

        self.funcionarios.append(funcionario)
        return True

    def remover(self, cpf: str):
        for funcionario in self.funcionarios:
            if funcionario.getCpf() == cpf:
                self.funcionarios.remove(funcionario)
                return True
        return False

    def obterFuncionario(self, cpf: str):
        for funcionario in self.funcionarios:
            if funcionario.getCpf() == cpf:
                return funcionario
        return None

    def getFuncionarios(self):
        nomes_ordem = sorted([funcionario.getNome() for funcionario in self.funcionarios])
        funcionarios_ordem = []
        for nome in nomes_ordem:
            for funcionario in self.funcionarios:
                if nome == funcionario.getNome():
                    funcionarios_ordem.append(funcionario)
        return funcionarios_ordem

    def getFuncionariosPorCategorias(self, tipo):
        funcionarios_categoria = []
        for funcionario in self.funcionarios:
            if funcionario.getTipo() == tipo:
                funcionarios_categoria.append(funcionario)

        nomes_ordem = sorted([funcionario.getNome() for funcionario in funcionarios_categoria])
        funcionarios_categoria_ordem = []
        for nome in nomes_ordem:
            for funcionario in funcionarios_categoria:
                if nome == funcionario.getNome():
                    funcionarios_categoria_ordem.append(funcionario)
        return funcionarios_categoria_ordem

    def getTotalFuncionarios(self):
        return len(self.funcionarios)

    def solicitarDiaria(self, cpf: str):
        for funcionario in self.funcionarios:
            if funcionario.getCpf() == cpf:
                if funcionario.getTipo() == Tipo.TERC:
                    return False
                if funcionario.getNome() in self.diarias.keys():
                    if funcionario.getTipo() == Tipo.PROF:
                        if self.diarias[funcionario.getNome()] < 3:
                            funcionario.salario += 100
                            self.diarias[funcionario.getNome()] += 1
                            return True
                        else:
                            return False
                    elif funcionario.getTipo() == Tipo.STA:
                        return False
                else:
                    self.diarias[funcionario.getNome()] = 1
                    funcionario.salario += 100
                    return True

        return False

    def partilharLucros(self, valor: float):
        self.partilha = valor/self.getTotalFuncionarios()
        if len(self.funcionarios) == 0:
            return False
        for funcionario in self.funcionarios:
            funcionario.salario += self.partilha
        return True

    def iniciarMes(self):
        self.diarias.clear()
        for funcionario in self.funcionarios:
            funcionario.salario -= self.partilha
        return True

    def calcularSalarioDoFuncionario(self, cpf: str):
        for funcionario in self.funcionarios:
            if funcionario.getCpf() == cpf:
                return funcionario.getSalario()
        return None

    def calcularFolhaDePagamento(self):
        return sum([funcionario.getSalario() for funcionario in self.funcionarios])
