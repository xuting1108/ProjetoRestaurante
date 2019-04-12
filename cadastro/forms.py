from django import forms

from .models import Cadastro

class CadastroForm(forms.ModelForm):

    class Meta:
        model = Cadastro
        fields = ('nome', 'website', 'descricao', 'foto', 'data_criacao', 'data_publicacao', )