from src.cliente.icirculo_operations_manager import ICirculoOperationsManager
from src.cliente.icirculos_manager import ICirculosManager
from src.cliente.icontatos_manager import IContatosManager
from src.aluno.base.contato import Contato
from src.aluno.base.circulo import Circulo
from src.cliente.circulo_not_found_exception import CirculoNotFoundException
from src.cliente.contato_not_found_exception import ContatoNotFoundException


class GContatos(IContatosManager, ICirculosManager, ICirculoOperationsManager):
    def __init__(self):
        self.circulos = []
        self.contatos = []
        self.favoritos = []

    def createContact(self, id: str, email: str) -> bool:
        for contato in self.contatos:
            if contato.getId() == id:
                return False
        self.contatos.append(Contato(id, email))
        return True

    def getAllContacts(self) -> list:
        return sorted(self.contatos, key=lambda f: f.getId())

    def updateContact(self, contato: Contato) -> bool:
        for contato_lista in self.contatos:
            if contato.id == contato_lista.id:
                contato_lista.email = contato.email
                return True
        return False

    def removeContact(self, id: str) -> bool:
        for contato in self.contatos:
            if contato.getId() == id:
                self.contatos.remove(contato)
                for circle in self.circulos:
                    for ctt in circle.ctt_circle:
                        if ctt.getId() == id:
                            circle.ctt_circle.remove(ctt)
                if contato in self.favoritos:
                    self.favoritos.remove(contato)
                return True
        return False

    def getContact(self, id: str) -> Contato:
        for contato in self.contatos:
            if contato.getId() == id:
                return contato
        return None

    def getNumberOfContacts(self) -> int:
        return len(self.contatos)

    def favoriteContact(self, idContato: str) -> bool:
        for contato in self.contatos:
            if contato.getId() == idContato:
                self.favoritos.append(contato)
                return True
        return False


    def unfavoriteContact(self, idContato: str) -> bool:
        for contato in self.contatos:
            if contato.getId() == idContato:
                self.favoritos.remove(contato)
                return True
        return False

    def isFavorited(self, id: str) -> bool:
        if id in [ctt.getId() for ctt in self.favoritos]:
            return True
        return False

    def getFavorited(self) -> list:
        return sorted(self.favoritos, key=lambda f: f.getId())

    def createCircle(self, id: str, limite: int) -> bool:
        for circle in self.circulos:
            if circle.getId() == id:
                return False
        self.circulos.append(Circulo(id, limite))
        return True

    def updateCircle(self, circulo: Circulo) -> bool:
        if circulo.getLimite() <= 0:
            return False

        for circle in self.circulos:
            if circle.getId() == circulo.getId():
                circle.limite = circulo.getLimite()
                return True
        return False

    def getCircle(self, idCirculo: str) -> Circulo:
        for circle in self.circulos:
            if circle.getId() == idCirculo:
                return circle
        return None

    def getAllCircles(self) -> list:
        return sorted(self.circulos, key=lambda f: f.getId())

    def removeCircle(self, idCirculo: str) -> bool:
        for circle in self.circulos:
            if circle.getId() == idCirculo:
                self.circulos.remove(circle)
                return True
        return False

    def getNumberOfCircles(self) -> int:
        return len(self.circulos)


    def tie(self, idContato: str, idCirculo: str) -> bool:
        if idCirculo not in [circle.id for circle in self.circulos]:
            raise CirculoNotFoundException(idCirculo)

        if idContato not in [ctt.getId() for ctt in self.contatos]:
            raise ContatoNotFoundException(idContato)

        for circle in self.circulos:
            if circle.getId() == idCirculo and circle.getLimite() > circle.getNumberOfContacts():
                for ctt in self.contatos:
                    if ctt.getId() == idContato and ctt not in circle.ctt_circle:
                        circle.ctt_circle.append(ctt)
                        return True
        return False

    def untie(self, idContato: str, idCirculo: str) -> bool:
        if idCirculo not in [circle.id for circle in self.circulos]:
            raise CirculoNotFoundException(idCirculo)

        if idContato not in [ctt.getId() for ctt in self.contatos]:
            raise ContatoNotFoundException(idContato)

        for circle in self.circulos:
            if circle.getId() == idCirculo:
                for ctt in circle.ctt_circle:
                    if ctt.getId() == idContato:
                        circle.ctt_circle.remove(ctt)
                        return True
        return False

    def getContacts(self, id: str) -> list:
        if id not in [circle.id for circle in self.circulos]:
            raise CirculoNotFoundException(id)

        for circle in self.circulos:
            if circle.getId() == id:
                return sorted(circle.ctt_circle, key=lambda f: f.getId())
        return None

    def getCircles(self, id: str) -> list:
        if id not in [ctt.getId() for ctt in self.contatos]:
            raise ContatoNotFoundException(id)
        circles = []

        for circle in self.circulos:
            for ctt in circle.ctt_circle:
                if ctt.getId() == id:
                    circles.append(circle)
        return sorted(circles, key=lambda f: f.getId())

    def getCommomCircle(self, idContato1: str, idContato2: str) -> list:
        if idContato1 not in [ctt.getId() for ctt in self.contatos]:
            raise ContatoNotFoundException(idContato1)

        if idContato2 not in [ctt.getId() for ctt in self.contatos]:
            raise ContatoNotFoundException(idContato2)
        commom_circles = []
        for circle1 in self.getCircles(idContato1):
            for circle2 in self.getCircles(idContato2):
                if circle1 == circle2:
                    commom_circles.append(circle1)
        return sorted(commom_circles, key=lambda f: f.getId())
