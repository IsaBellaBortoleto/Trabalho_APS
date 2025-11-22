from django.urls import path
from . import views  # Importa as views DO MESMO app (pedidos)

urlpatterns = [
    path('pedidos/', views.pedidos, name='pedidos'),           # http://localhost:8000/
    path('login/', views.login_pedidos, name='login_pedidos'),  # http://localhost:8000/login/
    path('logout/', views.logout_pedidos, name='logout_pedidos'),
    path('reportar_problema/', views.reportar_problema_view, name='reportar_problema'),
]