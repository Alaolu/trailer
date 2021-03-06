# Generated by Django 2.1.7 on 2020-12-24 15:21

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mainiki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Baslik')),
                ('image', models.ImageField(null=True, upload_to='fotolar/')),
                ('text', ckeditor.fields.RichTextField(null=True, verbose_name='Uzun İçerik')),
                ('url', ckeditor.fields.RichTextField(null=True, verbose_name='url')),
            ],
        ),
    ]
