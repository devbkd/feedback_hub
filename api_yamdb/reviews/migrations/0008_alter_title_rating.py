# Generated by Django 3.2.16 on 2023-05-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_alter_title_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.IntegerField(blank=True, default=None, verbose_name='Рейтинг'),
        ),
    ]