from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def home(request):
    print('home')
    #return HttpResponse('home1')
    return render(
            request,
            'Aula21.html' # o endereço é buscado automaticamente dentro de templates
            #então apenas o caminho relativo à templates é necessário
    )

""" from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def processar_pedido(request):
    if request.method == "POST":
        pedido = request.POST.get("pedido")  # pega a variável enviada
        # aqui você faz o que quiser com a variável em Python
        return HttpResponse(f"Pedido recebido: {pedido}")
    return HttpResponse("Método inválido") """