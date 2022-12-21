from django.db import models


class Autor(models.Model):
    nome = models.CharField("Nome Completo", max_length=200)
    email = models.EmailField("Email", null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Autores'


class Categoria(models.Model):
    nome = models.CharField("Categoria",max_length=200)
    descricao = models.TextField(blank=True, null= True)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField("Titulo", max_length=200)
    autor = models.ManyToManyField(Autor)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria", blank=True, null=True)
    data_publicacao = models.DateField(blank=True, null=True)
    edicao = models.CharField("Edição", max_length=200, blank=True, null=True)
    genero = models.CharField("Gênero textual", max_length=200, blank=True, null=True)
    editora = models.CharField("Editora", max_length=200, blank=True, null=True)
    valor = models.FloatField("Valor", default=100)
    # imagem = models.ImageField(upload_to='livraria/media', blank=True)
    descricao = models.TextField(blank=True, null=True)
    isbn = models.CharField("ISBN", max_length=13, unique=True, help_text="13 Caracteres <a "
                                                                          "href='https://www.isbn-international.org/content/what-isbn""'>ISBN number</a>")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'Livros'


class Endereco(models.Model):
    cep = models.CharField("CEP", max_length=120)
    rua = models.CharField("Rua", max_length=120)
    numero = models.IntegerField("Numero")
    complemento = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cep




class Usuario(models.Model):

    SEXO_CHOICES = (
        ('M', u'Masculino'),
        ('F', u'Feminino'),
        ('N', u'Não Declarar'),
    )

    ESTADO_CIVIL_CHOICES = (
        ('S', u'Solteiro'),
        ('C', u'Casado'),
        ('D', u'Divorciado'),
        ('v', u'Viúv(o/a)'),
    )

    nome = models.CharField("Nome Completo", max_length=200)
    data_nasc = models.DateField()
    cpf = models.CharField("CPF", max_length=120)
    email = models.EmailField("Email")
    telefone = models.IntegerField("Telefone")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, verbose_name="Endereco", blank=True, null=True)

    def __str__(self):
        return self.cpf






class Carrinho(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario", blank=True, null=True)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name="Livro", blank=True, null=True)
    quantidade = models.IntegerField("Quantidade")

    def __str__(self):
        return self.livro.titulo




