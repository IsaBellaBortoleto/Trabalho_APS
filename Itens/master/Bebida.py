#from .Itens.master.Entidade import Entidade
from .Entidade import Entidade
class Bebida(Entidade):

    descricao = ["preco", "capacidade", "imagem"] #colunas q eu posso alterar
    
    def __init__(self):
       pass