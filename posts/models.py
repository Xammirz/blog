from django.db import models
from django.db.models.fields import CharField, TextField
from django.urls import reverse
class Post(models.Model):
    title = models.CharField('Заголовок',max_length=100)
    body = models.TextField('Описание')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор' )
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural = 'Посты'
    def get_absolute_url(self): # Тут мы создали новый метод
        return reverse('post_detail', args=[str(self.id)])

# Create your models here.
