from django.db import models


class AbstractModel(models.Model):
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
