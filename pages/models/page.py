from django.db import models
from django_resized import ResizedImageField
from common.models import CommonFields
from common.tools import set_media_url
from pages.models import (
    Social,
    Contact,
    SEOInfo
)

def logo(instance, filename):
    return set_media_url( 'Page', filename)

class Page (
        CommonFields,
        Social,
        Contact,
        SEOInfo
    ):
    slogan=models.CharField (
        null=True,
        blank=True,
        max_length=128
    )
    img_logo=ResizedImageField (
        null=True,
        blank=False,
        size=[256, 256],
        quality=95,
        upload_to=logo
    )
    views=models.PositiveIntegerField (
        default=1,
        blank=False,
        null=False
    )
    version=models.PositiveIntegerField (
        default=1,
        blank=False,
        null=False
    )

    def __str__(self):
        return str(self.id)

    class JSONAPIMeta:
        resource_name="Page"
