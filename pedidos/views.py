from django.shortcuts import render

#teste pro negócio de login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .produtos import *
import pymysql
# Create your views here.
PRODUTOS_DISPONIVEIS = {
    "camiseta": {"nome": "Camiseta Básica", "preco": 49.90},
    "calca": {"nome": "Calça Jeans", "preco": 129.50},
    "tenis": {"nome": "Tênis Esportivo", "preco": 250.00},
    produto_guarana.getnome(): {"nome": produto_guarana.getnome(), "preco":produto_guarana.getpreco() },
    produto_cocacola.getnome(): {"nome": produto_cocacola.getnome(), "preco":produto_cocacola.getpreco() },
    produto_sucovale.getnome(): {"nome": produto_sucovale.getnome(), "preco":produto_sucovale.getpreco() },
    produto_hotdogfrango.getnome(): {"nome": produto_hotdogfrango.getnome(), "preco":produto_hotdogfrango.getpreco() },
    produto_hotdognaotradicional.getnome(): {"nome": produto_hotdognaotradicional.getnome(), "preco":produto_hotdognaotradicional.getpreco() },
    produto_hotdogtradicional.getnome(): {"nome": produto_hotdogtradicional.getnome(), "preco":produto_hotdogtradicional.getpreco() },
    produto_milkshakechocolatudo.getnome(): {"nome": produto_milkshakechocolatudo.getnome(), "preco":produto_milkshakechocolatudo.getpreco() },
    produto_milkshakekitkat.getnome(): {"nome": produto_milkshakekitkat.getnome(), "preco":produto_milkshakekitkat.getpreco() },
    produto_milkshakemoranguete.getnome(): {"nome": produto_milkshakemoranguete.getnome(), "preco":produto_milkshakemoranguete.getpreco() },
    produto_pizzacalabreza.getnome(): {"nome": produto_pizzacalabreza.getnome(), "preco":produto_pizzacalabreza.getpreco() },
    produto_pizzafrango.getnome(): {"nome": produto_pizzafrango.getnome(), "preco":produto_pizzafrango.getpreco() },
    produto_pizzaricota.getnome(): {"nome": produto_pizzaricota.getnome(), "preco":produto_pizzaricota.getpreco() },
    produto_sanduichechicken.getnome(): {"nome": produto_sanduichechicken.getnome(), "preco":produto_sanduichechicken.getpreco() },
    produto_sanduichetradicional.getnome(): {"nome": produto_sanduichetradicional.getnome(), "preco":produto_sanduichetradicional.getpreco() },
    produto_sanduichefish.getnome(): {"nome": produto_sanduichefish.getnome(), "preco":produto_sanduichefish.getpreco() },

}
# PEDIDOS_ESTATICOS_EXEMPLO = [
#     {
#         "mesa": 5,
#         "itens": [
#             {"nome_chave": "pizzacalabreza", "nome": "Pizza Calabresa", "preco": 10.00, "nota": "Sem cebola."},
#             {"nome_chave": "cocacola", "nome": "Coca-Cola", "preco": 6.00, "nota": "Com gelo e limão."},
#         ],
#         "total": 16.00
#     },
#     {
#         "mesa": 14,
#         "itens": [
#             {"nome_chave": "sanduichechicken", "nome": "Sanduíche Chicken Crispy", "preco": 22.00, "nota": "Pão integral, por favor."},
#             {"nome_chave": "sucovale", "nome": "Suco Del Valle", "preco": 7.50, "nota": ""},
#             {"nome_chave": "hotdogtradicional", "nome": "Hot Dog Tradicional", "preco": 12.00, "nota": "Muito catchup!"},
#         ],
#         "total": 41.50
#     },
#     {
#         "mesa": 2,
#         "itens": [
#             {"nome_chave": "milkshakechoc", "nome": "Milkshake Chocolatudo", "preco": 18.00, "nota": "Extra chantilly."},
#             {"nome_chave": "milkshakechoc", "nome": "Milkshake Chocolatudo", "preco": 18.00, "nota": ""},
#         ],
#         "total": 36.00
#     },
#     {
#         "mesa": 9,
#         "itens": [
#             {"nome_chave": "pizzafrango", "nome": "Pizza Frango c/ Catupiry", "preco": 11.50, "nota": "Retirar o Catupiry."},
#         ],
#         "total": 11.50
#     },
#     {
#         "mesa": 19,
#         "itens": [
#             {"nome_chave": "guarana", "nome": "Guaraná Antarctica", "preco": 5.00, "nota": ""},
#             {"nome_chave": "hotdogfrango", "nome": "Hot Dog de Frango", "preco": 15.00, "nota": "Maionese à parte."},
#             {"nome_chave": "cocacola", "nome": "Coca-Cola", "preco": 6.00, "nota": "Sem gelo."},
#         ],
#         "total": 26.00
#     },
#     {
#         "mesa": 8,
#         "itens": [
#             {"nome_chave": "sanduichetrad", "nome": "Sanduíche Tradicional", "preco": 19.00, "nota": "Queijo extra."},
#             {"nome_chave": "sucovale", "nome": "Suco Del Valle", "preco": 7.50, "nota": ""},
#         ],
#         "total": 26.50
#     },
#     {
#         "mesa": 1,
#         "itens": [
#             {"nome_chave": "pizzacalabreza", "nome": "Pizza Calabresa", "preco": 10.00, "nota": ""},
#             {"nome_chave": "milkshakechoc", "nome": "Milkshake Chocolatudo", "preco": 18.00, "nota": "Para viagem."},
#         ],
#         "total": 28.00
#     },
# ]

import traceback
def pedidos(request):
    ordem_status = [
                "Recebido pela cozinha",
                "Em preparo",
                "Finalizando",
                "Finalizado",
                "Entregue",
            ]
    if request.method == 'POST':
        acao = request.POST.get('acao')

        # ----------------------------------------------------
        # 2. Lógica para Processar a Edição do Produto
        # ----------------------------------------------------
        if acao == 'editar_produto_modal':
            # Capturar os três valores enviados pelo formulário
            nome_original = request.POST.get('original_product_name')
            novo_nome = request.POST.get('new_product_name')
            
            # Converte o preço para float de forma segura
            try:
                novo_preco = float(request.POST.get('new_product_price'))
            except (ValueError, TypeError):
                # Tratar erro: se o preço não for válido, defina um valor padrão ou ignore
                print("ERRO: Preço inválido recebido.")
                novo_preco = 0.00 
            
            # Executa a função de salvamento no DB
            salvar_edicao_produto_sql(nome_original, novo_nome, novo_preco)
            
            # Redireciona para evitar reenvio do formulário
            return redirect('pedidos') 
        elif 'atualizar_status' in request.POST:
            pedido_id, status_atual = [s.strip() for s in request.POST.get('atualizar_status').split(',')]
            try:
                conn = pymysql.connect(**db_config)
                with conn.cursor() as cursor:

                    # Buscar status atual
                    # cursor.execute("SELECT status FROM pedidos WHERE id = %s", (pedido_id,))
                    # resultado = cursor.fetchone()

                    # if not resultado:
                    #     print("Pedido não encontrado.")
                    #     return redirect('pedidos')

                    # status_atual = resultado[0]

                    # Ache o status seguinte
                    print("Status recebido do POST:", status_atual)
                    if status_atual in ordem_status:
                        idx = ordem_status.index(status_atual)
                        # Só avança se não for o último
                        if idx < len(ordem_status) - 1:
                            novo_status = ordem_status[idx + 1]
                        else:
                            # Já está no último status
                            novo_status = status_atual
                    else:
                        # Se o status atual não estiver na lista, defina o inicial
                        novo_status = ordem_status[0]

                    # Atualizar no banco
                    
                    cursor.execute(
                        "UPDATE pedidos SET status = %s WHERE id = %s",
                        (novo_status, pedido_id)
                    )
                    print("==============================================================")
                    print("Atualizado para:", novo_status)
                    print("==============================================================")

                    conn.commit()

            except Exception as e:
                print("ERRO AO ATUALIZAR STATUS:", e)



    # erro_validacao = None
    # valor_mesa_invalido = None

    # ######### if request.method == 'POST':
    #     # --- 1. Lógica de Adicionar/Remover Item (Ações de Carrinho) ---
    #     carrinho = request.session.get('carrinho', [])
        
    #     if 'adicionar_item' in request.POST:
    #         nome_produto = request.POST.get('adicionar_item')
    #         if nome_produto in PRODUTOS_DISPONIVEIS:
    #             carrinho.append(nome_produto)
    #             request.session['carrinho'] = carrinho
    #         # Sempre redirecione após uma ação de carrinho para evitar reenvio do form
    #         return redirect('home')
            
    #     elif 'remover_item_por_posicao' in request.POST:
    #         posicao = request.POST.get('remover_item_por_posicao')
    #         try:
    #             posicao = int(posicao)
    #             if 0 <= posicao < len(carrinho):
    #                 carrinho.pop(posicao)
    #                 request.session['carrinho'] = carrinho
    #         except (ValueError, IndexError):
    #             pass
    #         # Sempre redirecione após uma ação de carrinho
    #         return redirect('home')

    #     # --- 2. Lógica de Finalizar Pedido (Validação do Número da Mesa) ---
    #     # Se chegamos aqui, é porque nenhum botão de carrinho foi apertado. 
    #     # Assumimos que é o formulário de finalização.
        
    #     numero_mesa_str = request.POST.get('numero_mesa')
        
    #     # --- VALIDAÇÃO DE BACKEND ---
    #     if not numero_mesa_str:
    #         erro_validacao = "O número da mesa é obrigatório."
    #     else:
    #         try:
    #             numero_mesa = int(numero_mesa_str)
    #             if not (1 <= numero_mesa <= 20):
    #                 erro_validacao = "O número da mesa deve ser entre 1 e 20."
    #         except ValueError:
    #             erro_validacao = "Formato de número de mesa inválido."

    #     # --- PROCESSAMENTO / RE-RENDERIZAÇÃO ---
    #     if not erro_validacao:
    #         # SUCESSO! Lógica para processar o pedido final, salvar no DB, limpar carrinho, etc.
    #         # ...
    #         # Limpa o carrinho após o sucesso:
    #         if 'carrinho' in request.session:
    #              del request.session['carrinho']
            
    #         return redirect('pagina_de_sucesso')
    #     else:
    #         # ERRO! Guarda o valor digitado para preencher o formulário novamente
    #         valor_mesa_invalido = numero_mesa_str

    # # --- Lógica de Requisição GET (ou re-renderização pós-erro POST) ---
    
    # # Carrega o carrinho para exibir na página (GET ou erro POST)
    # carrinho_atual = request.session.get('carrinho', [])
    
    # # Prepara os dados para o template
    # itens_com_detalhes = []
    # total = 0
    
    # for i, item_nome in enumerate(carrinho_atual):
    #     if item_nome in PRODUTOS_DISPONIVEIS:
    #         detalhes = PRODUTOS_DISPONIVEIS[item_nome]
    #         total += detalhes['preco']
    #         itens_com_detalhes.append({
    #             'nome': detalhes['nome'], 
    #             'preco': detalhes['preco'], 
    #             'posicao': i
    #         })
    pedidos_realizados = []
    pedidos_realizados = pedidos_clientes(request)
    # ----------------------------------------------------
    # 3. Lógica para Carregar Dados (GET)
    # ----------------------------------------------------

    problemas_reportados = [] # Inicializa a lista de problemas
    conn = None

    try:
        # CONEXÃO COM O BANCO DE DADOS
        conn = pymysql.connect(**db_config)
        
        # O DictCursor facilita o uso dos dados no template
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            
            # --- O SELECT CRUCIAL PARA BUSCAR OS PROBLEMAS ---
            sql_problemas = """
            SELECT 
                prob.id AS problema_id,
                prob.problema AS descricao,
                p.mesa AS numero_mesa,
                p.pedido AS nome_pedido
            FROM 
                problemas prob
            JOIN 
                pedidos p ON prob.pedido_id = p.id
            ORDER BY 
                prob.id DESC;
            """
            cursor.execute(sql_problemas)
            # A lista de problemas prontos para o HTML
            problemas_reportados = cursor.fetchall()
            
    except Exception as e:
        print(f"Erro ao carregar problemas do banco de dados: {e}")

    finally:
        if conn:
            conn.close()
    
    # Evitar erro quando a lista estiver vazia
    if pedidos_realizados:
        print(pedidos_realizados[0])
    else:
        print("Nenhum pedido realizado ainda.")

    context = {
        'produtos': PRODUTOS_DISPONIVEIS.items(),
        #'itens_carrinho': itens_com_detalhes,
        #'total': total,
        # Adiciona o contexto de erro AQUI
        #'erro_mesa': erro_validacao, 
        #'valor_mesa_invalido': valor_mesa_invalido,
        'lista_de_bebidas': BEBIDAS_DISPONIVEIS,
        'lista_de_pizzas': PIZZAS_DISPONIVEIS,
        'lista_de_hotdogs' : HOTDOG_DISPONIVEIS,
        'lista_de_milkshakes' : MILKSHAKES_DISPONIVEIS,
        'lista_de_sanduiches' : SANDUICHES_DISPONIVEIS,

        # Para mostrar a lista completa de produtos (PRODUTOS_DISPONIVEIS)
        'produtos_disponiveis': PRODUTOS_DISPONIVEIS.items(),
        
        # O novo conjunto de dados estáticos para exibir os pedidos
        #'pedidos_exemplo': PEDIDOS_ESTATICOS_EXEMPLO,
        'pedidos_realizados': pedidos_realizados,
        'problemas_reportados': problemas_reportados,

    }
    
    return render(request, 'pedidos/Pedidos.html', context)

db_config = {
    "host": "localhost",
    "user": "usuario_python",
    "password": "senha123",
    "database": "cardapio_digital"
}

def pedidos_clientes(request):
    lista_de_pedidos = []
    connection = pymysql.connect(**db_config)

    try:
        with connection.cursor() as cursor:

            sql_query = """
                SELECT id, mesa, pedido, nota, status 
                FROM pedidos 
                WHERE status IS NOT NULL AND status != 'Entregue'
                ORDER BY id DESC                      /* 2. Ordene "de baixo para cima" (pelo ID) */
                LIMIT 10;                             /* 3. Pegue APENAS os 15 mais recentes */
            """
        
            # Executa a consulta
            cursor.execute(sql_query)
            
            # 2. Pega o nome das colunas...
            colunas = [col[0] for col in cursor.description]
        
            # 3. Transforma os resultados em uma lista de dicionários
            # (Este loop 'for' agora só vai rodar 10 vezes, no máximo)
            for row in cursor.fetchall():
                pedido_dict = dict(zip(colunas, row))
            
                # 2. ADICIONA A LÓGICA DO STATUS LIMPO
                status_do_pedido = pedido_dict.get('status')
                if status_do_pedido and status_do_pedido is not None:
                    
                    # Sequência de Limpeza Definitiva: strip() -> lower() -> replace()
                    status_limpo = status_do_pedido.strip()  # Remove espaços extras nas bordas
                    status_limpo = status_limpo.lower()       # Tudo minúsculo
                    status_limpo = status_limpo.replace(' ', '-') # Substitui espaços internos por hífens
                    
                    # Adiciona a nova chave 'classe_css' ao dicionário
                    pedido_dict['classe_css'] = 'status-' + status_limpo
                else:
                    # Define uma classe padrão para status nulos/desconhecidos
                    pedido_dict['classe_css'] = 'status-desconhecido'
                    # 3. Adiciona o dicionário processado à lista final
                lista_de_pedidos.append(pedido_dict)
            # Fecha a conexão (Só depois de fazer TUDO)
            connection.close()

    except Exception as e:
        print(f" = = = = = = = = = = =Erro ao buscar pedidos na PEDIDOS: {e}")

    #contexto = { 'pedidos_realizados': lista_de_pedidos }
    
    # 2. Use a função 'render' para processar o template e retornar a resposta HTTP.
    #    (Substitua 'seu_template.html' pelo nome real do arquivo.)
    #return render(request, 'Pedidos.html', contexto)
    return (lista_de_pedidos)
  
#teste pro negócio de login
def login_pedidos(request):
    # Se usuário JÁ ESTIVER LOGADO, redireciona direto para pedidos
    if request.user.is_authenticated:
        return redirect('/pedidos/')  # Redireciona para a view 'pedidos'
    
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('senha')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/pedidos/')  # ✅ CORRIGIDO: Agora redireciona para 'pedidos'
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    
    return render(request, 'pedidos/login.html')

def logout_pedidos(request):
    logout(request)
    return redirect('home')

def salvar_edicao_produto_sql(nome_original, novo_nome, novo_preco):
    conn = None
    try:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        
        # Comando SQL: Atualiza os campos na tabela 'sanduiche'
        # IMPORTANTE: Se o nome da tabela no seu DB for diferente (ex: 'produtos'), MUDAR AQUI.
        sql = """
        UPDATE sanduiche 
        SET nome = %s, preco = %s 
        WHERE nome = %s
        """
        
        # A tupla de valores DEVE seguir a ordem do SQL: (novo nome, novo preco, nome original)
        valores = (novo_nome, novo_preco, nome_original)
        
        cursor.execute(sql, valores)
        conn.commit()
        
    except Exception as e:
        print(f"Erro no DB: {e}")
        if conn:
            conn.rollback() 
    finally:
        if conn:
            conn.close()

def reportar_problema_view(request):
    """
    Recebe o ID do pedido e a descrição do problema e atualiza o DB.
    """
    if request.method == 'POST':
        pedido_id_str = request.POST.get('pedido_id')
        descricao_problema = request.POST.get('descricao_problema', '').strip()

        if not pedido_id_str or not descricao_problema:
            messages.error(request, "ID do pedido ou descrição do problema não foram fornecidos.")
            return redirect('pagina_de_sucesso') # Volte para a página de acompanhamento

        try:
            pedido_id = int(pedido_id_str)
            
            # Conexão e Atualização do Banco de Dados
            conn = pymysql.connect(**db_config)

            with conn.cursor() as cursor:
                sql_update = "INSERT INTO problemas (pedido_id, problema) VALUES (%s, %s)"
                cursor.execute(sql_update, [pedido_id, descricao_problema])
            
            conn.commit()
            conn.close()
            
            messages.success(request, f"Problema reportado com sucesso para o Pedido ID: {pedido_id}!")
            
        except ValueError:
            messages.error(request, "ID de pedido inválido.")
        except Exception as e:
            messages.error(request, f"Erro ao atualizar o banco de dados: {e}")
            print(f"ERRO DE DB: {e}") # Log para debug

    # Redireciona de volta para a página de onde veio
    return redirect('pagina_de_sucesso')

# Mapeamento do status do banco de dados para a classe CSS
def obter_classe_status(status_do_pedido):
    # Simplificamos o status removendo espaços e convertendo para minúsculas
    status_limpo = status_do_pedido.lower().replace(' ', '-')
    
    # Exemplo de mapeamento, ou apenas retorno direto
    if 'recebido-pela-cozinha' in status_limpo:
        return 'status-recebido'
    elif 'em-preparo' in status_limpo:
        return 'status-preparo'
    elif 'finalizado' in status_limpo:
        return 'status-finalizado'
    # ... adicione o restante
    
    # Se quiser que a classe seja o próprio status limpo:
    # return 'status-' + status_limpo

    # Se quiser retornar diretamente a classe limpa, garantindo que
    # os nomes batam com o CSS:
    return 'status-' + status_limpo