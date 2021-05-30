from django.db import models
from colorfield.fields import ColorField
from common.models import Picture

# Create your models here.

class InfoGridItem(Picture):
    page=models.ForeignKey (
        'pages.Page',
        related_name='page_infoGrid_item',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    hide_on_mobile = models.BooleanField (
        blank = False,
        default = False
    )
    info_grid=models.ForeignKey (
        'info_grid.InfoGrid',
        related_name='info_grid_item',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    color=ColorField(
        null=True,
        blank=True,
        default='#42a5f5'
    )
    order=models.PositiveIntegerField (
        null=True,
        blank=True,
        default=1
    )
    icon=models.CharField (
        null=True,
        blank=True,
        max_length=32
    )
    link=models.URLField (
        null=True,
        blank=True
    )
    button_text=models.CharField (
        null=True,
        blank=True,
        max_length=32
    )

    def __str__(self):
        if self.title:
            return '{0} [{1}]'.format(
                self.title,
                self.info_grid.name
            )
        return 'Slide [{0}]'.format(
                self.info_grid.name
            ) 
    
    def save(self, *args, **kwargs):
        self.info_grid.version=self.info_grid.version + 1
        self.info_grid.save()
        super().save(*args, **kwargs)

    class JSONAPIMeta:
        resource_name="InfoGridItem"
