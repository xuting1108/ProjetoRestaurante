from django import forms

from .models import Cadastro

class CadastroForm(forms.ModelForm):

    class Meta:
        model = Cadastro
        fields = ('nome', 'restaurante', 'website', 'descricao', 'foto', 'quantidade_pessoas', 'faturamento', 'data_criacao', 'data_publicacao', )