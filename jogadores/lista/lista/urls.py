"""lista URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lista_jogadores import views # importa a aba views da aplicação, assim poderemos importar as funções criadas nela
from usuarios import views as view # Importa a views do usuario
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('conta/', view.novo_usuario, name='novo_usuario'), 
    path('inicial',views.pagina_inicial,name= 'inicio'),
    path('',auth_views.LoginView.as_view(template_name='usuario/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='usuario/logout.html'),name='logout'),
    path('lista_dos_melhores/', views.lista_dos_melhores, name= 'lista_dos_melhores'), 
    path('lista_brasil/', views.lista_brasil, name= 'lista_brasil'),
    path('lista_brasil/<int:id>',views.ver_brasil,name='brasil'),
    path('lista_dos_melhores/<int:id>',views.ver_melhores,name='historia'),
    path('novo_jogador_Brasil/', views.novo_jogador_Br, name= 'novo_jogador_Brasil'),
    path('novo_melhor_da_historia/',views.novo_melhor_historia,name= 'novo_melhor_historia'),
    path('alterar_lista_Brasil/<int:id_jogador>',views.alterar_lista_Brasil, name= 'alterar_lista_Brasil'),
    path('alterar_melhores/<int:id_jogador>',views.alterar_lista_mundial,name='alterar_melhores'),
    path('excluir_melhores/<int:id_jogador>', views.excluir_melhores,name= 'excluir_melhores'),
    path('excluir_brasil/<int:id_jogador>', views.excluir_brasil, name ='excluir_Brasil')
    # altera o banco de dados do brasil
 
    ]


# O comando name= nomeia a função que esta em verde. Utilizamos a nomeação que esta em name 
# para relacionar os botões no parametro URL dos templates

""" 
linha 21 - cria a aba admin
linha 22 - cria a pagina principal, é a primeira a aparecer quando o django é iniciado
linha 23 - cria a pagina lista dos melhores, e nomeia a func verde como name= lista_dos_melhores
linha 24 - cria a pagina lista_brasil, e nomeia a func verde como name= lista_brasil
linha 25 - A estudar
linha 26 - A estudar
linha 27 - A estudar 
linha 29 - cria a aba alterar lista_Brasil, quando o botão alterar é clicado, essa linha é chamada e redireciona a aplicação para a função
           alterar_lista_brasil. 
"""

""" como funciona o path:

path('aqui é o nome que vai aparecer/ser digitado na url', views.nome da func de views, name= 'tag de nome') """