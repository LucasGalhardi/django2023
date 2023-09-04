from django.shortcuts import render
from django.http import HttpResponse
from .models import RegistroAcesso
from .forms import FormSimples, FormProduto

# Create your views here.
def index2(request):
    meu_dict = {'variavel': 'eu vim do serveeeeeeer!'}
    return render(request, 'index.html', context=meu_dict)
    
# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def registros(request):
    registros = RegistroAcesso.objects.all()
    return render(request, 'registros.html', context={'registros': registros})

def calculadora(request):
    return render(request, 'calculadora.html')

def formulario_simples(request):
    form = FormSimples()
    
    if request.method == 'POST':
        form = FormSimples(request.POST)
        if form.is_valid():
            print(form.cleaned_data['nome'])
            print(form.cleaned_data['sobrenome'])
            print(form.cleaned_data['email'])
    
    return render(request, 'form_simples.html', context={'form': form})

def form_produto(request):
    form = FormProduto()
    
    if request.method == 'POST':
        form = FormProduto(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Vish, deu erro")
    
    return render(request, 'form_produto.html', context={'form': form})
