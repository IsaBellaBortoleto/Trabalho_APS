from django.shortcuts import render

# Create your views here.
def pedidos(request):
    print('pedidos')
    #return HttpResponse('home1')
    return render(
            request,
            'Pedidos.html' # o endereço é buscado automaticamente dentro de templates
            #então apenas o caminho relativo à templates é necessário
    )