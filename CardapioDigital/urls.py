"""
URL configuration for CardapioDigital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from home import views as homeViwes
from pedidos import views as pedViews

#urlpatterns = [
 #   path('admin/', admin.site.urls),
  #  path('', homeViwes.home), #não comça url com barra, se fora vazia não coloca barra
   # path('pedidos/', pedViews.pedidos),
#]
urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', homeViwes.home , name='home'), #não comça url com barra, se fora vazia não coloca barra
    path('pedidos/', pedViews.pedidos),
     path('sucesso/', homeViwes.pagina_de_sucesso, name='pagina_de_sucesso'),

]
    #path('pedidos/', pedViews.pedidos, name='pedidos'),
    # Mapeia a URL 'carrinho/' para a view listar_carrinho
    #path('carrinho/', homeViwes.listar_carrinho, name='listar_carrinho'),

    # Mapeia a URL para adicionar um item.
    # A URL terá o formato: /carrinho/adicionar/nome_produto/
    #path('carrinho/adicionar/<str:nome_produto>/', homeViwes. adicionar_item, name='adicionar_item'),

    # Mapeia a URL para remover um item.
    # A URL terá o formato: /carrinho/remover/posicao/
    #path('carrinho/remover/<int:posicao>/', homeViwes.remover_item_por_posicao, name='remover_item_por_posicao'),

    # URL para a página de produtos. Vamos criar uma view simples para isso.1# path('', views.listar_produtos, name='lista_produtos'),