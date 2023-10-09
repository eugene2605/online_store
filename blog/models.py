from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='Slug')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', null=True, blank=True, verbose_name='Превью')
    date_of_creation = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return f'{self.title} {self.date_of_creation}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('-date_of_creation',)
