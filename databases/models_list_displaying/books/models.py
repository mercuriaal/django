# coding=utf-8

from django.db import models


class Book(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64)
    author = models.CharField(verbose_name='Автор', max_length=64)
    pub_date = models.DateField(verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.name} {self.author}'
