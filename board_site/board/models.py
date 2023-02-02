from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    def __str__(self):
        return self.title

    class Meta:
        # Название модели во множественном числе
        verbose_name_plural = 'Объявления'
        # Название модели в единственном числе
        verbose_name = 'Объявление'
        # Сортировка объектов
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        # Название модели во множественном числе
        verbose_name_plural = 'Рубрики'
        # Название модели в единственном числе
        verbose_name = 'Рубрика'
        # Сортировка объектов
        ordering = ['name']
