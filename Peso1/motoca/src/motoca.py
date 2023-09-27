from src.pessoa import Pessoa


class Motoca:

    def __init__(self, potencia: int):
        self.potencia = potencia
        self.tempo = 0
        self.pessoa = None

    def getPessoa(self):
        return self.pessoa

    def getTempo(self):
        return self.tempo

    def getPotencia(self):
        return self.potencia

    def subir(self, pessoa: Pessoa):
        if self.pessoa:
            print('Já tem uma pessoa na motocicleta')
            return False
        else:
            self.pessoa = pessoa
            return True

    def descer(self):
        if self.pessoa:
            self.pessoa = None
            print('Descendo')
            return True
        else:
            print('Não há pessoas na moto')
            return False

    def colocarTempo(self, tempo: int):
        if tempo > 0:
            self.tempo = tempo
            return True
        else:
            print('Valor de tempo invalido')
            return False

    def dirigir(self, tempo: int):
        if self.pessoa:
            if self.pessoa.getIdade() <= 10 and self.tempo:
                if tempo <= self.tempo:
                    self.tempo = tempo
                    print('Pode dirigir')
                    return True
                else:
                    tempo_andado = tempo - self.tempo
                    self.tempo = 0
                    print(f'O tempo andado foi {tempo_andado}')
                    return True
            else:
                print('Não pode dirigir')
                return False
        else:
            print('Não pode dirigir')
            return False
    def buzinar(self):
        if self.pessoa:
            txt = 'P'
            for i in range(self.potencia):
                txt += 'e'
            txt += 'm'
            return txt
        else:
            return ''