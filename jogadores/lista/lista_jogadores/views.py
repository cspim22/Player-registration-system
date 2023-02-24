from django.shortcuts import render, redirect #importa funções para criação da pagina html 
from django.shortcuts import HttpResponse #Importa funções para criação de uma pagina sem html
from .models import Melhores_Do_Brasil # Importa o modelo com os campos melhores do brasil, localizados em models
from .models import Melhores_Da_Historia # Importa o modelo com os campos melhores da historia, localizados em models
from .forms  import AddBrForm # importa a função que habilita add novos jogadores na lista mehores do brasil, porem
                              # sem utilizar a aba admim
from.forms import AddHForm
from django.contrib.auth.decorators import login_required # Importa uma função que permite apenas que usuarios 
                                                          # Cadastrados acessem a pagina.
# Essa função cria a pagina incial, onde será possivel selecionar qual lista vocÊ quer ver
# Seu template esta na pasta  inicial
@login_required
def pagina_inicial(request):
    
    return render(request,'inicial/template.html') # 'inicial/template.html' redireciona a pasta template/inicial/template
                                                   # lá definimos como a pagina deve-se comportar

# Essa função cria a pagina onde é possivel ver a lista dos melhores jogadores de futebol da historia.
# Seu template esta na pasta lista_melhores
@login_required # Cria um bloqueio para so poder ver se estiver logado
def lista_dos_melhores(request):
    melhores_historia = {
        'dado' : Melhores_Da_Historia.objects.all() # Aqui ele pega todas as informaçoes da função
    }
    return render (request,'lista_melhores/template.html',melhores_historia)  


#Essa função cria a pagina onde é possivel ver a lista dos melhores do Brasil
#Seu template esta na pasta lista_brasil
@login_required
def lista_brasil(request):
    melhores_jogadores = {
    'dados' : Melhores_Do_Brasil.objects.all()
        }
    return render (request,'lista_brasil/template.html',melhores_jogadores)  


#Essa função habilita um button em frente ao nome do jogador, que quando clicado mostra a sua biografia
# Ela recebe o ID que esta no banco de dados e o redireciona para a pagina 'brasil/template.html'
# Com isso o dicionario impprime aimformação solicitada na pagina 'brasil/template.html' de acordo com o id
@login_required
def ver_brasil(request,id):
    dados = {
        'dados': Melhores_Do_Brasil.objects.get(pk = id)# Aqui ele pega  a informação desejada, de acordo com a ID
    }
    return render(request,'brasil/template.html', dados)  

#Essa função habilita um button em frente ao nome do jogador, que quando clicado mostra a sua biografia
# Ela recebe o ID que esta no banco de dados e o redireciona para a pagina 'historia/template.html'
# Com isso o dicionario impprime aimformação solicitada na pagina 'historia/template.html' de acordo com o id
@ login_required
def ver_melhores(request, id): 

    melhores = {
        'dado' : Melhores_Da_Historia.objects.get(pk = id)# Aqui ele pega  a informação desejada, de acordo com a ID
    }
    return render(request,'historia/template.html',melhores)


# essa função é similiar a def novo_melhor_historia, por isso os comentarios estão nela e são validos para essa tbm
@login_required
def novo_jogador_Br(request):
    if request.method == 'POST':
        salvar_add = AddBrForm(request.POST)
        if salvar_add.is_valid():
            salvar_add.save()
        return redirect('lista_brasil')

    add = AddBrForm()
    formulario = {
            'formulario' : add

    }
    return render(request, 'novo_jogador_Brasil/template.html',context= formulario)

@login_required
def novo_melhor_historia(request):
    
    # Aqui ele add um novo jogado
    if request.method == 'POST': # Verifica se o request foi do tipo POST
        salvar_add = AddHForm(request.POST) # salva os campos preenchidos de ADDForm em salvar_add
        if salvar_add.is_valid(): # Se os valores foram preenchidos corretamente
            salvar_add.save() # Salva os valores no banco de dados
        return redirect('lista_dos_melhores') # Apos salvar, vamos redirecionar para o template em ('')
    
    # Aqui ele consulta o formulario, caso não clicamos no botão add
    else:
        add = AddHForm()
        formulario = {
            'formulario' : add

    }
    return render(request, 'novo_melhor_historia/template.html',context= formulario)

@login_required
def alterar_lista_Brasil(request, id_jogador): # essa função altera a lista Brasil
    lista = Melhores_Do_Brasil.objects.get(pk = id_jogador) # Carrega uma variavel com as informações do banco de dados
    if request.method == 'GET': # Get é um request para consulta de dados apenas, no caso mostra a tela com os dados preeenchidos
        formulario = AddBrForm(instance= lista) # preenche os dados com oque ja ésta salvo em lista
        return render(request,'novo_jogador_Brasil/template.html',{'formulario' : formulario})
    else: #  caso não seja GET, será POST, que é uma requisição de envio de dados( Alguma ação )
        dados = AddBrForm(request.POST, instance=lista) # permite a modificação dos dados, pois é um post
        if dados.is_valid():# Se o botão save for clicado e estiver tudo ok ele salva as alterações
            dados.save()
    return redirect('lista_brasil')

@login_required
def alterar_lista_mundial(request, id_jogador):

    lista = Melhores_Da_Historia.objects.get(pk = id_jogador) # carrega os dados já preenchidos na variavel lista
    if request.method == 'GET':
        formulario = AddHForm(instance= lista)
        return render(request, 'novo_melhor_historia/template.html', {'formulario' : formulario})
    else: 
        dados = AddHForm(request.POST, instance=lista)
        if dados.is_valid():
            dados.save()
    return redirect('lista_dos_melhores')

@login_required
def excluir_melhores(request, id_jogador):

    lista = Melhores_Da_Historia.objects.get(pk = id_jogador)
    if request.method == 'POST':
        lista.delete()
        return redirect('lista_dos_melhores')
    return render (request, 'lista_melhores/excluir.html')

@login_required
def excluir_brasil(request, id_jogador):
    lista = Melhores_Do_Brasil.objects.get(pk = id_jogador)
    if request.method == 'POST':
        lista.delete()
        return redirect('lista_brasil')
    return render(request, 'lista_brasil/excluir.html')