from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок", unique=True)
    slug = models.CharField(max_length=150, verbose_name="slug", db_index=True, unique=True)
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(verbose_name="изображение (превью)", null=True)
    publication_date = models.DateTimeField(verbose_name="Дата публикации", auto_now_add=True)
    published = models.BooleanField()
    views_number = models.IntegerField(default=0)
    comments = models.TextField(null=True)