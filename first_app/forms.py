from django import forms
from django.core import validators
from .models import Produto

class FormSimples(forms.Form):
    nome = forms.CharField(max_length=128)
    sobrenome = forms.CharField(max_length=128)
    email = forms.EmailField(validators=[validators.MaxLengthValidator(11)])

class FormProduto(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(FormProduto, self).__init__(*args, **kwargs)
        self.fields['quantidade_estoque'].label = "Quantidade atual em estoque"
    
    class Meta:
        model = Produto
        fields = '__all__'
    