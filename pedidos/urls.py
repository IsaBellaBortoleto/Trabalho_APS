from django.urls import path
from . import views  # Importa as views DO MESMO app (pedidos)

urlpatterns = [
    path('pedidos/', views.pedidos, name='pedidos'),           # http://localhost:8000/
    path('login/', views.login_pedidos, name='login_pedidos'),  # http://localhost:8000/login/
]