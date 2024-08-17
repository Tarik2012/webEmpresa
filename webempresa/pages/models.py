from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Page(models.Model):
    title = models.CharField(verbose_name=('titulo'),max_length=200)
    content = RichTextField('Contenido', config_name='default')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "pagina"
        verbose_name_plural = "paginas"
        ordering = ['title']

    def __str__(self):
        return self.title