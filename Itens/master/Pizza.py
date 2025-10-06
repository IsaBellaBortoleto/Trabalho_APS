from.Entidade import Entidade

class Pizza(Entidade):

    descricao = ["preco", "principal", "massa", "queijo", "borda", "imagem"] #colunas q eu posso alterar
    ingredientes = ["principal", "massa", "queijo", "borda"]
    
    def __init__(self):
       pass