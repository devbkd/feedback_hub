# Generated by Django 3.2.16 on 2023-05-11 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20230512_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Рейтинг'),
        ),
    ]