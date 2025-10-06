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


produto_guarana=Guarana()
preco_guarana=produto_guarana.getpreco()
nome_guarana = produto_guarana.getnome()

produto_cocacola=CocaCola()
produto_hotdogfrango=HotDogFrango()
produto_hotdognaotradicional=HotDogNaoTradicional()
produto_hotdogtradicional=HotDogTradicional()
produto_milkshakechocolatudo=MilshakeChocolatudo()
produto_milkshakekitkat=MilshakeKitKat()
produto_milkshakemoranguete=MilshakeMoranguete()
produto_pizzacalabreza=PizzaCalabresa()
produto_pizzafrango=PizzaFrango()
produto_pizzaricota=PizzaRicota()
produto_sanduichechicken=SanduicheChicken()
produto_sanduichefish=SanduicheFish()
produto_sanduichetradicional=SanduicheTradicional()
produto_sucovale=SucoVale()

BEBIDAS_DISPONIVEIS =[
    produto_guarana, produto_cocacola, produto_sucovale
]
PIZZAS_DISPONIVEIS = [
    produto_pizzacalabreza,produto_pizzaricota, produto_pizzafrango
]