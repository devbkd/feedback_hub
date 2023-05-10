# Generated by Django 3.2.16 on 2023-05-10 15:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20230509_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название категории')),
                ('slug', models.SlugField(unique=True, validators=[django.core.validators.RegexValidator(code=400, regex='^[-a-zA-Z0-9_]+$')])),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата коммента')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название жанра')),
                ('slug', models.SlugField(unique=True, validators=[django.core.validators.RegexValidator(code=400, regex='^[-a-zA-Z0-9_]+$')])),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата ревью')),
                ('rating', models.IntegerField(default=0, verbose_name='Рейтинг')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(10)], verbose_name='Оценка')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='название')),
                ('year', models.IntegerField(verbose_name='год выпуска')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='title', to='reviews.categorie')),
                ('genres', models.ManyToManyField(blank=True, related_name='title', through='reviews.GenreTitle', to='reviews.Genre')),
            ],
        ),
        migrations.RemoveField(
            model_name='titles',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='titles',
            name='genres',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.TextField(unique=True, validators=[django.core.validators.RegexValidator(code=400, message='Username must be in the format: litters,numbers, @, ., +, -,', regex='^[\\w.@+-]+\\Z')]),
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.title'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.review'),
        ),
        migrations.AlterField(
            model_name='genretitle',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.genre'),
        ),
        migrations.AlterField(
            model_name='genretitle',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.title'),
        ),
        migrations.DeleteModel(
            name='Genres',
        ),
        migrations.DeleteModel(
            name='Titles',
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('author', 'title'), name='unique_review'),
        ),
    ]
