from SanduicheTradicional import SanduicheTradicional
from SanduicheChicken import SanduicheChicken
from SanduicheFish import SanduicheFish
from MilkshakeMoranguete import MilshakeMoranguete
from MilkshakeChocolatudo import MilshakeChocolatudo
from MilkshakeKitKat import MilshakeKitKat
from PizzaCalabresa import PizzaCalabresa
from PizzaRicota import PizzaRicota
from PizzaFrango import PizzaFrango
from HotDogTradicional import HotDogTradicional
from HotDogNaoTradicional import HotDogNaoTradicional
from HotDogFrango import HotDogFrango
from CocaCola import CocaCola
from SucoVale import SucoVale
from Guarana import Guarana

class Carrinho():
    def __init__(self):
        self.itens = []

    def incluiritem(self, item):
        self.itens.append(item)

    def removeritem(self, item):
        if item in self.itens:
            self.itens.remove(item)

    def exibirtodositens(self):
        return self.itens
    
    def limpar(self):
        self.itens.clear()

    def somatotal(self):
        return sum(i.getpreco() for i in self.itens)
    

    

