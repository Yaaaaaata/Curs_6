from newsletter.services import send_newsletter
from newsletter.models import Newsletter


def daily_tasks():
    newsletters = Newsletter.objects.filter(periodicity="DAILY", status=True)
    if newsletters.exists():
        for newsletter in newsletters:
            send_newsletter(newsletter)


def weekly_tasks():
    newsletters = Newsletter.objects.filter(periodicity="WEEKLY", status=True)
    if newsletters.exists():
        for newsletter in newsletters:
            send_newsletter(newsletter)


def monthly_tasks():
    newsletters = Newsletter.objects.filter(periodicity="MONTHLY", status=True)
    if newsletters.exists():
        for newsletter in newsletters:
            send_newsletter(newsletter)
