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
from Itens.master.Guarana import Guarana
# --- Simulação de produtos ---
# Isso é um dicionário que simula a sua base de dados de produtos.
# Em um projeto real, você buscaria esses dados de um banco de dados
# usando os modelos do Django.
produto_guarana=Guarana()
tupla_preco_guarana=produto_guarana.getpreco()
preco_guarana=float(tupla_preco_guarana[0])
nome_guarana = produto_guarana.getnome()

PRODUTOS_DISPONIVEIS = {
    "camiseta": {"nome": "Camiseta Básica", "preco": 49.90},
    "calca": {"nome": "Calça Jeans", "preco": 129.50},
    "tenis": {"nome": "Tênis Esportivo", "preco": 250.00},
    "guarana": {"nome": nome_guarana, "preco":preco_guarana }
}

def home(request):
    """
    Esta view lida com a exibição da página e com todas as
    ações de carrinho e finalização (POST).
    """
    erro_validacao = None
    valor_mesa_invalido = None

    if request.method == 'POST':
        # --- 1. Lógica de Adicionar/Remover Item (Ações de Carrinho) ---
        carrinho = request.session.get('carrinho', [])
        
        if 'adicionar_item' in request.POST:
            nome_produto = request.POST.get('adicionar_item')
            if nome_produto in PRODUTOS_DISPONIVEIS:
                carrinho.append(nome_produto)
                request.session['carrinho'] = carrinho
            # Sempre redirecione após uma ação de carrinho para evitar reenvio do form
            return redirect('home')
            
        elif 'remover_item_por_posicao' in request.POST:
            posicao = request.POST.get('remover_item_por_posicao')
            try:
                posicao = int(posicao)
                if 0 <= posicao < len(carrinho):
                    carrinho.pop(posicao)
                    request.session['carrinho'] = carrinho
            except (ValueError, IndexError):
                pass
            # Sempre redirecione após uma ação de carrinho
            return redirect('home')

        # --- 2. Lógica de Finalizar Pedido (Validação do Número da Mesa) ---
        # Se chegamos aqui, é porque nenhum botão de carrinho foi apertado. 
        # Assumimos que é o formulário de finalização.
        
        numero_mesa_str = request.POST.get('numero_mesa')
        
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
            # ...
            # Limpa o carrinho após o sucesso:
            if 'carrinho' in request.session:
                 del request.session['carrinho']
            
            return redirect('pagina_de_sucesso')
        else:
            # ERRO! Guarda o valor digitado para preencher o formulário novamente
            valor_mesa_invalido = numero_mesa_str

    # --- Lógica de Requisição GET (ou re-renderização pós-erro POST) ---
    
    # Carrega o carrinho para exibir na página (GET ou erro POST)
    carrinho_atual = request.session.get('carrinho', [])
    
    # Prepara os dados para o template
    itens_com_detalhes = []
    total = 0
    
    for i, item_nome in enumerate(carrinho_atual):
        if item_nome in PRODUTOS_DISPONIVEIS:
            detalhes = PRODUTOS_DISPONIVEIS[item_nome]
            total += detalhes['preco']
            itens_com_detalhes.append({
                'nome': detalhes['nome'], 
                'preco': detalhes['preco'], 
                'posicao': i
            })
            
    context = {
        'produtos': PRODUTOS_DISPONIVEIS.items(),
        'itens_carrinho': itens_com_detalhes,
        'total': total,
        # Adiciona o contexto de erro AQUI
        'erro_mesa': erro_validacao, 
        'valor_mesa_invalido': valor_mesa_invalido,
    }
    
    return render(request, 'Aula21.html', context)

def pagina_de_sucesso(request):
    """View para a página de confirmação de pedido."""
    return render(request, 'sucesso/pagina_de_sucesso.html', {})