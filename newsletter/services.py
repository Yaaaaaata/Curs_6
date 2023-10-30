from smtplib import SMTPException

from django.core.mail import send_mail
from django.core.cache import cache
from django.conf import settings
from django.utils import timezone

from newsletter.models import Log, Client, Message


def get_cache_clients():
    if settings.CACHE_ENABLED:
        key = 'client_list'
        client_list = cache.get(key)
        if client_list is None:
            client_list = Client.objects.all()
            cache.set(key, client_list)
    else:
        client_list = Client.objects.all()
    return client_list


def get_cache_messages():
    if settings.CACHE_ENABLED:
        key = 'message_list'
        message_list = cache.get(key)
        if message_list is None:
            message_list = Message.objects.all()
            cache.set(key, message_list)
    else:
        message_list = Message.objects.all()
    return message_list


def send_newsletter(newsletter):
    now = timezone.localtime(timezone.now())

    if newsletter.start_to_send <= now <= newsletter.stop_to_send:
        for client in newsletter.client.all():
            try:
                send_mail(
                    newsletter.message.head,
                    newsletter.message.body,
                    settings.EMAIL_HOST_USER,
                    recipient_list=[client],
                    fail_silently=False
                )
                log = Log.objects.create(
                    last_try=newsletter.start_to_send,
                    status_try='Успешно',
                    mailling=newsletter,
                    client=client.email
                )
                log.save()
                return log

            except SMTPException as error:
                log = Log.objects.create(
                    last_try=newsletter.time_to_send,
                    status_try='Ошибка',
                    mailling=newsletter,
                    client=client.email,
                    answer=error
                )
                log.save()
                return log
