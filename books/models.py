from django.db import models


class Author(models.Model):
    """Book author"""

    # Used for book description
    name = models.CharField(
        'Имя автора',
        help_text='Имя автора, указываемое в описании книги',
        max_length=100,
        unique=True,
    )

    # Used for author description
    full_name = models.CharField(
        'Полное имя автора',
        max_length=100,
        unique=True,
    )
    info = models.TextField(
        'Информация об авторе',
        null=True,
        blank=True,
    )
    image = models.ImageField(
        'Фотография автора',
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']
        db_table = 'author'
