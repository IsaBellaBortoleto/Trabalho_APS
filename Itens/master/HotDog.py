from Entidade import Entidade

class HotDog(Entidade):

    descricao = ["preco", "principal", "ketchup", "mostarda", "batata_palha", "vinagrete", "imagem"] #colunas q eu posso alterar
    ingredientes = ["principal", "ketchup", "mostarda", "batata_palha", "vinagrete"]
    
    def __init__(self):
       pass