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

def pedidos(request):
    ordem_status = [
                "Recebido pela cozinha",
                "Em preparo",
                "Finalizando",
                "Finalizado",
                "Entregue",
                "Atrasado em 30 minutos"
            ]
    if request.method == 'POST':
        acao = request.POST.get('acao')
        if acao == 'editar_produto_modal':
            nome_original = request.POST.get('original_product_name')
            novo_nome = request.POST.get('new_product_name')

            try:
                novo_preco = float(request.POST.get('new_product_price'))
            except (ValueError, TypeError):
                # Tratar erro: se o preço não for válido, defina um valor padrão ou ignore
                print("ERRO: Preço inválido recebido.")
                novo_preco = 0.00 
            

            salvar_edicao_produto_sql(nome_original, novo_nome, novo_preco)
            
            # Redireciona para evitar reenvio do formulário
            return redirect('pedidos') 
        elif 'atualizar_status' in request.POST:
            pedido_id, status_atual = [s.strip() for s in request.POST.get('atualizar_status').split(',')]
            try:
                conn = pymysql.connect(**db_config)
                with conn.cursor() as cursor:
                    print("Status recebido do POST:", status_atual)
                    if status_atual in ordem_status:
                        idx = ordem_status.index(status_atual)
                        # Só avança se não for o último
                        if idx < len(ordem_status) - 2:
                            novo_status = ordem_status[idx + 1]
                        else:
                            # Já está no último status
                            novo_status = ordem_status[2]
                    else:
                        # Se o status atual não estiver na lista, defina o inicial
                        novo_status = ordem_status[0]

                    cursor.execute(
                        "UPDATE pedidos SET status = %s WHERE id = %s",
                        (novo_status, pedido_id)
                    )

                    conn.commit()
            except Exception as e:
                print("ERRO AO ATUALIZAR STATUS:", e)
        elif 'set_atraso' in request.POST:
                pedido_id, status_atual = [s.strip() for s in request.POST.get('set_atraso').split(',')]
                try:
                    conn = pymysql.connect(**db_config)
                    with conn.cursor() as cursor:

                        novo_status = ordem_status[ - 1]
                        # Atualizar no banco
                        
                        cursor.execute(
                            "UPDATE pedidos SET status = %s WHERE id = %s",
                            (novo_status, pedido_id)
                        )

                        conn.commit()
                except Exception as e:
                    print("ERRO AO ATUALIZAR STATUS 2 2 2 2 2 2 22 :", e)   

                      
    pedidos_realizados = []
    pedidos_realizados = pedidos_clientes(request)

    problemas_reportados = [] 
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
        'lista_de_bebidas': BEBIDAS_DISPONIVEIS,
        'lista_de_pizzas': PIZZAS_DISPONIVEIS,
        'lista_de_hotdogs' : HOTDOG_DISPONIVEIS,
        'lista_de_milkshakes' : MILKSHAKES_DISPONIVEIS,
        'lista_de_sanduiches' : SANDUICHES_DISPONIVEIS,
        'produtos_disponiveis': PRODUTOS_DISPONIVEIS.items(),
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

            cursor.execute(sql_query)

            colunas = [col[0] for col in cursor.description]
            
            for row in cursor.fetchall():
                pedido_dict = dict(zip(colunas, row))
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
            
            connection.close()

    except Exception as e:
        print(f" = = = = = = = = = = =Erro ao buscar pedidos na PEDIDOS: {e}")

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