from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('listar_produtos')  # Redirecionar para a página principal ou onde desejar
    else:
        form = AuthenticationForm()
    return render(request, 'estoque/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('login')  # Redirecionar para a página de login após o logout

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'estoque/register.html', {'form': form})

@login_required
def listar_produtos(request):
    query = request.GET.get('query', '')
    
    # Filtra os produtos com base na pesquisa
    if query:
        produtos = Produto.objects.filter(nome__icontains=query)
    else:
        produtos = Produto.objects.all()

    # Verifica se é uma requisição AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Renderiza apenas o template parcial
        html = render_to_string('estoque/includes/produto_list.html', {'produtos': produtos})
        return JsonResponse({'html': html})
    
    return render(request, 'estoque/listar_produtos.html', {'produtos': produtos})

@login_required
def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'estoque/detalhe_produto.html', {'produto': produto})

@login_required
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'estoque/lista_categorias.html', {'categorias': categorias})

@login_required
def adicionar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'estoque/adicionar_categoria.html', {'form': form})

@login_required
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

@login_required
def deletar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'estoque/deletar_categoria.html', {'categoria': categoria})

@login_required
def detalhe_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    produtos = categoria.produtos.all()
    return render(request, 'estoque/detalhe_categoria.html', {'categoria': categoria, 'produtos': produtos})

@login_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'estoque/adicionar_produto.html', {'form': form})

@login_required
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

@login_required
def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')
    return render(request, 'estoque/deletar_produto_confirmar.html', {'produto': produto})

@login_required
def base(request):
    return render(request, 'estoque/base.html')
