from django.urls import path
from .views import listar_itens, criar_item, atualizar_item, deletar_item, home

urlpatterns = [
    path('', home, name='home'),
    path('itens/', listar_itens, name='listar_itens'),
    path('itens/criar/', criar_item, name='criar_item'),
    path('itens/atualizar/<int:pk>/', atualizar_item, name='atualizar_item'),
    path('itens/deletar/<int:pk>/', deletar_item, name='deletar_item'),
]
