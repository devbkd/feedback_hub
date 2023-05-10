from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from rest_framework import status
from django.contrib.auth.models import User


class User(AbstractUser):
    class Role(models.TextChoices):
        USER = 'user', 'пользователь'
        MODERATOR = 'moderator', 'модератор'
        ADMIN = 'admin', 'администратор'

    username = models.TextField(
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+\Z',
                message='150 characters or fewer. '
                'Letters, digits and @/./+/-/_ only',
                code=status.HTTP_400_BAD_REQUEST,
            )
        ],
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Фамилия',
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Биография',
    )
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER,
        verbose_name='Роли',
    )
    confirmation_code = models.CharField(
        max_length=150,
        null=True,
        blank=False,
        verbose_name='Код подтверждения',
    )


class Categories(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название категории')
    slug = models.SlugField(
        max_length=50,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[-a-zA-Z0-9_]+$',
                code=status.HTTP_400_BAD_REQUEST,
            )
        ],
    )


class Genres(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название жанра')
    slug = models.SlugField(
        max_length=50,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[-a-zA-Z0-9_]+$',
                code=status.HTTP_400_BAD_REQUEST,
            )
        ],
    )


class Titles(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='название',
    )
    year = models.IntegerField(verbose_name='год выпуска')
    description = models.TextField(verbose_name='описание')
    categories = models.ForeignKey(
        Categories,
        related_name='title',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    genres = models.ManyToManyField(
        Genres,
        through='GenreTitle',
        related_name='title',
        blank=True,
    )


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    title = models.ForeignKey(Titles, on_delete=models.CASCADE)

    def str(self):
        return f'{self.title} {self.genre}'
