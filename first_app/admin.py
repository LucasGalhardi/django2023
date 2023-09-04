from django.contrib import admin
from .models import Topico, Pagina, RegistroAcesso, Produto
# Register your models here.

admin.site.register(Topico)
admin.site.register(Pagina)
admin.site.register(RegistroAcesso)
admin.site.register(Produto)
