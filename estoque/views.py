from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm

def listar_produtos(request):
    query = request.GET.get('query', '')
    if query:
        produtos = Produto.objects.filter(nome__icontains=query)
    else:
        produtos = Produto.objects.all()
    
    return render(request, 'estoque/listar_produtos.html', {'produtos': produtos})



def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'estoque/detalhe_produto.html', {'produto': produto})



def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'estoque/lista_categorias.html', {'categorias': categorias})


def adicionar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'estoque/adicionar_categoria.html', {'form': form})


def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'estoque/editar_categoria.html', {'form': form, 'categoria': categoria})


def deletar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'estoque/deletar_categoria.html', {'categoria': categoria})


def detalhe_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    produtos = categoria.produtos.all()
    return render(request, 'estoque/detalhe_categoria.html', {'categoria': categoria, 'produtos': produtos})


def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'estoque/adicionar_produto.html', {'form': form})


def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    context = {
        'produto': produto,
        'categorias': categorias,
        'form': form,
    }
    return render(request, 'estoque/editar_produto.html', context)


def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')
    return render(request, 'estoque/deletar_produto_confirmar.html', {'produto': produto})


def base(request):
    return render(request, 'estoque/base.html')

