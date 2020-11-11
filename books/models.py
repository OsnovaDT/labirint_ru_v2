from django.db import models


COVER_TYPES = (
    ('solid', '7Б - твердая (плотная бумага или картон)'),
    ('soft', 'мягкий переплет (крепление скрепкой или клеем)'),
    ('with_flaps', 'Обл. с клапанами'),
)
ILLUSTRATIONS_INFO = (
    ('bw', 'Черно-белые'),
    ('color', 'Цветные'),
    ('none', 'Без иллюстраций'),
)


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


class PublishingHouse(models.Model):
    """Book publishing house"""

    name = models.CharField(
        'Название издательства',
        max_length=100,
        unique=True,
    )
    info = models.TextField(
        'Информация об издательстве',
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name='Логотип издательства',
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'
        ordering = ['name']
        db_table = 'publishing_house'


class Episode(models.Model):
    """Publishing house episode"""
    name = models.CharField(
        'Название серии',
        max_length=100,
        unique=True,
    )
    publishing_house = models.ForeignKey(
        'PublishingHouse',
        on_delete=models.CASCADE,
        verbose_name='Издательство серии',
        related_name='episodes'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'
        ordering = ['name']
        db_table = 'episode'


class Genre(models.Model):
    """Book genre"""

    name = models.CharField(
        'Название жанра',
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']
        db_table = 'genre'


class Book(models.Model):
    """Book"""

    title = models.CharField(
        'Название книги',
        max_length=255
    )
    authors = models.ManyToManyField(
        'Author',
        verbose_name='Автор(ы) книги',
    )
    publishing_house = models.ForeignKey(
        'PublishingHouse',
        on_delete=models.CASCADE,
        verbose_name='Книжное издательство',
    )
    episode = models.ForeignKey(
        'Episode',
        on_delete=models.CASCADE,
        verbose_name='Серия книжного издательства',
        null=True,
        blank=True,
    )

    price = models.PositiveIntegerField('Цена книги')

    genres = models.ManyToManyField(
        'Genre',
        verbose_name='Жанр книги',
        blank=True
    )

    ID = models.PositiveIntegerField('ID книги')

    ISBN = models.CharField('ISBN книги', max_length=30)

    pages_amount = models.PositiveIntegerField(
        'Количество страниц в книге'
    )

    weight = models.PositiveIntegerField('Масса книги (г)')

    sizes = models.CharField('Размеры книги', max_length=20)

    cover_type = models.CharField(
        'Тип обложки книги',
        max_length=50,
        choices=COVER_TYPES,
        default='solid'
    )
    illustrations_info = models.CharField(
        'Информация об иллюстрации',
        max_length=50,
        choices=ILLUSTRATIONS_INFO,
        default='none'
    )
    annotation = models.TextField(
        'Аннотация к книге',
        null=True,
        blank=True
    )
    published_date = models.DateField(
        'Дата публикации книги',
        auto_now_add=True
    )
    image = models.ImageField(
        'Изображение обложки книги',
    )

    # To display the authors of the book on the administrative site
    def get_authors(self):
        return '\n'.join(
            [author.name for author in self.authors.all()]
        )
    
    # To display the genres of the book on the administrative site
    def get_genres(self):
        return '\n'.join(
            [genre.name for genre in self.genres.all()]
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['published_date', 'title']
        db_table = 'book'
