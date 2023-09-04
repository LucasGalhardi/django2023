import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','teste.settings')

import django
django.setup()

import random
from faker import Faker
from first_app.models import Topico, Pagina, RegistroAcesso

fakegen = Faker()
topics = ['Pesquisa', 'Social', 'Marketplace', 'Notícias', 'Jogos']


def add_topic():
    t = Topico.objects.get_or_create(nome=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        top = add_topic()

        url = fakegen.url()
        data = fakegen.date()
        nome = fakegen.company()

        pagina = Pagina.objects.get_or_create(topico=top, url=url, nome=nome)[0]
        print(pagina.id)

        _ = RegistroAcesso.objects.get_or_create(pagina=pagina, data=data)[0]


print("Populando o BD... por favor aguarde.")
populate(20)
print('População finalizada')
