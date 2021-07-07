# qdm-studios-site

## **Instalação e comandos terminal**
```bash
py -m install Django
django-admin startproject mypage
py manage.py runserver  #test server
py manage.py startapp my_app
py manage.py makemigrations #rodar toda vez que modifcar models.py
py manage.py migrate #rodar toda vez que modifcar models.py
py manage.py shell ## interagir com o banco
```

## **settings.py**

> para reconhecer apps: adicionar app na lista INSTALLED_APPS (ex. 'my_app')

> para reconhecer templates no diretório base (usar extends nos html): add BASE_DIR/"templates" na lista 'DIRS' dentro de TEMPLATES

> para reconhecer arquivos static no diretório base: add STATICFILES_DIRS = [BASE_DIR/"static"]

## **urls.py**
```py
from django.urls import path, include
from . import views
path('posts/<slug:slug>', views.post_detail)
```

## Enviar página html salva com argumentos (variáveis do código)
```python
from django.shortcuts import render
return render(request, "pasta/arquivo.html", {
    "arg1": var1,
    "arg2": var2
})
```

## mostrar pagina de erro (carrega template 404.html)
```python
from django.http import Http404
try:
    something
except:
    raise Http404()
#ou
from django.shortcuts import get_object_or_404
book= get_object_or404(Book, pk=id)
```



## **Html e filtros**

```html
- add css style
<link rel="stylesheet" href="{% static 'app.css' %}">
- redirecionar para url
<a href="{% url "url_name" %}">All Challenges</a>
```



# carregar html passando variável
{% include "./includes/header.html" with var1="var_1" %}

# para carregar arquivo css no arquivo
{% load static %} 
<link rel="stylesheet" href="{% static "templates/app/"|add:css_file_var_or_file %}">

#inserir blocos em um arquivo template
<title>{% block page_title %}Título Padrão{% endblock %}</title>
{% block css_files %}{% endblock css_files %}
<body>{%block content%}{%endblock%}</body>

#Formatar data
<time>{{post.date|date:"d M Y"}}</time>

#Preservar quebra de linha
{{post.content|linebreaks}}

##### views.py




##### models.py 
class Book(models.Model): #pesquisar django model field reference (FieldTypes)

## MySQL django queries
## pesquisar django making queries 
## Book.objects.filter(rating__gt=3) #pesquisar Field lookups
from .models import Book #Queries na views
bestsellers=Book.objects.filter(is_bestselling=True) #só armazena a query e não o resultado!
amazing_bestsellers=bestsellers.filter(rating__gt=4) #idem acima
print(amazing_bestsellers) #só executa a query completa agora (melhor performance)
print(bestsellers) #se rodar, não executa a query, mas pega o resultado em cache (mais rápido)
print(Book.objects.filter(is_bestselling=True))#não armazena em cache

## Slug automático em models.py (ex.: Harry Potter 1 -> harry-potter-1)
from django.utils.text import slugify
slug = models.SlugField(default='', blank=True, editable=False, null=False, db_index=True)
    self.slug = slugify(self.title)
    super().save(*args, **kwargs)

## administras dados - Pesquisar django admin site
py manage.py createsuperuser
## admin.py
from .models import Book
admin.site.register(Book)

# pra testar no celular, acrescentar no setup.py:
ALLOWED_HOSTS = ['*']
py manage.py runserver 0.0.0.0:8000
entrar no ip do pc pelo cel + :8000
    



