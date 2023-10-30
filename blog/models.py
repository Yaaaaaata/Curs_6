from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=128, verbose_name="заголовок")
    content = models.TextField(verbose_name="содержимое статьи")
    image = models.ImageField(upload_to='blog_images/', verbose_name="изображение", null=True)
    views = models.IntegerField(default=0, verbose_name="количество просмотров", null=True)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="дата публикации", null=True)
    slug = models.CharField(max_length=100, verbose_name='slug', null=True)
    date_of_creation = models.DateTimeField(verbose_name='дата создания', null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блог"
