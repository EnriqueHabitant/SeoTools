from django.db import models

# Create your models here.
class KeywordSearch(models.Model):
    method = models.CharField(verbose_name="Método", max_length=50)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    keyword = models.CharField(verbose_name="Keyword", max_length=250, blank=True, null=True)
    language = models.CharField(verbose_name="Idioma/País", max_length=70, blank=True, null=True)
    limit = models.PositiveSmallIntegerField(verbose_name="Límite", blank=True, null=True)
    depth = models.PositiveSmallIntegerField(verbose_name="Profundidad", blank=True, null=True)
    filters = models.TextField(verbose_name="Filtros", blank=True, null=True)
    result = models.TextField(verbose_name="Resultado", blank=True, null=True)

    class Meta:
        verbose_name = "KeywordSearch"
        verbose_name_plural = "KeywordSearch"

    def __str__(self):
        return self.method
