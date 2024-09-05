from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),  # Define a view para a URL raiz
    path('produto/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/adicionar/', views.adicionar_categoria, name='adicionar_categoria'),
    path('categoria/<int:categoria_id>/', views.detalhe_categoria, name='detalhe_categoria'),
    path('categorias/<int:categoria_id>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categorias/<int:categoria_id>/deletar/', views.deletar_categoria, name='deletar_categoria'),
    path('produto/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('produto/<int:produto_id>/editar/', views.editar_produto, name='editar_produto'),
    path('produto/<int:produto_id>/deletar/', views.deletar_produto, name='deletar_produto'),
]
