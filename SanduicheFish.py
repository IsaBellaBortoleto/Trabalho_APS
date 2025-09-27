import pymysql
from Sanduiche import Sanduiche

class SanduicheFish(Sanduiche):
    #construtora
    def __init__(self): 
        pass
    
    #retorna o preço
    def getpreco(self): #retorno o preço na variável resultado
        # conecta ao MySQL usando pymysql
        conn = pymysql.connect(**self.db_config)
        cursor = conn.cursor()

        # busca preço na tabela
        cursor.execute("SELECT preco FROM sanduiche WHERE id = 3")
        resultado = cursor.fetchone()

        conn.close()
        return resultado
    
        #retorna o nome na variável resultado
    def getnome(self):
        conn = pymysql.connect(**self.db_config)
        cursor = conn.cursor()

        cursor.execute("SELECT nome from sanduiche WHERE id = 3")
        resultado = cursor.fetchone()

        conn.close()
        return resultado

    #retorna uma tupla de ingredientes
    def getingredientes(self):
        conn = pymysql.connect(**self.db_config)
        cursor = conn.cursor()

        colunas = ', '.join(self.ingredientes)
        cursor.execute(f"SELECT {colunas} FROM sanduiche WHERE id = 3")
        resultado = cursor.fetchall()

        conn.close()
        return resultado

    #retorna a uma tupla com o caminho da imagem
    def getimagem(self):
        conn = pymysql.connect(**self.db_config)
        cursor = conn.cursor()

        cursor.execute("SELECT imagem FROM sanduiche WHERE id = 3")
        resultado = cursor.fetchone()

        conn.close()
        return resultado

    #altera o valor de alguma coluna
    def alteraritem(self, coluna, novovalor): #altera a coluna pra novovalor
        if coluna not in self.descricao:
            pass

        conn = pymysql.connect(**self.db_config)
        cursor = conn.cursor()

        atualizacao = f"UPDATE sanduiche SET {coluna} = %s WHERE id = 3"
        cursor.execute(atualizacao, novovalor)
        conn.commit()
        conn.close()