from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

#mudança dia 27/09/2025 - setembro
#def home(request):
   # print('home')
    #return HttpResponse('home1')
    #return render(
     #       request,
      #      'Aula21.html' # o endereço é buscado automaticamente dentro de templates
            #então apenas o caminho relativo à templates é necessário
    #)

""" from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def processar_pedido(request):
    if request.method == "POST":
        pedido = request.POST.get("pedido")  # pega a variável enviada
        # aqui você faz o que quiser com a variável em Python
        return HttpResponse(f"Pedido recebido: {pedido}")
    return HttpResponse("Método inválido") """
# carrinho_app/views.py
from django.shortcuts import render, redirect
#import produtos
from .produtos import *

# --- Simulação de produtos ---
# Isso é um dicionário que simula a sua base de dados de produtos.
# Em um projeto real, você buscaria esses dados de um banco de dados
# usando os modelos do Django.


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

def home(request):
    """
    Esta view lida com a exibição da página e com todas as
    ações de carrinho e finalização (POST).
    """
    erro_validacao = None
    valor_mesa_invalido = None
    lista_detalhada = []
    if request.method == 'POST':
        # --- CARREGANDO AS DUAS LISTAS ---
        carrinho = request.session.get('carrinho', [])
        carrinho_notas = request.session.get('carrinho_notas', [])
        
        if 'adicionar_item' in request.POST:
            nome_produto = request.POST.get('adicionar_item')
            if nome_produto in PRODUTOS_DISPONIVEIS:
                # 1. Adiciona o nome à lista principal
                carrinho.append(nome_produto)
                # 2. Adiciona uma nota vazia à lista de notas, mantendo o índice
                carrinho_notas.append('') 
                
                request.session['carrinho'] = carrinho
                request.session['carrinho_notas'] = carrinho_notas # Salva a lista de notas
            return redirect('home')
            
        elif 'remover_item_por_posicao' in request.POST:
            posicao = request.POST.get('remover_item_por_posicao')
            try:
                posicao = int(posicao)
                if 0 <= posicao < len(carrinho):
                    carrinho.pop(posicao)
                    # 3. REMOVE a nota correspondente para não quebrar os índices
                    if 0 <= posicao < len(carrinho_notas):
                        carrinho_notas.pop(posicao) 
                        
                    request.session['carrinho'] = carrinho
                    request.session['carrinho_notas'] = carrinho_notas # Salva a lista de notas atualizada
            except (ValueError, IndexError):
                pass
            return redirect('home')

        # --- NOVA LÓGICA: Salvar Nota Adicional (POST) ---
        elif 'salvar_nota' in request.POST:
            posicao_str = request.POST.get('posicao_item_nota')
            nova_nota = request.POST.get('nota_adicional', '').strip()
            
            try:
                posicao = int(posicao_str)
                # 4. Altera a nota APENAS na lista de notas
                if 0 <= posicao < len(carrinho_notas):
                    carrinho_notas[posicao] = nova_nota
                    request.session['carrinho_notas'] = carrinho_notas # Salva a lista de notas
            except (ValueError, IndexError):
                pass
            
            return redirect('home') # Redireciona para exibir o carrinho atualizado
        # Código que falta no seu if request.method == 'POST':
        elif 'editar_nota' in request.POST:
            posicao_para_editar = request.POST.get('posicao_para_editar')
            # Neste ponto, você pode salvar a posição na sessão ou apenas deixá-la
            # ser passada para o template no contexto (o que é mais simples).
            # return redirect('home')
            #parece que é só continuar
            pass
        elif 'fechar_edicao' in request.POST:
            # Também não faz nada, apenas recarrega a página
            # sem a variável de contexto 'posicao_para_editar'.
            pass
        elif request.method == 'POST' and 'finalizar_real' in request.POST:
            # Chama sua função auxiliar passando o request
            return redirect('pagina_de_sucesso') 
        else:
            pass
         # --- 2. Lógica de Finalizar Pedido (Validação do Número da Mesa) ---
        # Se chegamos aqui, é porque nenhum botão de carrinho foi apertado. 
        # Assumimos que é o formulário de finalização.
        
        numero_mesa_str = request.POST.get('numero_mesa')
        nome = request.POST.get('nome_cliente', '').strip()
        # --- VALIDAÇÃO DE BACKEND ---
        if not numero_mesa_str:
            erro_validacao = "O número da mesa é obrigatório."
        else:
            try:
                numero_mesa = int(numero_mesa_str)
                if not (1 <= numero_mesa <= 20):
                    erro_validacao = "O número da mesa deve ser entre 1 e 20."
            except ValueError:
                erro_validacao = "Formato de número de mesa inválido."

        #confirmar_pedido(request)
        #- PROCESSAMENTO / RE-RENDERIZAÇÃO ---
        if not erro_validacao:
            # SUCESSO! Lógica para processar o pedido final, salvar no DB, limpar carrinho, etc.
            if not numero_mesa_str:
                erro_validacao = "O número da mesa é obrigatório."
            else:
                try:
                    numero_mesa = int(numero_mesa_str)
                    if not (1 <= numero_mesa <= 20):
                        erro_validacao = "O número da mesa deve ser entre 1 e 20."
                except ValueError:
                    erro_validacao = "Formato de número de mesa inválido."
            if not nome:
                erro_validacao = "O nome do produto é obrigatório."
            if len(nome) > 50:
                erro_validacao = "O nome do produto deve ter no máximo 50 caracteres."
            # 3. Se a validação FALHAR, volte para home
            # (Idealmente, você enviaria o erro de volta, mas vamos simplificar)
            if erro_validacao:
                # Você pode usar o sistema de 'messages' do Django para mostrar o erro
                # messages.error(request, erro_validacao) 
                return redirect('home')

            # 4. SUCESSO! Salva no banco de dados
            try:
                conn = pymysql.connect(**db_config)
                status_inicial = "Recebido pela cozinha"
                with conn.cursor() as cursor:
                    for i, item_nome_chave in enumerate(carrinho):
                        item_nota = carrinho_notas[i] if i < len(carrinho_notas) else ''
                        nome_real_produto = PRODUTOS_DISPONIVEIS[item_nome_chave]['nome']
                            
                        sql_insert = "INSERT INTO pedidos (mesa, cliente,  pedido, nota, status) VALUES (%s, %s, %s, %s);"
                        cursor.execute(sql_insert, [numero_mesa,nome, nome_real_produto, item_nota, status_inicial])
                conn.commit() 
                print("--- DEBUG: Commit realizado! ---")
            except Exception as e:
                print(f"--- DEBUG: ERRO NO BANCO! {e} ---")
                return redirect('home')

                # Fazemos o loop e a lógica AQUI no Python, onde é fácil
            for i, chave_produto in enumerate(carrinho):
                # Pega o nome real do dicionário
                dados_produto = PRODUTOS_DISPONIVEIS.get(chave_produto, {'nome': 'Produto Desconhecido'})
                nome_real = dados_produto['nome']
                
                # Pega a nota (com segurança para não dar erro de índice)
                nota_texto = carrinho_notas[i] if i < len(carrinho_notas) else ''

                # Adiciona na lista um dicionário simples
                lista_detalhada.append({
                    'nome': nome_real,
                    'nota': nota_texto
                })

            context = {
                'lista_detalhada': lista_detalhada, # Mandamos a lista pronta
                'mesa': numero_mesa,
                'notas': carrinho_notas,
                # ... outros dados
            }
            
            # 5. Limpa a sessão
            if 'carrinho' in request.session:
                del request.session['carrinho']
            if 'carrinho_notas' in request.session:
                del request.session['carrinho_notas']
                
            # 6. Redireciona para uma página de sucesso
            if 'carrinho' in request.session:
                 del request.session['carrinho']
            #return redirect('pagina_de_sucesso') # Você precisa criar essa página/URL
            return render(request, 'confirmando/carrinho/confirmacao_carrinho.html', context)
            # Limpa o carrinho após o sucesso:
            # if 'carrinho' in request.session:
            #      del request.session['carrinho']
            
            # return redirect('pagina_de_sucesso')
        else:
            # ERRO! Guarda o valor digitado para preencher o formulário novamente
            valor_mesa_invalido = numero_mesa_str

    #- Lógica de Requisição GET (e exibição) ---
    carrinho_atual = request.session.get('carrinho', [])
    carrinho_notas = request.session.get('carrinho_notas', []) # Carrega a lista de notas
    
    # Prepara os dados para o template, combinando as duas listas
    itens_com_detalhes = []
    total = 0
    
    for i, item_nome in enumerate(carrinho_atual):
        item_nota = carrinho_notas[i] if i < len(carrinho_notas) else '' # Pega a nota correta
        
        if item_nome in PRODUTOS_DISPONIVEIS:
            detalhes = PRODUTOS_DISPONIVEIS[item_nome]
            total += detalhes['preco']
            
            itens_com_detalhes.append({
                'nome': detalhes['nome'], 
                'preco': detalhes['preco'], 
                'posicao': i,
                'nota_atual': item_nota # NOVO: Envia a nota correta para o template
            })
    context = {
        'produtos': PRODUTOS_DISPONIVEIS.items(),
        'itens_carrinho': itens_com_detalhes,
        'total': total,
        # Adiciona o contexto de erro AQUI
        'erro_mesa': erro_validacao, 
        'valor_mesa_invalido': valor_mesa_invalido,
        'lista_de_bebidas': BEBIDAS_DISPONIVEIS,
        'lista_de_pizzas': PIZZAS_DISPONIVEIS,
        'lista_de_hotdogs' : HOTDOG_DISPONIVEIS,
        'lista_de_milkshakes' : MILKSHAKES_DISPONIVEIS,
        'lista_de_sanduiches' : SANDUICHES_DISPONIVEIS,

        'posicao_para_editar': request.POST.get('posicao_para_editar'), # Envia o valor do último POST de edição
    }
    
    return render(request, 'Aula21.html', context)
def confirmar_pedido(request):
        
        finalizar_real = request.POST.get('finalizar_real') == "true"
        erro_validacao = None
        lista_detalhada = []
        numero_mesa_str = request.POST.get('numero_mesa')
        nome = request.POST.get('nome_cliente', '').strip()

        carrinho = request.session.get('carrinho', [])
        carrinho_notas = request.session.get('carrinho_notas', [])

        # --- VALIDAÇÃO DE BACKEND ---
        if not numero_mesa_str:
            erro_validacao = "O número da mesa é obrigatório."
        else:
            try:
                numero_mesa = int(numero_mesa_str)
                if not (1 <= numero_mesa <= 20):
                    erro_validacao = "O número da mesa deve ser entre 1 e 20."
            except ValueError:
                erro_validacao = "Formato de número de mesa inválido."

        # --- PROCESSAMENTO / RE-RENDERIZAÇÃO ---
        if not erro_validacao:
             # SUCESSO! Lógica para processar o pedido final, salvar no DB, limpar carrinho, etc.
            if not numero_mesa_str:
                 erro_validacao = "O número da mesa é obrigatório."
            else:
                try:
                     numero_mesa = int(numero_mesa_str)
                     if not (1 <= numero_mesa <= 20):
                         erro_validacao = "O número da mesa deve ser entre 1 e 20."
                except ValueError:
                     erro_validacao = "Formato de número de mesa inválido."
            if not nome:
                 erro_validacao = "O nome do produto é obrigatório."
            if len(nome) > 50:
                 erro_validacao = "O nome do produto deve ter no máximo 50 caracteres."
            # 3. Se a validação FALHAR, volte para home
            # (Idealmente, você enviaria o erro de volta, mas vamos simplificar)
            if erro_validacao:
                 # Você pode usar o sistema de 'messages' do Django para mostrar o erro
                 # messages.error(request, erro_validacao) 
                 return redirect('home')
            #  # 4. SUCESSO! Salva no banco de dados
            #  try:
            #      conn = pymysql.connect(**db_config)
            #      status_inicial = "Recebido pela cozinha"
            #      with conn.cursor() as cursor:
            #          for i, item_nome_chave in enumerate(carrinho):
            #              item_nota = carrinho_notas[i] if i < len(carrinho_notas) else ''
            #              nome_real_produto = PRODUTOS_DISPONIVEIS[item_nome_chave]['nome']
                           
            #              sql_insert = "INSERT INTO pedidos (mesa, cliente,  pedido, nota, status) VALUES (%s, %s, %s, %s, %s);"
            #              cursor.execute(sql_insert, [numero_mesa,nome, nome_real_produto, item_nota, status_inicial])
            #      conn.commit() 
            #      print("--- DEBUG: Commit realizado! ---")
            #  except Exception as e:
            #      print(f"--- DEBUG: ERRO NO BANCO! {e} ---")
            #      return redirect('home')
            #      # Fazemos o loop e a lógica AQUI no Python, onde é fácil
            #  for i, chave_produto in enumerate(carrinho):
            #      # Pega o nome real do dicionário
            #      dados_produto = PRODUTOS_DISPONIVEIS.get(chave_produto, {'nome': 'Produto Desconhecido'})
            #      nome_real = dados_produto['nome']
                
            #      # Pega a nota (com segurança para não dar erro de índice)
            #      nota_texto = carrinho_notas[i] if i < len(carrinho_notas) else ''
            #      total += dados_produto['preco']
            #      # Adiciona na lista um dicionário simples
            #      lista_detalhada.append({
            #          'nome': nome_real,
            #          'nota': nota_texto,
            #          'total': total,
            #      })

            #  context = {
            #      'lista_detalhada': lista_detalhada, # Mandamos a lista pronta
            #      'mesa': numero_mesa,
            #      'notas': carrinho_notas,
            #      # ... outros dados
            #  }
            
            #  # 5. Limpa a sessão
            #  if 'carrinho' in request.session:
            #      del request.session['carrinho']
            #  if 'carrinho_notas' in request.session:
            #      del request.session['carrinho_notas']
                
            #  # 6. Redireciona para uma página de sucesso
            #  if 'carrinho' in request.session:
            #       del request.session['carrinho']
            #  #return redirect('pagina_de_sucesso') # Você precisa criar essa página/URL
            #  return render(request, 'confirmando/carrinho/confirmacao_carrinho.html', context)
            # --- SE O USUÁRIO AINDA NÃO CONFIRMOU ---
            if finalizar_real:
                return redirect('pagina_de_sucesso')
            if not finalizar_real:

                # construir lista para mostrar na tela
                total = 0
                for i, chave_produto in enumerate(carrinho):
                    dados = PRODUTOS_DISPONIVEIS[chave_produto]
                    total += dados['preco']

                    lista_detalhada.append({
                        'nome': dados['nome'],
                        'nota': carrinho_notas[i] if i < len(carrinho_notas) else '',
                        'total': total,
                    })

                context = {
                    'mesa': numero_mesa,
                    'nome': nome,
                    'lista_detalhada': lista_detalhada,
                }

                return redirect('home')


            # --- SE O USUÁRIO CLICOU EM "SIM, FINALIZAR COMPRA" ---
            try:
                conn = pymysql.connect(**db_config)
                with conn.cursor() as cursor:
                    for i, item_nome_chave in enumerate(carrinho):
                        sql = """
                        INSERT INTO pedidos (mesa, cliente, pedido, nota, status)
                        VALUES (%s, %s, %s, %s, %s)
                        """

                        cursor.execute(sql, [
                            numero_mesa,
                            nome,
                            PRODUTOS_DISPONIVEIS[item_nome_chave]['nome'],
                            carrinho_notas[i] if i < len(carrinho_notas) else '',
                            "Recebido pela cozinha"
                        ])

                conn.commit()

            except Exception as e:
                print("ERRO NO BANCO:", e)
                return redirect('home')


            # limpa sessão
            request.session.pop('carrinho', None)
            request.session.pop('carrinho_notas', None)
            
            return render(request, 'confirmar_pedido', context={})
         
def pagina_de_sucesso(request):
    """
    Busca todos os pedidos no banco de dados que 
    não estão com o status 'Finalizado' e os exibe.
    """
    print("═" * 50)
    print(f"📨 REQUISIÇÃO /pedidos/ RECEBIDA")
    print(f"📎 Referer: {request.META.get('HTTP_REFERER', 'Direto/Nenhum')}")
    print(f"🖥️ User-Agent: {request.META.get('HTTP_USER_AGENT', 'N/A')}")
    print(f"🔗 Método: {request.method}")
    print(f"🌐 IP: {request.META.get('REMOTE_ADDR')}")
    print(f"🔍 Caminho: {request.path}")
    print("═" * 50)
    
    lista_de_pedidos = []
    lista_finalizados = []
    lista_entregues = []
    connection = pymysql.connect(**db_config)

    try:
        with connection.cursor() as cursor:

            sql_query = """
                SELECT id, mesa, pedido, nota, status 
                FROM pedidos 
                WHERE ((status != %s AND status != %s) OR status IS NULL)  /* 1. Primeiro, filtre os ativos */
                ORDER BY id DESC                      /* 2. Ordene "de baixo para cima" (pelo ID) */
                LIMIT 10;                             /* 3. Pegue APENAS os 15 mais recentes */
            """
        
            # Executa a consulta
            cursor.execute(sql_query, ['Finalizado', 'Entregue'])
            
            # 2. Pega o nome das colunas...
            colunas = [col[0] for col in cursor.description]
        
            # 3. Transforma os resultados em uma lista de dicionários
            # (Este loop 'for' agora só vai rodar 15 vezes, no máximo)
            for row in cursor.fetchall():
                lista_de_pedidos.append(dict(zip(colunas, row)))
            
           
        
            # AGORA PEGA OS PEDIDOS ENTREGUES
            sql_query_finalizados = """
                SELECT mesa, pedido, nota, status 
                FROM pedidos 
                WHERE status = %s 
                ORDER BY id DESC 
                LIMIT 5;
            """
                
            # 2. Executa usando o mesmo cursor
            cursor.execute(sql_query_finalizados, ['Finalizado'])
                
            # 3. Pega os nomes das colunas novamente (caso sejam diferentes)
            colunas_fin = [col[0] for col in cursor.description]
                
            # 4. Transforma em dicionário e coloca na lista
            for row in cursor.fetchall():
                lista_finalizados.append(dict(zip(colunas_fin, row)))
            

            sql_query_finalizados = """
                SELECT mesa, pedido, nota, status 
                FROM pedidos 
                WHERE status = %s 
                ORDER BY id DESC 
                LIMIT 5;
            """
                
            # 2. Executa usando o mesmo cursor
            cursor.execute(sql_query_finalizados, ['Finalizado'])
                
            # 3. Pega os nomes das colunas novamente (caso sejam diferentes)
            colunas_fin = [col[0] for col in cursor.description]
                
            # 4. Transforma em dicionário e coloca na lista
            for row in cursor.fetchall():
                lista_finalizados.append(dict(zip(colunas_fin, row)))

            # Fecha a conexão (Só depois de fazer TUDO)
            connection.close()

    except Exception as e:
        print(f"Erro ao buscar pedidos na pagina_de_sucesso: {e}")
   
    # 4. Envia a lista para o template
    context = {
        'pedidos_ativos': lista_de_pedidos,
        'pedidos_finalizados': lista_finalizados,
        'pedidos_entregues': lista_entregues,
    }
    
    # 5. Renderiza o novo arquivo HTML
    return render(request, 'sucesso/pagina_de_sucesso.html', context)

import pymysql;

db_config = {
    "host": "localhost",
    "user": "usuario_python",
    "password": "senha123",
    "database": "cardapio_digital"
}
def finalizar_pedido_view(request):
    """
    Esta view tem UMA responsabilidade: validar a mesa,
    salvar o carrinho no banco e limpar a sessão.
    """
    lista_detalhada = []
    # Esta view SÓ deve aceitar POST
    if request.method == 'POST':
        
        # 1. Carrega os dados da sessão
        carrinho_final = request.session.get('carrinho', [])
        notas_finais = request.session.get('carrinho_notas', [])

        # Se o carrinho estiver vazio, não faça nada
        if not carrinho_final:
            return redirect('pedidos') # Volta para casa

        # 2. Pega e Valida o número da mesa
        numero_mesa_str = request.POST.get('numero_mesa')
        nome = request.POST.get('nome_cliente', '').strip()
        erro_validacao = None
        
        if not numero_mesa_str:
            erro_validacao = "O número da mesa é obrigatório."
        else:
            try:
                numero_mesa = int(numero_mesa_str)
                if not (1 <= numero_mesa <= 20):
                    erro_validacao = "O número da mesa deve ser entre 1 e 20."
            except ValueError:
                erro_validacao = "Formato de número de mesa inválido."
        if not nome:
            erro_validacao = "O nome do produto é obrigatório."
        if len(nome) > 50:
            erro_validacao = "O nome do produto deve ter no máximo 50 caracteres."
        # 3. Se a validação FALHAR, volte para home
        # (Idealmente, você enviaria o erro de volta, mas vamos simplificar)
        if erro_validacao:
            # Você pode usar o sistema de 'messages' do Django para mostrar o erro
            # messages.error(request, erro_validacao) 
            return redirect('home')

        # 4. SUCESSO! Salva no banco de dados
        try:
            conn = pymysql.connect(**db_config)
            status_inicial = "Recebido pela cozinha"
            with conn.cursor() as cursor:
                for i, item_nome_chave in enumerate(carrinho_final):
                    item_nota = notas_finais[i] if i < len(notas_finais) else ''
                    nome_real_produto = PRODUTOS_DISPONIVEIS[item_nome_chave]['nome']
                        
                    sql_insert = "INSERT INTO pedidos (mesa, cliente,  pedido, nota, status) VALUES (%s, %s, %s, %s, %s);"
                    cursor.execute(sql_insert, [numero_mesa,nome, nome_real_produto, item_nota, status_inicial])
            conn.commit() 
            print("--- DEBUG: Commit realizado! ---")
        except Exception as e:
            print(f"--- DEBUG: ERRO NO BANCO! {e} ---")
            #return redirect('home')

            # Fazemos o loop e a lógica AQUI no Python, onde é fácil
        for i, chave_produto in enumerate(carrinho_final):
            # Pega o nome real do dicionário
            dados_produto = PRODUTOS_DISPONIVEIS.get(chave_produto, {'nome': 'Produto Desconhecido'})
            nome_real = dados_produto['nome']
            
            # Pega a nota (com segurança para não dar erro de índice)
            nota_texto = notas_finais[i] if i < len(notas_finais) else ''

            # Adiciona na lista um dicionário simples
            lista_detalhada.append({
                'nome': nome_real,
                'nota': nota_texto
            })

        context = {
            'lista_detalhada': lista_detalhada, # Mandamos a lista pronta
            'numero_mesa': numero_mesa,
            # ... outros dados
        }
        context = {
        'itens': carrinho_final,
        'notas': notas_finais,
        'mesa' : numero_mesa,
        }
        # 5. Limpa a sessão
        if 'carrinho' in request.session:
            del request.session['carrinho']
        if 'carrinho_notas' in request.session:
            del request.session['carrinho_notas']
            
        # 6. Redireciona para uma página de sucesso
        
        #return redirect('pagina_de_sucesso') # Você precisa criar essa página/URL
        return render(request, 'confirmando/carrinho/confirmacao_carrinho.html', context)

    # Se alguém tentar acessar /finalizar-pedido/ com GET, apenas volte para casa
    return redirect('home')
def retonraTodosOsPedidos():
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor() 

    consulta = {"SELECT * FROM pedidos"}
    cursor.execute(consulta)

    resultados = cursor.fetchall()

    for linha in resultados:
        return linha

def retornaPedidosNaoEntregues():
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor() 

    consulta = {"SELECT * FROM pedidos WHERE status = 'Finalizado'"}
    cursor.execute(consulta)

    resultados = cursor.fetchall()

    for linha in resultados:
        return linha
    
def SetEmPreparo(self):
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor() 

    sql = "UPDATE pedidos SET status = %s WHERE id = %s"
    values = ("Em preparo", self.id) #descobrir como acessar o id

    cursor.execute(sql, values)

    conn.commit()
    conn.close()

def SetFinalizando(id):
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor() 

    sql = "UPDATE pedidos SET status = %s WHERE id = %s"
    values = ("Finalizando", id) 

    cursor.execute(sql, values)

    conn.commit()
    conn.close()


def SetFinalizado(self):
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor() 

    sql = "UPDATE pedidos SET status = %s WHERE id = %s"
    values = ("Finalizado", self.id)

    cursor.execute(sql, values)

    conn.commit()
    conn.close()


def SetEntregue(self):
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor() 

    sql = "UPDATE pedidos SET status = %s WHERE id = %s"
    values = ("Entregue", self.id)

    cursor.execute(sql, values)

    conn.commit()
    conn.close()


