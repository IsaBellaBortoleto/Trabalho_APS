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

# --- Simulação de produtos ---
# Isso é um dicionário que simula a sua base de dados de produtos.
# Em um projeto real, você buscaria esses dados de um banco de dados
# usando os modelos do Django.
PRODUTOS_DISPONIVEIS = {
    "camiseta": {"nome": "Camiseta Básica", "preco": 49.90},
    "calca": {"nome": "Calça Jeans", "preco": 129.50},
    "tenis": {"nome": "Tênis Esportivo", "preco": 250.00}
}

def home(request):
    """
    Esta única view lida com a exibição da página e com todas as
    ações de adicionar e remover itens do carrinho.
    """
    # Lógica para processar requisições POST (adicionar/remover)
    if request.method == 'POST':
        carrinho = request.session.get('carrinho', [])
        
        # Ação de adicionar item: verificamos se o nome do botão 'adicionar_item' foi enviado.
        if 'adicionar_item' in request.POST:
            nome_produto = request.POST.get('adicionar_item')
            if nome_produto in PRODUTOS_DISPONIVEIS:
                carrinho.append(nome_produto)
                # Salva o carrinho na sessão
                request.session['carrinho'] = carrinho
        
        # Ação de remover item: verificamos se o nome do botão 'remover_item_por_posicao' foi enviado.
        elif 'remover_item_por_posicao' in request.POST:
            posicao = request.POST.get('remover_item_por_posicao')
            try:
                posicao = int(posicao)
                if 0 <= posicao < len(carrinho):
                    carrinho.pop(posicao)
                    # Salva o carrinho na sessão
                    request.session['carrinho'] = carrinho
            except (ValueError, IndexError):
                pass
        
        # Redireciona para o mesmo URL após a ação POST para evitar reenvio de formulário.
        return redirect('home')

    # Lógica para processar requisições GET (exibir a página)
    carrinho_atual = request.session.get('carrinho', [])
    
    # Prepara os dados para o template
    itens_com_detalhes = []
    total = 0
    
    for i, item_nome in enumerate(carrinho_atual):
        if item_nome in PRODUTOS_DISPONIVEIS:
            detalhes = PRODUTOS_DISPONIVEIS[item_nome]
            total += detalhes['preco']
            # Incluímos a posição do item para que o botão de remover funcione
            itens_com_detalhes.append({
                'nome': detalhes['nome'], 
                'preco': detalhes['preco'], 
                'posicao': i
            })
            
    context = {
        'produtos': PRODUTOS_DISPONIVEIS.items(),
        'itens_carrinho': itens_com_detalhes,
        'total': total
    }
    
    return render(request, 'Aula21.html', context)

#request,'Aula21.html' # o endereço é buscado automaticamente dentro de templates
            #então apenas o caminho relativo à templates é necessário

