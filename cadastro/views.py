from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Cadastro
from .forms import CadastroForm
from django.shortcuts import redirect

# Create your views here.
def lista_cadastro(request):
    #cadastros = Cadastro.objects.filter(data_publicacao=timezone.now()).order_by('data_criacao') 
    cadastros = Cadastro.objects.all()
    return render(request, 'cadastro/lista_cadastro.html', {'cadastros': cadastros})

def relatorio(request):
    #cadastros = Cadastro.objects.filter(data_publicacao=timezone.now()).order_by('data_criacao') 
    cadastros = Cadastro.objects.all()
    return render(request, 'cadastro/relatorio.html', {'cadastros': cadastros})

def detalhe_cadastro(request, pk):
    cadastro = get_object_or_404(Cadastro, pk=pk)
    return render(request, 'cadastro/detalhe_cadastro.html', {'cadastro': cadastro})

def novo_cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST, request.FILES) #faz o request dos textos e de tudo que for media(imagens, videos, etc)
        if form.is_valid():
            cadastro = form.save(commit=False)
            cadastro.nome = request.user
            cadastro.save()
            return redirect('detalhe_cadastro', pk=cadastro.pk)
    else:
        form = CadastroForm()
    return render(request, 'cadastro/edita_cadastro.html', {'form': form})

def edita_cadastro(request, pk):
    cadastro = get_object_or_404(Cadastro, pk=pk)
    if request.method == "POST":
        form = CadastroForm(request.POST, instance=cadastro)
        if form.is_valid():
            cadastro = form.save(commit=False)
            cadastro.nome = request.user
            cadastro.data_publicacao = timezone.now()
            cadastro.save()
            return redirect('detalhe_cadastro', pk=cadastro.pk)
    else:
        form = CadastroForm(instance=cadastro)
    return render(request, 'cadastro/edita_cadastro.html', {'form': form})


#def cadastro_website(request):
