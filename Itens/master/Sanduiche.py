from Entidade import Entidade

class Sanduiche(Entidade):

    descricao = ["preco", "pao", "proteina", "verdura", "queijo", "extra", "imagem"] #colunas q eu posso alterar
    ingredientes = ["pao", "proteina", "verdura", "queijo", "extra"]
    
    def __init__(self):
       pass