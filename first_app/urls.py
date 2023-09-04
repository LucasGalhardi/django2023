from django.urls import path
from . import views

urlpatterns = [
    path('', views.index2, name='index'),
    path('registros', views.registros, name='registros'),
    path('formsimples', views.formulario_simples, name='formsimples'),
    path('formproduto', views.form_produto, name='formproduto'),
]
