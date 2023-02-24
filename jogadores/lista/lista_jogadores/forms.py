from django.forms import ModelForm
from .models import Melhores_Do_Brasil          
from .models import Melhores_Da_Historia

#Ele cria uma classe do tipo forms, que ira permitir 'copiar' os parametros de um model.
class AddBrForm(ModelForm):
    class Meta:
        model = Melhores_Do_Brasil # define uma variavel 'herdando' os parametros de Melhores_Do_Brasil
        fields = '__all__'  #recebe todos os campos de Melhores_Do_Brasil

class AddHForm(ModelForm):
    class Meta:
        model = Melhores_Da_Historia
        fields = '__all__' # esse metodo coloca todos os parametros que estão em Melhores da historia,
                           # Para add um valor especifico fazer: - fields = ['campoA', 'campoB']