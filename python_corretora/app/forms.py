from django.forms import ModelForm
from app.models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','cpf','email','sexo','telefone','status_civil','endereco','data_nascimento','salario']