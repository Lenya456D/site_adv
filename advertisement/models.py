from django.db import models
from django.template import defaultfilters
from unidecode import unidecode


# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Заголовок')
    slug = models.CharField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    about = models.TextField(db_index=True, verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена", db_index=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to="images/", verbose_name="Картинка")

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(unidecode(str(self.title)))
        super().save(*args, **kwargs)
