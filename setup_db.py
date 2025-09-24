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

        #cria tabela sanduiche
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
            'imagem VARCHAR(50), ' 
            'PRIMARY KEY (id) '
            ')'
        )
        cursor.execute(sql)

        sql = (
            'INSERT INTO sanduiche '
            '(nome, preco, pao, proteina, verdura, queijo, extra, imagem) '
            'VALUES (%(nome)s, %(preco)s, %(pao)s, %(proteina)s, %(verdura)s, %(queijo)s, %(extra)s, %(imagem)s) '
        )
        dados = (
        {  "nome" : "sanduíche tradicional", 
            "preco" : 10.50,
            "pao" : "branco",
            "proteina" : "carne", 
            "verdura" : "alface",
            "queijo" : "mussarela",
            "extra" : "maionese",
            "imagem" : "sandu.jpg" } ,

        {  "nome" : "sanduíche chicken", 
            "preco" : 12.50,
            "pao" : "integral",
            "proteina" : "frango", 
            "verdura" : "pepino",
            "queijo" : "mussarela",
            "extra" : "ketchup", 
            "imagem" : "sandu.jpg" },
        
        {  "nome" : "sanduíche fish", 
            "preco" : 15.50,
            "pao" : "branco",
            "proteina" : "peixe", 
            "verdura" : "tomate",
            "queijo" : "branco",
            "extra" : "mostasda", 
            "imagem" : "sandu.jpg" },
        )
        cursor.executemany(sql, dados)

        #cria tabela bebida
        cursor.execute('DROP TABLE bebida')

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

        #cria tabela milkshake
        cursor.execute('DROP TABLE milkshake')

        sql = (
            'CREATE TABLE IF NOT EXISTS milkshake ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'preco DECIMAL(10,2) NOT NULL, '
            'principal VARCHAR(50), '
            'leite VARCHAR(50), '
            'cobertura VARCHAR(50), '
            'capacidade VARCHAR(50), '
            'imagem VARCHAR(50), ' 
            'PRIMARY KEY (id) '
            ')'
        )
        cursor.execute(sql)

        sql = (
            'INSERT INTO milkshake '
            '(nome, preco, principal, leite, cobertura, capacidade, imagem) '
            'VALUES (%(nome)s, %(preco)s, %(principal)s, %(leite)s, %(cobertura)s, %(capacidade)s, %(imagem)s) '
        )
        dados = (
        {
            "nome" : "milkshake moranguete",
            "preco" : 15.00,
            "principal" : "morango",
            "leite" : "normal",
            "cobertura" : "não",
            "capacidade" : "300 ml",
            "imagem" : "teste.jpg" } ,
        {
            "nome" : "milkshake moranguete",
            "preco" : 19.00,
            "principal" : "morango",
            "leite" : "normal",
            "cobertura" : "não",
            "capacidade" : "500 ml",
            "imagem" : "teste.jpg" } ,
        {
            "nome" : "milkshake chocolatudo",
            "preco" : 15.00,
            "principal" : "chocolate",
            "leite" : "desnatado",
            "cobertura" : "não",
            "capacidade" : "300 ml",
            "imagem" : "teste.jpg" } , 
        {
            "nome" : "milkshake chocolatudo",
            "preco" : 19.00,
            "principal" : "chocolate",
            "leite" : "desnatado",
            "cobertura" : "não",
            "capacidade" : "500 ml",
            "imagem" : "teste.jpg" } ,       
        {
            "nome" : "milkshake de kitkat",
            "preco" : 20.00,
            "principal" : "baunilha e chocolate",
            "leite" : "normal",
            "cobertura" : "kitkat",
            "capacidade" : "300 ml",
            "imagem" : "teste.jpg" } ,
        {
            "nome" : "milkshake de kitkat",
            "preco" : 25.00,
            "principal" : "baunilha com chocolate e kitkat",
            "leite" : "normal",
            "cobertura" : "kitkat",
            "capacidade" : "500 ml",
            "imagem" : "teste.jpg" } ,
        )
        cursor.executemany(sql, dados)

        #cria tabela pizza 

        cursor.execute('DROP TABLE pizza')

        sql = (
            'CREATE TABLE IF NOT EXISTS pizza ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'preco DECIMAL(10,2) NOT NULL, '
            'principal VARCHAR(50), '
            'massa VARCHAR(50), '
            'queijo VARCHAR(50), '
            'borda VARCHAR(50), '
            'imagem VARCHAR(50), ' 
            'PRIMARY KEY (id) '
            ')'
        )
        cursor.execute(sql)

        sql = (
            'INSERT INTO pizza '
            '(nome, preco, principal, massa, queijo, borda, imagem) '
            'VALUES (%(nome)s, %(preco)s, %(principal)s, %(massa)s, %(queijo)s, %(borda)s, %(imagem)s) '
        )   

        dados = (
        {
            "nome" : "pizza de calabresa",
            "preco" : 35.50,
            "principal" : "calabresa",
            "massa" : "tradicional",
            "queijo" : "mussarela",
            "borda" : "sim",
            "imagem" : "teste.jpg"  },
        {
            "nome" : "pizza de ricota e brocolis",
            "preco" : 40.50,
            "principal" : "ricota e brocolis",
            "massa" :"sem gluten",
            "queijo" : "branco",
            "borda" : "nao",
            "imagem" : "teste.jpg"  },
        {
            "nome" : "pizza de frango com catupiry",
            "preco" : 31.25,
            "principal" : "frango com catupiry",
            "massa" : "tradicional",
            "queijo" : "mussarela",
            "borda" : "sim",
            "imagem" : "teste.jpg"  },
        )

        cursor.executemany(sql, dados)

        #cria tabela hotdog

        cursor.execute('DROP TABLE hotdog')
        
        sql = (
            'CREATE TABLE IF NOT EXISTS hotdog ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'preco DECIMAL(10,2) NOT NULL, '
            'principal VARCHAR(50), '
            'ketchup VARCHAR(50), '
            'mostarda VARCHAR(50), '
            'batata_palha VARCHAR(50), '
            'vinagrete VARCHAR(50), '
            'imagem VARCHAR(50), ' 
            'PRIMARY KEY (id) '
            ')'
        )
        cursor.execute(sql)

        sql = (
            'INSERT INTO hotdog '
            '(nome, preco, principal, ketchup, mostarda, batata_palha, vinagrete, imagem) '
            'VALUES (%(nome)s, %(preco)s, %(principal)s, %(ketchup)s, %(mostarda)s, %(batata_palha)s, %(vinagrete)s, %(imagem)s) '
        )   

        dados = (
            {
                "nome" : "cachorro quente tradicional",
                "preco" : 9.90,
                "principal" : "1 salsicha",
                "ketchup" : "sim",
                "mostarda" : "sim",
                "batata_palha" : "sim",
                "vinagrete" : "sim",
                "imagem" : "teste.png"
            },
            {
                "nome" : "cachorro quente não tradicional",
                "preco" : 9.90,
                "principal" : "2 salsicha",
                "ketchup" : "não",
                "mostarda" : "sim",
                "batata_palha" : "sim",
                "vinagrete" : "não",
                "imagem" : "teste.png"
            },
            {
                "nome" : "cachorro quente frango",
                "preco" : 9.90,
                "principal" : "1 salsicha de frango",
                "ketchup" : "sim",
                "mostarda" : "não",
                "batata_palha" : "não",
                "vinagrete" : "sim",
                "imagem" : "teste.png"
            }
        )
        cursor.executemany(sql, dados)
    connection.commit()