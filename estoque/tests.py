from django.test import TestCase
from django.db.utils import IntegrityError
from .models import Categoria, Produto

class CategoriaModelTest(TestCase):
    def setUp(self):
        # Configura os dados necessários para os testes
        self.categoria = Categoria.objects.create(nome="Eletrônicos", descricao="Dispositivos eletrônicos.")

    def test_categoria_str(self):
        """Testa a representação em string da Categoria."""
        self.assertEqual(str(self.categoria), "Eletrônicos")

    def test_categoria_nome_unique(self):
        """Testa a unicidade do nome da Categoria."""
        # Cria uma nova categoria com o mesmo nome
        with self.assertRaises(IntegrityError):
            Categoria.objects.create(nome="Eletrônicos", descricao="Outro descrição.")

    def test_categoria_nome_not_blank(self):
        """Testa que o nome da Categoria não pode estar em branco."""
        categoria = Categoria(nome="", descricao="Descrição válida.")
        with self.assertRaises(ValueError):
            categoria.save()

    def test_categoria_descricao_length(self):
        """Testa o comprimento máximo da descrição da Categoria."""
        descricao = "A" * 256  # Assume que o comprimento máximo é 255 caracteres
        categoria = Categoria(nome="Test", descricao=descricao)
        with self.assertRaises(ValueError):
            categoria.save()

class ProdutoModelTest(TestCase):
    def setUp(self):
        # Configura os dados necessários para os testes
        self.categoria = Categoria.objects.create(nome="Eletrônicos", descricao="Dispositivos eletrônicos.")
        self.produto = Produto.objects.create(
            nome="Smartphone",
            descricao="Smartphone com tela de 6.5 polegadas",
            preco=1500.00,
            quantidade=10,
            categoria=self.categoria
        )

    def test_produto_str(self):
        """Testa a representação em string do Produto."""
        self.assertEqual(str(self.produto), "Smartphone")

    def test_produto_preco(self):
        """Testa se o preço do produto está correto."""
        self.assertEqual(self.produto.preco, 1500.00)

    def test_produto_quantidade(self):
        """Testa se a quantidade do produto está correta."""
        self.assertEqual(self.produto.quantidade, 10)

    def test_produto_preco_negative(self):
        """Testa se o preço do produto não pode ser negativo."""
        produto = Produto(
            nome="Produto Teste",
            descricao="Descrição válida.",
            preco=-100.00,  # Preço negativo
            quantidade=5,
            categoria=self.categoria
        )
        with self.assertRaises(ValueError):
            produto.save()

    def test_produto_quantidade_negative(self):
        """Testa se a quantidade do produto não pode ser negativa."""
        produto = Produto(
            nome="Produto Teste",
            descricao="Descrição válida.",
            preco=100.00,
            quantidade=-5,  # Quantidade negativa
            categoria=self.categoria
        )
        with self.assertRaises(ValueError):
            produto.save()
