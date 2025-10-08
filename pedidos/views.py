from django.shortcuts import render

#teste pro negócio de login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
PRODUTOS_DISPONIVEIS = {
    "camiseta": {"nome": "Camiseta Básica", "preco": 49.90},
    "calca": {"nome": "Calça Jeans", "preco": 129.50},
    "tenis": {"nome": "Tênis Esportivo", "preco": 250.00},

}

def pedidos(request):
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
        'lista_de_bebidas': BEBIDAS_DISPONIVEIS,
        'lista_de_pizzas': PIZZAS_DISPONIVEIS,
        'lista_de_hotdogs' : HOTDOG_DISPONIVEIS,
        'lista_de_milkshakes' : MILKSHAKES_DISPONIVEIS,
        'lista_de_sanduiches' : SANDUICHES_DISPONIVEIS,


    }
    
    return render(request, 'Aula21.html', context)

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
    
    return render(request, 'login.html')

def logout_pedidos(request):
    logout(request)
    return redirect('home')