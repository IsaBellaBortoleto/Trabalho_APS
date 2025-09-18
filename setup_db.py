import pymysql

connection = pymysql.connect(
    host='localhost',          
    user='usuario_python',  
    password='senha123',      
    charset= 'utf8mb4'  
)

with connection :
    with connection.cursor() as cursor : 
        #cria o banco

        sql = ("CREATE DATABASE IF NOT EXISTS cardapio_digital")
        cursor.execute(sql)

        #seleciona o banco que vai usar
        sql = ("USE cardapio_digital")
        cursor.execute(sql)

        cursor.execute('DROP TABLE sanduiche')

        #cria tabelas
        sql = (
            'CREATE TABLE IF NOT EXISTS sanduiche ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'preco DECIMAL(10,2) NOT NULL, '
            'pao VARCHAR(50), '
            'proteina VARCHAR(50), '
            'verdura VARCHAR(50), ' 
            'queijo VARCHAR(50), '
            'extra VARCHAR(50), ' 
            'PRIMARY KEY (id) '
            ')'
        )
        cursor.execute(sql)

        sql = (
            'INSERT INTO sanduiche '
            '(nome, preco, pao, proteina, verdura, queijo, extra) '
            'VALUES (%(nome)s, %(preco)s, %(pao)s, %(proteina)s, %(verdura)s, %(queijo)s, %(extra)s) '
        )
        dados = (
        {  "nome" : "sanduíche simples", 
            "preco" : 10.50,
            "pao" : "branco",
            "proteina" : "carne", 
            "verdura" : "alface",
            "queijo" : "mussarela",
            "extra" : "maionese", } ,

        {  "nome" : "sanduíche chicken", 
            "preco" : 12.50,
            "pao" : "integral",
            "proteina" : "frango", 
            "verdura" : "pepino",
            "queijo" : "mussarela",
            "extra" : "ketchup", },
        
        {  "nome" : "sanduíche fish", 
            "preco" : 15.50,
            "pao" : "branco",
            "proteina" : "peixe", 
            "verdura" : "tomate",
            "queijo" : "branco",
            "extra" : "mostasda", },
        )
        cursor.executemany(sql, dados)

        sql = (
            'CREATE TABLE IF NOT EXISTS bebida ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'capacidade VARCHAR(10), '
            'preco DECIMAL(10,2) NOT NULL, '
            'PRIMARY KEY (id) '
            ')'
        )
        cursor.execute(sql)

        sql = (
            'INSERT INTO bebida '
            '(nome, preco, capacidade) '
            'VALUES (%(nome)s, %(preco)s, %(capacidade)s) '
        )
        dados = (
        {   "nome" : "Coca-Cola",
            "preco" : 4.50,
            "capacidade" : "200ml", },
        {   "nome" : "Suco Vale",
            "preco" : 5.50,
            "capacidade" : "200ml", },
        {   "nome" : "Guaraná",
            "preco" : 8.00,
            "capacidade" : "1L", },
        )
        cursor.executemany(sql, dados)
                
    connection.commit()