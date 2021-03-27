# Proxyid   

A Django utility to hide the primary key of a given model. 

![PyPI](https://img.shields.io/pypi/v/proxyid)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/proxyid)
![PyPI - Django Version](https://img.shields.io/pypi/djversions/proxyid)
![PyPI - License](https://img.shields.io/pypi/l/proxyid)


[EN](#quick-start) | [PT](#início-rápido)


Proxyid turns **`https://myapp.com/model/1`** into **`https://myapp.com/model/5NxJD1dG6V`**

Proxyid makes use of the [hashids library](https://hashids.org) to mask your integer or uuid based primary keys with a facade, proxy, mask. It's plug'n play, therefore, it doesn't interfere with the database or model definitions.

| Type    | Primary Key                              | Exposed Proxied PK           |
| :------ | :--------------------------------------- | :--------------------------- |
| Integer | 3                                        | 5NxJD1dG6VB3ZR3eKyzYEWrba    |
| UUID    | 82df2e8e-553b-4330-bd46-8299ec67a9bb	 | 7ljjRD1qVLfjkQepdRZAimyDDZZ2 |

Please, check the following [demo](https://rydder.pythonanywhere.com/)

## Quick Start

Assuming a Django project is already set with an app called appmock, proxyid can be installed with **pip**.

```terminal
$ pip install proxyid
```

The configuration is set as a constant `PROXYID` in `settings.py`

```python
PROXYID = {
    "hashids": {
        "salt": "A grain of salt", # this is your salt
        "min_length": 15           # this is the minimum length of the proxied id
    }
}
```

Let's say the project has an Author model

```python
# djangoproject/appmock/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField()
    nationality = models.CharField()

    def __str__(self):
        return self.name
```

Now take a look at our `urls.py`

```python
# djangoproject/appmock/urls.py
from django.urls import path
from appmock import views


urlpatterns = [
    # ...other path configuration
    # ...other path configuration
    # ...other path configuration
    path("author/<pk>/", views.author_detail, name="author-detail")
]
```

### Proxify the Primary Key

If the app is exposing the database's primary key, the Author resource would be found, for example, at `http://myapp.com/author/1`
Let's hide our primary key. by importing the `proxify` decorator and defining a property method.


```python
# djangoproject/appmock/models.py
from django.db import models
from proxyid.decorators import proxify

class Author(models.Model):
    name = models.CharField()
    nationality = models.CharField()

    @property
    @proxify
    def id_(self): pass

    def __str__(self):
        return self.name
```

That's it, now our model instance will have the `id_` property with it's unique primary key encoded by proxyid by using the hashids library. All we need  is a method which doesn't return anything and the decorators `@property` and `@proxify`. You can name this property method whatever you want(except **pk** or **id**), let's name it `id_` for this example.

Let's check it by retrieving a model in a django shell session

```terminal
$ python manage.py shell
Python 3.9.2 (default, Mar 21 2021, 20:35:03)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from appmock import models
>>> author = models.Author.object.create(name="Lima Barreto", nationality="Brazil")
>>> author.id
1
>>> author.id_
RvBykxK6qojOJnOMrQeGpALDW
```

### Retrieving objects from encoded Primary Keys

Now, how about retrieving our object from the database if our user is giving us the encoded(`RvBykxK6qojOJnOMrQeGpALDW`) primary key?
Let's go to our hypothetical `author_detail` view function in `views.py`

```python
# djangoprojects/appmock/views.py
from django.shortcuts import render, HttpResponse

from appmock.models import Author

from proxyid.encoding import decode

# ...other code

def author_detail(request, pk):
    decoded_pk = decode(pk) # this will bring RvBykxK6qojOJnOMrQeGpALDW back to 1
    author = Author.objects.get(pk=decoded_pk)
    context = {"author" : author}
    return render(request, "appmock/author_detail.html", context)

```

We imported `decode` from `proxyid.encoding`, the `decode` function will transform our proxied value back to it's original primary key value, allowing us to retrieve our object by giving the pk value to the ORM.

How the urls were generated? By just passing the object `id_` instead of `pk` property or whatever name you have it to the url function. Like this:

```django-templates
<!-- some html -->

{% url 'author-detail' author.id_ %}
```

Now our author resource can be found at `http:myapp.com/author/RvBykxK6qojOJnOMrQeGpALDW`

### What about class based views?

Let's build the same logic of `author_detail` function view as a class based view now:

```python
# djangoproject/appmock/views.py
from django.views import generic

from appmock.models import Author

from proxyid.mixins import ProxyidMixin

class AuthorDetailView(ProxyidMixin, generic.DetailView):
    template_name = "appmock/author_detail.html"
    model = Author
    context_object_name = "author"
```

That's it, the view will work the same way as long as you use the `ProxyidMixin` as a parent class, and don't forget to provide a `pk` argument(this can be customized) from the url dispatcher.



----


Uma ferramenta baseado em Django para esconder a chave primária de um dado modelo.

Proxyid transforma **`https://meuapp.com/modelo/1`** em **`https://meuapp.com/modelo/5NxJD1dG6V`**

Proxyid utiliza a [biblioteca hashids](https://hashids.org) para codificar chaves primárias (int ou uuid). Como solução plug'n play, não interfere com a camada de banco de dados ou definição de modelos.

| Tipo    | Chave Primária                           | Chave Exposta pelo Proxyid   |
| :------ | :--------------------------------------- | :--------------------------- |
| Integer | 3                                        | 5NxJD1dG6VB3ZR3eKyzYEWrba    |
| UUID    | 82df2e8e-553b-4330-bd46-8299ec67a9bb	 | 7ljjRD1qVLfjkQepdRZAimyDDZZ2 |

Por favor, cheque a seguinte [demo](https://rydder.pythonanywhere.com/)

## Início Rápido

Considerando que um projeto Django já esteja configurado com um app chamado **appmock**, proxyid poder ser instalado via **pip**

```terminal
$ pip install proxyid
```

A configuração é aplicada em uma constante `PROXYID` no arquivo `settings.py`

```python
PROXYID = {
    "hashids": {
        "salt": "Uma pitada de sal", # esse é o sal
        "min_length": 15             # esse é o tamanho mínimo das ids geradas
    }
}
```

Digamos que o projeto possua um modelo Author

```python
# djangoproject/appmock/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField()
    nationality = models.CharField()

    def __str__(self):
        return self.name
```

Agora, vejamos nosso `urls.py`

```python
# djangoproject/appmock/urls.py
from django.urls import path
from appmock import views


urlpatterns = [
    # ...outras configurações path
    # ...outras configurações path
    # ...outras configurações path
    path("author/<pk>/", views.author_detail, name="author-detail")
]
```

### Escondendo nossa Chave Primária

Caso o app esteja expondo a chave primária do banco de ados, o modelo Author seria encontrado, por exemplo, em `http://meusite.com/autor/1`. Vamos esconder nossa chave primária, importando o decorator `proxify` e definindo um método propriedade.


```python
# djangoproject/appmock/models.py
from django.db import models
from proxyid.decorators import proxify

class Author(models.Model):
    name = models.CharField()
    nationality = models.CharField()

    @property
    @proxify
    def id_(self): pass

    def __str__(self):
        return self.name
```

Pronto, agora as instâncias de nosso modelo terão a propriedade `id_` com sua chave primária única codificada pelo proxyid, utilizando a biblioteca hashids. Tudo que precisamos foi de um método que retorna nada, e os decoradores `@property` e `@proxify`. Você pode nomear esse método como preferir (com exceção para **pk** ou **id**), o chamaremos de `id_` para este exemplo.

Vamos testar nosso modelo iniciando uma sesssão shell no Django.

```terminal
$ python manage.py shell
Python 3.9.2 (default, Mar 21 2021, 20:35:03)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from appmock import models
>>> author = models.Author.object.create(name="Lima Barreto", nationality="Brazil")
>>> author.id
1
>>> author.id_
RvBykxK6qojOJnOMrQeGpALDW
```

### Buscando objetos através de uma Chave Primária codificada

Agora, como buscar objects em nosso banco de dados, se nosso usuário estará acessando uma url com a chave primário codificada(`RvBykxK6qojOJnOMrQeGpALDW`)? Vamos para nossa hipotética função view chamada `author_detail` localizada em `views.py`.


```python
# djangoprojects/appmock/views.py
from django.shortcuts import render, HttpResponse

from appmock.models import Author

from proxyid.encoding import decode

# ...other code

def author_detail(request, pk):
    decoded_pk = decode(pk) # isso trará RvBykxK6qojOJnOMrQeGpALDW devolta para 1
    author = Author.objects.get(pk=decoded_pk)
    context = {"author" : author}
    return render(request, "appmock/author_detail.html", context)

```

Importamos a função `decode` de `proxyid.encoding`, a função `decode` transformará nosso valor codificado devolta para seu valor de chave primária original . permitindo que busquemos nosso objeto com a chave primária original.

Como as urls foram geradas? Simplesmente passando o atributo `id_` da instância do objeto Author ou seja lá qual for o nome da propriedade do seu modelo como argumento para a função url:

```django-templates
<!-- some html -->

{% url 'author-detail' author.id_ %}
```

Agora nosso autor pode ser encontrado em `http:myapp.com/author/RvBykxK6qojOJnOMrQeGpALDW`

### E as views baseadas em classes hein, e as classes?

Vmoas construir uma view com a mesma lógica daquela função `author_detail`, mas agora com views baseadas em classe:

```python
# djangoproject/appmock/views.py
from django.views import generic

from appmock.models import Author

from proxyid.mixins import ProxyidMixin

class AuthorDetailView(ProxyidMixin, generic.DetailView):
    template_name = "appmock/author_detail.html"
    model = Author
    context_object_name = "author"
```

Pronto, essa view funcionará da mesma maneira, desde que herde de ProxyidMixin e a sua url providencie um argumento nomeado como `pk`.

