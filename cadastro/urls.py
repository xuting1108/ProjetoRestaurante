from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cadastro, name='lista_cadastro'),
    path('cadastro/<int:pk>/', views.detalhe_cadastro, name='detalhe_cadastro'),
    path('cadastro/novo/', views.novo_cadastro, name='novo_cadastro'),
    path('cadastro/<int:pk>/edit/', views.edita_cadastro, name='edita_cadastro'),
    path('cadastro/relatorio/', views.relatorio, name='relatorio'),

    #path('cadastro/<int:pk>/', views.cadastro_website, name='cadastro_website'),
]
