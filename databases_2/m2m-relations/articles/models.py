from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    articles = models.ManyToManyField('Topic', through='Scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Topic(models.Model):

    name = models.TextField(verbose_name='Название')

    class Meta:
        verbose_name = 'Тематический раздел'
        verbose_name_plural = 'Тематические разделы'

    def __str__(self):
        return self.name


class Scope(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='Раздел')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной тег')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статьи'

    # def __str__(self):
    #     return f'{self.article}_{self.topic}'
