from django.conf import settings
from django.core.mail import send_mail, EmailMessage

from .models import User


def send_verify_code(user: User, url):
    mail = EmailMessage(
        'Подтверждение регистрации',
        f'Чтобы подтвердить регистрацию перейдите по ссылке {url}',
        settings.EMAIL_HOST_USER,
        [user.email]
    )
    mail.send(fail_silently=False)
