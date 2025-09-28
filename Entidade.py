from abc import ABC, abstractmethod

class Entidade(ABC) :
    db_config = {
        "host": "localhost",
        "user": "usuario_python",
        "password": "senha123",
        "database": "cardapio_digital"
    }
        
    def __init__(self):
        pass

    @abstractmethod
    def getpreco(self):
        pass

    @abstractmethod
    def getnome(self):
        pass

    @abstractmethod
    def executar(self):
        pass
    