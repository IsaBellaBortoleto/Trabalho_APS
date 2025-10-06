from .Entidade import Entidade

class Milkshake(Entidade):

    descricao = ["preco", "principal", "leite", "cobertura", "capacidade", "imagem"] #colunas q eu posso alterar
    ingredientes = ["principal", "leite", "cobertura"]

    def __init__(self):
       pass