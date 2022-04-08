from django.db import models
from django.contrib.auth.models import User


# Создаем модель базы данных

# Модель Author
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Имя')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    def update_rating(self, new_rating):
        self.rating = new_rating
        self.save()

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


# Модель Category (в определении поля необходимо написать параметр unique = True).
class Category(models.Model):
    name_category = models.CharField(max_length=100, unique=True, verbose_name='Категория')

    def __str__(self):
        return f'{self.name_category}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

# Модель Post
class Post(models.Model):
    article = 'a'
    news = 'n'

    POST_TYPE = [
        (article, "Статья"),
        (news, "Новость")
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Имя автора')
    post_type = models.CharField(max_length=1, choices=POST_TYPE, default=article, verbose_name='Тип')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    cats = models.ManyToManyField(Category, through='PostCategory', verbose_name='Категория')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Контент')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    # Методы like() и dislike() в модели Post
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        size = 124 if len(self.text) > 124 else len(self.text)
        return self.text[:size] + '...'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

# Модель PostCategory
class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

# Модель Comment
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Новость')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    # Методы like() и dislike() в модели Comment
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'