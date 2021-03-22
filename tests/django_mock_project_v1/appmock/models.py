from django.db import models

import uuid

from django.db import models
from proxyid.decorators import proxify


class PersonIntegerPK(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    @property
    @proxify
    def id_(self): pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PersonUUIDPK(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    @property
    @proxify
    def id_(self): pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

