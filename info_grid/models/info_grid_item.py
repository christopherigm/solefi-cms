from django.db import models
from colorfield.fields import ColorField
from common.models import Picture

# Create your models here.

class InfoGridItem(Picture):
    page=models.ForeignKey (
        'pages.Page',
        related_name='page_infoGrid_item',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    info_grid=models.ForeignKey (
        'info_grid.InfoGrid',
        related_name='info_grid_item',
        null=True,
        blank=True,
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

    def __str__(self):
        return '{0} [{1}]'.format(
            self.title,
            self.info_grid.title
        )

    class JSONAPIMeta:
        resource_name="InfoGridItem"
