from django.db import models
from ckeditor.fields import RichTextField

class Mainiki(models.Model):
    title = models.CharField(max_length=100, verbose_name='Baslik')
    image = models.ImageField(upload_to='fotolar/', null=True)
    text = RichTextField(verbose_name='Uzun İçerik', null=True)
    url = RichTextField(verbose_name='url', null=True)
