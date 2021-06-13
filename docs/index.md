# Welcome to Proxyid  

Hide your Django model's primary key

[![PyPI](https://img.shields.io/pypi/v/proxyid)](https://pypi.org/project/proxyid/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/proxyid)
![PyPI - Django Version](https://img.shields.io/pypi/djversions/proxyid)
![PyPI - License](https://img.shields.io/pypi/l/proxyid)

---

## Overview

**Proxyid** is a utility for the [**Django**](https://www.djangoproject.com/) web framework, it can hide a given model's primary key. If you need to hide your primary keys, **proxyid** may help you. It makes use of the [hashids](https://hashids.org) library to mask your **integer** or **uuid** based primary keys with a proxy id. It's plug'n play, therefore, it doesn't interfere with databases or models definitions.

It turns **https://myapp.com/mymodel/1** into **https://myapp.com/mymodel/5NxJD1dG6V**

| Type    | Primary Key                              | Exposed Proxied PK    |
| :------ | :--------------------------------------- | :-------------------- |
| Integer | 3                                        | 5NxJD1d               |
| UUID    | 82df2e8e-553b-4330-bd46-8299ec67a9bb	 | 7ljjRD1qVLfjkQG6R     |


A running [**demo**](https://rydder.pythonanywhere.com) is avaiable. You can check the demo's [**code**](https://github.com/felipepaes/proxyid/tree/master/tests/django_mock_project) also.

## Quick Start

To follow this quick start guide, it's assumed you know how to kickstart a django project and create apps.

---

### Install
Let's hide a model's primary key, we will create a mock `Author` model for demonstrating this.  
Assuming a Django project is already set with an app called **appmock**, proxyid can be installed with **pip**.

```
$ pip install proxyid
```

### Configuration
The configuration is set as a constant **`PROXYID`** in **`settings.py`**.
Add the following into your project's **`settings.py`**

```python
PROXYID = {
    "hashids": {
        "salt": "A grain of salt", # this is your salt
        "min_length": 15           # this is the minimum length of the proxied id
    }
}
```

### Model
Let's add our **`Author`** model.

```python
# djangoproject/appmock/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField()
    nationality = models.CharField()

    def __str__(self):
        return self.name
```

Now let's create a property method which will give access to a proxy primary key. To do that, we need to import a decorator from **`proxyid.decorators`** called **`proxify`**.

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

We named our property method **`id_`**(*with an underscore at the end, the word id without underscores is already reserved by the model*), but we could had called it bananas, we only can't use the names already reserved by our model as **`id`** or **`pk`**, for instance.

That's it, now our model instance will have the **`id_`** property with its unique primary key encoded by proxyid by using the hashids library. All we need is a method which doesn't return anything and the decorators **`@property`** and **`@proxify`**. Remember, we can name this property method whatever we want(except **pk** or **id**).

Let's check if everything is working by creating a model in a [django shell session](https://docs.djangoproject.com/en/3.2/ref/django-admin/#shell).

```python
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

### Views

Okay, we know our proxy primary key is being generated correctly and that we can retrieve it trought our model new property. But now we need to use it in a real web environment context, let's creat a view which receives a proxy id, decode it and retrieve the correct model to our user.

Let's add a **`author_detail`** view function into our **`views.py`** file

```python
# djangoprojects/appmock/views.py
from django.shortcuts import render

from appmock.models import Author

from proxyid.encoding import decode

# ...other code

def author_detail(request, pk):
    decoded_pk = decode(pk) # this will bring RvBykxK6qojOJnOMrQeGpALDW back to 1
    author = Author.objects.get(pk=decoded_pk)
    context = {"author" : author}
    return render(request, "appmock/author_detail.html", context)
```

We imported **`decode`** from **`proxyid.encoding`**. The **`decode`** function will decode our proxy id back to it's original primary key integer value, allowing us to retrieve our object by passing it to the ORM.

Now lets add our view into the **`urls.py`**.

```python
# urls.py
from django.urls import path
from appmock import views


urlpatterns = [
    # ...other path configuration
    # ...other path configuration
    # ...other path configuration
    path("author/<pk>/", views.author_detail, name="author-detail")
]
```

Now our author can be retrieved at **`http:localhost:8000/author/RvBykxK6qojOJnOMrQeGpALDW`**

The links can be easily generated in a **`list_detail`** view by passing the object's **`id_`** instead of **`pk`** property(*or whatever name you gave it*) to the url function like this:

```html
<!-- some django template author_detail.html -->
<!-- html -->

{% url 'author-detail' author.id_ %}
```

A running [**demo**](https://rydder.pythonanywhere.com) is avaiable. You can check the demo's [**code**](https://github.com/felipepaes/proxyid/tree/master/tests/django_mock_project) also.

## User Guide
Please, check the [**user guide**](/user-guide/) for detailed instructions about [**configuration**](user-guide/configuration.md), [**class based views**](user-guide/class-based-views.md) and more.
