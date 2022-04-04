from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Esto es lo que se muestra en las tarjetas de detalles, creo que se agrega
# aqui la parte el rol y departamento al que pertenece
#


class Article(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id])
