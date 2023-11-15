from src.contato import Contato
from src.identificador import Identificador


class Agenda:
    def __init__(self):
        self.contatos = []

    def getContatos(self) -> list:
        names = sorted([contato.getName() for contato in self.contatos])
        contato_em_ordem = []
        for name in names:
            for contato in self.contatos:
                if name == contato.getName():
                    contato_em_ordem.append(contato)
        return contato_em_ordem

    def getQuantidadeDeContatos(self) -> int:
        return len(self.contatos)

    def getContato(self, nome: str) -> Contato:
        for contato in self.getContatos():
            if contato.getName() == nome:
                return contato
        return None

    def adicionarContato(self, contato: Contato) -> bool:
        if len(self.contatos) > 0:
            ha_ctt = False
            for contato_lista in self.contatos:
                if contato_lista.getName() == contato.getName():
                    for fone in contato.getFones():
                        contato_lista.adicionarFone(fone)
                    ha_ctt = True

            if ha_ctt:
                return False
            else:
                self.contatos.append(contato)
                return True
        else:
            self.contatos.append(contato)
            return True

    def removerContato(self, nome: str) -> bool:
        for contato in self.getContatos():
            if contato.getName() == nome:
                self.contatos.remove(contato)
                return True
        return False

    def removerFone(self, nome: str, index: int) -> bool:
        for contato in self.contatos:
            if contato.getName() == nome:
                if contato.getQuantidadeFones() > index - 1:
                    contato.removerFone(index)
                    return True
        return False

    def getQuantidadeDeFonesPorIdentificador(self, identificador: Identificador) -> int:
        qtd = 0
        for contato in self.contatos:
            for fone in contato.getFones():
                if fone.getIdentificador() == identificador:
                    qtd += 1
        return qtd

    def getQuantidadeDeFones(self) -> int:
        qtd = 0
        for contato in self.contatos:
            qtd += contato.getQuantidadeFones()

        return qtd

    def pesquisar(self, expressao: str) -> list:
        resultado = []
        for contato in self.contatos:
            if expressao in contato.getName():
                resultado.append(contato)
            for fone in contato.getFones():
                if expressao in fone.getNumero():
                    resultado.append(contato)

        names = sorted([contato.getName() for contato in resultado])
        resultado_em_ordem = []
        for name in names:
            for contato in resultado:
                if name == contato.getName():
                    resultado_em_ordem.append(contato)
        return resultado_em_ordem
