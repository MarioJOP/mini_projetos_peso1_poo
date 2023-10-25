from src.crianca import Crianca


class PulaPula:

    def __init__(self, limiteMax):
        self.limiteMax = limiteMax
        self.filaEspera = []
        self.criancasPulando = []
        self.caixa = 0
        self.conta = {}

    def getFilaDeEspera(self):
        return self.filaEspera

    def getCriancasPulando(self):
        return self.criancasPulando

    def getLimiteMax(self):
        return self.limiteMax

    def getCaixa(self):
        return self.caixa

    def getConta(self, nome):
        # 'nome' está no dicionário
        if nome in self.conta.keys():
            # Criança esta pulando
            for crianca_pulando in self.criancasPulando:
                if crianca_pulando.getNome() == nome:
                    return self.conta[nome]
            # Criança esta na fila
            for crianca_fila in self.filaEspera:
                if crianca_fila.getNome() == nome:
                    return self.conta[nome]
            return False
        # 'nome' não está no dicionário
        return None

    def entrarNaFila(self, crianca: Crianca):
        # A fila nao esta vazia
        if len(self.filaEspera) > 0:
            ha_nome_fila = False
            for crianca_fila in self.filaEspera:
                # Verifica se ha crianca na fila com mesmo nome
                if crianca.getNome() == crianca_fila.getNome():
                    ha_nome_fila = True

            if not ha_nome_fila:
                self.filaEspera.append(crianca)
                return True
            # Há uma criança com mesmo nome na fila
            return False

        # A fila esta vazia
        else:
            self.filaEspera.append(crianca)
            return True

    def entrar(self):
        # Há espaço
        if len(self.filaEspera) > 0:
            if self.limiteMax - len(self.criancasPulando) > 0:
                self.caixa += 2.5
                # Incrementa 2.5 na conta se a conta ja foi criada
                if self.filaEspera[0].getNome() in self.conta.keys():
                    self.conta[self.filaEspera[0].getNome()] += 2.5
                # Cria a conta adicionando o primeiro valor
                else:
                    self.conta[self.filaEspera[0].getNome()] = 2.5
                self.criancasPulando.append(self.filaEspera[0])
                self.filaEspera.pop(0)
                return True
        #Não há espaço
        return False

    def sair(self):
        if len(self.criancasPulando) > 0:
            # Coloca na fila a primeira crianca que entrou no pula pula -> a que entrou a mais tempo (ultima posicao)
            self.filaEspera.append(self.criancasPulando[-1])
            self.criancasPulando.pop(-1)
            return True
        # Sem crianças pulando
        return False

    def papaiChegou(self, nome):
        for crianca_pulando in self.criancasPulando:
            # Crianca esta pulando
            if crianca_pulando.getNome() == nome:
                self.criancasPulando.remove(crianca_pulando)
                return True

        for crianca_na_fila in self.filaEspera:
            # Crianca esta na fila
            if crianca_na_fila.getNome() == nome:
                self.filaEspera.remove(crianca_na_fila)
                return True

        # Crianca nao esta pulando e nao esta na lista
        return False

    def fechar(self):
        self.criancasPulando.clear()
        self.filaEspera.clear()
        self.conta.clear()
        return True