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
            "pao" : "pao branco",
            "proteina" : "carne", 
            "verdura" : "alface",
            "queijo" : "quijo mussarela",
            "extra" : "maionese",
            "imagem" : "SanduicheTradicional.png" } ,

        {  "nome" : "sanduíche chicken", 
            "preco" : 12.50,
            "pao" : "pao integral",
            "proteina" : "frango", 
            "verdura" : "pepino",
            "queijo" : "queijo mussarela",
            "extra" : "ketchup", 
            "imagem" : "SanduicheChicken.png" },
        
        {  "nome" : "sanduíche fish", 
            "preco" : 15.50,
            "pao" : "pao branco",
            "proteina" : "peixe", 
            "verdura" : "tomate",
            "queijo" : "queijo branco",
            "extra" : "mostarda", 
            "imagem" : "SanduicheFish.png" },
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
            'imagem VARCHAR(50), '
            'PRIMARY KEY (id) '
            ')'
        )
        cursor.execute(sql)

        sql = (
            'INSERT INTO bebida '
            '(nome, preco, capacidade, imagem) '
            'VALUES (%(nome)s, %(preco)s, %(capacidade)s, %(imagem)s) '
        )
        dados = (
        {   "nome" : "Coca-Cola",
            "preco" : 6.50,
            "capacidade" : "500ml", 
            "imagem" : "CocaCola.png" },
        {   "nome" : "Suco Vale",
            "preco" : 5.50,
            "capacidade" : "200ml", 
            "imagem" : "SucoVale.png" },
        {   "nome" : "Guaraná",
            "preco" : 8.00,
            "capacidade" : "1L", 
            "imagem" : "Guarana.png" },
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
            "leite" : "leite normal",
            "cobertura" : "sem cobertura",
            "capacidade" : "300 ml",
            "imagem" : "MilkshakeMoranguete.png" } ,
        {
            "nome" : "milkshake chocolatudo",
            "preco" : 19.00,
            "principal" : "chocolate",
            "leite" : "leite desnatado",
            "cobertura" : "cobertura de kitkat",
            "capacidade" : "500 ml",
            "imagem" : "MilkshakeChocolatudo.png" } ,       
        {
            "nome" : "milkshake de kitkat",
            "preco" : 25.00,
            "principal" : "baunilha com chocolate e kitkat",
            "leite" : "leite normal",
            "cobertura" : "cobertura de kitkat",
            "capacidade" : "500 ml",
            "imagem" : "MilkshakeKitKat.png" } ,
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
            "massa" : "massa tradicional",
            "queijo" : "queijo mussarela",
            "borda" : "com borda",
            "imagem" : "PizzaCalabresa.png"  },
        {
            "nome" : "pizza de ricota e brocolis",
            "preco" : 40.50,
            "principal" : "ricota e brocolis",
            "massa" :"massa sem gluten",
            "queijo" : "queijo branco",
            "borda" : "sem borda",
            "imagem" : "PizzaRicota.png"  },
        {
            "nome" : "pizza de frango com catupiry",
            "preco" : 31.25,
            "principal" : "frango com catupiry",
            "massa" : "massa tradicional",
            "queijo" : "queijo mussarela",
            "borda" : "com borda",
            "imagem" : "PizzaFrango.png"  },
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
                "ketchup" : "com ketchup",
                "mostarda" : "com mostarda",
                "batata_palha" : "com batata palha",
                "vinagrete" : "com vinagrete",
                "imagem" : "HotDogTradicional.png"
            },
            {
                "nome" : "cachorro quente não tradicional",
                "preco" : 9.90,
                "principal" : "2 salsicha",
                "ketchup" : "sem ketchup",
                "mostarda" : "com mostarda",
                "batata_palha" : "com batata palha",
                "vinagrete" : "sem vinagrete",
                "imagem" : "HotDogNaoTradicional.png"
            },
            {
                "nome" : "cachorro quente frango",
                "preco" : 9.90,
                "principal" : "1 salsicha de frango",
                "ketchup" : "com ketchup",
                "mostarda" : "sem mostarda",
                "batata_palha" : "sem batata palha",
                "vinagrete" : "com vinagrete",
                "imagem" : "HotDogFrango.png"
            }
        )
        cursor.executemany(sql, dados)

        cursor.execute('DROP TABLE pedidos')

        sql = (
            'CREATE TABLE IF NOT EXISTS pedidos ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'mesa VARCHAR(50) NOT NULL, '
            'pedido VARCHAR(50), '
            'nota VARCHAR(100), '
            'status ENUM("Recebido pela cozinha", "Em preparo", "Finalizando", "Finalizado", "Entregue"), '
            'PRIMARY KEY (id) '
            ')'
        )
        cursor.execute(sql)

        sql = (
            'CREATE TABLE IF NOT EXISTS logins ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(20) NOT NULL, '
            'senha VARCHAR(8) NOT NULL, '
            'PRIMARY KEY (id) '
            ')'
        )
        cursor.execute(sql)

        sql = (
            'CREATE TABLE IF NOT EXISTS problemas ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'pedido_id INT NOT NULL, '
            'problema VARCHAR(100), '
            'PRIMARY KEY (id), '
            'FOREIGN KEY(pedido_id) REFERENCES pedidos(id) '
            ')'
        )
        cursor.execute(sql)

    connection.commit()