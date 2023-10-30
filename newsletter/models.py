from django.db import models
from django.utils import timezone
from django.urls import reverse

from users.models import User


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name="почта клиента")
    full_name = models.CharField(max_length=128, verbose_name="имя клиента")
    comment = models.CharField(max_length=512, blank=True, null=True, verbose_name="комментарий")

    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name="кто создал запись"
    )

    def __str__(self):
        return f"{self.full_name} - {self.email}"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


class Message(models.Model):
    subject = models.CharField(max_length=128, verbose_name="тема письма")
    body = models.CharField(max_length=1024, verbose_name="тест письма")

    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name="кто создал запись"
    )

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('message_detail', kwargs={'pk': self.pk})


class Newsletter(models.Model):
    TIME_CHOICES = (
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    )

    send_time = models.DateTimeField(verbose_name="дата и время начала рассылки", default=timezone.now)
    interval = models.CharField(max_length=10, choices=TIME_CHOICES, verbose_name="интервал")
    status = models.CharField(max_length=10, default="created", verbose_name="статус")
    Client = models.ManyToManyField(Client, verbose_name='получатель')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение', null=True)

    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name="кто создал запись"
    )

    class Meta:
        verbose_name = "настройка рассылки"
        verbose_name_plural = "настройки рассылок"

    def __str__(self):
        return f"send_time: {self.send_time.date()}, interval: {self.interval}"


class Log(models.Model):
    STATUS_CHOICES = [
        ("success", "успешно"),
        ("failure", "ошибка"),
    ]

    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    attempt_time = models.DateTimeField(
        auto_now_add=True, verbose_name="дата в время попытки"
    )
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, verbose_name="статус", default='Успешно'
    )
    response = models.TextField(max_length=250, blank=True, null=True, verbose_name="ответ")

    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, verbose_name='рассылка', null=True)
    client = models.EmailField(max_length=150, verbose_name='клиент', null=True)

    class Meta:
        verbose_name = "результат рассылки"
        verbose_name_plural = "результат рассылок"

    def __str__(self):
        return f'{self.attempt_time} {self.status} {self.newsletter} {self.client}'
