from django.db import models
from django.core.exceptions import ValidationError

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)  # Nome da categoria, deve ser único
    descricao = models.TextField()  # Descrição da categoria

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nome']  # Ordena as categorias pelo nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)

    def __str__(self):
        return self.nome

    def clean(self):
        """Valida que o preço e a quantidade não sejam negativos."""
        if self.preco < 0:
            raise ValidationError({'preco': 'O preço não pode ser negativo.'})
        if self.quantidade < 0:
            raise ValidationError({'quantidade': 'A quantidade não pode ser negativa.'})
        
        # Chama o método clean da superclasse para garantir outras validações
        super().clean()
