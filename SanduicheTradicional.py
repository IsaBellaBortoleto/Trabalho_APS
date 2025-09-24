import pymysql
from Sanduiche import Sanduiche

class SanduicheTradicional(Sanduiche):
    def __init__(self):
        pass

    def getpreco(self): #retorno o preço na variável resultado
        # conecta ao MySQL usando pymysql
        conn = pymysql.connect(**self.db_config)
        cursor = conn.cursor()

        # busca preço na tabela
        cursor.execute("SELECT preco FROM sanduiche WHERE id = 1")
        resultado = cursor.fetchone()

        conn.close()

        if resultado:
            print(f"O {self.nome} custa R${resultado[0]:.2f}")
        else:
            print(f"Preço do {self.nome} não encontrado.")

    def getingredientes():
        pass

    def getimagem():
        pass

    def alteraritem(self, coluna, novovalor): #altera a coluna pra novovalor
        if coluna not in self.descricao:
            pass

        conn = pymysql.connect(**self.db_config)
        cursor = conn.cursor()

        atualizacao = f"UPDATE sanduiche SET {coluna} = %s WHERE id = 1"
        cursor.execute(atualizacao, novovalor)
        conn.commit()
        conn.close()


s = SanduicheTradicional("sanduiche simples")
s.exibirpreco()
s.alteraritem("abacaxi", 10.50)
s.exibirpreco()