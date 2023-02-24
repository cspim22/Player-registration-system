# Criamos uma nova aplicação para poder facilitar o desenvolvimento
# Essa views receberá a uma função responsavel por verificar e executar o cadastro de novos usuarios no servidor 
from django.shortcuts import render, redirect

#Essa biblioteca irá facilitar a criação do formulario de novo usuario
# Sem ela teriamos que programar varias funcionalidades
from django.contrib.auth.forms import UserCreationForm##  
# Como adicionamos +1 campo na bibli acima, devemos importar a classe 
#que criamos no forms, pois essa classe herda a django.contrib.auth.forms
from .forms import UserRegisterForm


#Essa biblioteca permite que criemos uma mensagem de usuario cadastrado com sucesso
from django.contrib import messages


# Definimos a função novo_usuario, que será responsavel por 
# criar e gerenciar o cadastro de usuarios

def novo_usuario(request):
    
    # Caso o metodo da URL seja POST
    if request.method == 'POST':
        # Irá guardar oque foi preencido no formulario na variavel formulario
        formulario = UserRegisterForm(request.POST) # o parametro em () serve para informar que o formulario
                                                    # é preenchido com o que foi escrito na url

        # Se tudo for preenchido corretamente
        if formulario.is_valid(): 
            # Ele vai salvar as informações no banco de dados, na guia > navegar dados > auth_user
            formulario.save()
            
            #Aqui ele pega as informações da pagina e separa o username
            # salva na variavel usuario e cria uma mensagem de success
            # essa mensagem será implementada no template base.html
            usuario = formulario.cleaned_data.get('username')
            messages.success(request, f'O usuario {usuario} foi criado com sucesso')
            # Após tudo ser executado, ele retorna para a pagina de inicio
            return redirect('login')

    # enquanto nada acontecer, a pagina ficara com o formulario
    else: 
        formulario = UserRegisterForm()

    #se a interação com a pagina for do tipo POST, o django/python pega as informações
    # preenchidas e salva no formulario

    return render(request,'usuario/template.html',{'formulario' : formulario})



# Create your views here.
