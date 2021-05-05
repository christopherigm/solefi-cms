from django.db import models

class CommonFields(models.Model):
    enabled = models.BooleanField (
        blank = False,
        default = True
    )
    created = models.DateTimeField (
        auto_now_add = True,
        null = False
    )
    modified = models.DateTimeField (
        auto_now = True
    )

    class Meta:
        abstract = True
