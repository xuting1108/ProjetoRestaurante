from django.db import models
from django.utils import timezone

class Cadastro(models.Model):
# cadastro é o nome do nosso modelo
#significa que o cadastro é um modelo de Django, então o Django
#sabe ele que deve ser salvo no banco de dados

# models.CharField - é assim que definimos um texto com um número limitado de caracteres.
# models.TextField - este campo é para textos sem um limite fixo. Parece ideal para o conteúdo de um blog, né?
# models.DateTimeField - este é uma data e hora.
# models.ForeignKey - este é um link para outro modelo
    nome = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    website = models.CharField(max_length=200)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='fotos_restaurantes', null=True, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now())
    data_publicacao = models.DateTimeField(blank= True, null = True)

    def cadastrando(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.website
