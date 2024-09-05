from django.contrib import admin
from .models import Categoria, Produto
from django.utils.html import format_html

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """Configuração do painel administrativo para o modelo Categoria."""
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    """Configuração do painel administrativo para o modelo Produto."""
    list_display = ('nome', 'preco', 'quantidade', 'categoria', 'image_tag')  # Adicione 'image_tag' se for um método definido
    list_filter = ('categoria',)
    search_fields = ('nome', 'descricao')
    
    # Se você quiser adicionar um link, certifique-se de que o método ou campo exista em 'list_display'
    list_display_links = ('nome', 'image_tag')  # 'image_tag' deve ser um método ou campo válido

    def image_tag(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.imagem.url)
        return 'No image'
    image_tag.short_description = 'Image'  # Opcional: Definir um título para a coluna
