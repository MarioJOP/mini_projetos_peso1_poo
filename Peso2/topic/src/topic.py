from src.passageiro import Passageiro


class Topic():
    def __init__(self, capacidade: int, qtdPrioritarios):
        if qtdPrioritarios > capacidade:
            raise ValueError('qtdPrioritarios maior que capacidade')
        self.capacidade = capacidade
        self.qtdPrioritarios = qtdPrioritarios
        self.assentosNormais = []
        self.assentosPrioritarios = []
        self.vagas_disponiveis = self.capacidade - (len(self.assentosPrioritarios) + len(self.assentosNormais))

    def getNumeroAssentosPrioritarios(self):
        return self.qtdPrioritarios

    def getNumeroAssentosNormais(self):
        return self.capacidade - self.qtdPrioritarios

    def getPassageiroAssentoNormal(self, lugar):
        if len(self.assentosNormais) == 0:
            return None
        return self.assentosNormais[lugar]

    def getPassageiroAssentoPrioritario(self, lugar):
        if len(self.assentosPrioritarios) == 0:
            return None
        return self.assentosPrioritarios[lugar]

    def getVagas(self):
        return self.vagas_disponiveis

    def subir(self, passageiro: Passageiro):
        # Há vagas
        if self.getVagas() > 0:
            # Prioritario -> verifica se há assentos prioritarios, caso nao haja, adiciona em assentos normais
            if passageiro.ePrioridade():
                if self.getNumeroAssentosPrioritarios() > len(self.assentosPrioritarios):
                    self.assentosPrioritarios.append(passageiro)
                    self.vagas_disponiveis -= 1
                    return True
                else:
                    self.assentosNormais.append(passageiro)
                    self.vagas_disponiveis -= 1
                    return True
            # Não prioritario -> verifica se há assentos normais, caso nao haja, adiciona em assentos prioritarios
            else:
                if self.getNumeroAssentosNormais() > len(self.assentosNormais):
                    self.assentosNormais.append(passageiro)
                    self.vagas_disponiveis -= 1
                    return True
                else:
                    self.assentosPrioritarios.append(passageiro)
                    self.vagas_disponiveis -= 1
                    return True
        # Não há vagas
        return False

    def descer(self, nome):
        for passageiro_prioritario in self.assentosPrioritarios:
            if passageiro_prioritario.getNome() == nome:
                self.assentosPrioritarios.remove(passageiro_prioritario)
                self.vagas_disponiveis += 1
                return True

        for passageiro_normal in self.assentosNormais:
            if passageiro_normal.getNome() == nome:
                self.assentosNormais.remove(passageiro_normal)
                self.vagas_disponiveis += 1
                return True
        # Não esta na topic
        return False



    def toString(self):
        topic = '['
        for passageiro_prioritario in self.assentosPrioritarios:
            topic += '@' + passageiro_prioritario.getNome() + ' '
        topic += '@ ' * (self.qtdPrioritarios - len(self.assentosPrioritarios))

        for passageiro_normal in self.assentosNormais:
            topic += '=' + passageiro_normal.getNome() + ' '
        topic += '= ' * (self.getNumeroAssentosNormais() - len(self.assentosNormais))
        return topic + ']'
