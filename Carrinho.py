""" import pymysql
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
 """
from Itens.master.Guarana import Guarana
from Itens.master.CocaCola import CocaCola
from Itens.master.HotDogFrango import HotDogFrango
from Itens.master.HotDogTradicional import HotDogTradicional
from Itens.master.HotDogNaoTradicional import HotDogNaoTradicional
from Itens.master.MilkshakeChocolatudo import MilshakeChocolatudo
from Itens.master.MilkshakeKitKat import MilshakeKitKat
from Itens.master.MilkshakeMoranguete import MilshakeMoranguete
from Itens.master.PizzaCalabresa import PizzaCalabresa
from Itens.master.PizzaFrango import PizzaFrango
from Itens.master.PizzaRicota import PizzaRicota
from Itens.master.SanduicheChicken import SanduicheChicken
from Itens.master.SanduicheFish import SanduicheFish
from Itens.master.SanduicheTradicional import SanduicheTradicional
from Itens.master.SucoVale import SucoVale
import pymysql;
class Carrinho():
    def __init__(self):
        self.itens = []
        self.mesa

    def incluiritem(self, item):
        self.itens.append(item)

    def removeritem(self, item):
        if item in self.itens:
            self.itens.remove(item)

    #retorna informações de cada item na lista
    def exibirtodositens(self):
        for i in self.itens:
            return i.executar()
    
    def limpar(self):
        self.itens.clear()

    def somatotal(self):
        return sum(i.getpreco() for i in self.itens)
    
    def finalizarpedido(self, mesa, pedido, nota):
        
        conn = pymysql.connect(**self.db_config)
        cursor = conn.cursor()

        insercao = (
            'INSERT INTO pedidos '
            '(mesa, pedido, nota, status) '
            'VALUES (%(mesa)s, %(pedido)s, %(nota)s, %(status)s) ' 
        )

        cursor.execute(insercao, mesa, pedido, nota, "Recebido")
        conn.commit()
        conn.close()
        
        soma = self.somatotal()
        self.limpar()
        return soma
        

        
    

    

